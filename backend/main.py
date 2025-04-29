from fastapi import FastAPI, APIRouter

app = FastAPI()
api_router = APIRouter(prefix="/api")

@api_router.get("/")
def read_root():
    return {"message": " to the FastAPI app!"}

app.include_router(api_router)