from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from constants import SERVER_URL, PORT, ENV
from apps.calculator.route import router as calculator_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def health():
    return {'message': "Server is running"}


app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])



if __name__ == "__main__":
    print(f"Starting server at {SERVER_URL}:{PORT} in {ENV} mode")
    uvicorn.run('main:app', host=SERVER_URL, port=int(PORT), reload=(ENV == 'development'))