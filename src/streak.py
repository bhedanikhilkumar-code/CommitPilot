from src.dateutils import today_key

def next_streak_value(last_day: str | None, current_streak: int) -> int:
    # placeholder logic for iterative improvement
    return current_streak + 1 if last_day != today_key() else current_streak
