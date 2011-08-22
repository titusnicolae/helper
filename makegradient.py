#!/usr/bin/python
import Image,ImageDraw
import numpy as np
class Color():
  def __init__(self,r,g,b):
    self.r,self.g,self.b=r,g,b
  
def f(x,k):
  return float(-x**2+x*800-800)/k

def mix(c1,c2,k):
  return c1*k+c2*(1-k)
  
im=Image.new("RGB",(800,1),(255,0,0))
draw=ImageDraw.Draw(im)
base=np.array((0xE7,0xD5,0xEE))
white=np.array((255,255,255))
margin=mix(base,white,0.9)
for i in xrange(800):
  k=(float(i)-400)**2/160000
  color=tuple(map(int,mix(margin,base,k)))
  draw.point((i,0),fill=color) 
im.save("gradient.png","PNG") 
  
