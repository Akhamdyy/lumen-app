'use client';

import React, { createContext, useContext, useState, ReactNode } from 'react';

interface CourseContextType {
  activeCourseId: string | null;
  setActiveCourseId: (id: string) => void;
}

const CourseContext = createContext<CourseContextType | undefined>(undefined);

export function CourseProvider({ children }: { children: ReactNode }) {
  const [activeCourseId, setActiveCourseId] = useState<string | null>(null);

  return (
    <CourseContext.Provider value={{ activeCourseId, setActiveCourseId }}>
      {children}
    </CourseContext.Provider>
  );
}

export function useCourse() {
  const context = useContext(CourseContext);
  if (context === undefined) {
    throw new Error('useCourse must be used within a CourseProvider');
  }
  return context;
}