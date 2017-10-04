#!/bin/sh

LIST=$(find ${1} -name '*.py' | grep -v -e test -e Tools)
for i in ${LIST}
do
	cat ${i} | grep -i '__main__' |
		awk -v "i=${i}" '{ print i }' | sort -u
done
