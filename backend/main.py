from fastapi import FastAPI
from app.routers import users, ai  # ייבוא של שני הראוטרים

app = FastAPI(title="FitTrack AI API")

# חיבור הראוטרים לשרת
app.include_router(users.router)
app.include_router(ai.router)

@app.get("/")
def read_root():
    return {"message": "FitTrack AI Server is Running Successfully!"}