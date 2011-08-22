#!/usr/bin/python
#inserts tabs and newlines in xml to make it readable
import re
import sys
def tab(t):
  return t*"\t"

def indent(s,f,t):
  while s is not "":
    m=re.match(r"(<([^<>]*)( [^<>]*)*>)(.*)(</\2>)(.*)",s)  
    if m is not None:
      f(tab(t)+m.group(1))
      indent(m.group(4),f,t+1)
      f(tab(t)+m.group(5))
      s=m.group(6)
    else:
      m=re.match(r"(<[^<>]*>)(.*)",s)
      if m is not None:
        f(tab(t)+m.group(1))
        s=m.group(2)
      else: 
        if s is not "":
          f(tab(t)+s) 
          s=""
      
if  __name__=="__main__":
  if sys.argv>1:
    f=open(sys.argv[1],'r')
    s=''.join(f.read().split('\n'))
    f=open("output",'w')
    fu=lambda x:f.write(x+"\n") 
  else:
    s="<Missing argument></Missing argument>"
    fu=lambda x:sys.stdout.write(x+"\n")
  indent(s,fu,0)
