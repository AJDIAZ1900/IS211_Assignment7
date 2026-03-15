import random

random.seed(0)

class Die:
    def roll(self):
        return random.randint(1,6)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class PigGame:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.die = Die()
        self.current_player = 0

    def play(self):
        while True:
            player = self.players[self.current_player]
            turn_total = 0

            print(f"\n{player.name}'s turn")
            print(f"Total score: {player.score}")

            while True:
                decision = input("Roll or hold? (r/h): ")

                if decision == 'r':
                    roll = self.die.roll()
                    print("Rolled:", roll)

                    if roll == 1:
                        print("Turn over! No points earned.")
                        turn_total = 0
                        break
                    else:
                        turn_total += roll
                        print("Turn total:", turn_total)

                elif decision == 'h':
                    player.score += turn_total
                    print("Score added. Total score:", player.score)
                    break

            if player.score >= 100:
                print(player.name, "wins!")
                break

            self.current_player = (self.current_player + 1) % 2


game = PigGame()
game.play()
