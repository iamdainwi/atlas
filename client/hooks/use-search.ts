import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";

export interface SearchResult {
  document_id: string;
  title: string;
  chunk: string;
  score: number;
  chunk_index: number;
}

export function useSearch(query: string, n = 10, document_id?: string) {
  return useQuery({
    queryKey: ["search", query, n, document_id],
    queryFn: async () => {
      if (!query.trim()) return [];
      const params: Record<string, string | number> = { q: query, n };
      if (document_id) params.document_id = document_id;
      const res = await api.get<{ data: SearchResult[] }>("/search", { params });
      return res.data.data;
    },
    enabled: !!query.trim(),
    staleTime: 30_000,
  });
}
