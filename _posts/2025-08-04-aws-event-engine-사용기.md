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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f9e7a059-46e2-4def-9ad9-f5c46e3d7f2c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIOMFHSR%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQC4BD7Xw46y2RcOQfJsPiee34eU%2F%2FNtiLLEA4GiLPZkOwIhAJeSJgHw5U17CXwlyAS2BlnkbuY8WNgPoZgzrUBL5VdnKv8DCFcQABoMNjM3NDIzMTgzODA1IgwJdPQHq41ibE8qs0Qq3AMC%2FinN%2FthiKcBZPuJaCeCNMslimJtiRdADJRrGgvADwdoGircUD8Z5mulBN%2BQjE7Y2tGsiUWgezNd2RLsA6L6YsN7940rY0wMRTF%2Bsc7ckllCkhT54FrvW6p8r8OUh2RLebmFWVQvJxmN1QPVWHmN6JKjHH1RS6jcbZWYR%2FqAORRAbzHeR9L54H6qThZgCnCaPRC4C32iY77OxhVZjrsildnfekWWNHE%2FEDS%2FgKwGs3CwKbdbEf8II82fCoYNQmnZOkFn1yDBCBME7NDHCwjzZGTNAkXJtDpskeT7aPe1H%2FgF2mUnkt26j885KDurAxjvS3Zb2qIjmOm2NWW77iT3eDkrHvRkBnKU9DPx5ZPnfgQyLrM2XXnl%2Fatppo4ecGZZevMLkQrGJejFWy35Mw%2B8bnzmosuuxDhKZWXYSUGC%2FpIityuR%2B8NujyjD0SS%2BQzK3hSbMYwiGnx6eiHc%2Fgk6WortPZ%2FRTBjI2ebNV%2BARW4iGzs1yJpj4naT1HAzkbx6qGcdrl16wUClu%2FZCUN5oL5XKTZsyerLFN7C%2B0L3BSGTXksmi0oF9nF9cdaTPm7UlP09fzovyc3opr3YvBGoDxcWeMfrvzZJ2O8A6%2Bh%2FKN2Kcui8CEl%2B6onWYVw4BzCptMbEBjqkAZopbNO4MKiEchlQ9%2BjeF215C1iOcC8E1rpp5ydL8JWLQeJGVNFJdlgHTwp5M4Lm%2B%2BXdhuMeCBKyKwRgfggQWNczQVCsxZYDnfmcH7wOog%2FHqeIOcnEk4%2BHaSf8hN%2BJmGob1Dq5unJhxaqb1SxPz1iDkKYqlRjEhQCioZXSURSl%2FIZuQIeP8mMCLw8aNzCFpnzQODRXbUymHtXIcPKPWRF2U8Ezw&X-Amz-Signature=e34f0c616311a8e4ffe114ce0b1c35b2037a085d77f922ab6531562161886c06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


