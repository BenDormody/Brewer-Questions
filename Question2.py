def main():
    """
    Question setup:
    P_X = Probability pitcher pitches into strike zone
    P_S_given_X = Probability batter swings given pitch was into strike zone
    P_S_given_B = Probability batter swings given pitch was out of strike zone

    We want to find:
    P_X_given_S = Probability a pitch was in the strike zone given the batter swung

    Important Formulas:
    P(X|S) = P(XS)/P(S)
    P(S) = P(SX) + P(SB)
    P(SX) = P(S|X)P(X)
    """

    P_X = .48
    P_S_given_X = .64
    P_S_given_B = .29

    P_S_and_X = P_S_given_X * P_X
    # Note P_B = 1 - P_X
    P_S_and_B = P_S_given_B * (1 - P_X)

    P_S = P_S_and_X + P_S_and_B

    P_X_given_S = P_S_and_X/P_S

    print(f'Probability a pitch was in the strike zone given the batter swung is:')
    print(f'{P_X_given_S}')


if __name__ == '__main__':
    main()
