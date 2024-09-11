# Rock, Paper, and Scissor Game

This repository contains a simple implementation of the classic Rock, Paper, and Scissor game.

## Game Rules

- `1` = Rock
- `2` = Paper
- `3` = Scissor

## Brute Force Approach

The game logic is as follows:

- If `computer == your_ch`, it's a Tie.
- Otherwise:
  - If `computer == 1` (Rock):
    - `your_ch == 2` (Paper) --> You Win
    - `your_ch == 3` (Scissor) --> You Lose
  - If `computer == 2` (Paper):
    - `your_ch == 1` (Rock) --> You Lose
    - `your_ch == 3` (Scissor) --> You Win
  - If `computer == 3` (Scissor):
    - `your_ch == 1` (Rock) --> You Win
    - `your_ch == 2` (Paper) --> You Lose

### Code

```python
if computer == your_ch:
    print("It's a Tie.")
else:
    if computer == 1 and your_ch == 2:
        print("You Win.")
    elif computer == 1 and your_ch == 3:
        print("You Lose!")
    elif computer == 2 and your_ch == 1:
        print("You Lose!")
    elif computer == 2 and your_ch == 3:
        print("You Win.")
    elif computer == 3 and your_ch == 1:
        print("You Win.")
    elif computer == 3 and your_ch == 2:
        print("You Lose!")
    else:
        print("Error 404!")