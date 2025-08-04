---
title: "Kubernetes - PV & PVC"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# PersistentVolume과 PersistentVolumeClaim

- Infra 세부 사항을 알지 못해도 클러스터의 스토리지를 사용할 수 있도록 제공해주는 리소스
- POD안에서 영구 볼륨을 사용도록 하는 방법은 다소 복잡
- 결론 → PV를 ADMIN이 설정만 하면 사용자는 PVC를 통해서 클레임만 걸면 된
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f9e09a82-644b-4f5f-888f-a9fdd8f46b19/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNI4VAUF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCICCkF1RKpNE5ZJ1F0PSC6SvrIROcKt%2BgPaXAWApFjvOsAiEAgsUlstyPVaDfa%2B9V1OvH2LzSOE%2BwsaKo7UIrMcd8YUYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDL%2FaxnI0qe1GsA0fpCrcAxvO0dhgmiB6C1GPCRUn7cy5mOvrLx%2Fz01AQbdeRELnQW6vAdrLb%2Bygp8ij6iKmlzoFNldPrmyLuuroQ38gzScwYUw71D37ikN11MR40p%2FAzj6pSGP2XLXpu8BPaSAmCG8n1F4tBfzK2JwAcdTrdGQkyj%2BlRvDRFeo4JVKHuGtr8WXMqjmMT4huPwqWzg8PNSdkxr1JI%2Bnd5rQswH2NDcEhYmkHv8NpUhcWeh9M97l5%2Bpgx0c3Ye7TiGThSAbyllYefs6RUnR8GnDSq1z0uVwkWMGzh3ieQLziwdgo9iIzczA2B22ZofQyB2LIzRdSoNqseEOX2wYzrJnGWrZpAYrPLksWp8HHF%2BB5XVvdpLLl15XwI8fclcvcONiocS49J5xTubBakHzeIgIrTL6nWu3gYmF6nTteX1y14%2BALI4YoMeKdKcR3UizlrRAi3WHsiNs%2BR4CsmSMcigahAaeByyaGbn6yjpLd67%2BrNnINvAImb24eXx732j8JMZxFYh23YfJjHvtp%2FVJd9FOAxJTnLMKw1WxzrWstFUZr%2BsdxM63AQekoA3%2BmpWoP0wSbSA2adxYIlGVD0Vw7BpYM21qZUzsALfGj%2FZRvd2Yp0dwhKhkjjqynUgBN23ap0YVlisMIqNwcQGOqUB0GeRjiZ3%2FVxTeXuXJywbRUCiL%2BY5mP%2BolqAcPO%2FDYhmXiKj5P%2Fw2oQIW%2B3EqWxY915mMliC1MNnzjQZrHwZn3PXBuuaDQTq2hLpL0kuP7xvytM6%2FeeCZ3qEssXlFwwoaOJVTKd4lZfLXaF%2B2xbtQ1NXlVNxsYe%2FExWoWb4AvfU9jybg3z%2BlFx2ccE%2FBkLbIXAbeAsLqI8Iq9Ylp0K%2Bl%2Bibd3G49V&X-Amz-Signature=b4f9798a718637d62ab01533223098320770824b3ae9275446d9587aae74434f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/98250676-eec9-47ee-84f7-159b7f64b989/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNI4VAUF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCICCkF1RKpNE5ZJ1F0PSC6SvrIROcKt%2BgPaXAWApFjvOsAiEAgsUlstyPVaDfa%2B9V1OvH2LzSOE%2BwsaKo7UIrMcd8YUYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDL%2FaxnI0qe1GsA0fpCrcAxvO0dhgmiB6C1GPCRUn7cy5mOvrLx%2Fz01AQbdeRELnQW6vAdrLb%2Bygp8ij6iKmlzoFNldPrmyLuuroQ38gzScwYUw71D37ikN11MR40p%2FAzj6pSGP2XLXpu8BPaSAmCG8n1F4tBfzK2JwAcdTrdGQkyj%2BlRvDRFeo4JVKHuGtr8WXMqjmMT4huPwqWzg8PNSdkxr1JI%2Bnd5rQswH2NDcEhYmkHv8NpUhcWeh9M97l5%2Bpgx0c3Ye7TiGThSAbyllYefs6RUnR8GnDSq1z0uVwkWMGzh3ieQLziwdgo9iIzczA2B22ZofQyB2LIzRdSoNqseEOX2wYzrJnGWrZpAYrPLksWp8HHF%2BB5XVvdpLLl15XwI8fclcvcONiocS49J5xTubBakHzeIgIrTL6nWu3gYmF6nTteX1y14%2BALI4YoMeKdKcR3UizlrRAi3WHsiNs%2BR4CsmSMcigahAaeByyaGbn6yjpLd67%2BrNnINvAImb24eXx732j8JMZxFYh23YfJjHvtp%2FVJd9FOAxJTnLMKw1WxzrWstFUZr%2BsdxM63AQekoA3%2BmpWoP0wSbSA2adxYIlGVD0Vw7BpYM21qZUzsALfGj%2FZRvd2Yp0dwhKhkjjqynUgBN23ap0YVlisMIqNwcQGOqUB0GeRjiZ3%2FVxTeXuXJywbRUCiL%2BY5mP%2BolqAcPO%2FDYhmXiKj5P%2Fw2oQIW%2B3EqWxY915mMliC1MNnzjQZrHwZn3PXBuuaDQTq2hLpL0kuP7xvytM6%2FeeCZ3qEssXlFwwoaOJVTKd4lZfLXaF%2B2xbtQ1NXlVNxsYe%2FExWoWb4AvfU9jybg3z%2BlFx2ccE%2FBkLbIXAbeAsLqI8Iq9Ylp0K%2Bl%2Bibd3G49V&X-Amz-Signature=cf4a88eac9c2086b4d52afae94a3de91ebc91e9a36eebef913beaefc69709f97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## PV와 PVC YAML파일로 구성

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/fd678829-4686-4349-975c-ec5dd96b6b14/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNI4VAUF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCICCkF1RKpNE5ZJ1F0PSC6SvrIROcKt%2BgPaXAWApFjvOsAiEAgsUlstyPVaDfa%2B9V1OvH2LzSOE%2BwsaKo7UIrMcd8YUYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDL%2FaxnI0qe1GsA0fpCrcAxvO0dhgmiB6C1GPCRUn7cy5mOvrLx%2Fz01AQbdeRELnQW6vAdrLb%2Bygp8ij6iKmlzoFNldPrmyLuuroQ38gzScwYUw71D37ikN11MR40p%2FAzj6pSGP2XLXpu8BPaSAmCG8n1F4tBfzK2JwAcdTrdGQkyj%2BlRvDRFeo4JVKHuGtr8WXMqjmMT4huPwqWzg8PNSdkxr1JI%2Bnd5rQswH2NDcEhYmkHv8NpUhcWeh9M97l5%2Bpgx0c3Ye7TiGThSAbyllYefs6RUnR8GnDSq1z0uVwkWMGzh3ieQLziwdgo9iIzczA2B22ZofQyB2LIzRdSoNqseEOX2wYzrJnGWrZpAYrPLksWp8HHF%2BB5XVvdpLLl15XwI8fclcvcONiocS49J5xTubBakHzeIgIrTL6nWu3gYmF6nTteX1y14%2BALI4YoMeKdKcR3UizlrRAi3WHsiNs%2BR4CsmSMcigahAaeByyaGbn6yjpLd67%2BrNnINvAImb24eXx732j8JMZxFYh23YfJjHvtp%2FVJd9FOAxJTnLMKw1WxzrWstFUZr%2BsdxM63AQekoA3%2BmpWoP0wSbSA2adxYIlGVD0Vw7BpYM21qZUzsALfGj%2FZRvd2Yp0dwhKhkjjqynUgBN23ap0YVlisMIqNwcQGOqUB0GeRjiZ3%2FVxTeXuXJywbRUCiL%2BY5mP%2BolqAcPO%2FDYhmXiKj5P%2Fw2oQIW%2B3EqWxY915mMliC1MNnzjQZrHwZn3PXBuuaDQTq2hLpL0kuP7xvytM6%2FeeCZ3qEssXlFwwoaOJVTKd4lZfLXaF%2B2xbtQ1NXlVNxsYe%2FExWoWb4AvfU9jybg3z%2BlFx2ccE%2FBkLbIXAbeAsLqI8Iq9Ylp0K%2Bl%2Bibd3G49V&X-Amz-Signature=ebc73e84a545681dd5e804a6918ec1b07e84bb6082f62bfd4fec99f5b01cf893&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# provisioning

