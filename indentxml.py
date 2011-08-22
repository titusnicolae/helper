#!/usr/bin/python
#inserts tabs and newlines in xml to make it readable
import re
import sys
def tab(t):
  return t*"\t"

def indent(s,f,t):
  while s is not "":  #there could be open close pairs on the same indentation level, all need to be processed ()()() 
    m=re.match(r"(<([^<>]*)( [^<>]*)*>)(.*)(</\2>)(.*)",s) #ex (<(tag)( attribute="a b")>) (everything here will be processed recursively)(</tag>)(the rest will be processed in the next iteration of the while loop)
    if m is not None:         #if matching was succesful
      f(tab(t)+m.group(1))    #print the current number of tabs, and the group (<(tag)( attribute="a b")>)
      indent(m.group(4),f,t+1)#recursively process the inner tags, with the indentation incremented
      f(tab(t)+m.group(5))    #print current number of tabs, and the closing (</tag>) group
      s=m.group(6)            #the string for the next while iteration is the last group
    else:                            #if previous match not successful
      m=re.match(r"(<[^<>]*>)(.*)",s)#try to match single element (<tag>)(other elements that will be processed on the next while iteration)
      if m is not None:       #if match was successful
        f(tab(t)+m.group(1))  #print current number of tabs, and (<tag>)
        s=m.group(2)          #remaining group will be processed in the next while iteration
      else:              #if no matching worked
        if s is not "":  #if there is something in s
          f(tab(t)+s)    #print it
          s=""           #while loop will exit after this
      
if  __name__=="__main__":
  if sys.argv>1:               #if there is a command line argument
    f=open(sys.argv[1],'r')         #open the file specified in the command line for reading
    s=''.join(f.read().split('\n')) #read everything from the file, split the content at newlines and put all the lines in a list, join the lines with ''
                                    #this actually removes all newlines from the string
    f=open("output",'w')            #open a file for output
    fu=lambda x:f.write(x+"\n")     #f here is a function that takes one parameter and writes to a file, appending newline to the end of the string x
  else:                        #if there is no command line argument
    s="<Missing argument></Missing argument>" #create a test string
    fu=lambda x:sys.stdout.write(x+"\n")      #create a function fu that writes to standard output
  indent(s,fu,0)   #send the string to the recursive function, the printing function, and the current indentation
