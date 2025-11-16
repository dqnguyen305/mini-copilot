"use client";

import { useState } from "react";
import {
  generateCode,
  autocomplete,
  fixCode,
  summarizeCode,
} from "@/utils/api";

import ApiButtons from "@/components/ApiButtons";
import OutputBox from "@/components/OutputBox";

export default function Home() {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  const handleResult = (res) => {
    setOutput(res.output || res.error || "No response");
  };

  return (
    <div className="p-6 max-w-4xl mx-auto text-white">
      <h1 className="text-3xl font-bold mb-4">Mini Copilot</h1>

      {/* TEXTAREA INPUT */}
      <textarea
        className="w-full h-40 p-3 bg-gray-900 border border-gray-700 rounded text-white"
        placeholder="Nhập đoạn code hoặc mô tả..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      {/* BUTTONS */}
      <ApiButtons
        onGenerate={async () => handleResult(await generateCode(input))}
        onAutocomplete={async () => handleResult(await autocomplete(input))}
        onFix={async () => handleResult(await fixCode(input))}
        onSummarize={async () => handleResult(await summarizeCode(input))}
      />

      {/* OUTPUT */}
      <OutputBox text={output} />
    </div>
  );
}
