import random

def play_game(bet):
    roll = random.randint(1, 6)
    if roll <= 2:
        return -bet
    else:
        return 2 * bet

def monte_carlo_simulation(num_trials, bet):
    total_return = 0
    for _ in range(num_trials):
        total_return += play_game(bet)
    return total_return / num_trials

num_trials = 1000000
bet_amount = 1
expected_return = monte_carlo_simulation(num_trials, bet_amount)

print("Expected return per game with a $1 bet:", expected_return)
