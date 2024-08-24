**Pac-Man with Minimax AI and Heuristic Evaluation**

### Overview

This project implements a terminal-based Pac-Man game where Pac-Man navigates a grid to consume food while avoiding randomly moving ghosts. The core of the AI is driven by the Minimax algorithm, enabling Pac-Man to make strategic decisions that maximize its score while maintaining a safe distance from the ghosts. Key features include:

- **Minimax Algorithm**: The algorithm is used to evaluate the best moves for Pac-Man by exploring various game states up to a defined depth. This allows Pac-Man to effectively plan its actions to avoid being caught by the ghosts and maximize its score.
  
- **Random Ghost Movement**: The ghosts (Pinky and Blinky) move randomly within the grid, providing dynamic challenges for Pac-Man. The AI strategy focuses on optimizing Pac-Man’s movements to outmaneuver these unpredictable enemies.

- **Heuristic Evaluation**: A custom heuristic function (`eutility`) evaluates game states based on Pac-Man’s distance to the ghosts, the amount of food eaten, and the remaining distance to the nearest food. This function is crucial for making informed decisions in the Minimax algorithm.

- **Game Testing**: The game includes testing functionality to run multiple simulations with varying depths of the Minimax algorithm, assessing the performance and effectiveness of the AI.

The project combines classic game mechanics with advanced AI techniques to create a challenging and engaging Pac-Man experience in a terminal environment.
### Game Class: Distance Method

In this Pac-Man game project, a significant challenge arose when implementing the AI for the Pac-Man agent. Initially, the agent was programmed to maximize its score by pursuing the closest food item using Euclidean distance. However, this approach led to a critical issue: Pac-Man often got stuck behind walls, repeatedly moving up and down without finding the correct path to the food, making it vulnerable to the ghosts.

#### Distance Method
To overcome this challenge, the `distance` method was introduced. This method calculates the shortest path from Pac-Man's current position to the nearest food item, taking into account the maze's walls. 

- **Breadth-First Search (BFS)**: The method uses BFS to explore the grid systematically, ensuring that the shortest path to the food is found, even if it's behind walls.
- **Avoiding Obstacles**: The method checks each possible move (up, down, left, right) and ensures that Pac-Man doesn't attempt to move through walls (`board[temp[0]][temp[1]] == 2`).
- **Accurate Food Targeting**: By accurately calculating the distance to the nearest reachable food, the method prevents Pac-Man from getting stuck and increases its chances of evading the ghosts.

This improvement significantly enhances the Pac-Man agent's ability to navigate the maze efficiently and avoid unnecessary dangers.

## Player and Ghost Classes

The **Player** and **Ghost** classes are central to managing the movement and positions of the agents within the game.

### Player Class
- **`self.position`**: Initializes the player's position on the game board.
- **Movement Methods**: 
  - `up()`: Moves the player up.
  - `down()`: Moves the player down.
  - `right()`: Moves the player to the right.
  - `left()`: Moves the player to the left.

### Ghost Class
- **`self.name`**: Unique identifier for each ghost ("Pinky" and "Blinky").
- **`getPosition()`**: Returns the ghost's current position.
- **Movement Methods**: Inherits the same movement methods as the Player class, allowing the ghosts to move around the board.

The `Player` class handles the basic movement, while the `Ghost` class extends it by adding names and a method to retrieve their positions.

### Game Over Method

The `gameover` method checks if Pac-Man's position matches either Pinky's or Blinky's. If it does, the method returns `0`, indicating the game is over. If not, it returns `1`, meaning the game continues.

### Eutility Method

The `eutility` method is a critical heuristic function designed to balance Pac-Man's objectives: maximizing score and maintaining a safe distance from ghosts.

- **Score Calculation**: The method starts by calculating a `static_value` based on the number of foods eaten by Pac-Man (`eaten`). This value increases as more food is consumed.
  
- **Distance to Food**: It then calculates the distance to the nearest food using the `distance` method and adjusts the score, encouraging Pac-Man to seek out food.

