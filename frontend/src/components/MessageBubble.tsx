interface Props {
  role: "user" | "assistant";
  content: string;
}

export default function MessageBubble({ role, content }: Props) {
  return (
    <div
      className={`mb-4 flex ${
        role === "user" ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`max-w-[80%] rounded-xl px-4 py-3 ${
          role === "user"
            ? "bg-blue-600 text-white"
            : "bg-zinc-800 text-gray-200"
        }`}
      >
        {content}
      </div>
    </div>
  );
}