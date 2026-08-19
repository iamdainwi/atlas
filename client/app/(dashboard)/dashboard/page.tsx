"use client";

import { useAuth } from "@/contexts/auth-context";
import { useDocuments } from "@/hooks/use-documents";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { FileText, MessageSquare, Clock, Loader2 } from "lucide-react";
import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function DashboardPage() {
  const { user, isLoading: authLoading } = useAuth();
  const { data: documentsData, isLoading: docsLoading } = useDocuments(1, 1);

  if (authLoading) {
    return <div className="p-8">Loading...</div>;
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-heading font-bold tracking-tight">Welcome, {user?.name}</h1>
        <p className="text-muted-foreground mt-2">Here&apos;s an overview of your knowledge base.</p>
      </div>

      <div className="grid gap-4 md:grid-cols-3">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Total Documents</CardTitle>
            <FileText className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {docsLoading ? <Loader2 className="h-4 w-4 animate-spin" /> : (documentsData?.total || 0)}
            </div>
            <p className="text-xs text-muted-foreground mt-1">
              Documents in your library
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Active Chats</CardTitle>
            <MessageSquare className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">0</div>
            <p className="text-xs text-muted-foreground mt-1">
              Conversations with AI
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Recent Activity</CardTitle>
            <Clock className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">-</div>
            <p className="text-xs text-muted-foreground mt-1">
              No recent activity
            </p>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Getting Started</CardTitle>
          <CardDescription>
            Start by uploading some documents to your library. Once uploaded and processed, you can ask questions about them.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <Link href="/documents">
            <Button>
              Go to Documents
            </Button>
          </Link>
        </CardContent>
      </Card>
    </div>
  );
}
