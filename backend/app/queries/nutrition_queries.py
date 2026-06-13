from app.models.nutrition import DailyNutritionSummary

def get_daily_nutrition_summary() -> DailyNutritionSummary:
    # כאן בהמשך יבוא ה-SQL מול pyodbc. כרגע מחזירים נתונים זמניים לבדיקה
    return DailyNutritionSummary(
        current_calories=1450,
        target_calories=2000,
        protein_g=105,
        carbs_g=150,
        fat_g=45
    )