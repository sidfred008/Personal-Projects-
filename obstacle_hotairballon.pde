class HotAirBalloon extends Birds{ //designing the class HotAirBalloon and adding the concept of inheritance
  
  PImage balloon; 
  HotAirBalloon(int x, int y)
  {
    super(x,y);
 
  }
  
  @Override
  void display()//defining the method display to manifest the obstacle hot air balloon
  {
    balloon = loadImage("HotAirBalloon.png");
    balloon.resize(width,height);
    image(balloon,x,y);
  }
  
  @Override
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
