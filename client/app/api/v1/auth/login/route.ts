import { fetchFastAPI } from "@/lib/server-api";
import { cookies } from "next/headers";
import { NextResponse } from "next/server";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    
    const res = await fetchFastAPI("/api/v1/auth/login", {
      method: "POST",
      body: JSON.stringify(body),
    });

    const data = await res.json();

    if (res.ok && data.success && data.data) {
      const cookieStore = await cookies();
      
      // Set access token (HttpOnly)
      cookieStore.set("access_token", data.data.access_token, {
        httpOnly: true,
        secure: process.env.NODE_ENV === "production",
        sameSite: "lax",
        path: "/",
        maxAge: data.data.expires_in,
      });

      // Set refresh token (HttpOnly)
      cookieStore.set("refresh_token", data.data.refresh_token, {
        httpOnly: true,
        secure: process.env.NODE_ENV === "production",
        sameSite: "lax",
        path: "/",
        // Refresh token typically lives longer, e.g. 7 days. We don't get refresh expires_in from API currently,
        // so we'll just set it to 7 days
        maxAge: 7 * 24 * 60 * 60,
      });

      // Strip tokens from the response sent to the client browser for security
      const safeData = { ...data };
      safeData.data = { message: "Authenticated successfully" };
      
      return NextResponse.json(safeData, { status: res.status });
    }

    // Forward the error response from FastAPI
    return NextResponse.json(data, { status: res.status });
  } catch (error) {
    return NextResponse.json(
      { success: false, error: { message: "Internal Server Error" } },
      { status: 500 }
    );
  }
}
