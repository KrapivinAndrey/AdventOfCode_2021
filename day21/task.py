with open("input.txt") as f:
    player1 = int(f.readline().strip()[-1])
    player2 = int(f.readline().strip()[-1])


dice = 1
count = score1 = score2 = 0


def roll_dice():
    global dice
    global count

    a = dice
    dice += 1
    if dice == 101:
        dice = 1
    count += 1

    b = dice
    dice += 1
    if dice == 101:
        dice = 1
    count += 1

    c = dice
    dice += 1
    if dice == 101:
        dice = 1
    count += 1

    print(count)

    return a+b+c


while True:

    player1 += roll_dice()
    player1 = 10 if player1 % 10 == 0 else player1 % 10
    score1 += player1
    print(f"player One {player1} - {score1}")
    if score1 >= 1000:
        print(score2 * count)
        break

    player2 += roll_dice()
    player2 = 10 if player2 % 10 == 0 else player2 % 10
    score2 += player2
    print(f"player Two {player2} - {score2}")
    if score2 >= 1000:
        print(score1 * count)
        break


