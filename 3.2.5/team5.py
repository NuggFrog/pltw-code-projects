# Therefore, this is the best way to win at rock-paper-scissors: 
# if you lose the first round, switch to the thing that beats the thing your opponent just played. 
# If you win, don't keep playing the same thing, 
# but instead switch to the thing that would beat the thing that you just played. 
# In other words, play the hand your losing opponent just played. 
# To wit: you win a round with rock against someone else's scissors. 
# They are about to switch to paper. You should switch to scissors. 
# Got it? Good.

"""The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
"""

strategy_name = 'W Strategy'

def move(my_history, their_history):
    if len(my_history) == 0:
        return 'r'
    elif their_history[-1] == 'r':
        return 'p'
    elif their_history[-1] == 'p':
        return 's'
    elif their_history[-1] == 's':
        return 'r'
    else:
        return 'r'