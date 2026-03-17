# Frontend Specification: Lumen UI
**Framework:** Next.js 14 (App Router)
**Styling:** Tailwind CSS + Shadcn/UI

## 1. Core UI Components
* **Layout:** Sidebar-based navigation for switching between courses.
* **Chat Interface:**
    * **Message Bubbles:** Distinct styles for User and AI.
    * **Streaming Text:** Real-time character-by-character rendering.
    * **LaTeX Support:** Integration of `react-markdown` with `remark-math` and `rehype-katex` to render engineering formulas.
    * **Source Citations:** Clickable "badges" at the end of AI responses that show the PDF name and Page/Slide number.
* **Upload Zone:** Drag-and-drop area with a real-time progress bar using Lucide-react icons.

## 2. State Management & Hooks
* **Context API:** To manage the `ActiveCourse` and `ChatHistory`.
* **SWR / TanStack Query:** For fetching course lists and handling the loading/error states of the Ingestion API.
* **Streaming Hook:** A custom `useChat` hook to handle Server-Sent Events (SSE) or Fetch-Stream from the FastAPI backend.

## 3. Page Routes
* `/` - **Welcome/Setup:** Quick links to recent courses and a "Get Started" guide.
* `/course/[id]` - **Chat Room:** The main RAG interface for a specific subject.
* `/settings` - **System Health:** Toggle between Ollama models (Llama 3 vs Mistral) and check connection status.

## 4. UI/UX Rules
* **Responsiveness:** Must be fully functional on tablets (for library studying).
* **Loading States:** Shimmer/Skeleton effects during PDF processing.
* **Theme:** Default "Dark Mode" to reduce eye strain during long study sessions.