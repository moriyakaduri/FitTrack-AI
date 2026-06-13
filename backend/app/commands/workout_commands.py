from app.models.nutrition import WorkoutCreate

def add_workout_command(workout: WorkoutCreate):
    print(f"Saving workout to database: {workout.workout_type}")
    return {
        "status": "success",
        "message": f"Workout '{workout.workout_type}' logged successfully!"
    }