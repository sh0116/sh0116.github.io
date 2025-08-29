---
title: "LS Electric XGT Protocol 정리 - Python"
date: 2025-08-28 09:14:00 +0900
categories: [PLC]
tags: [XGT, PLC, Hardware]
description: LS Electric XGT Protocol Python 사용법
toc: true
comments: true
---

## 1. 프로토콜 개요

- **목적**: PC/외부기기에서 PLC 내부 데이터를 읽기/쓰기 위한 전용 통신 서비스
- **포트 정보**
- **역할**:
- **지원 방식**
## 2. 프레임 구조

### 📌 Application Header Format

| 항목 | 크기(byte) | 내용 |
| --- | --- | --- |
| Company ID | 8 | `"LSIS-XGT"` (ASCII: 4C 53 49 53 2D 58 47 54) |
| Reserved | 2 | `0x0000` |
| PLC Info | 2 | 상태/CPU타입 등 |
| CPU Info | 1 | 보통 `0xA0` |
| Source of Frame | 1 | 요청: `0x33`, 응답: `0x11` |
| Invoke ID | 2 | 프레임 식별용 |
| Length | 2 | Instruction 영역 길이 |
| Position | 1 | 슬롯/베이스 번호 |
| Check Sum | 1 | BCC (Byte Sum, 현재 미사용 `0x00`) |

### 📌 Application Instruction Format

요청/응답 프레임은 아래 구조를 따름:

1. **명령어(Command)**
1. **데이터 타입**
1. **구조화된 데이터**
## 3. 주요 명령어

| 명령 | 코드(요청/응답) | 설명 |
| --- | --- | --- |
| **개별 읽기** | 0x0054 / 0x0055 | BIT/WORD 단위 개별 변수 읽기 (최대 16개) |
| **개별 쓰기** | 0x0058 / 0x0059 | BIT/WORD 단위 개별 변수 쓰기 (최대 16개) |
| **연속 읽기** | 0x0054 / 0x0055 | Block 단위 연속 읽기 (최대 1400byte) |
| **연속 쓰기** | 0x0058 / 0x0059 | Block 단위 연속 쓰기 (최대 1400byte) |
| **Status 요청** | 0x00B0 / 0x00B1 | PLC 상태 조회 |

## 4. 데이터 타입 예시

| 데이터 타입 | 예시 주소 |
| --- | --- |
| BIT | `%MX0`, `%PX0` |
| BYTE | `%MB0`, `%PB0` |
| WORD | `%MW0`, `%DW0` |
| DWORD | `%MD0`, `%DD0` |
| LWORD | `%ML0`, `%DL0` |

## 5. Python 코드 예제

### ✅ Word 읽기 (예: D번지 `%DW03010`)

```python
import socket

TCP_IP = '192.168.0.2'
TCP_PORT = 2004
BUFFER_SIZE = 1024

message = (b'LSIS-XGT\n\n\n\n\xA0\x33\x00\x00\x12\x00\x02\x00'
           b'\x54\x00\x02\x00\00\00\x01\x00\x08\x00%DW03010')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(message)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data: ", data.hex())


```

### ✅ Word 쓰기 (양수/음수 지원)

```python
def write_word(addr_str: str, value: int):
    addr = addr_str.encode('ascii')
    addr_len = len(addr).to_bytes(2, 'little')
    val = int(value).to_bytes(2, 'little', signed=True)  # 음수도 지원

    cmd_tail = b''.join([
        b'\x58\x00', b'\x02\x00', b'\x00\x00', b'\x01\x00',
        addr_len, addr, b'\x01\x00', val,
    ])
    length = len(cmd_tail).to_bytes(2, 'little')

    header = (b'LSIS-XGT' + b'\x0a\x0a\x0a\x0a' + b'\xA0\x33\x00\x00'
              + length + b'\x02\x00')

    msg = header + cmd_tail

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((TCP_IP, TCP_PORT))
        s.sendall(msg)
        rx = s.recv(BUFFER_SIZE)

    print("TX:", msg.hex())
    print("RX:", rx.hex())

write_word('%DW03020', -3100)  # 음수 쓰기
write_word('%DW03010', 3100)   # 양수 쓰기
```

### ✅ Bit 읽기 (예: `%MW00600`)

```python
body_read_bit = (
    b'\x54\x00' + b'\x00\x00' + b'\x00\x00' +
    b'\x01\x00' + b'\x07\x00' + b'%MW00600'
)
```

### ✅ Bit 쓰기 (예: `%MW00600` → 0/1)

```python
body_write_bit = (
    b'\x58\x00' + b'\x00\x00' + b'\x00\x00' +
    b'\x01\x00' + b'\x07\x00' + b'%MW00600' +
    b'\x00\x00' + b'\x01\x00'
)
```

## 6. 참고사항

- **Invoke ID**는 요청/응답 매칭용. PC에서 송신한 ID가 PLC 응답에 그대로 반영됨.
- *Checksum(BCC)**는 현재 사용하지 않으며 대부분 `0x00`.
- **음수 처리**: 반드시 `signed=True`로 변환해야 2’s complement 표현 가능.
- **주소 형식**: `%` 기호 포함 ASCII 문자열 그대로 전송해야 함.

