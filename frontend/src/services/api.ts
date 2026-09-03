
export async function sendMessage(
  studentId: string,
  message: string,
  code?: string
) {
  const API_URL =
    "http://127.0.0.1:8000";

const API_URL = "http://localhost:8000";


export async function sendMessage(message: string) {
  const res = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      student_id: "student_001",
      message: message,
    }),
  });

  if (!res.ok) {
    const errorText = await res.text();
    console.error("Backend error:", errorText);
    throw new Error(`Backend error ${res.status}: ${errorText}`);
  }

  return res.json();
}