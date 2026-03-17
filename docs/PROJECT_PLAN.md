# Project Lumen: AI-Powered Academic Knowledge Base
**Version:** 1.0.0
**Status:** Phase 0 (Planning)

## 1. Project Vision
Lumen is a specialized RAG (Retrieval-Augmented Generation) platform designed for Engineering students. It transforms static course PDFs into an interactive knowledge base, allowing for precise technical queries, formula extraction, and summarized learning.

## 2. Technical Stack (The "Senior-1" Stack)
| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend** | Next.js 14 (App Router) | Modern UI, Server Components for performance. |
| **Backend** | FastAPI (Python 3.11+) | Asynchronous API handling & AI library support. |
| **Orchestrator** | LangChain | Managing the flow between PDF, Vector DB, and LLM. |
| **LLM** | Ollama (Llama 3 / Mistral) | Local inference for privacy and zero cost. |
| **Vector DB** | ChromaDB | Efficient similarity search for technical context. |
| **Styling** | Tailwind CSS + Shadcn/UI | Clean, professional dashboard interface. |

## 3. Development Roadmap

### Phase 1: Foundations & Ingestion (Weeks 1-2)
* **Sprint 1: Environment Setup**
  * Dockerize the environment (FastAPI, Postgres/Chroma).
  * Integrate Ollama API health checks.
* **Sprint 2: The Ingestion Pipeline**
  * Implement PyMuPDF for text/table extraction.
  * Develop "Semantic Chunking" (splitting text by headers/topics).

### Phase 2: The RAG Core (Weeks 3-4)
* **Sprint 3: Embedding & Vector Storage**
  * Generate embeddings using `sentence-transformers`.
  * Implement metadata filtering (search by course or slide #).
* **Sprint 4: Intelligent Retrieval**
  * Prompt Engineering: System prompts optimized for Engineering math.
  * Context injection logic (handling "I don't know" for outside info).

### Phase 3: The Interface (Weeks 5-6)
* **Sprint 5: Dashboard & Management**
  * Course creation and PDF upload UI.
  * Processing status indicators (Progress bars for embedding).
* **Sprint 6: The Chat Experience**
  * Streaming responses (SSE) for a ChatGPT-like feel.
  * LaTeX rendering support for formulas.

### Phase 4: Quality Assurance (Week 7)
* **Sprint 7: Source Attributions**
  * Clicking an AI answer highlights the specific PDF source page.
* **Sprint 8: Performance & Stress Testing**
  * Testing with 100+ page textbooks and complex diagrams.

## 4. Success Metrics
* **Accuracy:** AI must cite the correct slide/page for 95% of queries.
* **Latency:** Initial response chunk under 2 seconds (running locally).
* **Privacy:** Zero data sent to external LLM APIs (OpenAI/Claude).