import json
from app.models.nutrition import MealCreate
from app.database.connection import get_db_connection

def add_meal_command(meal: MealCreate):
    # חיבור לדאטה-בייס בענן
    conn = get_db_connection()
    if not conn:
        return {"status": "error", "message": "Database connection failed"}
    
    try:
        cursor = conn.cursor()
        
        # הפיכת נתוני הארוחה לפורמט JSON בשביל ה-Event Sourcing
        event_data = json.dumps({
            "meal_name": meal.meal_name,
            "calories": meal.calories,
            "protein_g": meal.protein_g
        })
        
        # שמירת האירוע בטבלת האירועים בענן (בשלב זה נשתמש ב-UserID זמני 1)
        cursor.execute("""
            INSERT INTO SystemEvents (UserID, EventType, EventData)
            VALUES (?, ?, ?)
        """, (1, 'MEAL_LOGGED', event_data))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return {
            "status": "success",
            "message": f"Event 'MEAL_LOGGED' stored in Somee cloud for meal '{meal.meal_name}'!"
        }
        
    except Exception as e:
        return {"status": "error", "message": f"Failed to log event: {e}"}