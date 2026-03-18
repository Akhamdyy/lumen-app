'use client';

import React from 'react';
import Link from 'next/link';
import { useCourse } from '@/store/CourseContext';

export default function Sidebar() {
  const { activeCourseId, setActiveCourseId } = useCourse();

  const courses = [
    { id: 'math-3', name: 'Mathematics 3' },
    { id: 'ctrl-1', name: 'Control Systems' },
    { id: 'comm-1', name: 'Communications' },
  ];

  return (
    <aside className="w-64 bg-[#151921] border-r border-gray-800 flex flex-col h-full">
      <div className="p-6">
        <Link 
          href="/" 
          onClick={() => setActiveCourseId('')} 
          className="text-2xl font-bold tracking-tight text-blue-500"
        >
          LUMEN
        </Link>
      </div>

      <nav className="flex-1 px-4 space-y-2">
        <p className="text-xs font-semibold text-gray-500 uppercase px-2 mb-4">
          My Courses
        </p>
        
        {courses.map((course) => {
          const isActive = activeCourseId === course.id;
          
          return (
            <Link
              key={course.id}
              href={`/course/${course.id}`}
              onClick={() => setActiveCourseId(course.id)}
              className={`block px-3 py-2 rounded-lg transition-all duration-200 no-underline ${
                isActive 
                  ? 'bg-blue-600/20 text-blue-400 border border-blue-600/30 font-medium' 
                  : 'text-gray-400 hover:bg-gray-800 hover:text-gray-200'
              }`}
            >
              {course.name}
            </Link>
          );
        })}
      </nav>

      <div className="p-4 border-t border-gray-800">
        <button className="w-full py-2 bg-blue-600 hover:bg-blue-700 rounded-lg text-sm font-medium transition-colors">
          + New Course
        </button>
      </div>
    </aside>
  );
}