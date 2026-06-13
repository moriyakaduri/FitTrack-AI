from pydantic import BaseModel

# מודל לצפייה בסיכום היומי (זה מה שהיה לנו קודם)
class DailyNutritionSummary(BaseModel):
    current_calories: int
    target_calories: int
    protein_g: int
    carbs_g: int
    fat_g: int

# מודל חדש - בשביל להוסיף ארוחה חדשה!
class MealCreate(BaseModel):
    meal_name: str
    calories: int
    protein_g: int

    # מודל חדש - בשביל להוסיף אימון חדש!
class WorkoutCreate(BaseModel):
    workout_type: str
    duration_minutes: int
    calories_burned: int


    # מודל להודעת טקסט או תיאור אוכל מהמשתמש ל-AI
class AIChatMessage(BaseModel):
    message: str