import { FormEvent, useState } from "react";

interface Props {
  onSend: (message: string) => void;
  loading: boolean;
}

export default function ChatInput({ onSend, loading }: Props) {
  const [message, setMessage] = useState("");

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const trimmed = message.trim();
    if (!trimmed) return;

    onSend(trimmed);
    setMessage("");
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2 mt-4">
      <input
        type="text"
        placeholder="Ask a DSA question..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        disabled={loading}
        className="flex-1 p-3 rounded-lg bg-zinc-800 outline-none text-white placeholder:text-gray-500"
        aria-label="DSA question"
      />

      <button
        type="submit"
        disabled={loading}
        className="bg-blue-600 px-4 py-2 rounded-lg disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading ? "Sending..." : "Send"}
      </button>
    </form>
  );
}