"use client";

import Editor from "@monaco-editor/react";

export default function CodeEditor({ value, setValue }) {
  return (
    <div className="border rounded-lg">
      <Editor
        height="400px"
        theme="vs-dark"
        defaultLanguage="javascript"
        value={value}
        onChange={(v) => setValue(v)}
      />
    </div>
  );
}
