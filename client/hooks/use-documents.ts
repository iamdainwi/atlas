import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { api } from "@/lib/api";

export interface Document {
  id: string;
  title: string;
  filename: string;
  file_type: string;
  size: number;
  page_count: number;
  chunk_count: number;
  processing_status: string;
  created_at: string;
  updated_at: string;
}

export interface DocumentListResponse {
  items: Document[];
  total: number;
  page: number;
  limit: number;
}

export function useDocuments(page = 1, limit = 20) {
  return useQuery({
    queryKey: ["documents", page, limit],
    queryFn: async () => {
      const res = await api.get<{ data: DocumentListResponse }>("/documents", {
        params: { page, limit },
      });
      return res.data.data;
    },
  });
}

export function useUploadDocument() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (file: File) => {
      const formData = new FormData();
      formData.append("file", file);

      const res = await api.post<{ data: Document }>("/documents", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      return res.data.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["documents"] });
    },
  });
}

export function useDocument(id: string | null) {
  return useQuery({
    queryKey: ["documents", id],
    queryFn: async () => {
      if (!id) return null;
      const res = await api.get<{ data: Document }>(`/documents/${id}`);
      return res.data.data;
    },
    enabled: !!id,
  });
}

export function useRenameDocument() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async ({ id, title }: { id: string; title: string }) => {
      const res = await api.patch<{ data: Document }>(`/documents/${id}`, { title });
      return res.data.data;
    },
    onSuccess: (data, variables) => {
      queryClient.invalidateQueries({ queryKey: ["documents"] });
      queryClient.invalidateQueries({ queryKey: ["documents", variables.id] });
    },
  });
}
