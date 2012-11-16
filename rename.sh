#!/bin/bash
#take all the files in alphabetical order and rename them as 1.png, 2.png, ...
if [ $# -eq 1 ]
then 
  cnt=$1
else
  cnt=1
fi
for fname in `ls | sort -V`
do
  if [ "$fname" != "rename.sh" ]
  then
    mv $fname $cnt.png
    cnt=$(( $cnt + 1 ))
  fi
done
