'''Implement a class called playe'r that represents a cricket player.The player class should have a
method called play() which prints "The player is playing cricket.Derive two classes,Batsman and
Bowler,from the player class.override the play() method in each derived class to print "The batsman
is batting" and "The bowler is bowling ", respectively.write a program to create objects of both the
Batsman and Bowler classes and call the play() method for each object.'''


#Define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")

#Define the derived class Batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")

#Define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

#create objects of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

#Call the play() method for each object
batsman.play()
bowler.play()

    