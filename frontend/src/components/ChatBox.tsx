"use client";

import { useEffect, useRef, useState } from "react";

import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

import { Message } from "@/types/chat";
import { sendMessage } from "@/services/api";

export default function ChatBox() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const messageListRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messageListRef.current?.scrollTo({
      top: messageListRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [messages, loading]);

  const handleSend = async (message: string) => {
    const trimmedMessage = message.trim();
    if (!trimmedMessage) return;

    const userMessage: Message = {
      role: "user",
      content: trimmedMessage,
    };

    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const data = await sendMessage(trimmedMessage);

      const aiMessage: Message = {
        role: "assistant",
        content: data.response || "Sorry, I could not generate a response.",
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error("Chat API error:", error);
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "The AI service is unavailable. Please try again.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full max-w-2xl bg-zinc-900 p-4 rounded-xl shadow-lg">
      <div
        ref={messageListRef}
        className="h-[500px] overflow-y-auto p-4 border border-zinc-700 rounded-lg bg-zinc-950"
      >
        {messages.length === 0 ? (
          <p className="text-gray-500">
            Start asking DSA questions and the AI will respond here.
          </p>
        ) : (
          messages.map((message, index) => (
            <MessageBubble
              key={index}
              role={message.role}
              content={message.content}
            />
          ))
        )}

        {loading && (
          <div className="mt-4 text-center text-sm text-gray-400">
            AI is typing...
          </div>
        )}
      </div>

      <ChatInput
        onSend={handleSend}
        loading={loading}
      />
    </div>
  );
}