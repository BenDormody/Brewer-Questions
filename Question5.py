from sympy import symbols, Eq, solve


def main():
    """
    Question Setup:
    We are going to solve for two main probabilities:
    P(win in inning) = sum(P(home runs > road runs | road runs)P(road runs)) for all road run posibilities 0-3
    P(tie in inning) = sum(P(home runs == road runs| road runs)P(road runs)) for all road run possibilities 0-3

    Using these and the fact that
    P(win) = P(win in inning) + P(tie in inning)P(win)
    Which when solving for P(win) we get

    P(win) = P(win in inning)/(1 - P_tie_in_inning)

    and the fact that we want P(win) = .60, we can solve for p.
    We will use sympy to allow us to use variables in our equations that we can solve for.
    """

    # Set up the p as a symbol using sympy symbol class
    p = symbols('p')

    # In order these are win percentages where road runs are 0 , 1 , 2 (3 isn't included as at best we tie)
    P_win_in_inning = (p * .35) + (.45 * .40) + (.1 * .15)

    # This is probability of a tie where home and road score: (0,0), (1,1), (2,2), (3,3)
    P_tie_in_inning = ((p-1) * .35) + (.20 * .40) + (.15 * .15) + (.10 * .10)

    # This is the win probability we want
    P_win = .6
    # This is the equation shown in the notes above
    equation = Eq(P_win_in_inning / (1 - P_tie_in_inning), P_win)

    # Use sympy solve to solve this equation for p
    p_value = solve(equation, p)

    print(f'The value of p that makes our win probability 60% is {p_value}')


if __name__ == '__main__':
    main()
