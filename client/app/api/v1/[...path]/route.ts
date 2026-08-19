import { fetchFastAPI } from "@/lib/server-api";
import { cookies } from "next/headers";
import { NextRequest, NextResponse } from "next/server";

async function proxyRequest(request: NextRequest, { params }: { params: Promise<{ path: string[] }> }) {
  try {
    const { path } = await params;
    const endpoint = `/api/v1/${path.join("/")}`;
    
    const searchParams = request.nextUrl.search;
    const fullUrl = `${endpoint}${searchParams}`;

    const cookieStore = await cookies();
    const token = cookieStore.get("access_token")?.value;

    const headers = new Headers();
    if (token) {
      headers.set("Authorization", `Bearer ${token}`);
    }

    // Forward the body if it's a mutation method
    const hasBody = !["GET", "HEAD"].includes(request.method);
    const body = hasBody ? await request.arrayBuffer() : undefined;
    
    // Copy content type if body exists
    if (hasBody) {
      const contentType = request.headers.get("content-type");
      if (contentType) {
        headers.set("Content-Type", contentType);
      }
    }

    const res = await fetchFastAPI(fullUrl, {
      method: request.method,
      headers,
      body,
    });

    // Handle 204 No Content explicitly (no body to parse)
    if (res.status === 204) {
      return new NextResponse(null, { status: 204 });
    }

    // Handle responses that might not be JSON (like downloads in the future)
    const contentType = res.headers.get("content-type");
    if (contentType && contentType.includes("application/json")) {
      const data = await res.json();
      // If we get a 401 from FastAPI, we pass it back.
      // The Axios interceptor on the client will catch it and redirect to login.
      return NextResponse.json(data, { status: res.status });
    } else {
      const blob = await res.blob();
      const responseHeaders = new Headers(res.headers);
      return new NextResponse(blob, {
        status: res.status,
        headers: responseHeaders,
      });
    }
  } catch (error) {
    return NextResponse.json(
      { success: false, error: { message: "Internal Server Error" } },
      { status: 500 }
    );
  }
}

export const GET = proxyRequest;
export const POST = proxyRequest;
export const PUT = proxyRequest;
export const PATCH = proxyRequest;
export const DELETE = proxyRequest;
