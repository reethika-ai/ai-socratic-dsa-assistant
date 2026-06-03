export async function sendMessage(
  studentId: string,
  message: string,
  code?: string
) {
  const res = await fetch(
    "https://ai-socratic-dsa-assistant-8.onrender.com/chat",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        student_id: studentId,
        message,
        code,
      }),
    }
  );

  if (!res.ok) {
    console.log(await res.text());
    throw new Error("Failed to connect to backend");
  }

  return res.json();
}