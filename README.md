# AI Socratic DSA Assistant

This project is a production-ready AI-powered Data Structures and Algorithms learning system that guides students using a **Socratic teaching approach** instead of direct answers.

The system improves problem-solving skills by asking structured questions that help students think step-by-step.

# 📌 Problem Statement

Most students learning Data Structures and Algorithms tend to memorize solutions instead of building intuition.

This project solves that problem by creating an AI tutor that:

* Does NOT give direct answers
* Guides students using structured questioning
* Builds conceptual understanding of algorithms
* Encourages active problem solving

# ⚙️ Tech Stack

## Frontend

* Next.js
* TypeScript
* Tailwind CSS

## Backend

* FastAPI
* Python
* Groq LLM API
* REST API architecture

## Database

* PostgreSQL (Neon)

## Deployment

* Vercel (Frontend)
* Render (Backend)

# 🧠 System Architecture

```
User Input → Next.js Frontend → FastAPI Backend → Socratic Prompt Engine → Groq LLM → Response → UI
```

# 🔄 System Flow

* User asks a DSA question
* Frontend sends request to backend API
* Backend builds Socratic prompt using conversation context
* Groq LLM generates guided response
* Response is returned to frontend
* UI displays conversational learning experience

# 🤖 AI Behavior (Socratic Engine)

The AI is strictly designed to:

* Ask only ONE question at a time
* Avoid giving direct solutions
* Guide step-by-step reasoning
* Focus on intuition building
* Use hints only when needed

# 👨‍💻 Contributions

This project was developed as a collaborative effort.

## 🔹 My Contributions

* Designed and implemented FastAPI backend architecture
* Built chat API endpoints (`/chat`, `/chat-stream`)
* Developed Socratic prompt engineering system
* Integrated Groq LLM API for AI responses
* Implemented conversation history management
* Built frontend chat interface using Next.js
* Connected frontend with backend APIs
* Handled full-stack integration (frontend ↔ backend)
* Managed deployment configuration (Vercel + Railway)
* Created project documentation (README)

## 🔹 Teammate Contributions

* Designed overall project structure and system architecture
* Implemented database layer (PostgreSQL integration)
* Built data storage and retrieval logic
* Assisted in backend utility modules
* UI improvements and frontend styling enhancements
* Testing and debugging support during integration

# 🚀 How to Run

## 1. Clone Repository

```bash
git clone https://github.com/reethika-ai/ai-socratic-dsa-assistant
cd ai-socratic-dsa-assistant
```

---

## 2. Backend Setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn app.main:app --reload
```

---

## 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

# Environment Variables

## Backend (.env)

```env
GROQ_API_KEY=your_api_key
DATABASE_URL=your_postgres_url
```

---

# 🌐 API Endpoints

## Chat Endpoint

### POST /chat

### Sample Request

```json
{
  "student_id": "student_001",
  "message": "Explain quick sort",
  "code": ""
}
```

### Sample Response

```json
{
  "response": "What happens when you choose a pivot and divide the array into two parts?"
}
```

## Streaming Endpoint

### POST /chat-stream

Used for real-time Socratic responses.

# 💬 Sample Interaction

## User

Explain merge sort

## AI

What do you think happens when two already sorted lists are merged together?

## User

What is quick sort?

## AI

How does choosing a pivot help divide the problem into smaller parts?

# 🔗 Live Demo

* Frontend: [https://your-vercel-url](https://your-vercel-url)
* Backend API: [https://your-railway-url](https://your-railway-url)

# 📸 API Preview

* `/docs` → FastAPI Swagger UI available for testing

#  Deployment

## Backend

*  Render

## Frontend

* Vercel

## Database

* Neon PostgreSQL


# 📈 Future Improvements

* Adaptive difficulty based on student level
* Code execution support
* Progress tracking system
* Personalized learning paths
* Multi-language support

# 🏁 Summary

This project demonstrates a production-level AI tutoring system with:

* Full-stack architecture
* Real-time AI interaction
* Prompt engineering (Socratic method)
