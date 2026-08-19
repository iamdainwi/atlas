"use client";

import { AuthProvider } from "@/contexts/auth-context";
import { AppSidebar } from "@/components/layout/app-sidebar";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar";
import { ReactNode } from "react";

export default function DashboardLayout({ children }: { children: ReactNode }) {
  return (
    <AuthProvider>
      <SidebarProvider>
        <AppSidebar />
        <main className="flex-1 flex flex-col min-h-screen w-full">
          <header className="h-14 border-b flex items-center px-4 shrink-0 bg-background">
            <SidebarTrigger />
            {/* We can add Breadcrumbs or User Dropdown here later */}
          </header>
          <div className="flex-1 overflow-auto p-4 md:p-6">
            {children}
          </div>
        </main>
      </SidebarProvider>
    </AuthProvider>
  );
}
