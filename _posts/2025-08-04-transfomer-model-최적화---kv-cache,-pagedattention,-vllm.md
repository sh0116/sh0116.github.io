---
title: "Transfomer model 최적화 - KV Cache, PagedAttention, vLLM"
date: 2025-08-04 06:05:00 +0900
categories: [기술소개]
tags: [Transfomer, LLM, AI]
description: Transfomer model 기술 소개
toc: true
comments: true
---

# Transfomer model 최적화 - KV Cache, PagedAttention, vLLM

Transfomer 모델을 최적화하기 위한 방식 KV Cache와 해당 방법의 단점을 보완한 Paged KV Cache방식 그리고 실제 응용 사례인 vLLM을 소개하는 페이지이다. 

## KV Cache

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d2dedcd2-1e43-4280-baf2-bb42f853c099/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UT4FVH4%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCICu52%2B38%2BnJzXncDWHYD0iuS5mnT%2FlcVbj54RU3GKePBAiEAwVNGLAT1CK%2FsAjLyMqOcaQT%2Fk8VeKcGbxf1ghnJ%2F6O8q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDM08FtUVBG4hzV5TRyrcA1Wc2srBpk6zjvDZXqQlDJcIsyVztU8xk6GThiKN5WbHENxF0bMN9Y5LoyXjCm%2Fq52HsK3cmhwWEC%2B9WC4ihsOq4jfWcWUWx6WSx0XJf9MraaVHPcVcin8OVhxceqzmlE8%2FlZ0%2BBBHodkfded9I1aVW%2FeZlF9Fh23GN%2BygF601Dhzo1xV7CjUSi6fJmCYgDWKMecDQbL5gYEYHywdPuvViD0KSk8utOfO7k%2FidgwY40D%2F8pCbXQEby70DaRFp4WhMVY%2BjYdfGXaSuEI93CQ8v%2Fw2jSWdGdd3a04r%2FJY%2FOYwMy74maZ8UsSV5cypP4AHqVnNk9c6d9AW%2Bmsv5OthykgIHHXvU8pVTmwYPx9w9%2Bfei03i8fLR866NDtbt78ro3Y4XerDlgzGHBGXrXcGwt30gheR7RckNFMc6yNtkiA3Ulxm%2F27zrD8P5ndBFmhXvechYnx%2FBt2bI0%2Fg644tIDPu4hZ9a8d573peLJrVkFtSic%2BmQTsEHbjkot3B5bluzpM3OLvURdrAUG3szIkqWa4Am6QddJLrqgYfBR%2FBjDsREsaXJT5JFBR0YvlYPZIETcpzR7a84%2B1qkCtUmxmHjh%2BxRwGrPYl9%2B4bndimoD2G5QuHoJVi23kLWnO0P1fMKm4wcQGOqUB7qXUINlaSiQOiB%2B75rvkulOzGV0zQiKZ40tSPazdzA1egGRoq0SmPae5xKg3CnmKQQEXEovDXObJPK7ZNnLQ3WB0K0IQ%2FuyPNd9b8M42IgvF%2F1TkO8yuTzkvPDXxcYdeMi0PaexBbZtwNu5hw4qlRz7T7DLVyxQDsnvYLd46PrNYfJuxwMuanq2hWXTiCHzfE%2FW%2BxJ0t0HpDUQj8Q02FYZB%2BXzGC&X-Amz-Signature=420efd27a0772a695cc61c733ec742f576eee2da32f8a501b8d8a4c97249eedb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

트랜스포머 모델의 Attention 매커니즘을 짧게 소개하자면 Scaled Dot-Product Attention 연산을 여러 겹 올린 Multi-Head Attention 이 기본적이다.

이 모델 구조에서 Scaled Dot-Product Attention 연산을 반복적으로 수행하게 되는데 이 과정에서 중복된 연산이 많이 일어난다. 

Decoder에서 토큰을 생성하면서 Scaled Dot-Product Attention을 반복적으로 수행하는 과정 속에서 이전 토큰들의 계산을 중복적으로 계산을 하는데 이 과정을 Cache를 통해서 일정량의 저장비용을 통해 연산비용을 줄이는 기술이 KV Cache이다!

(KV Cahce인 이유는Key와 Value 영역의 정보를 Cache하기 때문에)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/75f005c6-c2f9-45e8-ad7a-efb9ebedb50e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UT4FVH4%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCICu52%2B38%2BnJzXncDWHYD0iuS5mnT%2FlcVbj54RU3GKePBAiEAwVNGLAT1CK%2FsAjLyMqOcaQT%2Fk8VeKcGbxf1ghnJ%2F6O8q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDM08FtUVBG4hzV5TRyrcA1Wc2srBpk6zjvDZXqQlDJcIsyVztU8xk6GThiKN5WbHENxF0bMN9Y5LoyXjCm%2Fq52HsK3cmhwWEC%2B9WC4ihsOq4jfWcWUWx6WSx0XJf9MraaVHPcVcin8OVhxceqzmlE8%2FlZ0%2BBBHodkfded9I1aVW%2FeZlF9Fh23GN%2BygF601Dhzo1xV7CjUSi6fJmCYgDWKMecDQbL5gYEYHywdPuvViD0KSk8utOfO7k%2FidgwY40D%2F8pCbXQEby70DaRFp4WhMVY%2BjYdfGXaSuEI93CQ8v%2Fw2jSWdGdd3a04r%2FJY%2FOYwMy74maZ8UsSV5cypP4AHqVnNk9c6d9AW%2Bmsv5OthykgIHHXvU8pVTmwYPx9w9%2Bfei03i8fLR866NDtbt78ro3Y4XerDlgzGHBGXrXcGwt30gheR7RckNFMc6yNtkiA3Ulxm%2F27zrD8P5ndBFmhXvechYnx%2FBt2bI0%2Fg644tIDPu4hZ9a8d573peLJrVkFtSic%2BmQTsEHbjkot3B5bluzpM3OLvURdrAUG3szIkqWa4Am6QddJLrqgYfBR%2FBjDsREsaXJT5JFBR0YvlYPZIETcpzR7a84%2B1qkCtUmxmHjh%2BxRwGrPYl9%2B4bndimoD2G5QuHoJVi23kLWnO0P1fMKm4wcQGOqUB7qXUINlaSiQOiB%2B75rvkulOzGV0zQiKZ40tSPazdzA1egGRoq0SmPae5xKg3CnmKQQEXEovDXObJPK7ZNnLQ3WB0K0IQ%2FuyPNd9b8M42IgvF%2F1TkO8yuTzkvPDXxcYdeMi0PaexBbZtwNu5hw4qlRz7T7DLVyxQDsnvYLd46PrNYfJuxwMuanq2hWXTiCHzfE%2FW%2BxJ0t0HpDUQj8Q02FYZB%2BXzGC&X-Amz-Signature=2b8ce1fe1b2591c3b28ad251d357154e2613afe06f6d5762af28e4fb1d36ed95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

결국 백터의 내적 계산을 반복적으로 수행하는 것 이기 때문에

K^t에서 Token1,2,3을 기억하고 있다면 Token 4의 Attention을 구할 때 굳이 1,2,3을 다시 계산할 필요가 없다. 

### KV 캐싱 문제점

### 참조


