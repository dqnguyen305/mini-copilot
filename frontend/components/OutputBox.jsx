"use client";

export default function OutputBox({ text }) {
  // Nếu API trả về có dấu ``` → tách cho sạch
  const cleanText = text
    ?.replace(/^```[a-zA-Z]*/g, "")   // bỏ ```java hoặc ```
    ?.replace(/```$/g, "")           // bỏ ``` ở cuối
    ?.trim();

  return (
    <pre
      className="mt-4 bg-[#0a0a0a] text-[#00ff95] p-4 rounded-lg 
                 min-h-[200px] whitespace-pre-wrap text-sm 
                 border border-gray-700 overflow-x-auto"
    >
      {cleanText || "// No output yet"}
    </pre>
  );
}
