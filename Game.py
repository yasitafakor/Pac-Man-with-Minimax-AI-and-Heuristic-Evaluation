import random
from random import randint
from Player import Player
from Ghost import Ghost
from os import system, name
from time import sleep
import os
import array as arr
from collections import deque
from queue import Queue
import copy


def distance(board, pacman):
    main_queue = []
    visit_list = []
    dist = {tuple(pacman): 0}

    main_queue.append(pacman)
    visit_list.append(pacman)

    while len(main_queue):
        temp = main_queue.pop(0)

        if board[temp[0]][temp[1]] == 1:
            return dist[tuple(temp)]

        if temp[0] >= 1 and board[temp[0] - 1][temp[1]] != 2:
            if [temp[0] - 1, temp[1]] not in visit_list:
                main_queue.append([temp[0] - 1, temp[1]])
                visit_list.append([temp[0] - 1, temp[1]])
                dist[tuple([temp[0] - 1, temp[1]])] = dist[tuple(temp)] + 1

        if temp[0] <= 7 and board[temp[0] + 1][temp[1]] != 2:
            if [temp[0] + 1, temp[1]] not in visit_list:
                main_queue.append([temp[0] + 1, temp[1]])
                visit_list.append([temp[0] + 1, temp[1]])
                dist[tuple([temp[0] + 1, temp[1]])] = dist[tuple(temp)] + 1

        if temp[1] >= 1 and board[temp[0]][temp[1] - 1] != 2:
            if [temp[0], temp[1] - 1] not in visit_list:
                main_queue.append([temp[0], temp[1] - 1])
                visit_list.append([temp[0], temp[1] - 1])
                dist[tuple([temp[0], temp[1] - 1])] = dist[tuple(temp)] + 1

        if temp[1] <= 16 and board[temp[0]][temp[1] + 1] != 2:
            if [temp[0], temp[1] + 1] not in visit_list:
                main_queue.append([temp[0], temp[1] + 1])
                visit_list.append([temp[0], temp[1] + 1])
                dist[tuple([temp[0], temp[1] + 1])] = dist[tuple(temp)] + 1

    return 0


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def gameover(pacman, pinky, blinky):
    if pinky == pacman or blinky == pacman:
        return 0
    else:
        return 1


def eutility(board, pacman, pinky, blinky, eaten):
    static_value = 50 * eaten
    o = distance(board, pacman)
    static_value += 3 * (40 - o)

    dist = abs(pacman[0] - pinky[0]) + abs(pacman[1] - pinky[1])
    dist = min(dist, abs(pacman[0] - blinky[0]) + abs(pacman[1] - blinky[1]))

    if dist <= 1:
        return dist

    return static_value + dist


