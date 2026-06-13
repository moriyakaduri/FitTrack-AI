from fastapi import APIRouter
from app.models.nutrition import MealCreate, WorkoutCreate
from app.queries.nutrition_queries import get_daily_nutrition_summary
from app.commands.nutrition_commands import add_meal_command
from app.commands.workout_commands import add_workout_command

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/profile")
def get_user_profile():
    return {
        "username": "Moriah",
        "weight_status": "On Track"
    }

@router.get("/nutrition-summary")
def get_nutrition():
    return get_daily_nutrition_summary()

@router.post("/log-meal")
def log_new_meal(meal: MealCreate):
    return add_meal_command(meal)

# נתיב כתיבה חדש (Command) - הוספת אימון למערכת!
@router.post("/log-workout")
def log_new_workout(workout: WorkoutCreate):
    return add_workout_command(workout)