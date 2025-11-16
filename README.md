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

POST /autocomplete
<img width="775" height="469" alt="image" src="https://github.com/user-attachments/assets/18b4457e-bae8-47d7-bc51-bd2ed82e3d17" />

POST /generate
<img width="1910" height="810" alt="image" src="https://github.com/user-attachments/assets/597c6842-ae6e-4c66-8de8-eab180034a7f" />

POST /fix
<img width="1806" height="968" alt="image" src="https://github.com/user-attachments/assets/b5b00481-77ff-4639-bbb9-7a5799f93986" />

POST /summarize
<img width="1520" height="897" alt="image" src="https://github.com/user-attachments/assets/f58f7bfa-33a7-43f2-81d8-66200892cd71" />