def minimax(agent, current_depth, target_depth, copy_maze, copy_pacman, copy_pinky, copy_blinky, eaten=0):
    if current_depth == target_depth or gameover(copy_pacman, copy_pinky, copy_blinky) == 0:
        return eutility(copy_maze, copy_pacman, copy_pinky, copy_blinky, eaten)

    elif agent == 0:

        max_value = -10000000
        best_move = 0

        if copy_pacman[0] >= 1 and copy_maze[copy_pacman[0] - 1][copy_pacman[1]] != 2:
            flag = 1
            if copy_maze[copy_pacman[0] - 1][copy_pacman[1]] == 1:
                copy_maze[copy_pacman[0] - 1][copy_pacman[1]] = 0
                flag = 0
                eaten += 1
            copy_pacman[0] -= 1
            new_value = minimax(1, current_depth, target_depth, copy_maze, copy_pacman, copy_pinky, copy_blinky, eaten)

            if new_value > max_value:
                max_value = new_value
                best_move = 1

            copy_pacman[0] += 1
            if flag == 0:
                copy_maze[copy_pacman[0] - 1][copy_pacman[1]] = 1
                eaten -= 1

        # next

        if copy_pacman[0] <= 7 and copy_maze[copy_pacman[0] + 1][copy_pacman[1]] != 2:
            flag = 1
            if copy_maze[copy_pacman[0] + 1][copy_pacman[1]] == 1:
                copy_maze[copy_pacman[0] + 1][copy_pacman[1]] = 0
                flag = 0
                eaten += 1
            copy_pacman[0] += 1
            new_value = minimax(1, current_depth, target_depth, copy_maze, copy_pacman, copy_pinky, copy_blinky, eaten)

            if new_value > max_value:
                max_value = new_value
                best_move = 2

            copy_pacman[0] -= 1
            if flag == 0:
                copy_maze[copy_pacman[0] + 1][copy_pacman[1]] = 1
                eaten -= 1

        # next

        if copy_pacman[1] >= 1 and copy_maze[copy_pacman[0]][copy_pacman[1] - 1] != 2:
            flag = 1
            if copy_maze[copy_pacman[0]][copy_pacman[1] - 1] == 1:
                copy_maze[copy_pacman[0]][copy_pacman[1] - 1] = 0
                flag = 0
                eaten += 1

            copy_pacman[1] -= 1
            new_value = minimax(1, current_depth, target_depth, copy_maze, copy_pacman, copy_pinky, copy_blinky, eaten)

            if new_value > max_value:
                max_value = new_value
                best_move = 3

            copy_pacman[1] += 1
            if flag == 0:
                copy_maze[copy_pacman[0]][copy_pacman[1] - 1] = 1
                eaten -= 1

        # next

        if copy_pacman[1] <= 16 and copy_maze[copy_pacman[0]][copy_pacman[1] + 1] != 2:
            flag = 1
            if copy_maze[copy_pacman[0]][copy_pacman[1] + 1] == 1:
                copy_maze[copy_pacman[0]][copy_pacman[1] + 1] = 0
                flag = 0
                eaten += 1
            copy_pacman[1] += 1
            new_value = minimax(1, current_depth, target_depth, copy_maze, copy_pacman, copy_pinky, copy_blinky, eaten)

            if new_value > max_value:
                max_value = new_value
                best_move = 4

            copy_pacman[1] -= 1
            if flag == 0:
                eaten -= 1
                copy_maze[copy_pacman[0]][copy_pacman[1] + 1] = 1

        if current_depth == 0:
            return best_move

        return max_value

    elif agent == 1:

        min_value = 10000000
        # temp_array = possible_moves(copy_pinky, copy_maze)

        if copy_pinky[0] >= 1:
            if copy_maze[copy_pinky[0] - 1][copy_pinky[1]] != 2:
                # ghost pinky can go up
                copy_pinky[0] -= 1
                new_value = minimax(2, current_depth, target_depth, copy_maze, copy_pacman, copy_pinky, copy_blinky,
                                    eaten)
                min_value = min(new_value, min_value)
                copy_pinky[0] += 1

        if copy_pinky[0] <= 7:
            if copy_maze[copy_pinky[0] + 1][copy_pinky[1]] != 2:
                # ghost pinky can go down
                copy_pinky[0] += 1
                new_value = minimax(2, current_depth, target_depth, copy_maze, copy_pacman, copy_pinky, copy_blinky,
                                    eaten)
                copy_pinky[0] -= 1
                min_value = min(new_value, min_value)

        if copy_pinky[1] >= 1:
            if copy_maze[copy_pinky[0]][copy_pinky[1] - 1] != 2:
                # ghost pinky can go left
                copy_pinky[1] -= 1
                new_value = minimax(2, current_depth, target_depth, copy_maze, copy_pacman, copy_pinky, copy_blinky,
                                    eaten)
                min_value = min(new_value, min_value)
                copy_pinky[1] += 1

        if copy_pinky[1] <= 16:
            if copy_maze[copy_pinky[0]][copy_pinky[1] + 1] != 2:
                # ghost pinky can go right
                copy_pinky[1] += 1
                new_value = minimax(2, current_depth, target_depth, copy_maze, copy_pacman, copy_pinky, copy_blinky,
                                    eaten)
                min_value = min(new_value, min_value)
                copy_pinky[1] -= 1

            # so far we changed the pinky position and copy of our board based on the valid move that we have
            # right now

        return min_value

    elif agent == 2:

        min_value = 10000000
        # temp_array = possible_moves(copy_blinky, copy_maze)

        if copy_blinky[0] >= 1:
            if copy_maze[copy_blinky[0] - 1][copy_blinky[1]] != 2:
                # ghost pinky can go up
                copy_blinky[0] -= 1
                new_value = minimax(0, current_depth + 1, target_depth, copy_maze, copy_pacman, copy_pinky, copy_blinky,
                                    eaten)
                min_value = min(new_value, min_value)
                copy_blinky[0] += 1

        if copy_blinky[0] <= 7:
            if copy_maze[copy_blinky[0] + 1][copy_blinky[1]] != 2:
                # ghost pinky can go down
                copy_blinky[0] += 1
                new_value = minimax(0, current_depth + 1, target_depth, copy_maze, copy_pacman, copy_pinky,
                                    copy_blinky, eaten)
                min_value = min(new_value, min_value)
                copy_blinky[0] -= 1

        if copy_blinky[1] >= 1:
            if copy_maze[copy_blinky[0]][copy_blinky[1] - 1] != 2:
                # ghost pinky can go left
                copy_blinky[1] -= 1
                new_value = minimax(0, current_depth + 1, target_depth, copy_maze, copy_pacman, copy_pinky,
                                    copy_blinky, eaten)
                min_value = min(new_value, min_value)
                copy_blinky[1] += 1

        if copy_blinky[1] <= 16:
            if copy_maze[copy_blinky[0]][copy_blinky[1] + 1] != 2:
                # ghost pinky can go right
                copy_blinky[1] += 1
                new_value = minimax(0, current_depth + 1, target_depth, copy_maze, copy_pacman, copy_pinky,
                                    copy_blinky, eaten)
                min_value = min(new_value, min_value)
                copy_blinky[1] -= 1

            # so far we changed the blinky position and copy of our board based on the valid move that we have
            # right now

        return min_value


