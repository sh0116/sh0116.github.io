---
title: "Kubernetes - Storage"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# 쿠버네티스 Storage 개념

### 불륨(Volume)

- 컨테이너가 외부 스토리지에 엑세스하고 공유하는 방법
- POD의 컨테이너에는 고유의 분리된 파일 시스템이 존재
- Volume은 POD의 컴포넌트이며 POD의 스펙에 의해 정의
- 독립적인 쿠버네티스의 오브젝트가 아니며 스스로 생성, 삭제 불가
- 각 컨테이너의 파일 시스템의 불륨을 마운트하여 생성
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d08779ff-3c8c-4b96-8118-7844ca4a7e40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXL2PDZI%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCID1Tp8OmkASIxx9QYsAzueeTQLa%2B%2Fb%2BXw4VAJACtN9YCAiEAvIEEvrK%2B0DeR7id9SkROGa3gsz%2Fp8MH1BunvHjjkENAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDGXCy1RJIo7miyrwxyrcA67p1VpAtL4cH5c6ttHyIxgk36ryIkhmuWE5E5a09WhSbjFnxNaqr4qerwzR9NrJbRNH6A0Ub2PdB31GtAsInm2%2B5pgQlW9XTqFWpIEW7uMi4umF%2FyH%2B1OOqy%2B16Rfh3eGnBtOF4M5aOsW%2BbJDCV5gsM7gMJsFwT9ibe%2F5JbEHhQq1hFssjMAYbSAj9aeY9E%2BJgKbou1Qgi4dIYg91DDTsJFaniPT21UYRTEnQ2WqsNs8yAvdYFR1GkEIQNy7Yg1xviqF7YZUK7ZTD83rWn128S5LdqTVp8A8KGnjLrUCKwh4XSjszqfiYxcjJCnZ0HTZpvDRkCN6EMmSvskjpxZrq%2Fm6sWX1BhVYg2RFzupimziBTZCbNtfz7EPsh7oZZwpFpWGAWGJpQpstx6XY0DdfICiPN82HE%2B3FP5%2B5bR0bHX73D%2BhVC0B8E91PNYW1rw6J00l9cfJPcgfy0r0IMkZhgXli75dAopRYYzJhUWTI5OUm410fwxujG8yW7w0GBpjmvAJzB724KMj%2BYxn9ZcB3wMA348E1iT8AVDiQuBsGkv0HdLe1oMUsQEawjQsLq9BRyXyOOONIXoUXpOZ20rsgNN3wK6uWV4kxRkQGZ3UcFAqak5yx0tXyMZgq5mbMMONwcQGOqUBEM%2Bbuv8mCYs5cms3Bwl0mReT2KzCCgxxpLn5a1p3iMcPNV1GBQLKTg%2BFDvSnVymxZoFx%2BDIM0wJ6ZHPXl18Ouz6AQmUYdbNTdr4YAlHK5ym%2BZjzU9b5L5Md432osvA%2FK6yw2Ad89FxwHZy48EY%2BDhakZEVSbtQrU6jYzUB06VjgxcijHnQze%2Bhys7kGO9aA1Cdu5vKQgtHI0KUN3QwZ7V3zIcuWJ&X-Amz-Signature=681964634720f38cb70cf2c9d636ad6b4aafc3f7df00013c96209486b6c3bffb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 임시 볼륨 : 
- 로컬 볼륨 :
- 네트워크 볼륨 :
- 네트워크 볼륨 (클라우드 종속) :
# EmptyDir 을 활용한 파일 시스템 공유

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/0fd040f0-b611-4ac4-887d-76487068320b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXL2PDZI%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCID1Tp8OmkASIxx9QYsAzueeTQLa%2B%2Fb%2BXw4VAJACtN9YCAiEAvIEEvrK%2B0DeR7id9SkROGa3gsz%2Fp8MH1BunvHjjkENAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDGXCy1RJIo7miyrwxyrcA67p1VpAtL4cH5c6ttHyIxgk36ryIkhmuWE5E5a09WhSbjFnxNaqr4qerwzR9NrJbRNH6A0Ub2PdB31GtAsInm2%2B5pgQlW9XTqFWpIEW7uMi4umF%2FyH%2B1OOqy%2B16Rfh3eGnBtOF4M5aOsW%2BbJDCV5gsM7gMJsFwT9ibe%2F5JbEHhQq1hFssjMAYbSAj9aeY9E%2BJgKbou1Qgi4dIYg91DDTsJFaniPT21UYRTEnQ2WqsNs8yAvdYFR1GkEIQNy7Yg1xviqF7YZUK7ZTD83rWn128S5LdqTVp8A8KGnjLrUCKwh4XSjszqfiYxcjJCnZ0HTZpvDRkCN6EMmSvskjpxZrq%2Fm6sWX1BhVYg2RFzupimziBTZCbNtfz7EPsh7oZZwpFpWGAWGJpQpstx6XY0DdfICiPN82HE%2B3FP5%2B5bR0bHX73D%2BhVC0B8E91PNYW1rw6J00l9cfJPcgfy0r0IMkZhgXli75dAopRYYzJhUWTI5OUm410fwxujG8yW7w0GBpjmvAJzB724KMj%2BYxn9ZcB3wMA348E1iT8AVDiQuBsGkv0HdLe1oMUsQEawjQsLq9BRyXyOOONIXoUXpOZ20rsgNN3wK6uWV4kxRkQGZ3UcFAqak5yx0tXyMZgq5mbMMONwcQGOqUBEM%2Bbuv8mCYs5cms3Bwl0mReT2KzCCgxxpLn5a1p3iMcPNV1GBQLKTg%2BFDvSnVymxZoFx%2BDIM0wJ6ZHPXl18Ouz6AQmUYdbNTdr4YAlHK5ym%2BZjzU9b5L5Md432osvA%2FK6yw2Ad89FxwHZy48EY%2BDhakZEVSbtQrU6jYzUB06VjgxcijHnQze%2Bhys7kGO9aA1Cdu5vKQgtHI0KUN3QwZ7V3zIcuWJ&X-Amz-Signature=4135ee04e5643b0145749abf851ae8364e50083cfd4b79cb47a16d70ca39e996&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## EmptyDir 연습문제

- 하나의 프로세스는 랜덤한 값을 생성 (count 이미지 사용)
- 하나의 프로세스는 랜덤한 값을 출력 (httpd이미지 사용)

