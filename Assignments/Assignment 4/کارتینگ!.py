import sys

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self, card1, card2):
        self.player1.take_damage(card2.get_damage())
        self.player2.take_damage(card1.get_damage())

        if card1.get_damage() > card2.get_damage():
            self.player1.score += 1
        elif card2.get_damage() > card1.get_damage():
            self.player2.score += 1

    def print_results(self):
        print(self.player1.get_name() + " -> Score: " + str(self.player1.get_score()) + ", Health: " + str(
            self.player1.get_health()))
        print(self.player2.get_name() + " -> Score: " + str(self.player2.get_score()) + ", Health: " + str(
            self.player2.get_health()))

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.score = 0

    def take_damage(self, damage):
        self.health -= damage

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_score(self):
        return self.score

class Card:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_damage(self):
        return self.damage

scan = sys.stdin

try:
    str1, str2 = input().strip().split()

    hp1, hp2 = [int(x) for x in scan.readline().split()]
    dmg1, dmg2, dmg3 = [int(x) for x in scan.readline().split()]

    player1 = Player(str1, hp1)
    player2 = Player(str2, hp2)

    card1 = Card("A", dmg1)
    card2 = Card("B", dmg2)
    card3 = Card("C", dmg3)

    game = Game(player1, player2)

    for i in range(3):
        cardOne, cardTwo = input().strip().split()

        if cardOne == "A" and cardTwo == "B":
            game.play_round(card1, card2)
        if cardOne == "A" and cardTwo == "C":
            game.play_round(card1, card3)

        if cardOne == "B" and cardTwo == "A":
            game.play_round(card2, card1)
        if cardOne == "B" and cardTwo == "C":
            game.play_round(card2, card3)

        if cardOne == "C" and cardTwo == "A":
            game.play_round(card3, card1)
        if cardOne == "C" and cardTwo == "B":
            game.play_round(card3, card2)

    game.print_results()
    
except ValueError:
    print("Invalid Command.")