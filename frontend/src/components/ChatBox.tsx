"use client";
import { useState } from "react";
import { sendMessage } from "../services/api";

const STUDENT_ID = "student_001";
;

export default function ChatBox() {
  const [input, setInput] = useState("");
  const [code, setCode] = useState("")
  const [messages, setMessages] = useState<any[]>([
    {
      role: "assistant",
      content:
        "Hi! I'm your AI Socratic DSA tutor. Ask me about sorting algorithms.",
    },
  ]);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = input;

    setMessages((prev) => [
      ...prev,
      { role: "user", content: userMessage },
    ]);

    setInput("");
    setLoading(true);

    try {
      const data = await sendMessage(STUDENT_ID, userMessage,code);

      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: data.response },
      ]);
    } catch (error) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Error getting response" },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      
      {/* Messages */}
      <div className="space-y-2 mb-4">
        {messages.map((msg, i) => (
          <div key={i}>
            <b>{msg.role === "user" ? "You" : "AI"}:</b>{" "}
            {msg.content}
          </div>
        ))}
      </div>

      {/* Loading */}
      {loading && (
        <div className="text-gray-400 text-sm">
          AI is thinking...
        </div>
      )}

      {/* Input */}
      <div className="flex gap-2 mt-2">
        <input
          className="border p-2 flex-1"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask something..."
        />
        <textarea
            placeholder="Paste your code here..."
            value={code}
            onChange={(e) => setCode(e.target.value)}
            className="border p-2 w-full mt-2 h-32"
          />
        <button
          onClick={handleSend}
          className="bg-blue-500 text-white px-4"
        >
          Send
        </button>
      </div>
    </div>
  );
}