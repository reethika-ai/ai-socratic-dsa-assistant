import ChatBox from "@/components/ChatBox";

export default function Home() {
  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-6">
      <h1 className="text-4xl font-bold mb-8">
        AI Socratic DSA Tutor
      </h1>

      <ChatBox />
    </main>
  );
}