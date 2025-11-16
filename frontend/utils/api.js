const BASE_URL = "http://127.0.0.1:8000";

export async function generateCode(description) {
  const res = await fetch(`${BASE_URL}/generate/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ description })
  });
  return res.json();
}

export async function autocomplete(code) {
  const res = await fetch(`${BASE_URL}/autocomplete/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code })
  });
  return res.json();
}

export async function fixCode(code) {
  const res = await fetch(`${BASE_URL}/fix-code/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code })
  });
  return res.json();
}

export async function summarizeCode(code) {
  const res = await fetch(`${BASE_URL}/summarize/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code })
  });
  return res.json();
}
