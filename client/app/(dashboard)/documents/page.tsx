"use client";

import { useCallback, useState } from "react";
import { format } from "date-fns";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { UploadCloud, FileText, Loader2, Trash2, MoreVertical, Download, Edit2, Info } from "lucide-react";
import { useDocuments, useUploadDocument, useRenameDocument, useDocument } from "@/hooks/use-documents";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { api } from "@/lib/api";
import { useQueryClient } from "@tanstack/react-query";
import { Spinner } from "@/components/ui/spinner";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/components/ui/alert-dialog";

export default function DocumentsPage() {
  const { data, isLoading } = useDocuments();
  const uploadDoc = useUploadDocument();
  const renameDoc = useRenameDocument();
  const queryClient = useQueryClient();

  const [isDragging, setIsDragging] = useState(false);
  const [uploadError, setUploadError] = useState("");

  // Dialog states
  const [deleteId, setDeleteId] = useState<string | null>(null);
  const [renameId, setRenameId] = useState<string | null>(null);
  const [renameTitle, setRenameTitle] = useState("");
  const [detailsId, setDetailsId] = useState<string | null>(null);

  // Fetch document details when the dialog is open
  const { data: docDetails, isLoading: isLoadingDetails } = useDocument(detailsId);

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  }, []);

  const handleDragLeave = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
  }, []);

  const processFile = useCallback((file: File) => {
    setUploadError("");
    const allowed = [".pdf", ".docx", ".txt", ".md"];
    const ext = "." + file.name.split('.').pop()?.toLowerCase();

    if (!allowed.includes(ext)) {
      setUploadError(`File type ${ext} not supported. Use PDF, DOCX, TXT, or MD.`);
      return;
    }
    if (file.size > 10 * 1024 * 1024) {
      setUploadError("File exceeds 10MB limit.");
      return;
    }

    uploadDoc.mutate(file, {
      onError: (err: unknown) => {
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        const error = err as any;
        setUploadError(error.response?.data?.error?.message || "Upload failed");
      }
    });
  }, [uploadDoc]);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);

    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      processFile(e.dataTransfer.files[0]);
    }
  }, [processFile]);

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      processFile(e.target.files[0]);
    }
  };

  const executeDelete = async () => {
    if (!deleteId) return;
    try {
      await api.delete(`/documents/${deleteId}`);
      queryClient.invalidateQueries({ queryKey: ["documents"] });
    } finally {
      setDeleteId(null);
    }
  };

  const executeRename = (e: React.FormEvent) => {
    e.preventDefault();
    if (!renameId || !renameTitle.trim()) return;

    renameDoc.mutate(
      { id: renameId, title: renameTitle },
      {
        onSuccess: () => {
          setRenameId(null);
          setRenameTitle("");
        }
      }
    );
  };

  const handleDownload = (id: string, filename: string) => {
    const url = `/api/v1/documents/${id}/download`;
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  };

  const openRenameDialog = (id: string, currentTitle: string) => {
    setRenameId(id);
    setRenameTitle(currentTitle);
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-heading font-bold tracking-tight">Documents</h1>
          <p className="text-muted-foreground mt-2">Manage your knowledge base files.</p>
        </div>
      </div>

      <Card
        className={`border-dashed transition-colors ${isDragging ? 'border-primary bg-primary/5' : ''}`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <CardContent className="flex flex-col items-center justify-center p-12 text-center relative">
          <input
            type="file"
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
            onChange={handleFileSelect}
            accept=".pdf,.docx,.txt,.md"
            disabled={uploadDoc.isPending}
          />
          <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center mb-4">
            {uploadDoc.isPending ? (
              <Loader2 className="h-6 w-6 text-primary animate-spin" />
            ) : (
              <UploadCloud className="h-6 w-6 text-primary" />
            )}
          </div>
          <CardTitle className="mb-2">Upload Document</CardTitle>
          <CardDescription className="max-w-sm mb-6">
            Drag and drop your PDF, DOCX, TXT, or MD files here, or click to browse. Max 10MB.
          </CardDescription>

          {uploadError && (
            <div className="text-sm text-destructive font-medium mb-4">
              {uploadError}
            </div>
          )}

          <Button disabled={uploadDoc.isPending}>
            {uploadDoc.isPending ? "Uploading..." : "Select File"}
          </Button>
        </CardContent>
      </Card>

      <div className="pt-8">
        <h2 className="text-xl font-semibold mb-4">Your Library</h2>

        {isLoading ? (
          <div className="flex items-center justify-center text-center text-muted-foreground p-8">
            <Spinner />
          </div>
        ) : data?.items?.length === 0 ? (
          <div className="text-center text-muted-foreground p-8 border bg-card">
            No documents uploaded yet.
          </div>
        ) : (
          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {data?.items?.map((doc) => (
              <Card key={doc.id} className="relative group flex flex-col">
                <CardHeader className="flex flex-row items-start justify-between space-y-0 pb-2">
                  <div className="flex items-center space-x-2 truncate pr-6">
                    <FileText className="h-4 w-4 text-primary shrink-0" />
                    <CardTitle className="text-sm font-medium truncate" title={doc.title}>
                      {doc.title}
                    </CardTitle>
                  </div>

                  <div className="absolute top-2 right-2">
                    <DropdownMenu>
                      <DropdownMenuTrigger className="flex h-8 w-8 items-center justify-center rounded-md hover:bg-muted focus:outline-none transition-colors">
                        <MoreVertical className="h-4 w-4" />
                      </DropdownMenuTrigger>
                      <DropdownMenuContent align="end">
                        <DropdownMenuItem onClick={() => setDetailsId(doc.id)}>
                          <Info className="mr-2 h-4 w-4" />
                          View Details
                        </DropdownMenuItem>
                        <DropdownMenuItem onClick={() => handleDownload(doc.id, doc.filename)}>
                          <Download className="mr-2 h-4 w-4" />
                          Download
                        </DropdownMenuItem>
                        <DropdownMenuItem onClick={() => openRenameDialog(doc.id, doc.title)}>
                          <Edit2 className="mr-2 h-4 w-4" />
                          Rename
                        </DropdownMenuItem>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem
                          className="text-destructive focus:text-destructive focus:bg-destructive/10"
                          onClick={() => setDeleteId(doc.id)}
                        >
                          <Trash2 className="mr-2 h-4 w-4" />
                          Delete
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </div>
                </CardHeader>
                <CardContent className="flex-1">
                  <div className="text-xs text-muted-foreground flex items-center justify-between mt-2">
                    <span className="capitalize">{doc.processing_status.replace('_', ' ')}</span>
                    <span>{(doc.size / 1024).toFixed(1)} KB</span>
                  </div>
                  <div className="text-xs text-muted-foreground mt-1">
                    {format(new Date(doc.created_at), "MMM d, yyyy")}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        )}
      </div>

      {/* Delete Confirmation */}
      <AlertDialog open={!!deleteId} onOpenChange={(open) => !open && setDeleteId(null)}>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Delete Document?</AlertDialogTitle>
            <AlertDialogDescription>
              Are you sure you want to permanently delete this document? This action cannot be undone.
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Cancel</AlertDialogCancel>
            <AlertDialogAction onClick={executeDelete} variant="destructive">
              Delete
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>

      {/* Rename Dialog */}
      <Dialog open={!!renameId} onOpenChange={(open) => !open && setRenameId(null)}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Rename Document</DialogTitle>
            <DialogDescription>
              Change the display name of your document.
            </DialogDescription>
          </DialogHeader>
          <form onSubmit={executeRename}>
            <div className="py-4">
              <Label htmlFor="title" className="sr-only">Title</Label>
              <Input
                id="title"
                value={renameTitle}
                onChange={(e) => setRenameTitle(e.target.value)}
                autoFocus
              />
            </div>
            <DialogFooter>
              <Button type="button" variant="outline" onClick={() => setRenameId(null)}>
                Cancel
              </Button>
              <Button type="submit" disabled={!renameTitle.trim() || renameDoc.isPending}>
                {renameDoc.isPending && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
                Save Changes
              </Button>
            </DialogFooter>
          </form>
        </DialogContent>
      </Dialog>

      {/* Details Dialog */}
      <Dialog open={!!detailsId} onOpenChange={(open) => !open && setDetailsId(null)}>
        <DialogContent className="max-w-md">
          <DialogHeader>
            <DialogTitle>Document Details</DialogTitle>
          </DialogHeader>
          {isLoadingDetails ? (
            <div className="py-8 flex justify-center">
              <Spinner />
            </div>
          ) : docDetails ? (
            <div className="space-y-4 py-4 text-sm">
              <div className="grid grid-cols-3 gap-2">
                <span className="text-muted-foreground">Title</span>
                <span className="col-span-2 font-medium truncate" title={docDetails.title}>{docDetails.title}</span>
              </div>
              <div className="grid grid-cols-3 gap-2">
                <span className="text-muted-foreground">Filename</span>
                <span className="col-span-2">{docDetails.filename}</span>
              </div>
              <div className="grid grid-cols-3 gap-2">
                <span className="text-muted-foreground">Type</span>
                <span className="col-span-2 uppercase">{docDetails.file_type}</span>
              </div>
              <div className="grid grid-cols-3 gap-2">
                <span className="text-muted-foreground">Size</span>
                <span className="col-span-2">{(docDetails.size / 1024).toFixed(2)} KB</span>
              </div>
              <div className="grid grid-cols-3 gap-2">
                <span className="text-muted-foreground">Status</span>
                <span className="col-span-2 capitalize">{docDetails.processing_status.replace('_', ' ')}</span>
              </div>
              <div className="grid grid-cols-3 gap-2">
                <span className="text-muted-foreground">Pages</span>
                <span className="col-span-2">{docDetails.page_count}</span>
              </div>
              <div className="grid grid-cols-3 gap-2">
                <span className="text-muted-foreground">Chunks</span>
                <span className="col-span-2">{docDetails.chunk_count}</span>
              </div>
              <div className="grid grid-cols-3 gap-2">
                <span className="text-muted-foreground">Uploaded At</span>
                <span className="col-span-2">{format(new Date(docDetails.created_at), "PPp")}</span>
              </div>
            </div>
          ) : (
            <div className="py-4 text-destructive">Failed to load document details.</div>
          )}
          <DialogFooter>
            <Button onClick={() => setDetailsId(null)}>Close</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  );
}
