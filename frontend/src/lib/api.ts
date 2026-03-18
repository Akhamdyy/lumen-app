const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";

export const uploadPDF = async (file: File) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE_URL}/ingest/upload`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || "Failed to upload PDF");
  }

  return response.json();
};

export const askQuestion = async (query: string) => {
  const response = await fetch(`${API_BASE_URL}/chat/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || "Failed to get answer");
  }

  return response.json();
};