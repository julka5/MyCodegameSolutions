def card_conv(card):
    faces = { 'J' : 11,
              'Q' : 12,
              'K' : 13,
              'A' : 14
              }
    if card in faces:
        return faces[card]
    else:
        return int(card)


def adding_cards(winner):
    for i in range(len(queue_p1)):
        winner.append(queue_p1.pop(0))
    for i in range(len(queue_p2)):
        winner.append(queue_p2.pop(0))


def fight(player1, player2):
    c1 = player1.pop(0)
    c2 = player2.pop(0)
    queue_p1.append(c1)
    queue_p2.append(c2)
    if c1 > c2:
        adding_cards(player1)
    elif c2 > c1:
        adding_cards(player2)
    else:
        if len(player1)<4 or len(player2)<4:
            global pat
            pat = 1
        else:
            for i in range(3):
                queue_p1.append(player1.pop(0))
                queue_p2.append(player2.pop(0))
            fight(player1, player2)
        # --------------------------------------------------------------
n = int(input())  # the number of cards for player 1
player1 = []
for i in range(n):
    cardp_1 = input()[:-1]  # the n cards of player 1
    player1.append(card_conv(cardp_1))


m = int(input())  # the number of cards for player 2
player2 = []
for i in range(m):
    cardp_2 = input()[:-1]  # the m cards of player 2
    player2.append(card_conv(cardp_2))
# --------------------------------------------------------------

counter = 0
queue_p1 = []
queue_p2 = []
pat = None
while len(player2)>0 and len(player1)>0:
    if pat is not None:
        break
    fight(player1, player2)
    counter += 1


if len(player1)==0 and pat is None:
    result = "2 {}".format(counter)
elif len(player2)==0 and pat is None:
    result = "1 {}".format(counter)
else:
    result = "PAT"

print(result)