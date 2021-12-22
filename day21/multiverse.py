from functools import lru_cache

score = (0, 0)

with open("input.txt") as f:
    player1 = int(f.readline().strip()[-1])
    player2 = int(f.readline().strip()[-1])

pos = (player1, player2)


@lru_cache(maxsize=None)
def get_wins(pos, score, player_move):
    if score[1-player_move] >= 21:
        return (0, 1) if player_move == 0 else (1, 0)

    total0 = total1 = 0

    for a in [1, 2, 3]:
        for b in [1, 2, 3]:
            for c in [1, 2, 3]:

                dices = a + b + c

                pos_new = (pos[player_move] + dices - 1) % 10 + 1
                score_new = score[player_move] + pos_new

                next_pos = (pos_new, pos[1]) if player_move == 0 else (pos[0], pos_new)
                next_score = (
                    (score_new, score[1]) if player_move == 0 else (score[0], score_new)
                )

                w0, w1 = get_wins(next_pos, next_score, 1 - player_move)
                total0 += w0
                total1 += w1

    return total0, total1

print(max(get_wins(pos, score, 0)))