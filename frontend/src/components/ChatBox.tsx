"use client";
import { useState, useRef, useEffect } from "react";
import { sendMessage } from "../services/api";

const STUDENT_ID = "student_001";

export default function ChatBox() {
  const [input, setInput] = useState("");
  const [code, setCode] = useState("");

  const [messages, setMessages] = useState<any[]>([
    {
      role: "assistant",
      content:
        "Hi! I'm your AI Socratic DSA tutor. Ask me about sorting algorithms.",
    },
  ]);

  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  const TypingIndicator = () => (
    <div className="text-gray-400 text-sm italic">
      AI is typing...
    </div>
  );

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = input;

    // add messages
    setMessages((prev) => [
      ...prev,
      { role: "user", content: userMessage },
      { role: "assistant", content: "Thinking..." },
    ]);

    setInput("");
    setLoading(true);

    try {
      const data = await sendMessage(
        STUDENT_ID,
        userMessage,
        code
      );

      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1] = {
          role: "assistant",
          content: data.response,
        };
        return updated;
      });

    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Error getting response",
        },
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

        {/* Typing indicator */}
        {loading && <TypingIndicator />}

        {/* Auto scroll */}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="mt-4 space-y-2">
        <input
          className="border p-2 w-full"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask something..."
        />

        <textarea
          className="border p-2 w-full h-32"
          value={code}
          onChange={(e) => setCode(e.target.value)}
          placeholder="Paste your code here..."
        />

        <button
          onClick={handleSend}
          disabled={loading}
          className="bg-blue-500 text-white px-4 py-2 w-full disabled:opacity-50"
        >
          Send
        </button>
      </div>
    </div>
  );
}