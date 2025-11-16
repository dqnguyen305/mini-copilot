"use client";

export default function ApiButtons({
  onGenerate,
  onAutocomplete,
  onFix,
  onSummarize,
}) {
  return (
    <div className="flex gap-3 mt-4">
      <button className="px-4 py-2 bg-gray-700 rounded" onClick={onAutocomplete}>
        Autocomplete
      </button>

      <button className="px-4 py-2 bg-gray-700 rounded" onClick={onFix}>
        Fix Code
      </button>

      <button className="px-4 py-2 bg-gray-700 rounded" onClick={onSummarize}>
        Summarize
      </button>

      <button className="px-4 py-2 bg-blue-600 rounded" onClick={onGenerate}>
        Generate
      </button>
    </div>
  );
}
