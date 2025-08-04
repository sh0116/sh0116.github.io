---
title: "**AWS Event Engine 사용기**"
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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f9e7a059-46e2-4def-9ad9-f5c46e3d7f2c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YV2HCQF4%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDkvwbShbPwanCMOY3dHtzferh4sHxeZxr6VyYi%2FyuuCwIgbeGQ3MCWP4rTq2d3doMpNHnp6AY58crplixCXMsNj3sq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDPS9rOQ%2F%2BZRAfuu9LyrcA1L5LtId%2FkXsuv7HVAz0%2BmarfvzC5kPVgkTNh3XBvC1qUZjP%2B%2BidgZlqeDJ1IazQV9rmTD76s%2FVInMN68vqXi1YlsgIC8TumKT9qW1cvzInGtHVPSSsSgLGvI1MPoa4UBWfSydYZHslpd%2FnbccfdwXdRnnGE0%2BbdjZ%2B7NOXV4R405UWHaE3mNCWvbxTMIBiS7RxtVlf4KzLl0vXiRmiUDxxu5oZXV27BIGZqzD1pkqKhMCT7rsy6oVB%2FK3frE%2FnRA8RxvWuc3iyPcJBi7rboctUod%2FLIY8xLZ3Gr8jGxGHPkCDTiB%2BlD7%2FJC95x6A8J3Lwl38QVrbgI7vOI026vSdGttqVueNmUAZ46Nq8SQtbbegm9AqxrF7BmlRH6pUrJsuGroaIcF%2BdPDPPvU1T3%2Fssi%2B8fX5ZeeQ8z65O3cXZbRuIdOayMHaA6%2FOFSkmK%2FQXyQ3Z1RZnEDfC7Td3uiM3tYAnYMmWSRfjgl%2FKoAlyYt1ulmmIkTRLBlRW3pWhze6mJU3ZuylnPlzlHhxWOKgdv7Aza2W5Tc9fJ2jU1187E2%2BvI8Ew1yn5cP0%2BFog78Nw2yALGkTUTAB2alnGLqts1fKNt89wFcTL8GvRyO%2BBSA%2F153pwkjErWnHLkT9gdMM62wcQGOqUBbyqKlYnRygthAmhlxNKRxinbv8vcZdJ2LGbvRiU8ebvJ5R0OixTk9tRIoPnYcxATqSlIt4%2F3EYqo6K2aAGx6ZNZvmYhN3jfNXOddEtZac1eOwPMzCAwM2ZpcMywH1fAucHZyVtL9BaK9NU5HY7StpqYWOtfkN3F6plGOp0Z3sktY9PANBnx%2Bx9lVQU1M%2BJ8XrSJNkF%2BOL6qtJGGKsGyA4OANG%2Br%2B&X-Amz-Signature=8fd96de2312cf7097a6e84110ec57e11190038d5d4f944a85674c1278aeafc12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


