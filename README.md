<div align="center">

# Mini Copilot  
### AI Coding Assistant — Generate • Fix • Summarize • Autocomplete

A lightweight GitHub Copilot alternative built with  
Next.js (React) + FastAPI + HuggingFace Router

<img src="https://raw.githubusercontent.com/github/explore/main/topics/artificial-intelligence/artificial-intelligence.png" width="400">

<br>

![Frontend](https://img.shields.io/badge/Frontend-Next.js-black?logo=nextdotjs)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![AI](https://img.shields.io/badge/AI-HuggingFace-orange?logo=huggingface)
![Editor](https://img.shields.io/badge/Editor-Monaco-blue?logo=visualstudiocode)

</div>

---

# Table of Contents
- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Backend Setup (FastAPI)](#-backend-setup-fastapi)
- [Frontend Setup (Next.js + React)](#-frontend-setup-nextjs--react)
- [AI Model Configuration](#-ai-model-configuration)
- [UI Preview](#-ui-preview)

---

# Overview
**Mini Copilot** là một trợ lý lập trình AI nhỏ gọn, thay thế nhẹ cho GitHub Copilot với các tính năng:

- Generate code từ mô tả tự nhiên  
- Fix code + giải thích lỗi  
- Summarize code  
- Autocomplete theo ngữ cảnh  
- Hỗ trợ đa ngôn ngữ: Python, JavaScript, Java, Kotlin, Go, Rust…

AI được cung cấp bởi **HuggingFace Router** – API hoàn toàn tương thích OpenAI.

---

# Tech Stack

### Frontend
- React 18  
- Next.js 14 (App Router)  
- Tailwind CSS  

### Backend
- FastAPI  
- Uvicorn  
- python-dotenv  
- OpenAI Python client  

### AI
- HuggingFace Router (OpenAI-compatible)  
- Model mặc định: `katanemo/Arch-Router-1.5B:hf-inference`

---

# Project Structure
mini-copilot/
│
├── backend/
│   ├── main.py
│   ├── routers/
│   │   ├── autocomplete.py
│   │   ├── fix_code.py
│   │   ├── summarize.py
│   │   └── generate.py
│   └── utils/
│       └── ai_client.py
│
└── frontend/
├── app/page.jsx
├── components/
│   ├── CodeEditor.jsx
│   ├── OutputBox.jsx
│   └── ApiButtons.jsx
└── utils/api.js
text---

# Backend Setup (FastAPI)

```bash
cd mini-copilot/backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
Tạo file .env trong thư mục backend/:
envHF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
MODEL=katanemo/Arch-Router-1.5B:hf-inference
Chạy server:
bashuvicorn main:app --reload --port 8000
→ API docs: http://127.0.0.1:8000/docs

Frontend Setup (Next.js + React)
bashcd ../frontend
npm install
npm run dev
→ Truy cập giao diện: http://localhost:3000

AI Model Configuration
Backend gọi HuggingFace Router bằng OpenAI client:
pythonfrom openai import OpenAI
import os

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
)
Bạn có thể thay bất kỳ model nào hỗ trợ OpenAI format chỉ bằng cách đổi MODEL trong .env.

UI Preview
Mini Copilot Preview
POST /generate
<img width="1910" height="810" alt="image" src="https://github.com/user-attachments/assets/597c6842-ae6e-4c66-8de8-eab180034a7f" />
POST /fix
<img width="1806" height="968" alt="image" src="https://github.com/user-attachments/assets/b5b00481-77ff-4639-bbb9-7a5799f93986" />
POST /summarize
<img width="1520" height="897" alt="image" src="https://github.com/user-attachments/assets/f58f7bfa-33a7-43f2-81d8-66200892cd71" />
POST /autocomplete
<img width="726" height="460" alt="image" src="https://github.com/user-attachments/assets/9e9f45e8-0dca-4880-8d39-c21cc8ed1fd9" />



