import os

import api.routers.auth as auth
import api.routers.get_investment_data as get_investment_data
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Fetch relevant environment variables
origins: List[str] = os.getenv("ALLOWED_ORIGINS", "").split(",")
enable_openapi_schema: str | bool = os.getenv("ENABLE_OPENAPI_SCHEMA", True)

# Set up FastAPI app
if enable_openapi_schema:
    app: FastAPI = FastAPI()
else:
    app = FastAPI(openapi_url=None)

# Add middleware to allow permitted origins (front-end)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add relevant routes
app.include_router(auth.router)
app.include_router(get_investment_data.router)
