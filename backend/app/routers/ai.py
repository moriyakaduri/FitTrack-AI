from fastapi import APIRouter
from app.models.nutrition import AIChatMessage

router = APIRouter(prefix="/ai", tags=["AI Consultant"])

@router.post("/analyze-food")
def analyze_food_intake(chat: AIChatMessage):
    # כאן בעתיד נחבר את ה-API של ה-AI שיודע לחשב אוטומטית לפי הטקסט!
    # כרגע מחזירים תשובה סטודנטיאלית שמדמה את הניתוח
    return {
        "ai_response": f"Analyzed: '{chat.message}'. Estimated values: 350 calories, 25g protein.",
        "status": "success"
    }