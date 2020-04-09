#!/bin/bash

Max=5
i=1

while [ $i -le $Max ]
do 
number=$RANDOM
echo $number
let "i=i+1"
done

