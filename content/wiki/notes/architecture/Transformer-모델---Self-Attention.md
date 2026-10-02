---
source: knowledge-base
origin: notion
title: "Transformer 모델 - Self-Attention "
area: "아키텍처와 기술 소개"
tags: ["area/architecture", "area/llm", "concept/ai", "concept/transformer"]
created: "2025-08-04T06:06:00.000Z"
last_edited: "2025-08-04T06:29:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-807b-9422-cdb0ad78e9e5"
notion_url: "https://www.notion.so/Transformer-Self-Attention-245172a556d6807b9422cdb0ad78e9e5"
type: note
updated: 2026-07-07
---

# Transformer 모델 - Self-Attention 

## 요약

Self-Attention 개념

LLM 기술 흐름과 구현 포인트를 비교하기 위한 기술 노트입니다.

## 핵심 포인트

- Self-Attention 개념
- 개요
- 내용
- ASIS
- TOBE

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/아키텍처와-기술-소개|아키텍처와 기술 소개]]

## 정리 내용

### 개요
2017년 NIPS에서 '[Attention Is All You Need](https://namu.wiki/w/Attention%20Is%20All%20You%20Need)’ 라는 논문으로 Transformer 모델이 나왔다.
병렬 처리가 안되던 RNN의 한계를 극복한 알고리즘으로 자연어처리에서 좋은 결과를 보여줬다.
### 내용
#### ASIS
17년도에 나온 Attentions Is All You Need 논문에서는 Attention만으로 구현된 모델을 소개한다. RNN 기법을 사용하지 않고 인코더, 디코더 구조로만 설계하고 번역 성능에서 RNN보다 뛰어난 성과를 냈습니다.
기존의 seq2seq 모델도 인코더와 디코더는 있었습니다.
입력  seq 를 하나의 백터로 압축하고 디코더는 이 백터를 기반으로 출력 seq 를 만들었습니다. 
이 과정에서 입력 seq의 정보가 손실되는 점이 문제였습니다.
RNN 구조를 사용하면 먼 단어일 수록 흐려진다는 단점들이 있었습니다. 
![[_attachments/notion/Transformer-모델---Self-Attention/245172a556d6815db5ccef3b450cfaf5.png]]

![[_attachments/notion/Transformer-모델---Self-Attention/245172a556d6816e8d4dee38e2d21153.png]]
또한 병렬 처리가 안된다..
RNN모델은 이전Tn-1에 결과값을 현재Tn 연산에 사용하는 점 때문이다. 
따라서 n의 차이가 크면 흐려지고, 이전 결과값을 재귀적으로 받기 때문에 병렬 연산이 불가능하다.
![[_attachments/notion/Transformer-모델---Self-Attention/245172a556d68170a43dc529bfe71d56.png]]
#### TOBE
이런 구조를 바꾼게 바로 2017년 NIPS에서 '[Attention Is All You Need](https://namu.wiki/w/Attention%20Is%20All%20You%20Need)’ 라는 논문이다. 
![[_attachments/notion/Transformer-모델---Self-Attention/245172a556d681b4a443c07367a584f2.png]]
### 참조
[https://namu.wiki/w/트랜스포머(인공신경망)](https://namu.wiki/w/%ED%8A%B8%EB%9E%9C%EC%8A%A4%ED%8F%AC%EB%A8%B8(%EC%9D%B8%EA%B3%B5%EC%8B%A0%EA%B2%BD%EB%A7%9D))
[https://chonchony.tistory.com/entry/순환신경망-RNN의-문제점-기울기-소실-기울기-폭주-Gradient-Vanishing-Exploding](https://chonchony.tistory.com/entry/%EC%88%9C%ED%99%98%EC%8B%A0%EA%B2%BD%EB%A7%9D-RNN%EC%9D%98-%EB%AC%B8%EC%A0%9C%EC%A0%90-%EA%B8%B0%EC%9A%B8%EA%B8%B0-%EC%86%8C%EC%8B%A4-%EA%B8%B0%EC%9A%B8%EA%B8%B0-%ED%8F%AD%EC%A3%BC-Gradient-Vanishing-Exploding)
[https://calmmimiforest.tistory.com/110](https://calmmimiforest.tistory.com/110)

## 출처

- 원문: https://www.notion.so/Transformer-Self-Attention-245172a556d6807b9422cdb0ad78e9e5
- Vault path: wiki/notes/architecture/Transformer-모델---Self-Attention.md
