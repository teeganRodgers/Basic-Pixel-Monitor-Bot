Automated Reaction Game Bot
This is a Python script that uses GUI automation to play a popular online reaction time test. The bot achieves superhuman scores by programmatically detecting on-screen pixel color changes and triggering a mouse click in response.

How It Works
Screen Monitoring: The script continuously monitors a specific pixel on the screen within the game's interface.

Color Detection: It waits for the pixel to change from the "waiting" color (e.g., red) to the "go" color (e.g., green).

Automated Click: The moment the color change is detected, the script triggers an automated mouse click, resulting in a reaction time of just a few milliseconds.

Tech Stack
Language: Python

Libraries: PyAutoGUI (for screen reading and mouse control)

Usage
Run the script from your terminal:

python bot.py

Quickly move your mouse over the game's reaction area.

The script will automatically click when the visual cue appears.
