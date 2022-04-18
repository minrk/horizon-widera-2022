#!/usr/bin/env bash
if [ `wc -c abstract.txt | awk '{print $1}'` -lt 2000 ];
then echo "Abstract length is okay"; 
else echo "Abstract too long"; exit 1; fi
