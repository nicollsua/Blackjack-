# Blackjack-
This project is a Python implementation of the classic Blackjack card game. The game includes features such as user and dealer gameplay, multiplayer support, scorekeeping across multiple rounds, and player elimination. The code is structured with object-oriented programming principles, and core game logic is broken down into modular, reusable functions.

Features
**Single and Multiplayer Modes:**
The game allows for multiple players to compete individually against the dealer.
Each player takes turns drawing cards, followed by the dealer’s turn.

**Game Logic:**
Players aim to get a hand value as close to 21 as possible without exceeding it (busting).
The dealer plays according to standard Blackjack rules: standing at 17 or higher and hitting otherwise.
Cards are randomly generated, and hand values are calculated based on card rankings.

**Advanced Features:**
Multiple rounds with scorekeeping: Players' scores increase or decrease based on wins/losses, and a push (tie) results in no score change.
Elimination: Players are eliminated if their score reaches 0, and the game ends when all players are eliminated.

**File Structure**
blackjack.py: Main game loop that controls the flow of the game for both the user and the dealer.
blackjack_helper.py: Contains helper functions that simplify game operations such as card drawing, hand value calculation, and result printing.
name.py, value.py, end_status.py: Supportive files from Part 1 that help with card naming, card value determination, and end-game status (Blackjack, Bust, or Push).

**How the Game Works**
1. User Turn
Players are dealt two cards, and their hand value is calculated.
Players can choose to "hit" (draw an additional card) or "stand" (keep their current hand).
The player's hand value is recalculated after each hit. If it exceeds 21, the player busts and automatically loses.
2. Dealer Turn
The dealer follows strict rules: They draw cards until their hand value is 17 or higher. If the dealer busts (exceeds 21), they lose.
The dealer's hand is revealed after all players have taken their turns.
3. Game Result
After both the user and dealer have finished, the game compares the hand values.
The winner is determined based on whose hand is closer to 21 without exceeding it.
If a tie occurs, it results in a push.

**Multiplayer and Scorekeeping (Extra Features)**
At the start of the game, users are prompted to input the number of players and their names.
Each player's score starts at 3 and is adjusted after every round based on win/loss conditions.
If a player's score reaches 0, they are eliminated, and the game continues with the remaining players.
The game ends if all players are eliminated or if users decide not to play another round.
