---
title: "AWS Event Engine 사용기"
date: 2025-08-04 06:05:00 +0900
categories: [세미나]
tags: [AWS]
description: AWS 세미나 리뷰
toc: true
comments: true
---

AWS Event Engine 워크샵 Portal에 로그인하여 실습을 진행하실 경우, **Team Hash** 값이 필요합니다. 여기를 클릭 한 후, 이벤트 주최자로부터 받은 12자리 **Participant Hash** 값을 입력하면 오른쪽 하단 버튼이 **Accept Terms & Login**으로 변경됩니다. 다음 단계로 넘어가기 위해, 해당 버튼을 누릅니다.

![Image](https://static.us-east-1.prod.workshops.aws/public/c63c1c87-bab3-4c57-8c69-af5581bfbb8a/static/images/eventengine/event-engine-01.png)

**Email One-Time Password (OTP)** 버튼을 누릅니다.

![Image](https://static.us-east-1.prod.workshops.aws/public/c63c1c87-bab3-4c57-8c69-af5581bfbb8a/static/images/eventengine/event-engine-02.png)

본인의 이메일 계정을 작성하고 **Send Code** 버튼을 누릅니다.

![Image](https://static.us-east-1.prod.workshops.aws/public/c63c1c87-bab3-4c57-8c69-af5581bfbb8a/static/images/eventengine/event-engine-03.png)

작성한 이메일 수신함에서 제목이 **Your one-time passcode** 이메일을 확인하고 아래와 같은 passcode를 복사합니다.

![Image](https://static.us-east-1.prod.workshops.aws/public/c63c1c87-bab3-4c57-8c69-af5581bfbb8a/static/images/eventengine/event-engine-04.png)

복사한 passcode를 아래와 같이 붙여넣기 한 뒤, **Sign in** 버튼을 누릅니다.

![Image](https://static.us-east-1.prod.workshops.aws/public/c63c1c87-bab3-4c57-8c69-af5581bfbb8a/static/images/eventengine/event-engine-05.png)

다음 화면에서 **AWS Console 버튼**을 누르면 콘솔에 로그인할 수 있는 로그인 링크를 받을 수 있습니다.

![Image](https://static.us-east-1.prod.workshops.aws/public/c63c1c87-bab3-4c57-8c69-af5581bfbb8a/static/images/eventengine/event-engine-06.png)

**Open AWS Console 버튼**을 누르면 AWS Console 창으로 접속할 수 있습니다. 또한, CLI 환경을 위한 Access Key와 Secret Access Key도 확인할 수 있습니다.

![Image](https://static.us-east-1.prod.workshops.aws/public/c63c1c87-bab3-4c57-8c69-af5581bfbb8a/static/images/eventengine/event-engine-07.png)

위의 단계를 모두 수행했다면 실습을 시작할 수 있습니다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f9e7a059-46e2-4def-9ad9-f5c46e3d7f2c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGVK3NZC%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQC4sdfBHa9iGy8MoRwGPPKaE4h1RMgWP52yz2waoRFzTAIhALcv5djhWU5dYgi3AiR%2Ba11H2pXhz0An2HtCQ1d4ZkFrKv8DCFAQABoMNjM3NDIzMTgzODA1Igw00dHMp%2F0FxipUIJwq3AO8N721hVZTqiTxZsX78EVHiHdH0udCj22xeGk136taw8L3uTw%2BS6RaBSPrbSn2a7l1dFuBXgdNs7TJH%2Ff8vFlftbGOyalIeLfO0YyocCiOEzN0O857ulu2%2Fjgp0ndBEWCM8hOZHDJ4mVz3Ll0klpinLt1smt0cJ0NzzC5HHDKYjyLI%2BNe%2BrA0l6n%2FCFbjWAdUueC0NSZV1h8T2DFa6%2BronKHc5Zg0cRObOO%2FYp8mPlXSDWEM7m6qgO1LX1fqyC7lYW6XlYgWQ2yyiT4huUQwLJI1%2B6JHX0thjxPPFQrBx4HsuMEtNvA2Lv2v99XdDHJIZJjizHXiV6t2OVGyI5DmB8qiHUbY7MNU7UjmNdC1FmUjhRaMQd88cDB45zSrMa9GF5AZoKV00%2F%2FfisSJzm0BsgJjw6kbpcauw8R4Fde3lZ%2Bi4sIWmA%2BvD71nwWy%2FSuvMkzwrntZTUEqupAi367smQPOm8jVBC9gC1TEejhIqMiUf2LdrN5rtCqspNxqSrUTDTNwAqJzB90%2BO4sMM7GgLTRw4P2hb3bdoHlRhMHTuhZuXjPZzhn733ivVFJxfxzkbE2GJ99LWYUdc0jQYTBwFdekfL20J5h15LmZ6Cp9YQSXwymhyFNUbPFPLy%2BPjD088TEBjqkAf0VlqnDeRptuFsBmWSYESHTPUZte38rCl2PdrMogd%2Bf9tZ6PESBHPSUqEcs6I8X1ypFCJCeWLBvJTFVNEQDITZHJHXCceiTK5QbxwqYXzsJmbHZE5hQFARaxSrGwBPUv00LnhEQ4QgpZfWKR6yfIkvFg%2BLXS1nzOjEw2P%2BPwUQAyffMVAsh6nMNGtT0hozc4GXGxz7K0rTKNj7fuX2IXyij7aOR&X-Amz-Signature=f16b1176ef73936e0b14ff037d60faf048b6f07eee2e45e5a7ade4910bdf87b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


