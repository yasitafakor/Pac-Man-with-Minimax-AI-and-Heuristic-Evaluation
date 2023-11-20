from Game import Game

game = Game()
pacman_win = 0
pacman_lost = 0

for i in range(0, 10):
    game.run_game_test()

print("Depth = 0, result:")
game.print_test()

