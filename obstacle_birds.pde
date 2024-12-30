class Birds //defining the class Birds

{
  //defining the data members
  PImage bird1; 
  int x,y, width, height, speedX, speedY; 
  
  //defining the constructor
  Birds(int x, int y)
  {
    this.x = x;
    this.y = y;
    this.height = 50;
    this.width = 50;
    this.speedX = int(random(-3,3));
    this.speedY = int(random(-3,3));
  }
  
  void display() //defining the method display to manifest the obstacle bird
  {
    bird1 = loadImage("birdie.gif");
    bird1.resize(width,height);
    image(bird1,x,y);
  }
  
  void move() //defining the method move for animating the obstacles in the game
  {
    x += speedX;
    y += speedY;
    
    if (keyCode ==  DOWN)
    {
      y = y-5;
    }
    if (keyCode == UP)
    {
      y = y+5;
    }
    if(keyCode == RIGHT)
    {
      x = x-5;
    }
    if(keyCode == LEFT)
    {
      x = x+5;
    }
  }
}
