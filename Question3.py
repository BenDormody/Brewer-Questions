import math
from scipy.stats import norm


def part_a():
    """
    Question setup:
    Regress_Weights: A dictionary of the weights of the regression. Intercept will also store the intercept
    We want to find the probability that pitcher A through our model < pitcher B through our model.

    To do so we will use a similar approach to question 1 where our mews is the output of the regression
    We can do this via P(B-A > 0 )
    """
    regress_weights = {'intercept': 138, 'velocity': -
                       1.77, 'vertical_break': -1.08, 'height': 8.62}
    pitcher_a = {'velocity': 92, 'vertical_break': 18, 'height': 6}
    pitcher_b = {'velocity': 95, 'vertical_break': 12, 'height': 5.5}
    pitcher_a_mean = 0 + regress_weights['intercept']
    pitcher_b_mean = 0 + regress_weights['intercept']

    for key in pitcher_a.keys():
        pitcher_a_mean += (pitcher_a[key] * regress_weights[key])
    for key in pitcher_b.keys():
        pitcher_b_mean += (pitcher_b[key] * regress_weights[key])
    mew_b_minus_a = pitcher_b_mean - pitcher_a_mean
    sigma_a = 9
    sigma_b = 9
    sigma_a_minus_b = math.sqrt(sigma_a**2 + sigma_b**2)

    z_score = mew_b_minus_a/sigma_a_minus_b

    probability = norm.sf(abs(z_score))

    print(f'The Probability of player A having a lower run expectancy then B is:')
    print(f'{probability}')


def part_b():
    """
    Question setup:
    We can think about it this way:
    If Velocity has weight X on Induced Vertical Break
    and Induced Vertical Break has weight Y on Run Expectancy X + Y + I = Z
                                                              Z + X + Y+ I = R 
    then it can be assumed that Velocity would have weight XY on Run Expectancy if we remove Vertical Break
    """

    vertical_break_weight = -1.08
    original_velocity_weight = -1.77
    original_height_weight = 8.62
    original_intercept = 138

    velocity_via_vertical = vertical_break_weight * 0.0126
    height_via_vertical = vertical_break_weight * 2.60
    intercept_via_vertical = vertical_break_weight * -.48

    new_velocity_weight = original_velocity_weight + velocity_via_vertical
    new_height_weight = original_height_weight + height_via_vertical
    new_intercept = original_intercept + intercept_via_vertical

    print(f'Coefficients of run expectancy would be')
    print(f'Velocity (mph): {new_velocity_weight}')
    print(f'Release Height (ft): {new_height_weight}')
    print(f'Intercept: {new_intercept}')


def part_c():
    """
    We can safely assume that if we where to add height into this model, 
    the height of the pitcher would account for some of the magnitude of the coefficient 
    of release height we currently have. Therefore the release height would be of smaller magnitude.
    """
    print("The magnitude of the coefficient of release height would decrease as some of it would now be accounted for in the pitchers height")


def part_d():
    print('One example of this being violeted is with our intercept')
    print('This would imply a pitch thrown with 0mph velocity, 0in Induced Vertical Break and at a release height of 0ft\nwould have a run expectancy of 138 which is obviously not correct as it should be much higher')
    print('You could use more of a exponential model for such things as velocity as a pitch at 20mph is exponentially easier to hit than that at 90mph')


if __name__ == '__main__':
    print('Part A')
    part_a()
    print('\nPart B')
    part_b()
    print('\nPart C')
    part_c()
    print('\nPart D')
    part_d()
