import axios from "axios";

// This Axios instance points to the Next.js Route Handlers (BFF pattern).
// It does not point directly to the FastAPI server.
// The browser will automatically send HttpOnly cookies to the same domain.

export const api = axios.create({
  baseURL: "/api/v1",
  headers: {
    "Content-Type": "application/json",
  },
});

// Interceptor to handle global 401 Unauthorized errors (e.g. session expired)
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      // Prevent infinite loops if the refresh endpoint itself returns 401
      originalRequest._retry = true;

      // Don't try to refresh if the original request was to the auth endpoints
      if (originalRequest.url?.includes("/auth/login") || originalRequest.url?.includes("/auth/refresh")) {
        return Promise.reject(error);
      }

      try {
        // Attempt to refresh the token via our Next.js BFF proxy
        await axios.post("/api/v1/auth/refresh", {}, {
          headers: { "Content-Type": "application/json" }
        });
        
        // If successful, the BFF proxy just set a new HttpOnly access_token cookie!
        // We can safely retry the original request.
        return api(originalRequest);
      } catch (refreshError) {
        // If refresh fails (e.g. refresh token is expired too), redirect to login
        if (typeof window !== "undefined") {
          window.location.href = "/login";
        }
        return Promise.reject(refreshError);
      }
    }

    // For any other error (or if we already retried), just reject
    return Promise.reject(error);
  }
);
