import math
from scipy.stats import norm


def main():
    """
    Question setup:
    P_A = Probability that hitter A draws a walk
    P_B = Probability that hitter B draws a walk
    at_bats = Amount of plate appearances for player A and B

    We want to find:
    The probability that A > B we can write P(A - B > 0) = 1 - P(Z <= z)

    """
    P_A = .7
    P_B = .10

    at_bats = 100

    # Calculate mew A-B = mew A - mew B
    mew_A = at_bats * P_A
    mew_B = at_bats * P_B
    mew_A_minus_B = mew_A - mew_B

    # Calculates sigma A-B = sqrt(sigma^2 A + sigma^2 B)
    sigma_A_squared = mew_A * (1-P_A)
    sigma_B_squared = mew_B * (1-P_B)
    sigma_A_minus_B_squared = sigma_A_squared + sigma_B_squared
    sigma_A_minus_B = math.sqrt(sigma_A_minus_B_squared)

    # Calculate the z_score
    z_score = mew_A_minus_B/sigma_A_minus_B

    # Use norm.sf as 1 - norm.cdf would round our probability to 0 (Which it practically is)
    probability = norm.sf(abs(z_score))

    print(f'The Probability of player A drawing more walks then player B is:')
    print(f'{probability}')


if __name__ == '__main__':
    main()
