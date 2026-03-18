'use client';

import React, { useState } from 'react';
import { askQuestion } from '../lib/api';

export default function ChatBox() {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const handleAsk = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query) return;

    setLoading(true);
    try {
      const res = await askQuestion(query);
      setAnswer(res.answer);
    } catch (err) {
      setAnswer("Error: Could not reach Lumen's brain.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full space-y-4">
      <form onSubmit={handleAsk} className="flex gap-2">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question about the lecture..."
          className="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
        />
        <button
          type="submit"
          disabled={loading}
          className="bg-blue-600 text-white px-6 py-2 rounded-lg font-medium hover:bg-blue-700 disabled:bg-gray-400"
        >
          {loading ? 'Thinking...' : 'Ask'}
        </button>
      </form>

      {answer && (
        <div className="p-6 bg-blue-50 border border-blue-100 rounded-xl">
          <h3 className="text-sm font-bold text-blue-800 uppercase mb-2">Lumen's Response</h3>
          <p className="text-gray-800 leading-relaxed whitespace-pre-wrap">{answer}</p>
        </div>
      )}
    </div>
  );
}