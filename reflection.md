# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
Bug 1: Incorrect Hint Logic. I guessed -6 and the secret was 60. The game told me "Go LOWER!" Expected: Since -6 is less than 60, it should have said "Go HIGHER!"

Bug 2: The logic is currently flipped—it's telling you to go "HIGHER" when your guess is already higher than the secret.

Bug 3: Broken Scoring. The game started with a score of -30 and ended at -35 without me making successful moves. Expected: The score should start at 0 (or a positive number) and should not go negative.

Bug 4: Immediate "Out of Attempts" Error. Even though I had 7 attempts left in the debug info, the game displayed a red "Out of attempts!" box immediately. Expected: The game should only show "Out of attempts" when the counter hits 0.


## 2. How did you use AI as a teammate?

The AI suggestion was suggesting a help in a previously program, complete irrelavant, I used Gemini and VS code Co pilot. I found out because I reread the generated code by AI.


---

## 3. Debugging and testing your fixes

Yes AI help me in debugging, I ran multiple pytest to validate the program. I reload the local host and it fixed the issue



---

## 4. What did you learn about Streamlit and state?

In the original app, the secret number was being redefined every time the script ran. Because Streamlit treats every user interaction (like clicking a button or entering text) as a trigger to run the entire script from top to bottom, a line of code like secret_number = random.randint(1, 100) would execute again and again, generating a brand new number every time you tried to submit a guess.

Imagine a chef who forgets everything the moment they finish a dish. Every time you ask for a side of fries, they forget they already made you a burger and start the whole menu from scratch—that’s a Streamlit rerun. Session State is like giving that chef a notepad. It allows the app to "write down" important info (like the secret number) so that when the script reruns, it can check the notepad and remember the info from the previous step instead of starting over.

The fix involved initializing the secret number within st.session_state. By checking if the number already existed in the session state before creating a new one, the app ensured the number was only generated once at the start of the game and stayed the same throughout the session.

## 5. Looking ahead: your developer habits

Habit to reuse: A key strategy to reuse is Modularization and Testing. Moving the core game logic into logic_utils.py and using pytest ensures that the "brain" of the app works correctly independently of the UI. This makes debugging much faster because you can prove the math is right before you even open the browser.

What to do differently: Next time, I would be more skeptical of "first-draft" AI code, especially regarding state management. I would specifically prompt the AI to consider how variables will persist across reruns in a framework like Streamlit, rather than assuming it will handle persistence automatically.

Changing perspective on AI code: This project highlighted that while AI is great at writing functional-looking snippets, it often fails at "architectural awareness," such as how a specific framework's lifecycle works. It changed my view of AI from a "code creator" to a "junior partner" whose work requires rigorous verification and manual logic checks.