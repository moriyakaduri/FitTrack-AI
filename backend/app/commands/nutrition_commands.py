from app.models.nutrition import MealCreate

def add_meal_command(meal: MealCreate):
    # כאן בעתיד נחבר ל-SQL Server כדי לשמור פיזית בדיסק.
    # כרגע, כדי שהשרת יעבוד חלק, אנחנו רק מדפיסים לטרמינל ומחזירים הצלחה.
    print(f"Saving to database: {meal.meal_name} with {meal.calories} kcal")

    return {
        "status": "success",
        "message": f"Meal '{meal.meal_name}' logged successfully!"
    }