최근 K8S를 공부하며 프로비저닝이라는 단어를 자주 접하게 되었다.

전공 수업을 들으면서 아님 프로젝트를 진행하면서 몇번 봤던 단어이지만 정확한 정의를 내릴 수 없었다. 그냥 문맥을 통해서 어느정도 뜻을 인지하는 정도로 넘어갔었는데

클라우드와 Infra를 진로로 잡고 공부하다 보니 자주 접해서 프로비저닝를 공부했다.

사전적 의미는 “제공하는 것”이다.

CS적 의미는 사용자의 요구에 맞게 서비스를 제공하는 것 으로 정의 내릴 수 있다.

사용자의 요구에 맞게 시스템 자원을 할당, 배치, 배포해두었다가 필요할 때 **즉시 사용할 수 있는 상태로 미리 준비해두는 것 **을 말한다.

## 프로비저닝의 종류 (redhat 프로비저닝 정의 참고)

### **네트워크**

*네트워크 프로비저닝*은 권한을 가진 서버, 장치, 사용자가 액세스할 수 있는 네트워크를 구축하고 확립하는 데 중점을 둡니다. 이 프로비저닝 수준은 기본적으로 연결 및 보안에 관련되어 있으며, 보안은 장치와 ID 관리에 따라 크게 달라집니다.

