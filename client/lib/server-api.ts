export const FASTAPI_URL = process.env.FASTAPI_URL || "http://127.0.0.1:8000";

/**
 * Helper to fetch from FastAPI from Next.js Route Handlers.
 */
export async function fetchFastAPI(
  endpoint: string,
  options: RequestInit = {}
) {
  const url = `${FASTAPI_URL}${endpoint}`;
  
  const headers = new Headers(options.headers);
  if (!headers.has("Content-Type") && options.body && typeof options.body === "string") {
    headers.set("Content-Type", "application/json");
  }

  const res = await fetch(url, {
    ...options,
    headers,
  });

  // We usually want to return the raw response so the Next.js Route Handler 
  // can proxy the exact status code and payload back to the client.
  return res;
}
