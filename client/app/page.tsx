import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Brain, Shield, Zap, Search, ArrowRight, Code } from "lucide-react";

export const metadata = {
  title: "Atlas - Your AI-Powered Knowledge Base",
  description: "Upload, manage, and instantly chat with your documents using privacy-first local AI.",
};

export default function LandingPage() {
  return (
    <div className="flex min-h-screen flex-col bg-background selection:bg-primary/20">
      {/* Header */}
      <header className="sticky top-0 z-50 w-full border-b bg-background/80 backdrop-blur-md">
        <div className="container flex h-16 items-center justify-between px-4 md:px-6 mx-auto">
          <div className="flex items-center gap-2">
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary text-primary-foreground font-bold">
              A
            </div>
            <span className="text-xl font-heading font-bold tracking-tight">Atlas</span>
          </div>
          <nav className="flex items-center gap-4">
            <Link href="/login" className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors">
              Log in
            </Link>
            <Link href="/register">
              <Button size="sm" className="rounded-full">Get Started</Button>
            </Link>
          </nav>
        </div>
      </header>

      <main className="flex-1">
        {/* Hero Section */}
        <section className="w-full py-24 md:py-32 lg:py-48 overflow-hidden relative">
          <div className="absolute inset-0 bg-grid-zinc-200/50 dark:bg-grid-zinc-800/50 bg-position-[bottom_1px_center] mask-[linear-gradient(to_bottom,transparent,black)] pointer-events-none" />
          <div className="container px-4 md:px-6 mx-auto relative z-10">
            <div className="flex flex-col items-center space-y-8 text-center">
              <div className="inline-flex items-center rounded-full border px-3 py-1 text-sm font-medium bg-muted/50 backdrop-blur-sm">
                <span className="flex h-2 w-2 rounded-full bg-primary mr-2"></span>
                Now live at atlas.iamdainwi.dev
              </div>
              <h1 className="text-4xl font-heading font-extrabold tracking-tight sm:text-5xl md:text-6xl lg:text-7xl max-w-4xl text-balance">
                Your Second Brain, <br className="hidden sm:block" />
                <span className="text-transparent bg-clip-text bg-linear-to-r from-primary to-blue-600">Powered by AI.</span>
              </h1>
              <p className="mx-auto max-w-175 text-muted-foreground md:text-xl text-balance">
                Upload your PDFs, Word documents, and text files. Instantly extract insights and ask questions using secure, local AI models.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
                <Link href="/register" className="w-full sm:w-auto">
                  <Button size="lg" className="w-full rounded-full gap-2 text-base h-12 px-8">
                    Start Building <ArrowRight className="w-4 h-4" />
                  </Button>
                </Link>
                <Link href="/login" className="w-full sm:w-auto">
                  <Button size="lg" variant="outline" className="w-full rounded-full gap-2 text-base h-12 px-8 bg-background/50 backdrop-blur-sm">
                    View Demo Dashboard
                  </Button>
                </Link>
              </div>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section className="w-full py-24 bg-muted/30 border-t">
          <div className="container px-4 md:px-6 mx-auto">
            <div className="flex flex-col items-center justify-center space-y-4 text-center mb-16">
              <h2 className="text-3xl font-heading font-bold tracking-tight md:text-4xl">
                Everything you need to manage knowledge
              </h2>
              <p className="max-w-225 text-muted-foreground md:text-lg">
                Atlas combines robust file storage with cutting-edge Retrieval-Augmented Generation (RAG) to give you instant answers from your own data.
              </p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
              {/* Feature 1 */}
              <div className="flex flex-col items-start space-y-3 p-6 rounded-2xl bg-background border shadow-sm transition-all hover:shadow-md">
                <div className="p-3 rounded-lg bg-primary/10 text-primary">
                  <Shield className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold">Privacy First</h3>
                <p className="text-sm text-muted-foreground">
                  Your documents never leave your server. Powered entirely by local Ollama models for absolute privacy.
                </p>
              </div>
              {/* Feature 2 */}
              <div className="flex flex-col items-start space-y-3 p-6 rounded-2xl bg-background border shadow-sm transition-all hover:shadow-md">
                <div className="p-3 rounded-lg bg-blue-500/10 text-blue-500">
                  <Brain className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold">Smart RAG</h3>
                <p className="text-sm text-muted-foreground">
                  Advanced text chunking and vector embeddings ensure the AI understands the exact context of your query.
                </p>
              </div>
              {/* Feature 3 */}
              <div className="flex flex-col items-start space-y-3 p-6 rounded-2xl bg-background border shadow-sm transition-all hover:shadow-md">
                <div className="p-3 rounded-lg bg-green-500/10 text-green-500">
                  <Search className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold">Instant Search</h3>
                <p className="text-sm text-muted-foreground">
                  Find exactly what you are looking for across thousands of documents in milliseconds.
                </p>
              </div>
              {/* Feature 4 */}
              <div className="flex flex-col items-start space-y-3 p-6 rounded-2xl bg-background border shadow-sm transition-all hover:shadow-md">
                <div className="p-3 rounded-lg bg-orange-500/10 text-orange-500">
                  <Zap className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-bold">Lightning Fast</h3>
                <p className="text-sm text-muted-foreground">
                  Built on FastAPI and Next.js for a blazingly fast, responsive, and seamless user experience.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* How It Works Section */}
        <section className="w-full py-24 border-t">
          <div className="container px-4 md:px-6 mx-auto">
            <div className="flex flex-col items-center justify-center space-y-4 text-center mb-16">
              <h2 className="text-3xl font-heading font-bold tracking-tight md:text-4xl">
                How Atlas Works
              </h2>
              <p className="max-w-225 text-muted-foreground md:text-lg">
                Three simple steps to transform your static documents into an interactive knowledge base.
              </p>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-12 lg:gap-16">
              {/* Step 1 */}
              <div className="flex flex-col items-center text-center space-y-4">
                <div className="flex h-16 w-16 items-center justify-center rounded-full bg-primary/10 text-primary font-heading font-bold text-2xl">
                  1
                </div>
                <h3 className="text-xl font-bold">Upload Your Files</h3>
                <p className="text-muted-foreground">
                  Securely upload your PDFs, DOCX, or text files to your local server. Your data remains entirely private and under your control.
                </p>
              </div>
              {/* Step 2 */}
              <div className="flex flex-col items-center text-center space-y-4">
                <div className="flex h-16 w-16 items-center justify-center rounded-full bg-blue-500/10 text-blue-500 font-heading font-bold text-2xl">
                  2
                </div>
                <h3 className="text-xl font-bold">AI Processing</h3>
                <p className="text-muted-foreground">
                  Atlas automatically chunks your text and generates high-dimensional vector embeddings, mapping the semantic meaning of your documents.
                </p>
              </div>
              {/* Step 3 */}
              <div className="flex flex-col items-center text-center space-y-4">
                <div className="flex h-16 w-16 items-center justify-center rounded-full bg-green-500/10 text-green-500 font-heading font-bold text-2xl">
                  3
                </div>
                <h3 className="text-xl font-bold">Ask Anything</h3>
                <p className="text-muted-foreground">
                  Open a chat and ask complex questions. The local LLM retrieves the exact context it needs to give you a highly accurate, cited answer.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Final CTA Section */}
        <section className="w-full py-24 bg-primary text-primary-foreground">
          <div className="container px-4 md:px-6 mx-auto">
            <div className="flex flex-col items-center justify-center space-y-8 text-center">
              <h2 className="text-3xl font-heading font-bold tracking-tight md:text-5xl max-w-2xl text-balance">
                Ready to rethink how you manage information?
              </h2>
              <p className="max-w-225 md:text-xl text-primary-foreground/80">
                Join now to experience the future of local, privacy-first AI document analysis.
              </p>
              <Link href="/register">
                <Button size="lg" variant="secondary" className="rounded-full h-14 px-10 text-lg font-medium shadow-lg hover:shadow-xl transition-all">
                  Create Your Free Account
                </Button>
              </Link>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="w-full border-t bg-background py-8">
        <div className="container flex flex-col md:flex-row items-center justify-between gap-4 px-4 md:px-6 mx-auto text-sm text-muted-foreground">
          <div className="flex items-center gap-2">
            <div className="font-heading font-semibold text-foreground">Atlas</div>
            <span>© {new Date().getFullYear()}</span>
          </div>
          <div className="flex gap-4">
            <a href="https://atlas.iamdainwi.dev" className="hover:text-foreground transition-colors font-medium">
              atlas.iamdainwi.dev
            </a>
            <a href="#" className="hover:text-foreground transition-colors flex items-center gap-1">
              <Code className="w-4 h-4" /> GitHub
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}
