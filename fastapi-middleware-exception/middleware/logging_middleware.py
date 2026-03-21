from fastapi import Request

async def log_requests(request: Request, call_next):
    # Before request
    print("🔹 Incoming Request")
    print(f"Method: {request.method}")
    print(f"Path: {request.url.path}")

    response = await call_next(request)

    # After response
    print("🔹 Response Sent")

    return response