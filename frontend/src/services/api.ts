const API_URL = "https://ai-socratic-dsa-assistant-9.onrender.com";

export async function sendMessage(
  studentId: string,
  message: string,
  code: string
) {
  const res = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      student_id: studentId,
      message: message,
      code: code,
    }),
  });

  const text = await res.text();

  if (!res.ok) {
    throw new Error(`API ${res.status}: ${text}`);
  }

  return JSON.parse(text);
}