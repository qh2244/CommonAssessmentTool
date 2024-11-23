"""
Main application entry point for the FastAPI service.

This module configures the FastAPI app, including routers and middleware,
and initializes the database during the startup event.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.clients.router import router as clients_router
from app.clients.database import create_clients_table

app = FastAPI()

# Set API endpoints on router
app.include_router(clients_router)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_methods=["*"],  # Allows all methods, including OPTIONS
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup_event():
    """
    Startup event handler that initializes the database by creating
    the necessary clients table if it doesn't already exist.
    """
    create_clients_table()