- **Ghost Avoidance**: The method also computes the Manhattan distance between Pac-Man and the nearest ghost (Pinky or Blinky). If a ghost is too close (`dist <= 1`), the method returns this distance as the utility, signaling a high-risk scenario.

- **Optimal Strategy**: The utility function has been refined through multiple iterations to achieve an optimal balance, guiding Pac-Man to maximize its score while avoiding close encounters with the ghosts.

This heuristic ensures Pac-Man plays strategically, prioritizing both safety and score.

### Minimax Method

The `minimax` method is a crucial part of the AI strategy, implementing the Minimax algorithm to make optimal decisions for Pac-Man.

- **Parameters**:
  - `agent`, `current_depth`, `target_depth`, `copy_maze`, `copy_pacman`, `copy_pinky`, `copy_blinky`, `eaten`: These parameters include the current game state, depth of the search tree, and copies of the game elements.

- **Base Case**:
  - The method first checks if the `current_depth` has reached the `target_depth` or if the game is over (`gameover(copy_pacman, copy_pinky, copy_blinky) == 0`).
  - If either condition is met, it returns the evaluated utility value from the `eutility` method.

This method ensures that Pac-Man's moves are evaluated up to a specified depth, making decisions that balance immediate rewards and long-term strategy.

### Minimax Method: Pac-Man's Moves

The Minimax algorithm evaluates Pac-Man’s optimal moves by simulating possible actions and their outcomes. Here’s how the method handles Pac-Man’s moves:

#### Pac-Man's Move Evaluation

1. **Initialization**:
   - `max_value` is set to a very low number (`-10000000`) to ensure any valid move will have a higher value.
   - `best_move` is initialized to `0` to keep track of the best move found.

2. **Move Validity Check**:
   - The method checks if Pac-Man's move in the given direction (e.g., up) is valid by ensuring:
     - The new position is within bounds (`copy_pacman[0] >= 1`).
     - The new position does not collide with a wall (`copy_maze[copy_pacman[0] - 1][copy_pacman[1]] != 2`).

3. **Food Check and Move Simulation**:
   - If the move is valid, the method checks if there is any food at the new position:
     - If food is present, `eaten` is incremented, and Pac-Man's position is updated.
   - It then recursively calls the `minimax` method to evaluate the new game state with `agent` set to `1` (indicating it's now the ghost's turn), passing in the updated state (`copy_maze`, `copy_pacman`, `copy_pinky`, `copy_blinky`, `eaten`).

4. **Maximizing Utility**:
   - The result of the recursive `minimax` call (`new_value`) is compared to `max_value`.
   - If `new_value` is greater than `max_value`, `max_value` is updated, and `best_move` is set to `1` (indicating the move was favorable).

5. **Restore State**:
   - After evaluating the move, Pac-Man's position is restored to its original place to test other possible moves (down, right, left) under the same conditions.

This process is repeated for all possible valid moves (up, down, right, left), with the method exploring each action's potential impact on the game. The goal is to find the move that maximizes Pac-Man's score while keeping a safe distance from ghosts.

### Minimax Method: Ghost Moves and Pac-Man Movement

#### Ghost Moves (agent == 1 or agent == 2)

1. **Initialization**:
   - `min_value` is set to a very high number (`10000000`) to ensure any valid move will have a lower value.

2. **Move Validity Check**:
   - For each ghost (Pinky or Blinky), the method checks if a move in the given direction (e.g., up) is valid:
     - Ensures the move keeps the ghost within bounds (`copy_pinky[0] >= 1`).
     - Checks that the new position does not collide with a wall (`copy_maze[copy_pinky[0] - 1][copy_pinky[1]] != 2`).

3. **Move Simulation**:
   - If the move is valid, the ghost’s position is updated.
   - The `minimax` method is then called recursively with `agent` set to `2` (or `3` for the second ghost), evaluating the new state of the game (`copy_maze`, `copy_pacman`, `copy_pinky`, `copy_blinky`, `eaten`).

4. **Minimizing Utility**:
   - The result of the recursive `minimax` call (`new_value`) is compared to `min_value`.
   - `min_value` is updated to the minimum of `new_value` and the current `min_value`.

