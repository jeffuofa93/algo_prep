def tournamentWinner(competitions, results):
    """
    comp = [home, away]
    result = 0 = away win
    result = 1 = home win

    my idea
    create a dictonary where the key is the string and value is the number of wins
    create a variable that tracks the current highest scoring string
    on each update check if the update made a new highest scoring string
    :param competitions:
    :param results:
    :return:
    """
    score_dict = {}
    cur_highest = None
    for i in range(len(competitions)):
        home = competitions[i][0]
        away = competitions[i][1]
        result = results[i]
        winner = home if result == 1 else away
        score_dict[winner] = score_dict.get(winner, 0) + 1
        if cur_highest is None:
            cur_highest = winner
        else:
            cur_highest = (
                winner if score_dict[winner] > score_dict[cur_highest] else cur_highest
            )
    return cur_highest
