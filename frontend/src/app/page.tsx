import UploadBox from '../components/UploadBox';

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50 py-12 px-4">
      <div className="max-w-3xl mx-auto space-y-8">
        <header className="text-center">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">Lumen</h1>
          <p className="text-gray-600 italic">Your Engineering Course Auditor</p>
        </header>

        <section>
          <h2 className="text-xl font-semibold text-gray-800 mb-4 text-center">
            Step 1: Ingest Lecture Materials
          </h2>
          <UploadBox />
        </section>
        
        {/* We will add the ChatBox here in the next task! */}
      </div>
    </main>
  );
}