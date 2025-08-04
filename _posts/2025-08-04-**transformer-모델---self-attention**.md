---
title: "**Transformer 모델 - Self-Attention**"
date: 2025-08-04 06:06:00 +0900
categories: [기술소개]
tags: [Transfomer, AI, LLM]
description: Self-Attention 개념
toc: true
comments: true
---

## 개요

2017년 NIPS에서 'Attention Is All You Need’ 라는 논문으로 Transformer 모델이 나왔다.

병렬 처리가 안되던 RNN의 한계를 극복한 알고리즘으로 자연어처리에서 좋은 결과를 보여줬다.

## 내용

### ASIS

17년도에 나온 Attentions Is All You Need 논문에서는 Attention만으로 구현된 모델을 소개한다. RNN 기법을 사용하지 않고 인코더, 디코더 구조로만 설계하고 번역 성능에서 RNN보다 뛰어난 성과를 냈습니다.

기존의 seq2seq 모델도 인코더와 디코더는 있었습니다.

입력  seq 를 하나의 백터로 압축하고 디코더는 이 백터를 기반으로 출력 seq 를 만들었습니다. 

이 과정에서 입력 seq의 정보가 손실되는 점이 문제였습니다.

RNN 구조를 사용하면 먼 단어일 수록 흐려진다는 단점들이 있었습니다. 

또한 병렬 처리가 안된다..

RNN모델은 이전Tn-1에 결과값을 현재Tn 연산에 사용하는 점 때문이다. 

따라서 n의 차이가 크면 흐려지고, 이전 결과값을 재귀적으로 받기 때문에 병렬 연산이 불가능하다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1e7f5e6f-9228-4d68-9d1d-6554327138c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GHYNYTF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIC1OVYKearvSTkiIanade%2Fp0qd5cmaTvwte7iGVtm94sAiEAkwAIAWJx48bkieOTQOKPSuHdVicZlvTXx9TKGqynZk0q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDDnIfZP6rO%2FueYyX6SrcA6ciVZTeElv0w6EFuxNkmCLneUTqbT1eWTH6mMb2gXa2SNxOhmfqpE4yOixj23X5tiJqCrBhc43rlz1ubp1w4LB7TQLU3n5dQq0FZk1VEec2PZozFWd6mu2c8Qy8N3oSLjylfqQoUu%2FAnlb5MIVMd1L6qJ0SjiN1P66UZ6ZKbzTaW%2Fkc3uDwwrrum2cZn8L1rskRFyPOUICrgHhFs0XQ2wh0Crd6BILBs5T7IVNKd3RQV%2BC%2BNM6KbV%2BUD1r6eMAzPL4QLuvYKJdqHQN9Xl7%2FVhFjx7m4PJ%2F8e1OJWEEVeCyLgFYePedqMPVtHvS0StPbBf4ssdmyoekReFcgnXBU23I%2FizZsS42NjBLTSPtYqR3JJcegAFlvYd%2FyY%2F%2BP6nb65qG4TTh16xbq%2F4H9TzbQbsVdTTFO10p9lZpNr5HXhArXUQb5gcYrKgLfY9J3t3YJFRFSNcmVZswxLC7yjJL%2F3PKHIDMQId5upn3tZoRL4bpNkbeX8idmqQZvv7hy8OR%2F%2Fuekdt%2BevKWod0LhngpHu9wuci0%2BLplgmuxL2Hv7PYooFKwGAczNsRxx7z%2BVyD3YIqRjt6%2B5Jwfqv1dcZ8cb8gZp3QJ5%2BMYInTCBBwjnDujTTHQ9Y1BRhPhj3sCLMMe2wcQGOqUBQzSjtjJ8U5twyVwaWL7TYa0nk5wC21H7nhFI6bXdgcd8NCVSGxcLejtD8QuqBGTc3z56rpbQ16AB76Doq0Bs40afTmHUWFBGWgEYnMZ%2BE1TeE22iOEkHQE7HvR3lfeTGV1Ore4ZkRulcr%2FAAlubNWNmgBHUaJ8kRZcjzKhx72H%2FtdRsASthmKXcaqsWYiQCnl1%2FSSMWmaLdyzIaexQ0p24K4x5XY&X-Amz-Signature=7b04069ed376f1e11843c47ef8aefa79e0baed689f6279e3bda6710e388a459d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### TOBE

이런 구조를 바꾼게 바로 2017년 NIPS에서 'Attention Is All You Need’ 라는 논문이다. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/6e9cd139-802d-46d7-a36a-93043fd1cafc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GHYNYTF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIC1OVYKearvSTkiIanade%2Fp0qd5cmaTvwte7iGVtm94sAiEAkwAIAWJx48bkieOTQOKPSuHdVicZlvTXx9TKGqynZk0q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDDnIfZP6rO%2FueYyX6SrcA6ciVZTeElv0w6EFuxNkmCLneUTqbT1eWTH6mMb2gXa2SNxOhmfqpE4yOixj23X5tiJqCrBhc43rlz1ubp1w4LB7TQLU3n5dQq0FZk1VEec2PZozFWd6mu2c8Qy8N3oSLjylfqQoUu%2FAnlb5MIVMd1L6qJ0SjiN1P66UZ6ZKbzTaW%2Fkc3uDwwrrum2cZn8L1rskRFyPOUICrgHhFs0XQ2wh0Crd6BILBs5T7IVNKd3RQV%2BC%2BNM6KbV%2BUD1r6eMAzPL4QLuvYKJdqHQN9Xl7%2FVhFjx7m4PJ%2F8e1OJWEEVeCyLgFYePedqMPVtHvS0StPbBf4ssdmyoekReFcgnXBU23I%2FizZsS42NjBLTSPtYqR3JJcegAFlvYd%2FyY%2F%2BP6nb65qG4TTh16xbq%2F4H9TzbQbsVdTTFO10p9lZpNr5HXhArXUQb5gcYrKgLfY9J3t3YJFRFSNcmVZswxLC7yjJL%2F3PKHIDMQId5upn3tZoRL4bpNkbeX8idmqQZvv7hy8OR%2F%2Fuekdt%2BevKWod0LhngpHu9wuci0%2BLplgmuxL2Hv7PYooFKwGAczNsRxx7z%2BVyD3YIqRjt6%2B5Jwfqv1dcZ8cb8gZp3QJ5%2BMYInTCBBwjnDujTTHQ9Y1BRhPhj3sCLMMe2wcQGOqUBQzSjtjJ8U5twyVwaWL7TYa0nk5wC21H7nhFI6bXdgcd8NCVSGxcLejtD8QuqBGTc3z56rpbQ16AB76Doq0Bs40afTmHUWFBGWgEYnMZ%2BE1TeE22iOEkHQE7HvR3lfeTGV1Ore4ZkRulcr%2FAAlubNWNmgBHUaJ8kRZcjzKhx72H%2FtdRsASthmKXcaqsWYiQCnl1%2FSSMWmaLdyzIaexQ0p24K4x5XY&X-Amz-Signature=8fe6ed505a6192af7363411b2410f31ac8923acc9d94dfa4e468e7efb952d6e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 참조

https://namu.wiki/w/트랜스포머(인공신경망)

https://chonchony.tistory.com/entry/순환신경망-RNN의-문제점-기울기-소실-기울기-폭주-Gradient-Vanishing-Exploding

https://calmmimiforest.tistory.com/110


