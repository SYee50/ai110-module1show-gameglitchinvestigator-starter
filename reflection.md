# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game looked like it could potentially work, but there were several bugs when attempting to play it. It had a sidebar where the game difficulty could be selected, and there was information about the range and number of attempts for each difficulty level. There were instructions at the top of the page, but they did not appear to match the secret number range associated with the selected difficulty level. There was also a Developer Debug Info table that displayed the secret number, number of attempts, score, difficulty level, and history of attempts. The game included an input box for entering a guess, a button to submit the guess, and a checkbox that allowed the user to enable hints. When enabled, a hint was displayed after each attempt until all attempts were exhausted and the game ended. However, the hints appeared to be backwards. There was a New Game button. However, after clicking it, new guesses could not be submitted. Although a new secret number was generated, the number of attempts was set to zero.

- List at least two concrete bugs you noticed at the start  

1. The hints were backwards.
2. The New Game button did not allow new guesses to be submitted.
3. The range for the number to be guessed did not change when a new difficulty level was selected. The range was always 1 to 100.
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Clicked "New Game" button |A new game starts |Unable to submit new guesses even though a new "Secret" number was created and presumably it is a new game |Console does not allow me to submit new guesses for the new game, but based on the Developer Debug Info box a new secret number was generated, but the attempts are set to 0  |
|Guessed a number |Console hint should tell me to go lower if my guess is greater than the secret number or higher if the guess is less than the secret number |Console hint gives the opposite direction. If my guess is greater than the secret number it tells me to go higher, if is it less than then it tells me to go lower. |Hint does not give the correct direction for getting closer to the secret number. The hint tells the user to go higher if the guess is already higher than the secret number and lower if the guess is already lower than the secret number |
|Change the difficulty |The instructions message should update to reflect the selected difficulty level's number range |The range for the secret number always stayed the same, based on the instruction message |Selected an easy difficulty level, which should have a range of 1 to 20. However, the instructions still stated that the user should guess a number between 1 and 100, and the secret number shown in the Developer Debug Info box was outside the expected 1 to 20 range. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude and ChatGPT.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Claude suggested that a potential fix for starting a new game was to update the session state status to "playing" and set the session state attempts value to 1 when a new game is created. I verified the result by playing the game manually and selecting the New Game button and submitting guesses. If the guess was submitted and it was saved to the "history" list in the Developer Debug Info console and I was given a hint after clicking Submit Guess, then I considered that issue temporarily resolved, at least for being able to submit new guesses after clicking the New Game button.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Claude suggested that a potential fix for needing to submit a guess twice in order for the guess to be submitted was to delete three lines. This appeared to work at first. However, it did not work when I submitted the correct number. When submitting the correct number, the game still required users to click Submit Guess twice. I verified the result by first testing guessing incorrect numbers manually, then I tried guessing the correct number. The issue appeared to be resolved for incorrect guesses, but not for correct guesses.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided whether a bug was really fixed if it worked correctly across several rounds of manual testing (playing the game). I wrote out a few scenarios to test and then manually played the game. I wrote down the results for each scenario, and if it passed all of the scenarios I tried, then I considered the bug to be fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One test I ran was to manually test if the Submit Guess button worked with a single click. I tested this functionality by trying three different types of guesses. Guesses that were too low, guesses that were too high, and guesses that were correct. I entered guesses for each of the three guess types and clicked Submit Guess three times for each guess type. I wrote down the expected result and the actual result of each manual test. In this case, the tests showed that the correction allowed low and high guesses to be submitted with a single click of the button, but correct guesses still required two clicks of the button. This showed that multiple parts of the code can affect the same functionality, even when they initially appear to be controlled by a single section of code.

- Did AI help you design or understand any tests? How?

I didn't ask AI to help me design the tests I ran. However, I did ask it to help me understand why the correction did not work for all of my test scenarios. It helped me by letting me know that there was additional code that also controlled submitting guesses and gave me the lines of code that might be causing the additional glitch.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit "reruns" are the execution of the entire game code when a user interacts with the app, such as clicking a button or inputting a value. This behavior results in variables being reset. A session state is similar to a dictionary that persists between reruns. This allows states, or values, to be remembered across reruns, unlike regular variables that are reset. When using Streamlit, anything that needs to persist across reruns should be stored in session state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

One habit from this project that I want to reuse in future labs or projects is prompting the AI to explain the logic to me. I noticed that when I ask something like, "How can I correct the error?", the AI often tells me what to do line by line while providing minimal explanation. However, when I prompt the AI with something like "can you explain the underlying logic causing the error?" it tends to walk me through more of the code, explain what went wrong and why certain changes need to be made and the reasoning behind.

- What is one thing you would do differently next time you work with AI on a coding task?

One thing I would do differently next time I work with AI on a coding task is to ask it to design some tests for me. I plan to design my own tests, and did so for the project, but I am curious about what kind of tests the AI may suggest. Also, I believe this will allow me to create more robust tests in the future.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project changed the way I think about AI-generated code by showing me how powerful AI models can be for identifying and explaining errors. To correct some of the glitches I found, I used the Haiku model, which I had been told was one of the less powerful models, yet it still provided useful solutions and helpful explanations when I asked follow up questions.
