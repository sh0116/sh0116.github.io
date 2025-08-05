---
title: "Kubernetes - CNI pod통신"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# CNI 플러그인

- pod끼리 통신을 하여면 CNI플러그인이 필요함
- ACI, AOS, AWS VPN CNI, CNI-Genie, GCE, Weave Net, Calico 등
### Weave Net 사용

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2ae01027-be35-4a98-812b-4fe47306e572/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLX75ZDU%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIGlBG%2FuVodpQS23aLfL%2BYXek3f8hnt7TP0SQGDxqiI6uAiBZIPdCOekgW1gG3quKPmFrGOW%2Fujs8HSY%2BfhNpn0RYPir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMhqmTYgHkCo0aJ6AkKtwDpv1ag29YnoQzQDaOxIrFAww8OvHn8Y3L%2Fof6HbWXfTExYYweU2MX42cEu4suD1nFOigh0S%2BH9HVPj6ijqs13za4lrnQurmkYq1HJt6Wx07X6QqK0639wR9LxUUPR10AkuzlHCdsVcKiMtkPOjHixRpaXYgDPMaC96MBtVPy3q7yjtuChkE%2BSub8xJBuSljKqB3q8U%2FiymJ59HmJU8tPcf9J5IVXr8LCiONNjaoZXyHPjGuzje99TXX5ElgbsrBrX5w5xH1fLDZsSJ7lke8yU2b25kND6gDJgVxiP8F%2ByEYIhOQlG2EqFYcskuJiTVBvrEkaPNaG%2FD%2Bk8TUAe16sSUeXlYy3rMPTUgLvjhKuDfWt06KV4g9kN2%2FKwfe0wou3131U5GikiDtKs6DgL1PSyHuRbc5GYepxBqVjM7PoZPWmsQlUduKsyzG443uL5zzsV087ze81WKE8aDPRemg65GSjlCgImyutPetOhRh7jknSl3m6YX%2FDaI51qxTgdFg4swDciE5kzDYNRKvXwg%2B9xxfgJLjZxQGcjC5giSw%2FsKw%2B7v6ZdnewlsF0LzscFJ7U%2Bi%2FgKEV8tKMA5lbX914cvK6Bp2%2FDajPxMmZNVE95cYUzSf5NJQlWfcqDpztswtLPGxAY6pgHNp5fBPDyVliBMPO8h9ZwFFghYp3ZCfoeU9S%2FZsWlIKdsmrco7kXaL34JjeOC9dzHLNJqNtrIhBVhBkZ8q8fDo1vxX9%2F19n2wI7zI6hESoxUvH%2BExGO27sDD%2Bik5uFUSOq0T7ii7Lo36OdfUQuTfzv0gOxaV3TDl1Ags90neBTkdaQCLY8YCUM7pfLpxHBSxt6cDfYr4azM0t0aF7Nw3EN1Twwwj5Y&X-Amz-Signature=897795b003b5adc79715e8c7bd5ab503b6cffab7237bcc261d787e59b177af56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


