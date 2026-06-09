---
title: "📄 Paper2Code: Automating Code Generation from Scientific Papers"
date: 2025-08-07 04:18:00 +0900
categories: [기술소개]
tags: [LLM, agent, paper2code]
description: 논문을 자동으로 코드 저장소로 변환하는 다중 에이전트 기반의 LLM 시스템
toc: true
comments: true
redirect_from:
  - /posts/📄-paper2code:-automating-code-generation-from-scientific-papers/
---

# 📄 Paper2Code: Automating Code Generation from Scientific Papers

## 📌 PaperCoder 개요

**PaperCoder**는 머신러닝 논문을 기반으로 자동으로 코드 저장소를 생성하는 다중 에이전트 기반의 LLM 시스템으로, **기획(planning)**, **분석(analysis)**, **코드 생성(code generation)**의 세 단계로 구성된 파이프라인을 사용합니다.

## ⚙️ 파이프라인 구조

- **기획(Planning)**: 논문의 핵심 내용을 분석하여 코드 구조와 필요한 작업을 계획합니다.
- **분석(Analysis)**: 계획된 작업을 심층적으로 분석하고, 논문의 세부 내용을 이해합니다.
- **코드 생성(Code Generation)**: 분석 결과를 기반으로 고품질의 코드를 자동으로 생성합니다.
## 🚀 사용 방법 (Quick Start)

### ✅ OpenAI API를 사용하는 경우

```bash
pip install openai
export OPENAI_API_KEY="<OPENAI_API_KEY>"
cd scripts
bash run.sh

```

### ✅ 오픈소스 모델(vLLM)을 사용하는 경우

기본 모델은 `deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct`입니다.

```bash
pip install vllm
cd scripts
bash run_llm.sh

```

## 📁 결과물 구조

```text
outputs
├── Transformer
│   ├── analyzing_artifacts
│   ├── coding_artifacts
│   └── planning_artifacts
└── Transformer_repo # 최종 생성된 코드 저장소

```

## 🛠️ 상세 환경 설정

필요에 따라 선택적으로 설치할 수 있습니다:

```bash
pip install openai
pip install vllm
# 또는 모든 의존성 설치
pip install -r requirements.txt

```

### 📄 PDF를 JSON으로 변환 (선택적)

논문 PDF를 JSON 형식으로 변환하려면 다음과 같이 진행합니다:

```bash
git clone https://github.com/allenai/s2orc-doc2json.git
cd ./s2orc-doc2json/grobid-0.7.3
./gradlew run
mkdir -p ./s2orc-doc2json/output_dir/paper_coder
python ./s2orc-doc2json/doc2json/grobid2json/process_pdf.py \
    -i ${PDF_PATH} \
    -t ./s2orc-doc2json/temp_dir/ \
    -o ./s2orc-doc2json/output_dir/paper_coder

```

## 📊 저장소 품질 평가 방법

PaperCoder로 생성된 저장소의 품질을 모델 기반으로 평가합니다.

### 📝 레퍼런스 없는 평가

```bash
cd codes/
python eval.py \
    --paper_name Transformer \
    --pdf_json_path ../examples/Transformer_cleaned.json \
    --data_dir ../data \
    --output_dir ../outputs/Transformer \
    --target_repo_dir ../outputs/Transformer_repo \
    --eval_result_dir ../results \
    --eval_type ref_free \
    --generated_n 8 \
    --papercoder

```

### 📝 레퍼런스 기반 평가

```bash
cd codes/
python eval.py \
    --paper_name Transformer \
    --pdf_json_path ../examples/Transformer_cleaned.json \
    --data_dir ../data \
    --output_dir ../outputs/Transformer \
    --target_repo_dir ../outputs/Transformer_repo \
    --gold_repo_dir ../examples/Transformer_gold_repo \
    --eval_result_dir ../results \
    --eval_type ref_based \
    --generated_n 8 \
    --papercoder

```

📌 **Paper2Code**를 통해 논문의 아이디어를 효율적으로 구현 가능한 코드로 빠르게 변환하고, 코드의 정확성과 신뢰성을 모델 기반 평가를 통해 검증할 수 있습니다.

### 📋 링크

https://github.com/going-doer/Paper2Code?utm_source=pytorchkr&ref=pytorchkr


