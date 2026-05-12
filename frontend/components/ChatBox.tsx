export default function ChatBox() {
  return (
    <div className="w-full max-w-2xl bg-zinc-900 p-4 rounded-xl">
      <div className="h-96 overflow-y-auto border border-zinc-700 rounded-lg p-4">
        <p className="text-sm text-gray-400">
          AI messages will appear here...
        </p>
      </div>

      <div className="flex mt-4 gap-2">
        <input
          type="text"
          placeholder="Ask a DSA question..."
          className="flex-1 p-3 rounded-lg bg-zinc-800 outline-none"
        />

        <button className="bg-blue-600 px-4 py-2 rounded-lg">
          Send
        </button>
      </div>
    </div>
  );
}