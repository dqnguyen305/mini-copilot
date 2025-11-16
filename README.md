# Mini Copilot

**AI Coding Assistant --- Generate • Fix • Summarize • Autocomplete**

A lightweight GitHub Copilot alternative built with:\
**Next.js (React) + FastAPI + HuggingFace Router**

------------------------------------------------------------------------

## 🔧 Modules

-   **Frontend**
-   **Backend**
-   **AI**
-   **Editor**

------------------------------------------------------------------------

## 📚 Table of Contents

1.  Overview
2.  Tech Stack
3.  Backend Setup (FastAPI)
4.  Frontend Setup (Nextjs--react)
5.  AI Model Configuration
6.  UI Preview

------------------------------------------------------------------------

## 🧠 Overview

Mini Copilot là một trợ lý lập trình AI nhỏ gọn, "thay thế nhẹ" cho
GitHub Copilot với các tính năng:

-   Generate code từ mô tả tự nhiên
-   Fix code + giải thích lỗi
-   Summarize code
-   Autocomplete theo ngữ cảnh
-   Hỗ trợ đa ngôn ngữ: Python, JavaScript, Java, Kotlin, Go, Rust, ...

AI được cung cấp bởi HuggingFace Router -- API hoàn toàn tương thích
OpenAI.

------------------------------------------------------------------------

## 🏗 Tech Stack

### Frontend

-   React 18\
-   Next.js 14 (App Router)\
-   Tailwind CSS

### Backend

-   FastAPI\
-   Uvicorn\
-   python-dotenv\
-   OpenAI Python client

### AI

-   Provider: HuggingFace Router (OpenAI-compatible)\
-   Model mặc định: katanemo/Arch-Router-1.5B:hf-inference

------------------------------------------------------------------------

## 🔙 Backend Setup (FastAPI)

``` bash
cd mini-copilot/backend

python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Tạo file `.env`:

    HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    MODEL=katanemo/Arch-Router-1.5B:hf-inference

Chạy server:

``` bash
uvicorn main:app --reload --port 8000
```

→ http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 🖼 Frontend Setup (Next.js + React)

``` bash
cd ../frontend
npm install
npm run dev
```

→ http://localhost:3000

------------------------------------------------------------------------

## 🤖 AI Model Configuration

``` python
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
)
```

------------------------------------------------------------------------

## 🧷 UI Preview

(Images omitted in file version)
