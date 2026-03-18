'use client';

import React, { useState } from 'react';
import { askQuestion } from '@/lib/api'; // Corrected alias to match Task 2/3

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
      setAnswer("Error: Could not reach Lumen's brain. Check if the backend container is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full space-y-6">
      <form onSubmit={handleAsk} className="flex gap-3">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question about the lecture..."
          className="flex-1 p-3 bg-[#1A1F26] border border-gray-800 rounded-lg text-gray-100 placeholder-gray-500 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all"
        />
        <button
          type="submit"
          disabled={loading}
          className="bg-blue-600 text-white px-8 py-2 rounded-lg font-bold hover:bg-blue-500 active:scale-95 disabled:bg-gray-700 disabled:text-gray-500 disabled:active:scale-100 transition-all"
        >
          {loading ? 'Thinking...' : 'Ask'}
        </button>
      </form>

      {answer && (
        <div className="p-6 bg-[#151921] border border-blue-900/30 rounded-xl shadow-lg">
          <div className="flex items-center gap-2 mb-4">
            <span className="text-blue-500 text-xs font-black uppercase tracking-widest">Lumen AI</span>
            <div className="h-[1px] flex-1 bg-blue-900/20"></div>
          </div>
          <p className="text-gray-200 leading-relaxed whitespace-pre-wrap text-[15px]">
            {answer}
          </p>
        </div>
      )}
    </div>
  );
}