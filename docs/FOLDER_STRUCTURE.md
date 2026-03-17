# Project Structure: Lumen

lumen-app/
├── backend/                # FastAPI Application
│   ├── app/
│   │   ├── api/            # Route handlers (auth, chat, upload)
│   │   ├── core/           # RAG Logic (chunking.py, vector_store.py, llm_chain.py)
│   │   ├── models/         # Pydantic schemas (request/response)
│   │   ├── services/       # Business logic (PDF processing, Ollama wrapper)
│   │   └── main.py         # Entry point
│   ├── tests/              # Pytest suite
│   ├── requirements.txt
│   └── .env                # OLLAMA_URL, DATABASE_URL
├── frontend/               # Next.js Application
│   ├── src/
│   │   ├── app/            # App Router (pages & layouts)
│   │   ├── components/     # UI Components (Chat/, Course/, Shared/)
│   │   ├── hooks/          # Custom React hooks (useChat, useUpload)
│   │   ├── lib/            # Utilities (formatters, api-client)
│   │   └── store/          # Context/State management
│   ├── public/             # Static assets (logos, icons)
│   └── package.json
├── data/                   # Git-ignored Data Persistence
│   ├── uploads/            # Temporary storage for uploaded PDFs
│   └── chroma_db/          # Persistent Vector Database files
├── docs/                   # Phase 0 Documentation
│   ├── PROJECT_PLAN.md
│   ├── BACKEND_SPEC.md
│   └── FRONTEND_SPEC.md
└── docker-compose.yml      # Orchestrates Backend + Frontend + Chroma