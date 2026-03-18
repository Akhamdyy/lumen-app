'use client';

import React, { useState } from 'react';
import { uploadPDF } from '../lib/api';

export default function UploadBox() {
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState<string | null>(null);

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setLoading(true);
    setStatus('Processing engineering documents...');

    try {
      const data = await uploadPDF(file);
      setStatus(`Success! Processed ${data.total_pages} pages into ${data.total_chunks} vectors.`);
    } catch (err) {
      setStatus('Upload failed. Check backend logs.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-8 border-2 border-dashed border-gray-300 rounded-xl text-center hover:border-blue-500 transition-colors bg-white shadow-sm">
      <input 
        type="file" 
        accept=".pdf" 
        onChange={handleFileUpload} 
        className="hidden" 
        id="fileInput"
        disabled={loading}
      />
      <label htmlFor="fileInput" className="cursor-pointer block">
        <div className="text-4xl mb-4">📄</div>
        <p className="text-lg font-semibold text-gray-700">
          {loading ? 'Lumen is reading...' : 'Drop your lecture PDF here'}
        </p>
        <p className="text-sm text-gray-500 mt-2">Click to browse your files</p>
      </label>
      {status && (
        <p className={`mt-4 text-sm font-medium ${status.includes('failed') ? 'text-red-500' : 'text-green-600'}`}>
          {status}
        </p>
      )}
    </div>
  );
}