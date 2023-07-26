# Pong Game

A simple implementation of the classic Pong game using Python's Turtle graphics library.

## Description

Pong is a two-player table tennis-themed arcade game where players control paddles and try to hit a ball back and forth. The objective is to prevent the ball from passing your paddle and score points when your opponent misses.

## How to Play

- Player 1 (Left Paddle): Use "W" to move the paddle up and "S" to move it down.
- Player 2 (Right Paddle): Use the "Up" arrow key to move the paddle up and the "Down" arrow key to move it down.

## Getting Started

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Open a terminal/command prompt and navigate to the project directory.
4. Run the main.py file to start the game.

## Controls

- Player 1 (Left Paddle):
  - Move Up: "W"
  - Move Down: "S"

- Player 2 (Right Paddle):
  - Move Up: "Up" arrow key
  - Move Down: "Down" arrow key

## Rules

- The game starts with the ball in the center of the screen, moving in a random direction.
- Each time a player misses the ball (lets it pass their paddle), the opposing player earns a point.
- The game continues until one of the players reaches the set number of points (default is 5).

## Features

- Smooth ball movement with adjustable speed.
- Paddles automatically bounce the ball back when hit.
- Real-time scoring displayed on the screen.
- Game window size is 800x600 pixels.

## Acknowledgments

This game was created as a fun project to practice Python programming with the Turtle graphics library.

## Credits

- The Paddle class: [paddle.py](paddle.py)
- The Ball class: [ball.py](ball.py)
- The Scoreboard class: [scoreboard.py](scoreboard.py)


# Ball Class

A class that defines the behavior and properties of the ball used in the Pong game.

## Description

The Ball class represents the ball object in the Pong game. It handles the ball's movement, bouncing off walls and paddles, and resetting its position.

## Class Methods

- `__init__(self)`: Initializes the ball object with the following properties:
  - Shape: "circle"
  - Color: "white"
  - Position: (0, 0) initially
  - X and Y movement speed: 10 (positive values indicate movement to the right/up, negative values to the left/down)
  - Move speed: 0.1 (controls the speed at which the ball moves)

- `move(self)`: Updates the ball's position by moving it forward based on its x and y movement speed.

- `bounce_y(self)`: Reverses the vertical movement direction of the ball when it collides with the top or bottom wall.

- `bounce_x(self)`: Reverses the horizontal movement direction of the ball when it collides with a paddle. It also slightly increases the ball's speed to make the game more challenging.

- `reset_position(self)`: Resets the ball's position to the center of the screen and restores its original movement speed. It also calls the `bounce_x()` method to randomize the ball's initial direction after each point scored.

## Usage

1. Import the `Ball` class into your main Pong game script.
2. Create an instance of the `Ball` class, which will represent the ball in the game.

   Example:
   ```python
   ball = Ball()
   ```

3. Update the ball's position and handle collisions with walls and paddles by calling the respective methods during the game loop.

   Example:
   ```python
   # Inside the game loop
   ball.move()

   # Collisions with walls
   if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()

   # Collisions with paddles
   if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
       ball.bounce_x()

   # Reset ball position after scoring
   if ball.xcor() > 380:
       ball.reset_position()

   if ball.xcor() < -380:
       ball.reset_position()
   ```

## Note

This class is part of the Pong game implementation and requires the `turtle` module to work correctly. For the full Pong game experience, ensure that you have the complete game script set up with paddles, score tracking, and user input handling.


# Paddle Class

A class that defines the behavior and properties of a paddle used in the Pong game.

## Description

The Paddle class represents a paddle object in the Pong game. It handles the paddle's movement, size, and appearance.

## Class Methods

- `__init__(self, position)`: Initializes the paddle object with the following properties:
  - Shape: "square"
  - Color: "white"
  - Size: 5 times taller (stretch_wid=5) and 1 times wider (stretch_len=1) than the default square size
  - Position: The initial position provided as an argument (x, y) when creating the paddle instance.

- `go_up(self)`: Moves the paddle upwards by 20 units on the y-axis.

- `go_down(self)`: Moves the paddle downwards by 20 units on the y-axis.

## Usage

1. Import the `Paddle` class into your main Pong game script.
2. Create instances of the `Paddle` class to represent the left and right paddles in the game. Provide the desired initial positions for each paddle.

   Example:
   ```python
   # Creating left paddle
   l_paddle = Paddle((-350, 0))

   # Creating right paddle
   r_paddle = Paddle((350, 0))
   ```

3. Set up event listeners to handle user input for moving the paddles up and down.

   Example:
   ```python
   # Left paddle controls:
   screen.onkey(l_paddle.go_up, "w")
   screen.onkey(l_paddle.go_down, "s")

   # Right paddle controls:
   screen.onkey(r_paddle.go_up, "Up")
   screen.onkey(r_paddle.go_down, "Down")
   ```

4. In the game loop, call the `go_up()` and `go_down()` methods based on user input to move the paddles.

   Example:
   ```python
   # Inside the game loop
   # Call the methods based on user input

   # Example: For the left paddle (control using "w" and "s" keys)
   # If "w" is pressed, move the left paddle up
   # If "s" is pressed, move the left paddle down

   # Example: For the right paddle (control using arrow keys)
   # If "Up" arrow key is pressed, move the right paddle up
   # If "Down" arrow key is pressed, move the right paddle down
   ```

## Note

This class is part of the Pong game implementation and requires the `turtle` module to work correctly. Make sure you have the complete game script set up, including the `Ball` class, score tracking, and user input handling, to experience the full functionality of the Pong game.


# Scoreboard Class

A class that defines the behavior and properties of the scoreboard used in the Pong game.

## Description

The Scoreboard class represents the scoreboard in the Pong game. It keeps track of the left and right players' scores and updates the display accordingly.

## Class Methods

- `__init__(self)`: Initializes the scoreboard with the following properties:
  - Color: "white"
  - Position: Hidden initially (off-screen)
  - Left player score: 0
  - Right player score: 0
  - Calls the `update_scoreboard()` method to display the initial scores.

- `update_scoreboard(self)`: Updates the displayed scores on the screen. It clears the previous score and writes the new scores for both players.

- `l_point(self)`: Awards a point to the left player and updates the scoreboard.

- `r_point(self)`: Awards a point to the right player and updates the scoreboard.

## Usage

1. Import the `Scoreboard` class into your main Pong game script.
2. Create an instance of the `Scoreboard` class, which will represent the scoreboard in the game.

   Example:
   ```python
   scoreboard = Scoreboard()
   ```

3. Update the scoreboard by calling the `l_point()` and `r_point()` methods when a player scores a point.

   Example:
   ```python
   # Inside the game loop

   # Detect right paddle miss:
   if ball.xcor() > 380:
       ball.reset_position()
       scoreboard.l_point()

   # Detect left paddle miss:
   if ball.xcor() < -380:
       ball.reset_position()
       scoreboard.r_point()
   ```

## Note

This class is part of the Pong game implementation and requires the `turtle` module to work correctly. Make sure you have the complete game script set up, including the `Ball` and `Paddle` classes, to experience the full functionality of the Pong game with the scoreboard tracking the scores for both players.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute and improve this game! Happy gaming!