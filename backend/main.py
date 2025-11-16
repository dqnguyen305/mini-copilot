from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import autocomplete, fix_code, summarize, generate

app = FastAPI(title="Mini Copilot Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # sau này có thể giới hạn domain frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(autocomplete.router)
app.include_router(fix_code.router)
app.include_router(summarize.router)
app.include_router(generate.router)


@app.get("/")
def root():
    return {"message": "Mini Copilot Backend is running!"}
