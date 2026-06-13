from pydantic import BaseModel

class DailyNutritionSummary(BaseModel):
    current_calories: int
    target_calories: int
    protein_g: int
    carbs_g: int
    fat_g: int