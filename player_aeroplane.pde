class Aeroplane { //designing the class Aeroplane
  
  PImage image1; //Defining relevant data members
  int x,y;
  Aeroplane(int x, int y)//Defining constructor aeroplane
  {
    this.x = x;
    this.y = y;
  }
  
  void display(){ //creating the method display to show the player on the screen
    
    image1 = loadImage("UAV.gif");
    image1.resize(x,y);
    imageMode(CENTER);
    image(image1,width/2,height/2);
  }
  
  boolean collidesWith(Birds other) //creating the method collidesWith to collide the birds with the aeroplane
  {
   return dist(this.x, this.y, other.x, other.y)>(250);
  }
  boolean collidesWith(HotAirBalloon other2) //creating the method collidesWith to collide the hot air balloons with the aeroplane
  {
   return dist(this.x, this.y, other2.x, other2.y)>(250);
  }
}
