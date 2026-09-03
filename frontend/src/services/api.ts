const API_URL = "http://127.0.0.1:8000";

export async function sendMessage(
  studentId: string,
  message: string
) {
  const res = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      student_id: studentId,
      message: message,
    }),
  });

  const text = await res.text();

  if (!res.ok) {
    throw new Error(`API ${res.status}: ${text}`);
  }

  return JSON.parse(text);
}