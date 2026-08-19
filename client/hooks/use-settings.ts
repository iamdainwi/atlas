import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { api } from "@/lib/api";

export interface Settings {
  id: string;
  theme: string;
  llm_provider: string;
  embedding_model: string;
  temperature: number;
  top_k: number;
  chunk_size: number;
  overlap: number;
}

export interface SettingsUpdate {
  theme?: string;
  llm_provider?: string;
  embedding_model?: string;
  temperature?: number;
  top_k?: number;
  chunk_size?: number;
  overlap?: number;
}

export function useSettings() {
  return useQuery({
    queryKey: ["settings"],
    queryFn: async () => {
      const res = await api.get<{ data: Settings }>("/settings");
      return res.data.data;
    },
  });
}

export function useUpdateSettings() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (data: SettingsUpdate) => {
      const res = await api.put<{ data: Settings }>("/settings", data);
      return res.data.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["settings"] });
    },
  });
}
