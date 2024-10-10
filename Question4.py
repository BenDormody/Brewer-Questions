from collections import defaultdict
import random
"""
Question setup:

This question can most likely be approached in 2 ways:
1. Use expected values for teams final results to find probability that mets finish 3rd with normal distributions
2. Use simulation to simulate remaining games and count amount of times mets end in 3rd
I decided to take the second approach as it is more straightforward and could easily scale (code wise) with the addition of more games or teams

Drawbacks:
Simulation takes a lot of time, and results could vary each time run. The second of these drawbacks is dealt with due to our large sample size, which normalizes our results
"""


def simulate_season(teams, head_to_head):
    """
    This function takes in our teams and head_to_heads and does the following:
    1. Creates object results, with each team's current win/loss
    2. Loops through head_to_heads giving one team a win and the other a loss (50/50 chance)
    3. Loops through each teams remaining games and gives them a win 50% of the time and loss the other 50%
    """
    # Instantiate our dictionary for storing results
    results = defaultdict(lambda: {'wins': 0, 'losses': 0})

    # We will initialize this dictionary with our current wins/losses
    for team, wins, losses in teams:
        results[team]['wins'] = wins
        results[team]['losses'] = losses

    # First we will simulate head to heads in which only 1 of the 2 teams can win
    for (team1, team2), games in head_to_head.items():
        for _ in range(games):
            if random.random() < 0.5:
                results[team1]['wins'] += 1
                results[team2]['losses'] += 1
            else:
                results[team2]['wins'] += 1
                results[team1]['losses'] += 1

    # Simulate non head to head games where the win or loss of the team doesn't effect other teams
    for team, _, _ in teams:
        remaining_games = 162 - \
            (results[team]['wins'] + results[team]['losses'])
        for _ in range(remaining_games):
            if random.random() < 0.5:
                results[team]['wins'] += 1
            else:
                results[team]['losses'] += 1
    return results


def rank_teams(results, tiebreaker):
    """
    This function will rank our teams by sorting them using our helper function winloss_key.
    """
    def winloss_key(team):
        """
        This function creates a object in which we use to rank our teams. 
        It exists of a teams win/loss and then their tiebreaker index for ties
        """
        wins = results[team]['wins']
        total_games = wins + results[team]['losses']
        return (-wins / total_games, -tiebreaker.index(team))
    return sorted(results.keys(), key=winloss_key)


def main():
    """
    Main function that simulates rest of season, then adds to third_place_count if Mets ended in 3rd place.
    """
    # Create our teams and head_to_head objects. These can be changed and the simulation still functions
    teams = [
        ('San Diego Padres', 91, 66),
        ('New York Mets', 87, 70),
        ('Arizona Diamondbacks', 87, 71),
        ('Atlanta Braves', 86, 71)
    ]
    head_to_head = {
        ('New York Mets', 'Atlanta Braves'): 2,
        ('San Diego Padres', 'Arizona Diamondbacks'): 3
    }
    # The current order saved for tie breakers
    tie_breaker = [team for team, _, _ in teams]

    # Amount of simulations to run
    simulation_count = 1000000

    # Initialize variable to hold amount of times Mets end in 3rd place
    third_place_count = 0

    # Run through the simulations and update the third_place_count when our rank_teams function returns the Mets in 3rd
    for _ in range(simulation_count):
        results = simulate_season(teams, head_to_head)
        rankings = rank_teams(results, tie_breaker)
        if rankings.index('New York Mets') == 2:
            third_place_count += 1

    # Finally calculate the probability as the amount of simulations with mets in 3rd divided by the total simulations
    probability = third_place_count/simulation_count

    print(f'The probability Mets Finish 3rd is {probability}')


if __name__ == '__main__':
    main()
