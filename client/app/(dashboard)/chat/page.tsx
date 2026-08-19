"use client";

import { MessageSquarePlus } from "lucide-react";

export default function ChatEmptyPage() {
  return (
    <div className="h-[calc(100vh-8rem)] flex flex-col items-center justify-center text-center px-4">
      <div className="h-16 w-16 rounded-full bg-primary/10 flex items-center justify-center mb-6">
        <MessageSquarePlus className="h-8 w-8 text-primary" />
      </div>
      <h1 className="text-3xl font-heading font-bold tracking-tight mb-2">How can I help you today?</h1>
      <p className="text-muted-foreground max-w-md mb-8">
        Ask a question and I'll search your document library for the answer.
      </p>
      
      <div className="w-full max-w-2xl relative">
        <div className="relative flex items-center w-full rounded-full border bg-background px-4 py-2 shadow-sm focus-within:ring-1 focus-within:ring-ring">
          <input 
            type="text" 
            placeholder="Ask anything about your documents... (Phase 7)" 
            className="flex h-10 w-full rounded-md bg-transparent px-3 py-1 text-sm shadow-none outline-none disabled:cursor-not-allowed disabled:opacity-50"
            disabled
          />
          <button 
            disabled 
            className="ml-2 inline-flex h-8 items-center justify-center rounded-full bg-primary px-4 text-xs font-medium text-primary-foreground opacity-50 cursor-not-allowed"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
