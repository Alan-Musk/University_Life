def swine_align(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Swine Align.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> swine_align(30, 45)  # The GCD is 15.
    True
    >>> swine_align(35, 45)  # The GCD is 5.
    False
    """
    # BEGIN PROBLEM 4a
    "*** YOUR CODE HERE ***"
    if player_score<10 or opponent_score<10:
        return False
    else:
        gcd=min(player_score,opponent_score)
        while gcd>=10:
            if(player_score%gcd==0 and opponent_score%gcd==0):
                return True
            gcd-=1
    return False

print(swine_align(36,24))