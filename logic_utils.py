import random

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Hard":
        return 1, 500  # Fixed Hard range to be harder
    return 1, 100

def parse_guess(raw: str):
    if not raw or raw.strip() == "":
        return False, None, "Enter a guess."
    try:
        value = int(float(raw))
        return True, value, None
    except ValueError:
        return False, None, "That is not a number."

def check_guess(guess, secret):
    # Convert both to int to prevent the "Type Error" glitch
    guess = int(guess)
    secret = int(secret)
    
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess < secret:
        return "Too Low", "📈 Go HIGHER!"
    return "Too High", "📉 Go LOWER!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        # Bonus for winning early
        points = max(10, 100 - (attempt_number * 10))
        return current_score + points
    if outcome in ["Too High", "Too Low"]:
        # Subtract 5 points for every wrong guess, but don't go below 0
        return max(0, current_score - 5)
    return current_score