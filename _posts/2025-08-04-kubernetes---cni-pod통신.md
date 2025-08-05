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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2ae01027-be35-4a98-812b-4fe47306e572/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGAWJCB5%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDm5GBKdaTLnirF352B3gVRauCGmnPltdmXq7S8GoAkkgIgIoObFPf2GHbi%2F9Wza6DyY7uETUok9ygD1uZ8MJynPtkq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDCokBkdOqTd0QMfssircA%2BKn2CwutGEy9KDQ8egyQcepuOJz1pPsZJa2ihN%2FlspOwVbE8gB8BT5tNCATWe%2FM3RfvdE0qih6RVLO2NWtYnTGfzLIQDufPiad28xOR7eBvfVO%2FF9GPgX%2FsRcP8fLtrnFtAN%2Bq5BRJvz4evAF7sAnOhTaH8QMRzrW5Qf2kcQ%2FVnAP%2BvS1v6ZHLWVGKsP4%2B4tNlm%2BURs41KPKySyFEG%2FwgjvpJ%2F6x7F2miUzOT0UDGQa0NDtUlDPSuU33BRXHhWLIyJa0OuGmf%2BIuiEKwIqIDsRzMj8jgWVYGIbqZg51M4SxgK3UhdBRJzctdHJz%2FL0r4Ij12oM9ZKlGwc6%2B%2By9PP4hlgUnOpBCgJsgpWghRbHxfbAfCXs%2FVMLYjB6iQ5AGEmwzm5YnyKOtvQQtpVaFHEHXv96eETVZAd4rSlUA81skhOvD2NunaWdofZ8JZk47EmxkkEt1imqF5tQT48NM6FmHeQFgLQumEzNeUoJ59SimhAPmFh1d9jDwm%2F7HSSpv7SzQRRVEc2T628aeCHGb81dtDUPPjRBnjQfAtLRXsawJJ8v4%2F7Grt1GxZKyeyZRSHFgd3bQa02Rb%2BTcdzrCeCshLPy9G%2Fl8%2FU3Br8%2Btj98kOkJpXMlbyLJ4R2pntAMM%2F0xMQGOqUBmrOGprqEi1fECp4IOqD40AcuoxCRJxObdgmwrL67OAc%2BjRyT%2BvGpcju27nEOJ7fDj4Alk0kxuTlCI3jIfhCPJLNqOog53ow3TYe2fjAaWLssxRWzJXhyFqf8f%2Btig7dv2xomyB3UjoDcPLOSmKn1SlgkAaFpdiaz%2Fyz7BopUtTrshlbUntG5HkwloYIPX0v1r4hn%2B6VukztaArz%2B2Z4v%2BjxnOueu&X-Amz-Signature=db8281ad18d4235a313ad3d8ce7a7884b1e764f12c55ebbcb62c298e2742e2df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


