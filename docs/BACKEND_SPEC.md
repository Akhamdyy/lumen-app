# Backend Specification: Lumen API
**Base URL:** `http://localhost:8000/api/v1`

## 1. Data Models & Schema

### Course (Metadata)
* `id`: UUID (Primary Key)
* `name`: String (e.g., "Control Systems")
* `code`: String (e.g., "EE402")
* `created_at`: Timestamp

### Document (PDF Source)
* `id`: UUID
* `course_id`: ForeignKey(Course.id)
* `filename`: String
* `file_path`: String (Local Storage)
* `status`: Enum (Pending, Processing, Completed, Failed)

### Vector Metadata (ChromaDB Payload)
When text is embedded, we store the following metadata for filtering:
* `course_id`: UUID
* `doc_id`: UUID
* `page_label`: Integer (The actual slide/page number)
* `text_content`: String (The raw chunk)

## 2. API Endpoints

### Course Management
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/courses` | List all active courses. |
| `POST` | `/courses` | Create a new course category. |
| `DELETE` | `/courses/{id}` | Delete a course and its associated vectors. |

### Document Ingestion
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/ingest/upload` | Upload PDF and trigger the embedding pipeline. |
| `GET` | `/ingest/status/{doc_id}` | Poll the status of the embedding process. |

### AI Retrieval (The RAG Core)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/chat/query` | Send user message + course_id; returns streamed text. |
| `GET` | `/chat/history/{course_id}` | Retrieve past conversation for a specific course. |

## 3. RAG Pipeline Configuration
* **Chunk Size:** 1000 characters.
* **Overlap:** 200 characters (to maintain context between chunks).
* **Embedding Model:** `all-MiniLM-L6-v2` (Fast and efficient for local CPUs).
* **Search Type:** Similarity Search with Score Thresholding (0.7+ relevance).

## 4. Security & Validation
* **CORS:** Restricted to Frontend origin (`localhost:3000`).
* **Input Validation:** Pydantic models for all Request Bodies.
* **Error Handling:** Global Exception Handler for "File Corrupted" or "Ollama Offline".