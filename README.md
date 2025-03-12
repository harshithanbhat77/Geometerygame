# Geometerygame

Geometry Game (CLI + Turtle Graphics)
This Python-based Geometry Game challenges users to guess a point inside a randomly generated rectangle and estimate its area. The game visually represents the shapes using Turtle Graphics.

✅ Randomly generates a rectangle with random coordinates.
✅ Asks the user to guess a point (x, y) inside the rectangle.
✅ Asks the user to guess the rectangle's area.
✅ Checks if the guessed point is inside the rectangle.
✅ Displays the actual rectangle and guessed point using Turtle Graphics.

A random rectangle is generated using two random points.
The user inputs a guessed (x, y) coordinate and an area estimate.
The program checks if the guessed point falls inside the rectangle.
The difference between the actual area and the guessed area is displayed.
The Turtle Graphics window visually represents the rectangle and guessed point.

Example

Rectangle Coordinates: 150, 300 and 350, 100  
Guess x: 200  
Guess y: 150  
Guess rectangle area: 40000  
Your point was inside the rectangle: True  
Your area was off by: 10000

🛠️ Installation & Usage

Clone the repository
git clone https://github.com/harshithanbhat77/geometry-game.git
cd geometry-game

Run the script

python Rectangle.py

📌 Requirements

Python 3+
Turtle Graphics (Pre-installed with Python)

The game will open a Turtle Graphics window where:
The rectangle is drawn based on random coordinates.
The guessed point is marked inside or outside the rectangle.

🏗️ Project Structure

/Geo_Game
│── Rectangle.py   # Main game script  
│── README.md      # Project documentation  

📜 Code Breakdown

The program consists of the following classes:

1️⃣ Point Class
Represents a point (x, y).

2️⃣ Rectangle Class
Defines a rectangle using two points.

3️⃣ GuiRectangle (Inherits Rectangle)
Draws the rectangle using Turtle Graphics.

4️⃣ GuiPoint (Inherits Point)
Marks the guessed point on the Turtle Canvas.

📌 Future Enhancements
Add more geometric shapes like circles and triangles.
Implement score tracking for multiple rounds.

📝 License
This project is open-source and free to use.
