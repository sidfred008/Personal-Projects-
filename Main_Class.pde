Aeroplane aeroplane; //creating the object aeroplane to access the class Aeroplane
Birds birds;//creating the object birds to access the class Bird
Background sky;//creating the object sky to access the class background
HotAirBalloon hotairballoon;//creating the object hotairballoon to access the class hotairballoon

ArrayList<Birds> bird;//defining an array list to store the obstacles which are birds
ArrayList<HotAirBalloon> balloon; //defining an array list to store the obstacles which are hot air balloon
int lives = 1; //defining the variable lives for decreasing down to zero once the obstacle collides with the aeroplane
boolean gameOver = false; //setting gameOver variable to false until the obstacle collides with the aeroplane

void setup() //adding the setup method to set up things for the game and obstacles to be displayed on the screen
{
  size(500,500);//setting up the size of the canvas
  aeroplane = new Aeroplane(50,50);//creating the object in the memory and passing value as a parameters
  birds = new Birds((int)random(3,5), (int)random(3,5)); //adding birds at random positions within the range provided
  hotairballoon = new HotAirBalloon((int)random(3,5),(int)random(3,5)); //adding hot air balloon at random positions within the range provided
  bird = new ArrayList<Birds>(); //creating an ArrayList for birds
  balloon = new ArrayList<HotAirBalloon>(); //creating an ArrayList for hot air balloon
  sky = new Background(500,500); //adding the background 
  
  for (int i = 0; i<5; i++) //adding the birds inside the array list
  {
    bird.add(new Birds(int(random(width)), int (random(height)))); //adding birds inside the array list
    
  }
  for (int i = 0; i<5; i++) //adding hot air balloons inside the array list
  {
    balloon.add(new HotAirBalloon((int)random(width), (int)random(height))); //adding hot air balloon inside the array list
  }
}

void draw() //creating the methods draw the animate the game
{
  sky.display();//displaying the sky
  if (!gameOver) //setting a conditional looping statement for gameOver variable
  {
    for(int i = 0; i<5; i++) //creating a loop to access the obstacles inside the array list
    {
      Birds birds = bird.get(i); //getting the birds from the array list using the loop variable
      birds.display(); //displaying the birds
      birds.move(); //making the birds move
    }
    for(int i = 0; i<5; i++) //creating a loop to access the hot air balloons inside the array list
    {
      HotAirBalloon hotairballoon = balloon.get(i); //getting the hot air balloons from the array list using the loop variable
      hotairballoon.display(); //displaying the hot air balloon
      hotairballoon.move(); //moving the hot air balloon
    }
  }
  aeroplane.display();//accessing the display method inside the class Aeroplane 
  
  birds.move(); //accessing the move method inside the class Birds
  fill(255,255,0); //filling the lives 
  textSize(16);
  text("Lives: " + lives, 10,20);
  
  if (aeroplane.collidesWith(birds) && aeroplane.collidesWith(hotairballoon)) //setting a conditional looping once the birds collide with the aeroplane
  {
    lives = lives-1; 
    if(lives <= 0){
      //this will make the Game Over! text appear on the screen 
      gameOver = true;
      background(0);
      fill(255,0,0);
      textSize(32);
      textAlign(CENTER);
      text("Game Over!", width/2, height/2);
    }
  }
}

void keyPressed() //setting the keyPressed method to animate the game using the arrows on the keyboard
{
  birds.move();
  hotairballoon.move();
} 