5. **Restore State**:
   - After evaluating the move, the ghost’s position is restored to its original place to test other possible moves (up, down, right, left).

6. **Return Minimum Value**:
   - After considering all possible moves, the method returns the `min_value`, indicating the least favorable outcome for Pac-Man.

#### Pac-Man Movement

1. **Move Decision**:
   - The `move_pacman` method uses the `minimax` algorithm with `agent` set to `0` to determine the best move for Pac-Man.

2. **Execution**:
   - It returns the move with the highest utility value, guiding Pac-Man to make the optimal decision based on the current game state and future outcomes.

This process allows Pac-Man to make strategic decisions while navigating the maze and avoiding ghosts, leveraging the Minimax algorithm to simulate and evaluate possible moves for both Pac-Man and the ghosts.

### Game Class

The `Game` class manages the entire Pac-Man game, including board setup, player and ghost initialization, and game state visualization.

#### Initialization
- **`__init__` Method**:
  - **`self.board`**: Defines the 2D grid of the game where `1` represents food, `2` represents walls, and `0` represents empty spaces.
  - **`self.pacman`**: Initializes the Pac-Man player's position.
  - **`self.pinky`** and **`self.blinky`**: Initialize the two ghosts with their respective positions.
  - **`self.score`**: Tracks the score of Pac-Man.
  - **`self.iteration`**, **`self.counter`**, **`self.pacman_win`**, **`self.pacman_lost`**: Various counters to manage game progress and statistics.

#### Methods
- **`print_board`**:
  - **Purpose**: Visualizes the current state of the game board.
  - **Display**:
    - `.`: Represents food.
    - ` `: Represents empty spaces.
    - `%`: Represents walls.
    - `R`: Represents ghosts (Pinky and Blinky).
    - `P`: Represents Pac-Man.

The `print_board` method iterates over the grid and prints symbols for each element, including the positions of Pac-Man and the ghosts, allowing for a clear terminal-based visualization of the game state.

### `can_move_ghost` Method

The `can_move_ghost` method controls the movement of the ghosts, ensuring they move randomly but only in valid directions.

- **Purpose**: Randomly choose and execute a valid move for each ghost to prevent them from getting stuck.

#### Steps:

1. **Determine Possible Moves**:
   - For each ghost (Pinky and Blinky), the method calculates the valid movement directions based on their current position and the layout of the board.
   - Moves are considered valid if they do not lead the ghost into a wall (`2` on the board).

2. **Move Ghosts Randomly**:
   - For each ghost, it randomly selects from the valid directions and performs the corresponding move (up, down, left, or right) if the move remains within the board boundaries.

This method ensures that the ghosts are dynamic and continue to interact with Pac-Man without getting stuck in one place.

### `run_game` Method

The `run_game` method is the main loop for executing the Pac-Man game, handling the game state updates and interactions between Pac-Man and the ghosts.

#### Steps:

1. **Game Loop**:
   - The loop continues while Pac-Man is not caught by the ghosts (checked by `gameover` function).

2. **Move Pac-Man**:
   - Determine the best move for Pac-Man using `move_pacman` and execute it (up, down, left, or right).

3. **Update Score and Board**:
   - Decrease score by 1 for each move.
   - Increase score by 10 if Pac-Man eats food (cell value `1`), and update the board to remove the food.

4. **Check Game Over Conditions**:
   - If Pac-Man is caught by a ghost, print a loss message and update the game statistics.
   - If Pac-Man eats all the food (106 pieces), print a win message and update the game statistics.

5. **Move Ghosts**:
   - Call `can_move_ghost` to move the ghosts randomly.

6. **Print Board and Update Stats**:
   - Print the current game board and stats (score and iteration count).
   - Sleep for a short duration to slow down the game loop, then clear the screen for the next update.

This method drives the game by continuously updating Pac-Man's and the ghosts' positions, checking for win/loss conditions, and providing visual feedback through the console.

![sample](https://github.com/user-attachments/assets/b92a1c3c-a356-4f2b-ad87-5461fdf96cfb)
