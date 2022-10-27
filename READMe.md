The player will be responsible to help the snake find food, grow and most importantly avoid colliding with barriers such as its own self.

In order to get started, we will first import define random, turtle, and time, packages. Now, create class Square and declare the x and y variables. After this generate a self function to draw a black box coordinate. Use the for loop in range to add them, y coordinates. By using for loop initially range is 4.

 Now, we will create the Foodl class using the same x,y coordinates and keep the state as ON. Create the Food class and define changelocation(self), drawself(), changestate() function. The changelocation(self) function will allocate the food a random value of x,y coordinate. The food keeps itself away from the snake’s body by blinking on and off. We will control this using the drawself () and changestate () functions.

  Create the Snake class which has the init() function that contains the variable next which tells the snake which way to go next. Further functions defined determine collision detection, moving the snake head to the next spot and even resets the head and next position.

  Now that we have already created the Food and the Snake, we will now create the game play and define the snake’s movements. We start by creating the Game class which will include the functions moveup(), movedown(), moveleft(), moveright() to change a location and snake position on a screen. These functions will help our snake move in the directions the user selects on the screen.

  his set of codes will allow the snake to extend itself by 1 after eating the food. By defining the movedown (), eatFood () and drawself () functions, you’ll be able to add to the tail and extend the snake by 1, as well as draw the whole snake when it is called.

  This section includes the conditions that allow the snake to move positions when the command is called. We will also include a print function in each for debugging purposes. This will display the snake on the screen.