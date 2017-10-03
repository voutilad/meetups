#!/bin/sh

for i in `find $1 -name '*.py' | grep -v test | grep -v Tools`
do
	cat $i | grep -i '__main__' | awk -v "i=$i" '{ print i }' | sort -u
done