### **서버**

*서버 프로비저닝*이란 네트워크 내에서 사용할 서버를 설정하는 것을 의미합니다. 여기에는 운영 체제 설치, 소프트웨어 제어 패널 조정, 특정 사용자에 이미 구성된 서버 할당이 포함됩니다.

### **애플리케이션**

*애플리케이션 프로비저닝*은 기업 내 특정 IT 환경에 대한 성능 최적화를 중심으로 합니다. 관리자는 애플리케이션 프로비저닝을 사용하여 사용자 지정 구성(*패키지*)을 생성하고 배포합니다.

### **사용자**

*사용자 프로비저닝*(*계정 프로비저닝*이라고도 부름)은 IT 인프라 내 사용자 계정을 생성, 수정, 삭제 또는 비활성화하는 데 사용됩니다. 사용자 프로비저닝은 사용자 권리 및 권한, 그리고 이에 연결된 디지털 ID를 관리하는 데 중점을 둡니다. 액세스 권한을 삭제하는 것을 *프로비저닝 해제*라고도 합니다.

사용자 프로비저닝은 기업이 일상적으로 참여하는 프로비저닝에 가장 중요한 수준입니다. 회사 내 신입 직원 채용 또는 직책이 변경될 때마다 사용자 권한을 업데이트해야 하므로 사용자 프로비저닝 및 프로비저닝 해제는 조직 전체의 IT 보안, 직원 생산성, 프로세스 효율성에 필수적입니다.

# 쿠버네티스 프로비저닝

출처:https://bcho.tistory.com/1259


## 정적 프로비저닝

K8S관리자가 수동으로 저장소를 생성하고 PV로 연결한다.

개발자는 PVC를 PV로 바인딩하여 스토리지를 이용한

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/fad19bc9-1e86-4c04-8c0e-b177319e6987/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNI4VAUF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCICCkF1RKpNE5ZJ1F0PSC6SvrIROcKt%2BgPaXAWApFjvOsAiEAgsUlstyPVaDfa%2B9V1OvH2LzSOE%2BwsaKo7UIrMcd8YUYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDL%2FaxnI0qe1GsA0fpCrcAxvO0dhgmiB6C1GPCRUn7cy5mOvrLx%2Fz01AQbdeRELnQW6vAdrLb%2Bygp8ij6iKmlzoFNldPrmyLuuroQ38gzScwYUw71D37ikN11MR40p%2FAzj6pSGP2XLXpu8BPaSAmCG8n1F4tBfzK2JwAcdTrdGQkyj%2BlRvDRFeo4JVKHuGtr8WXMqjmMT4huPwqWzg8PNSdkxr1JI%2Bnd5rQswH2NDcEhYmkHv8NpUhcWeh9M97l5%2Bpgx0c3Ye7TiGThSAbyllYefs6RUnR8GnDSq1z0uVwkWMGzh3ieQLziwdgo9iIzczA2B22ZofQyB2LIzRdSoNqseEOX2wYzrJnGWrZpAYrPLksWp8HHF%2BB5XVvdpLLl15XwI8fclcvcONiocS49J5xTubBakHzeIgIrTL6nWu3gYmF6nTteX1y14%2BALI4YoMeKdKcR3UizlrRAi3WHsiNs%2BR4CsmSMcigahAaeByyaGbn6yjpLd67%2BrNnINvAImb24eXx732j8JMZxFYh23YfJjHvtp%2FVJd9FOAxJTnLMKw1WxzrWstFUZr%2BsdxM63AQekoA3%2BmpWoP0wSbSA2adxYIlGVD0Vw7BpYM21qZUzsALfGj%2FZRvd2Yp0dwhKhkjjqynUgBN23ap0YVlisMIqNwcQGOqUB0GeRjiZ3%2FVxTeXuXJywbRUCiL%2BY5mP%2BolqAcPO%2FDYhmXiKj5P%2Fw2oQIW%2B3EqWxY915mMliC1MNnzjQZrHwZn3PXBuuaDQTq2hLpL0kuP7xvytM6%2FeeCZ3qEssXlFwwoaOJVTKd4lZfLXaF%2B2xbtQ1NXlVNxsYe%2FExWoWb4AvfU9jybg3z%2BlFx2ccE%2FBkLbIXAbeAsLqI8Iq9Ylp0K%2Bl%2Bibd3G49V&X-Amz-Signature=ed4fc2410fef048e40d85c94f7a56908bab656e39420d7c1710b0d9bee8adf6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 동적 프로비저닝

