# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

# 📝 Document Your Experience
## Describe the game's purpose.
A debugging project where I used GitHub Copilot to identify and fix logic errors in a Python Streamlit game

## Detail which bugs you found.
Bug 1: Incorrect Hint Logic.
I guessed -6 and the secret was 60. The game told me "Go LOWER!" 
Expected: Since -6 is less than 60, it should have said "Go HIGHER!"

Bug 2: The logic is currently flipped—it's telling you to go "HIGHER" when your guess is already higher than the secret.

Bug 3: Broken Scoring.
The game started with a score of -30 and ended at -35 without me making successful moves.
Expected: The score should start at 0 (or a positive number) and should not go negative.

Bug 4: Immediate "Out of Attempts" Error.
Even though I had 7 attempts left in the debug info, the game displayed a red "Out of attempts!" box immediately.
Expected: The game should only show "Out of attempts" when the counter hits 0.

## Explain what fixes you applied.
1.  Fixed the check_guess function so hints correctly guide the player higher or lower.
2.  Fixed the session state initialization so the game doesn't end immediately on start.
3.  Encountered a ModuleNotFoundError when running tests. Fixed it by using python3 -m pytest to ensure the project root was in the Python.
4.  Fix it end's the game 1 try early.
## 📸 Demo

<img width="1275" height="905" alt="Screenshot 2026-03-04 at 1 24 13 PM" src="https://github.com/user-attachments/assets/4d4ae0dc-1cb2-4ca4-a54b-4aa57d34562b" />


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
