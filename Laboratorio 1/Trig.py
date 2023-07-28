import math
import datetime

class Trig:
  def __init__(self):
    self.val=math.pi

  def seno(self):
    return math.sin(self.val)
    
     
  def coseno(self):
    return math.cos(self.val)
    
  
  def tangente(self):
    return math.tan(self.val)

  def dat(self):
    fecha=datetime.datetime.now()
    return fecha
    