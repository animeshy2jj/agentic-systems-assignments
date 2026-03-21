from fastapi import FastAPI
from routes.hello import router as hello_router
from middleware.logging_middleware import log_requests
from exceptions.handlers import custom_404_handler

app = FastAPI()

# Register Middleware
app.middleware("http")(log_requests)

# Register Routes
app.include_router(hello_router)

# Register Exception Handler
app.add_exception_handler(404, custom_404_handler)