from fastapi import APIRouter

from app.queries.nutrition_queries import get_daily_nutrition_summary

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/profile/")
def get_user_profile():
    return {
        "username": "Moriah",
        "weight_status": "On Track"
    }


@router.get("/nutrition-summary/")
def get_nutrition():
    return get_daily_nutrition_summary()