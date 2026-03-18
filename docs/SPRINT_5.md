# Phase 3: The Web Interface | Sprint 5: Next.js Foundation & Upload UI
**Status:** ⚪ Not Started
**Target Date:** TBD

## 🎯 Sprint Goal
Initialize the Next.js frontend, configure Tailwind CSS, and build the Document Upload component that communicates with our FastAPI ingestion endpoint.

## 🛠 Tasks

### 1. Bootstrap the Next.js App
- [x] Open a terminal in the root `lumen-app` directory (outside the `backend` folder).
- [x] Run `npx create-next-app@latest frontend`.
- [x] Select the following options:
  - TypeScript: Yes
  - ESLint: Yes
  - Tailwind CSS: Yes
  - `src/` directory: Yes
  - App Router: Yes
  - Customize default import alias: No

### 2. Dockerize the Frontend
- [x] Create `frontend/Dockerfile`.
- [x] Update the root `docker-compose.yml` to include the new `frontend` service, mapping port `3000` to `3000`.

### 3. Build the API Client
- [x] Create a file `frontend/src/lib/api.ts`.
- [x] Write an `uploadPDF` function that takes a `File` object and posts it to `http://localhost:8000/api/v1/ingest/upload` using `FormData`.

### 4. The Upload Component
- [x] Create `frontend/src/components/UploadBox.tsx`.
- [x] Build a simple, stylized drag-and-drop or click-to-upload area using Tailwind CSS.
- [x] Wire the file input to the `uploadPDF` API function.
- [x] Add loading states (e.g., "Uploading & Processing...") so the user knows the AI is chunking the document.

## 📝 Engineering Notes
* **CORS (Cross-Origin Resource Sharing):** Before the frontend on port 3000 can talk to the backend on port 8000, we will need to add a quick CORS middleware patch to `backend/app/main.py`.