정적 프로비저닝과 달리 미리 저장소를 생성하지 않고 Storage Class를 생성하여 쿠버네티스에 요청한다. k8s는 해당 클래스를 구성 및 생성한다.

생성된 클래스에 PVC를 통해 바인딩한다

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9970cb0d-688b-4b20-9b3a-b8d948ef5316/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNI4VAUF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCICCkF1RKpNE5ZJ1F0PSC6SvrIROcKt%2BgPaXAWApFjvOsAiEAgsUlstyPVaDfa%2B9V1OvH2LzSOE%2BwsaKo7UIrMcd8YUYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDL%2FaxnI0qe1GsA0fpCrcAxvO0dhgmiB6C1GPCRUn7cy5mOvrLx%2Fz01AQbdeRELnQW6vAdrLb%2Bygp8ij6iKmlzoFNldPrmyLuuroQ38gzScwYUw71D37ikN11MR40p%2FAzj6pSGP2XLXpu8BPaSAmCG8n1F4tBfzK2JwAcdTrdGQkyj%2BlRvDRFeo4JVKHuGtr8WXMqjmMT4huPwqWzg8PNSdkxr1JI%2Bnd5rQswH2NDcEhYmkHv8NpUhcWeh9M97l5%2Bpgx0c3Ye7TiGThSAbyllYefs6RUnR8GnDSq1z0uVwkWMGzh3ieQLziwdgo9iIzczA2B22ZofQyB2LIzRdSoNqseEOX2wYzrJnGWrZpAYrPLksWp8HHF%2BB5XVvdpLLl15XwI8fclcvcONiocS49J5xTubBakHzeIgIrTL6nWu3gYmF6nTteX1y14%2BALI4YoMeKdKcR3UizlrRAi3WHsiNs%2BR4CsmSMcigahAaeByyaGbn6yjpLd67%2BrNnINvAImb24eXx732j8JMZxFYh23YfJjHvtp%2FVJd9FOAxJTnLMKw1WxzrWstFUZr%2BsdxM63AQekoA3%2BmpWoP0wSbSA2adxYIlGVD0Vw7BpYM21qZUzsALfGj%2FZRvd2Yp0dwhKhkjjqynUgBN23ap0YVlisMIqNwcQGOqUB0GeRjiZ3%2FVxTeXuXJywbRUCiL%2BY5mP%2BolqAcPO%2FDYhmXiKj5P%2Fw2oQIW%2B3EqWxY915mMliC1MNnzjQZrHwZn3PXBuuaDQTq2hLpL0kuP7xvytM6%2FeeCZ3qEssXlFwwoaOJVTKd4lZfLXaF%2B2xbtQ1NXlVNxsYe%2FExWoWb4AvfU9jybg3z%2BlFx2ccE%2FBkLbIXAbeAsLqI8Iq9Ylp0K%2Bl%2Bibd3G49V&X-Amz-Signature=3feab7b7ec4118b30dc85bfa3485bf7ace51a798d43e14c66c50905e83b8f7e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- StorageClass를 사용하려면 클라우드와 같은 가상화 디스크가 필요하다.
### Storage Class AWS예제

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
reclaimPolicy: Retain
allowVolumeExpansion: true
mountOptions:
  - debug
