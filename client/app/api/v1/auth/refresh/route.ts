import { fetchFastAPI } from "@/lib/server-api";
import { cookies } from "next/headers";
import { NextResponse } from "next/server";

export async function POST() {
  try {
    const cookieStore = await cookies();
    const refreshToken = cookieStore.get("refresh_token")?.value;

    if (!refreshToken) {
      return NextResponse.json(
        { success: false, error: { message: "No refresh token available" } },
        { status: 401 }
      );
    }

    const res = await fetchFastAPI("/api/v1/auth/refresh", {
      method: "POST",
      body: JSON.stringify({ refresh_token: refreshToken }),
    });

    const data = await res.json();

    if (res.ok && data.success && data.data) {
      // Set new access token (HttpOnly)
      cookieStore.set("access_token", data.data.access_token, {
        httpOnly: true,
        secure: process.env.NODE_ENV === "production",
        sameSite: "lax",
        path: "/",
        maxAge: data.data.expires_in,
      });

      // Strip tokens from response
      const safeData = { ...data };
      safeData.data = { message: "Token refreshed successfully" };
      
      return NextResponse.json(safeData, { status: res.status });
    }

    return NextResponse.json(data, { status: res.status });
  } catch (error) {
    return NextResponse.json(
      { success: false, error: { message: "Internal Server Error" } },
      { status: 500 }
    );
  }
}
