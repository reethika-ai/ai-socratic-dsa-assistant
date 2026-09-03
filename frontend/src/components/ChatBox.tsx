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

  // Auto-scroll to latest message
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
    // Don't send empty messages
    if (!input.trim()) return;

    const userMessage = input.trim();

    // Add user's message and thinking message
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: userMessage,
      },
      {
        role: "assistant",
        content: "Thinking...",
      },
    ]);

    // Clear input
    setInput("");

    // Show loading
    setLoading(true);

    try {
      // Send student ID + message + code to backend
      const data = await sendMessage(
        STUDENT_ID,
        userMessage,
        code
      );

      console.log("AI response:", data);

      // Replace "Thinking..." with actual AI response
      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          content:
            data.response ||
            data.message ||
            "No response received from AI.",
        };

        return updated;
      });
    } catch (error) {
      console.error("Chat error:", error);

      // Replace "Thinking..." with error message
      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          content:
            "Error getting response. Please try again.",
        };

        return updated;
      });
    } finally {
      setLoading(false);
    }
  };

  // Allow Enter key to send message
  const handleKeyDown = (
    e: React.KeyboardEvent<HTMLInputElement>
  ) => {
    if (e.key === "Enter" && !loading) {
      handleSend();
    }
  };

  return (
    <div className="p-4 max-w-xl mx-auto">

      {/* Chat messages */}
      <div className="space-y-2 mb-4">

        {messages.map((msg, i) => (
          <div key={i}>
            <b>
              {msg.role === "user" ? "You" : "AI"}:
            </b>{" "}
            {msg.content}
          </div>
        ))}

        {/* Typing indicator */}
        {loading && <TypingIndicator />}

        {/* Auto-scroll target */}
        <div ref={messagesEndRef} />
      </div>

      {/* Input section */}
      <div className="mt-4 space-y-2">

        {/* Question input */}
        <input
          className="border p-2 w-full"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask something..."
          disabled={loading}
        />

        {/* Code input */}
        <textarea
          className="border p-2 w-full h-32"
          value={code}
          onChange={(e) => setCode(e.target.value)}
          placeholder="Paste your code here..."
          disabled={loading}
        />

        {/* Send button */}
        <button
          onClick={handleSend}
          disabled={loading || !input.trim()}
          className="bg-blue-500 text-white px-4 py-2 w-full disabled:opacity-50"
        >
          {loading ? "Thinking..." : "Send"}
        </button>
      </div>
    </div>
  );
}