volumeBindingMode: Immediate
```

## 동적 프로비저닝 동작 순서

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/4deceb2e-be54-4ca5-a849-072950ce7305/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNI4VAUF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCICCkF1RKpNE5ZJ1F0PSC6SvrIROcKt%2BgPaXAWApFjvOsAiEAgsUlstyPVaDfa%2B9V1OvH2LzSOE%2BwsaKo7UIrMcd8YUYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDL%2FaxnI0qe1GsA0fpCrcAxvO0dhgmiB6C1GPCRUn7cy5mOvrLx%2Fz01AQbdeRELnQW6vAdrLb%2Bygp8ij6iKmlzoFNldPrmyLuuroQ38gzScwYUw71D37ikN11MR40p%2FAzj6pSGP2XLXpu8BPaSAmCG8n1F4tBfzK2JwAcdTrdGQkyj%2BlRvDRFeo4JVKHuGtr8WXMqjmMT4huPwqWzg8PNSdkxr1JI%2Bnd5rQswH2NDcEhYmkHv8NpUhcWeh9M97l5%2Bpgx0c3Ye7TiGThSAbyllYefs6RUnR8GnDSq1z0uVwkWMGzh3ieQLziwdgo9iIzczA2B22ZofQyB2LIzRdSoNqseEOX2wYzrJnGWrZpAYrPLksWp8HHF%2BB5XVvdpLLl15XwI8fclcvcONiocS49J5xTubBakHzeIgIrTL6nWu3gYmF6nTteX1y14%2BALI4YoMeKdKcR3UizlrRAi3WHsiNs%2BR4CsmSMcigahAaeByyaGbn6yjpLd67%2BrNnINvAImb24eXx732j8JMZxFYh23YfJjHvtp%2FVJd9FOAxJTnLMKw1WxzrWstFUZr%2BsdxM63AQekoA3%2BmpWoP0wSbSA2adxYIlGVD0Vw7BpYM21qZUzsALfGj%2FZRvd2Yp0dwhKhkjjqynUgBN23ap0YVlisMIqNwcQGOqUB0GeRjiZ3%2FVxTeXuXJywbRUCiL%2BY5mP%2BolqAcPO%2FDYhmXiKj5P%2Fw2oQIW%2B3EqWxY915mMliC1MNnzjQZrHwZn3PXBuuaDQTq2hLpL0kuP7xvytM6%2FeeCZ3qEssXlFwwoaOJVTKd4lZfLXaF%2B2xbtQ1NXlVNxsYe%2FExWoWb4AvfU9jybg3z%2BlFx2ccE%2FBkLbIXAbeAsLqI8Iq9Ylp0K%2Bl%2Bibd3G49V&X-Amz-Signature=65eacb0fa9614ac42190815838ad3df4d5bba30db31bfaf0c909bf281ad1560a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# PV 리소스 반환의 옵션 3가지

### **Retain(보존)**

`Retain` 반환 정책은 리소스를 수동으로 반환할 수 있게 한다. 퍼시스턴트볼륨클레임이 삭제되면 퍼시스턴트볼륨은 여전히 존재하며 볼륨은 "릴리스 된" 것으로 간주된다. 그러나 이전 요청자의 데이터가 여전히 볼륨에 남아 있기 때문에 다른 요청에 대해서는 아직 사용할 수 없다. 관리자는 다음 단계에 따라 볼륨을 수동으로 반환할 수 있다.

동일한 스토리지 자산을 재사용하려는 경우, 동일한 스토리지 자산 정의로 새 퍼시스턴트볼륨을 생성한다.

### **Delete(삭제)**

`Delete` 반환 정책을 지원하는 볼륨 플러그인의 경우, 삭제는 쿠버네티스에서 퍼시스턴트볼륨 오브젝트와 외부 인프라(예: AWS EBS, GCE PD, Azure Disk 또는 Cinder 볼륨)의 관련 스토리지 자산을 모두 삭제한다. 동적으로 프로비저닝된 볼륨은 스토리지클래스의 반환 정책을 상속하며 기본값은 `Delete`이다. 관리자는 사용자의 기대에 따라 스토리지클래스를 구성해야 한다. 그렇지 않으면 PV를 생성한 후 PV를 수정하거나 패치해야 한다. 퍼시스턴트볼륨의 반환 정책 변경을 참고하길 바란다.

### **Recycle(재활용)**

**경고: **`**Recycle**`** 반환 정책은 더 이상 사용하지 않는다. 대신 권장되는 방식은 동적 프로비저닝을 사용하는 것이다.**

기본 볼륨 플러그인에서 지원하는 경우 `Recycle` 반환 정책은 볼륨에서 기본 스크럽(`rm -rf /thevolume/*`)을 수행하고 새 클레임에 다시 사용할 수 있도록 한다.

그러나 관리자는 레퍼런스에 설명된 대로 쿠버네티스 컨트롤러 관리자 커맨드라인 인자(command line arguments)를 사용하여 사용자 정의 재활용 파드 템플릿을 구성할 수 있다. 사용자 정의 재활용 파드 템플릿에는 아래 예와 같이 `volumes` 명세가 포함되어야 한다.


