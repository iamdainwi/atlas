"use client";

import { useState, useCallback } from "react";
import { useSearch, SearchResult } from "@/hooks/use-search";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Spinner } from "@/components/ui/spinner";
import { Search, FileText, AlertCircle } from "lucide-react";
import Link from "next/link";
import { useDebounce } from "use-debounce";

export default function SearchPage() {
  const [inputValue, setInputValue] = useState("");
  const [debouncedQuery] = useDebounce(inputValue, 500);

  const { data: results, isLoading, isError, isFetching } = useSearch(debouncedQuery);

  const isSearching = isLoading || isFetching;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-heading font-bold tracking-tight">Search</h1>
        <p className="text-muted-foreground mt-2">
          Hybrid semantic + keyword search across all your processed documents.
        </p>
      </div>

      {/* Search Input */}
      <div className="relative">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
        <Input
          id="search-input"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Ask anything about your documents..."
          className="pl-10 h-12 text-base"
          autoFocus
        />
        {isSearching && (
          <Spinner className="absolute right-3 top-1/2 -translate-y-1/2 size-4" />
        )}
      </div>

      {/* Info badge */}
      {!inputValue && (
        <div className="flex items-center gap-2 text-sm text-muted-foreground rounded-lg border bg-muted/30 p-4">
          <Search className="h-4 w-4 shrink-0" />
          <span>
            Powered by Chroma Cloud with <strong>Qwen dense</strong> + <strong>Splade sparse</strong> embeddings fused via RRF for best-in-class retrieval.
          </span>
        </div>
      )}

      {/* Error */}
      {isError && (
        <div className="flex items-center gap-2 text-destructive text-sm p-4 rounded-lg border border-destructive/20 bg-destructive/5">
          <AlertCircle className="h-4 w-4 shrink-0" />
          <span>Search failed. Make sure your documents are fully processed before searching.</span>
        </div>
      )}

      {/* Results */}
      {results && results.length > 0 && (
        <div className="space-y-3">
          <p className="text-sm text-muted-foreground font-medium">
            {results.length} result{results.length !== 1 ? "s" : ""} for &ldquo;{debouncedQuery}&rdquo;
          </p>
          <div className="grid gap-4">
            {results.map((result: SearchResult, i: number) => (
              <SearchResultCard key={`${result.document_id}-${result.chunk_index}-${i}`} result={result} />
            ))}
          </div>
        </div>
      )}

      {/* No results */}
      {results && results.length === 0 && debouncedQuery && !isSearching && (
        <div className="text-center text-muted-foreground py-16 border rounded-lg bg-card">
          <Search className="h-10 w-10 mx-auto mb-3 opacity-30" />
          <p className="font-medium">No results found</p>
          <p className="text-sm mt-1">
            Try a different query, or make sure your documents are{" "}
            <Link href="/documents" className="text-primary underline underline-offset-4">
              processed
            </Link>.
          </p>
        </div>
      )}
    </div>
  );
}

function SearchResultCard({ result }: { result: SearchResult }) {
  // Lower RRF score = better match (Chroma uses negative scores)
  const scorePercent = Math.max(0, Math.min(100, Math.round((1 + result.score) * 100)));

  return (
    <Card className="transition-all hover:shadow-md">
      <CardHeader className="pb-2">
        <div className="flex items-start justify-between gap-4">
          <div className="flex items-center gap-2 min-w-0">
            <FileText className="h-4 w-4 text-primary shrink-0" />
            <CardTitle className="text-sm font-semibold truncate" title={result.title}>
              {result.title}
            </CardTitle>
          </div>
          <span
            className="text-xs font-medium shrink-0 px-2 py-0.5 rounded-full bg-primary/10 text-primary"
            title="Relevance score (higher = more relevant)"
          >
            {scorePercent}% match
          </span>
        </div>
        <p className="text-xs text-muted-foreground">
          Chunk #{result.chunk_index + 1} &middot;{" "}
          <Link
            href={`/documents?highlight=${result.document_id}`}
            className="hover:text-foreground underline underline-offset-2 transition-colors"
          >
            View document
          </Link>
        </p>
      </CardHeader>
      <CardContent>
        <p className="text-sm text-muted-foreground leading-relaxed line-clamp-4">
          {result.chunk}
        </p>
      </CardContent>
    </Card>
  );
}
