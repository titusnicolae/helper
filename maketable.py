#!/usr/bin/python
#creates html table from space separated values
import sys
def createHTMLtableFromFile():
  if len(sys.argv)==1:
    print "missing input and output files"
    return 
  elif len(sys.argv)==2:
    print "missing output file"
    
  fin = open(sys.argv[1])
  out=['<table>\n']
  for line in fin:
    tr=["  <tr>\n"]
    for el in line.split():
      tr.append("    <td> %s </td>\n" % (el))
    tr.append("  </tr>\n")
    out+=tr
  out.append("</table>")
  fout=open(sys.argv[2],"w")
  fout.write(''.join(out))
 
if __name__ == "__main__":
  createHTMLtableFromFile()
