# Therefore, this is the best way to win at rock-paper-scissors: 
# if you lose the first round, switch to the thing that beats the thing your opponent just played. 
# If you win, don't keep playing the same thing, 
# but instead switch to the thing that would beat the thing that you just played. 
# In other words, play the hand your losing opponent just played. 
# To wit: you win a round with rock against someone else's scissors. 
# They are about to switch to paper. You should switch to scissors. 
# Got it? Good.

# The following code is a simple implementation of the above strategy.
strategy_name = "Best Strategy"

# "R" stands for rock, "P" stants for paper, and "S" stands for scissors.

def move(my_history, their_history):
    # The first round is always played randomly.
    if my_history.shape[1] == 0:
        return "r", None
    # If the opponent played rock, play paper.
    if my_history[1, -1] == "r":
        return "p", None
    # If the opponent played paper, play scissors.
    if my_history[1, -1] == "p":
        return "s", None
    # If the opponent played scissors, play rock.
    if my_history[1, -1] == "s":
        return "r", None