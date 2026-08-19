import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  const token = request.cookies.get("access_token")?.value;
  const { pathname } = request.nextUrl;

  // Public routes that don't require authentication
  const isAuthRoute = pathname.startsWith("/login") || pathname.startsWith("/register");
  
  // Protect root route - redirect based on auth status
  if (pathname === "/") {
    if (token) {
      return NextResponse.redirect(new URL("/dashboard", request.url));
    }
    // If no token, allow them to view the landing page
    return NextResponse.next();
  }

  // If user is on an auth route but already has a token, redirect to dashboard
  if (isAuthRoute && token) {
    return NextResponse.redirect(new URL("/dashboard", request.url));
  }

  // If user is on a protected route but has no token, redirect to login
  const isProtectedRoute = 
    pathname.startsWith("/dashboard") || 
    pathname.startsWith("/documents") || 
    pathname.startsWith("/chat") || 
    pathname.startsWith("/search") ||
    pathname.startsWith("/settings");

  if (isProtectedRoute && !token) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     */
    "/((?!api|_next/static|_next/image|favicon.ico).*)",
  ],
};
