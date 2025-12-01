# Minecraft Miner
- A simple minecraft auto clicker made to mine cobblestone from cobblestone generators.
- This simple script holds down the minecraft attack button to go afk when mining cobblestone

# Changing the configurations
- This script is configured to use ('x') as attack, also assumes you have '9' pickaxes, and you are using 'gold' pickaxes
- Enter the (main.py) file to follow the instructions below.

- To change the attack button, head to line 8 (pt.keyUp('x')) and change 'x' to whatever attack key you have set, example: (pt.keyUp('w')).
- Note: Mouse attack buttons are not yet supported.

- To change how many pickaxes it assumes you have, head to line 11 'pickaxes = 9' and change '9' to whatever amount you have...
- Note: your pickaxes must be in a row, the script loops through your hands/inventory(only the 9 ones on the main game) and attacks with the item in them.
- So if any of them aren't pickaxes, it will attack cobblestone with them!

- To change the type of pickaxe it assumes you have, it follows pickaxe attack speed... Head to line 18 (mine_block(25)) and change 25 to the attack speed of your pickaxe
- Note: 25 is the attack speed of a gold pickaxe

# IMPORTANT NOTE
- Before following the instructions to run on linux, you must setup a virtual enviroment within the project.
- Open the Visual studio code terminal, and type the following commands: (python3 -m venv venv) (source venv/bin/activate)
- This will enter a virtual enviroment where you can install everything via pip, and run the script
- If you accidently close the virtual enviroment in the terminal, simply run the source venv/bin/activate command again.

# Instructions #1 - Windows
--- requirements ---
- Visual Studio Code
- Python and it's libraries (such as pip)
- pyautogui (install via the visual studio code terminal: pip install pyautogui)

To run the script, type in the visual studio code terminal: (python ./main.py)
Quickly enter minecraft and position yourself infront of the cobblestone generator.

# Instructions #1 - Linux
--- requirements ---
- Visual Studio Code
- Python and it's libraries (such as pip)
- pyautogui (install via the visual studio code terminal: pip install pyautogui)

To run the script, type in the visual studio code terminal: (python3 ./main.py)
Quickly enter minecraft and position yourself infront of the cobblestone generator.