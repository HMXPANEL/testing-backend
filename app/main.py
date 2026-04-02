import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.api.websocket import router as ws_router
from app.core.task_manager.task_manager import task_manager
from app.core.controller_agent import controller_agent
from app.config import settings
from app.utils.logger import logger

# Import tools to register them in the registry
import app.tools.web
import app.tools.file
import app.tools.android
import app.tools.shell
import app.tools.memory_tool

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

# CORS configuration for Render deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API and WebSocket routers
app.include_router(api_router, prefix="/api")
app.include_router(ws_router)

@app.on_event("startup")
async def startup_event():
    """
    Initialize services and start background tasks on startup.
    """
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    
    # Start the task manager loop in the background
    # We pass the controller_agent's cognition_loop as the task executor
    asyncio.create_task(task_manager.start(controller_agent.cognition_loop))
    logger.info("Background task manager loop started.")

@app.on_event("shutdown")
async def shutdown_event():
    """
    Cleanup services on shutdown.
    """
    logger.info("Shutting down application...")
    task_manager.stop()

@app.get("/")
async def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "docs": "/docs"
    }

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred.", "detail": str(exc)}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
