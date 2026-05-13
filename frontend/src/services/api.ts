const BASE_URL = "http://127.0.0.1:8000";

export interface ChatResponse {
  response: string;
}

export async function sendMessage(message: string): Promise<ChatResponse> {
  const response = await fetch(`${BASE_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
    }),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(`Chat request failed with status ${response.status}: ${text}`);
  }

  return response.json();
}