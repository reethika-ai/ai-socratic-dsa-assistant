export async function sendMessage(
  studentId: string,
  message: string,
  code?: string
) {
  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      student_id: studentId,
      message,
      code,
    }),
  });

  return res.json();
}