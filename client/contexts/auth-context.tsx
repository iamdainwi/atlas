"use client";

import { createContext, use, ReactNode } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { api } from "@/lib/api";
import { useRouter } from "next/navigation";

interface User {
  id: string;
  name: string;
  email: string;
  avatar_url: string | null;
  provider: string;
  is_verified: boolean;
  created_at: string;
  updated_at: string;
}

interface AuthContextType {
  user: User | null;
  isLoading: boolean;
  logout: () => Promise<void>;
  refetchUser: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const queryClient = useQueryClient();
  const router = useRouter();

  // The proxy will automatically attach the HttpOnly cookie for auth
  const { data: user, isLoading, refetch } = useQuery({
    queryKey: ["currentUser"],
    queryFn: async () => {
      try {
        const res = await api.get<{ success: boolean; data: User }>("/users/me");
        return res.data.data;
      } catch (error) {
        return null;
      }
    },
    staleTime: Infinity, // Don't refetch automatically
    retry: false,
  });

  const logout = async () => {
    try {
      await api.post("/auth/logout");
    } catch (e) {
      console.error("Logout error", e);
    } finally {
      queryClient.setQueryData(["currentUser"], null);
      router.push("/login");
    }
  };

  const refetchUser = async () => {
    await refetch();
  };

  return (
    <AuthContext.Provider value={{ user: user || null, isLoading, logout, refetchUser }}>
      {children}
    </AuthContext.Provider>
  );
}

// React 19 use hook pattern
export function useAuth() {
  const context = use(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}
