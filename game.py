##Name: Normandie Essig
##Description: create a Game class

class Game():
     def __init__(self):
          self.score = 0
          self.rolls = []
          self.current_roll = 0
          
     def roll(self,pins):
          self.current_roll +=1
          self.rolls.append(pins)
     
     def score(self):
          score = 0
          frameIndex = 0
          
          for frame in range(10):
               
               if self.isStrike(frameIndex):
                    self.score = self.score + 10 + self.strikeBonus(frameIndex)
                    frameIndex += 1 

               elif self.isSpare(frameIndex): ##spare
                    self.score = self.score + 10 + self.spareBonus(frameIndex)
                    frameIndex += 2

               else:
                   self.score += self.sumOfBallsInFrame(frameIndex)
                   frameIndex +=2
                   
          return self.score

     def isSpare(self, frameIndex):
          return (self.rolls[frameIndex] + self.rolls[frameIndex+1] == 10)

     def isStrike(self,frameIndex):
          return (self.rolls[frameIndex]  == 10)

     def strikeBonus(self, frameIndex):
          return self.rolls[frameIndex+1] + self.rolls[frameIndex+2]

     def spareBonus(self, frameIndex):
          return self.rolls[frameIndex+2]

     def sumOfBallsInFrame(self, frameIndex):
          return self.rolls[frameIndex] + self.rolls[frameIndex+1]
          
