class Background { //designing the class Background to have sky as the background in the game 

  //assigning the relevant data members for background image
  PImage sky1; 
  int x,y;
  
  //designing the constructor
  Background(int x, int y)
  {
    this.x = x;
    this.y = y;
  }
  
  //creating a display method to have the background
  void display()
  {
    sky1 = loadImage("skyimage.jpg");
    image(sky1,x,y);
  }
}