def move_pacman(maze, pacman, pinky, blinky):
    best_move_pacman = minimax(0, 0, 1, maze, pacman, pinky, blinky)

    return best_move_pacman


class Game:
    def __init__(self):
        self.board = [
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
            [1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1],
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
            [1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1]
        ]
        self.pacman = Player([0, 0])
        self.pinky = Ghost("pinky", ([6, 15]))
        self.blinky = Ghost("blinky", ([4, 1]))
        self.score = 0
        self.iteration = 0
        self.counter = 0
        self.pacman_win = 0
        self.pacman_lost = 0

    def print_board(self):
        for i in range(0, 9):
            for j in range(0, 18):
                if self.pinky.position[0] == i and self.pinky.position[1] == j:
                    print("R", end=" ")
                elif self.blinky.position[0] == i and self.blinky.position[1] == j:
                    print("R", end=" ")
                elif self.pacman.position[0] == i and self.pacman.position[1] == j:
                    print("P", end=" ")
                elif self.board[i][j] == 1:
                    print(".", end=" ")
                elif self.board[i][j] == 2:
                    print("%", end=" ")
                elif self.board[i][j] == 0:
                    print(" ", end=" ")
            print()
        print()

    def can_move_ghost(self, pinky, blinky):

        directions_pinky = []
        directions_blinky = []

        if pinky.position[0] - 1 >= 0 and self.board[pinky.position[0] - 1][pinky.position[1]] != 2:
            directions_pinky.append('up')
        if pinky.position[0] + 1 <= 8 and self.board[pinky.position[0] + 1][pinky.position[1]] != 2:
            directions_pinky.append('down')
        if pinky.position[1] - 1 >= 0 and self.board[pinky.position[0]][pinky.position[1] - 1] != 2:
            directions_pinky.append('left')
        if pinky.position[1] + 1 <= 17 and self.board[pinky.position[0]][pinky.position[1] + 1] != 2:
            directions_pinky.append('right')

        random_pinky = random.choice(directions_pinky)

        if random_pinky == 'up' and pinky.position[0] - 1 >= 0:
            pinky.up()
        elif random_pinky == 'down' and pinky.position[0] + 1 <= 8:
            pinky.down()
        elif random_pinky == 'left' and pinky.position[1] - 1 >= 0:
            pinky.left()
        elif random_pinky == 'right' and pinky.position[1] + 1 <= 17:
            pinky.right()

        if blinky.position[0] - 1 >= 0 and self.board[blinky.position[0] - 1][blinky.position[1]] != 2:
            directions_blinky.append('up')
        if blinky.position[0] + 1 <= 8 and self.board[blinky.position[0] + 1][blinky.position[1]] != 2:
            directions_blinky.append('down')
        if blinky.position[1] - 1 >= 0 and self.board[blinky.position[0]][blinky.position[1] - 1] != 2:
            directions_blinky.append('left')
        if blinky.position[1] + 1 <= 17 and self.board[blinky.position[0]][blinky.position[1] + 1] != 2:
            directions_blinky.append('right')

        random_blinky = random.choice(directions_blinky)

        if random_blinky == 'up' and blinky.position[0] - 1 >= 0:
            blinky.up()
        elif random_blinky == 'down' and blinky.position[0] + 1 <= 8:
            blinky.down()
        elif random_blinky == 'left' and blinky.position[1] - 1 >= 0:
            blinky.left()
        elif random_blinky == 'right' and blinky.position[1] + 1 <= 17:
            blinky.right()

    def run_game(self):
        while gameover(self.pacman.position, self.pinky.position, self.blinky.position) > 0:
            v = move_pacman(self.board, self.pacman.position, self.pinky.position, self.blinky.position)
            if v == 1:
                self.pacman.up()
            elif v == 2:
                self.pacman.down()
            elif v == 3:
                self.pacman.left()
            elif v == 4:
                self.pacman.right()

            self.score -= 1
            self.iteration += 1

            if self.board[self.pacman.position[0]][self.pacman.position[1]] == 1:
                self.board[self.pacman.position[0]][self.pacman.position[1]] = 0
                self.score += 10
                self.counter += 1

            if gameover(self.pacman.position, self.pinky.position, self.blinky.position) == 0:
                print("Pacman Bakht :(((")
                print("Score Pacman:", self.score)
                print("Iteration:", self.iteration)
                self.print_board()
                self.pacman_lost += 1
                break
            if self.counter == 106:
                print("Pacman Booorddd")
                print("Score Pacman:", self.score)
                print("Iteration:", self.iteration)
                self.print_board()
                self.pacman_win += 1
                break
            self.can_move_ghost(self.pinky, self.blinky)
            self.print_board()
            print("Score Pacman:", self.score)
            print("Iteration:", self.iteration)
            sleep(0.08)
            clear()


    def run_game_test(self):

        while gameover(self.pacman.position, self.pinky.position, self.blinky.position) > 0:

            v = move_pacman(self.board, self.pacman.position, self.pinky.position, self.blinky.position)
            if v == 1:
                self.pacman.up()
            elif v == 2:
                self.pacman.down()
            elif v == 3:
                self.pacman.left()
            elif v == 4:
                self.pacman.right()

            self.score -= 1
            self.iteration += 1

            if self.board[self.pacman.position[0]][self.pacman.position[1]] == 1:
                self.board[self.pacman.position[0]][self.pacman.position[1]] = 0
                self.score += 10
                self.counter += 1

            if gameover(self.pacman.position, self.pinky.position, self.blinky.position) == 0:
                self.pacman_lost += 1
                break
            if self.counter == 106:
                self.pacman_win += 1
                break

            self.can_move_ghost(self.pinky, self.blinky)

    def print_test(self):
        print("Lost: ", self.pacman_lost)
        print("Win: ", self.pacman_win)