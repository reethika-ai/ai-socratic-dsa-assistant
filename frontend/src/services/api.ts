export async function sendMessage(
  studentId: string,
  message: string
) {
  const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";
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

  if (!res.ok) {
    throw new Error("API error");
  }

  return res.json();
}