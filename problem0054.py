with open("problem0054_data.txt", "r", encoding="utf-8") as file:
    games = file.read().split('\n')

ranks = {"1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6,
         "7" : 7, "8" : 8, "9" : 9, "T" : 10, "J" : 11, "Q" : 12,
         "K" : 13, "A" : 14}

for game in games:
    cards = game.split(" ")
    p1 = cards[0:5]
    p2 = cards[5:10]

    p1_ranks = [ranks[x[0]] for x in p1]
    p2_ranks = [ranks[x[0]] for x in p2]

    p1_suits = []