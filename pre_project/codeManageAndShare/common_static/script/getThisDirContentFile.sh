#!/bin/bash
dirString="^^"
fileString="^^"
for file in $(ls $1); do
	if [[ -d $1/$file ]]; then
		dirString=${dirString},$file
	else
		fileString=${fileString},$file
	fi
done
# echo dirString:$dirString
# echo fileString:$fileString
echo $dirString###$fileString