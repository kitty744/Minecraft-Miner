# Minecraft Miner
- A simple minecraft auto clicker made to mine cobblestone from cobblestone generators.
- This simple script holds down the minecraft attack button to go afk when mining cobblestone
- NOTE: This script is configured to use ('x') as attack, also assumes you have '9' pickaxes, and you are using 'gold' pickaxes
- If you would like to change this, first step is to change 'pt.keyUp('x') to whatever key you are using as attack in minecraft, (currently mouse is not supported)
- To change number of pickaxes you have, go to the 'pickaxes' variable located at line '16'
- For the pickaxe type, it uses speed. 'gold' pickaxe has a speed of 25, and you need to change this based on your pickaxe type!
- Go to line (25) 'mine_block(25)' and change 25 to whatever attack rate your pickaxe has.

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