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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2ae01027-be35-4a98-812b-4fe47306e572/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAYNSN7%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIEez%2Fou%2BdSQqYlxJTblzE%2BySnkwsiuGNmBbf6%2BSxRSXbAiEAynfS2E8%2BnJtkpvKmCYd1f3%2FbnQOI%2F20gzE3WWzIxpo8q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLeAQbgEjbUZa%2BMpdCrcA2jwf5QrFluwrqPmzSblvLomUzoVXNIwvArH%2FfJZcY3l%2FFrUpVafBq9gG3UdVRLhIoPWejnk3WHZqmtH1yAq41xpff2UYh09687Al7hm5DPVu%2F8fR0lhNOKZipx%2FuowmmK%2BLB%2B7vulhdssWjD4Uck8EMqKgXaUQBmUttciNm%2FJesjKkrvVRtolWBKzaRPip8LOUJuYVtR%2B45O6%2FRbDV44a0pvqm7ZGraV5Bm%2FeMEAVh6VUBgL57LRaSqP0rRI6m5AnOa9vaBOQZDnnNfuETYe1I0nAFcwA8XncssaaulUv5PcopG02Jdwdp7F%2Bd6B1IZl1v%2FkG%2FHOj3xVtBC0XXfOd2NnU%2FUtQlgzPnu%2BJW%2BQ6bdny7DtjLOBPtxcrIw4D8rn997C4xVYI4cFB%2FyhQO%2BLwcAIVUgiNfwU5E1bzGg9JjMtWc9N2h8mcasIaXG9guofy7l45SFNn4LhHWLIsAuyoBtfwaI4jAgFP4HxQ72OqwH%2Ba9xB7SFTVslFofs8xxdJdshP0Tj8axdDEZbfjnoFul%2FdXY9EgcFejPi%2F6vQ7IffIUco8u%2FSGwgjZao%2FnLIPvhVAL8KZ1VYvGydebFbsIgsnOx1wIXlhCQx%2BS%2BBj9NQpOA9l1LuQ391SuiX1MLy2wcQGOqUB9y%2BLYUcvzD6qh%2FlWs5%2FqiRvyhVIF7WrVvy8gomC57M9A5tChyxIYBeHTdx4Vw9cS537ewmkVB7LTAVu67FsYs4UdE4dJHrWkD94yH6XhvjTsUwPsbY38aql9y9Ww%2BkVyCY3Ocr2hP%2BPLVVKfjnfjcG5If1EmYsgEA38IhXQYwXKa2txeeOlpIfAQ8SnWUVzqvmvgd%2FFsiyYe1pZsBB4VpAVqF%2Ft%2F&X-Amz-Signature=5cc568e6680243ad86159f1b2653d39b36d2d87d04ef98fc642e526c97ef98e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


