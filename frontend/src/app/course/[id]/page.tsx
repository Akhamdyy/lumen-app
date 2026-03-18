'use client';

import { useParams } from 'next/navigation';
import ChatBox from '@/components/ChatBox';
import UploadBox from '@/components/UploadBox';

export default function CoursePage() {
  const params = useParams();
  const courseId = params.id as string;

  // Format the ID for display (e.g., math-3 -> MATH 3)
  const displayTitle = courseId.replace('-', ' ').toUpperCase();

  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <header className="border-b border-gray-800 pb-6">
        <h1 className="text-3xl font-bold text-white">{displayTitle}</h1>
        <p className="text-gray-400 mt-2">Upload your lectures and ask Lumen anything about this course.</p>
      </header>

      <div className="grid grid-cols-1 gap-8">
        <section>
          <h2 className="text-sm font-semibold text-gray-500 uppercase mb-4">Lecture Ingestion</h2>
          <UploadBox />
        </section>

        <section className="pt-4">
          <h2 className="text-sm font-semibold text-gray-500 uppercase mb-4">Course Tutor</h2>
          <ChatBox />
        </section>
      </div>
    </div>
  );
}