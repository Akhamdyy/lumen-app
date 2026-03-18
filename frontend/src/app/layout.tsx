import type { Metadata } from "next";
import "./globals.css";
import Sidebar from "../components/Sidebar";
import { CourseProvider } from "@/store/CourseContext";

export const metadata: Metadata = {
  title: "Lumen | Engineering Course Auditor",
  description: "AI-powered RAG for Cairo University students",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark" suppressHydrationWarning>
      <body className="bg-[#0B0E14] text-gray-100 flex h-screen overflow-hidden">
        <CourseProvider>
        <Sidebar />
        <main className="flex-1 overflow-y-auto p-8">
          {children}
        </main>
        </CourseProvider>
      </body>
    </html>
  );
}