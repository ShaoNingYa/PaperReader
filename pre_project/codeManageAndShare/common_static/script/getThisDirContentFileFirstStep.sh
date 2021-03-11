#!/bin/bash
# # allDir=($(ls $1))
# dirString=",,"
# fileString=",,"
# if [[ ! -d temp ]]; then
# 	mkdir temp
# 	unzip $1 -d temp &> /dev/null
# fi

# # echo lsDir:"   "$(ls temp)

# for file in $(ls temp/$(ls temp)); do
# 	if [[ -d temp/$(ls temp)/$file ]]; then
# 		dirString=${dirString},$file
# 	else
# 		fileString=${fileString},$file
# 	fi
# done
# # echo $(ls $0)
# # echo $dirString
# # echo $fileString
# # echo $(ls temp)%%%$dirString%%%$fileString | awk -F',,,' '{print $1$2$3}'
# # echo $dirString%%%$fileString | tr -d ',,,' 
# # rm -fr temp
# # echo $1
# # echo $(ls temp)%%%$dirString%%%$fileString | awk -F',,,' '{print $1$2$3}'

dirString=",,"
fileString=",,"
if [[ ! -d $2/temp ]]; then
	mkdir $2/temp
	unzip $1 -d $2/temp &> /dev/null
fi

# echo lsDir:"   "$(ls temp)

for file in $(ls $2/temp/$(ls $2/temp)); do
	if [[ -d $2/temp/$(ls $2/temp)/$file ]]; then
		dirString=${dirString},$file
	else
		fileString=${fileString},$file
	fi
done
echo $(ls $2/temp)%%%$dirString%%%$fileString | awk -F',,,' '{print $1$2$3}'
# echo dasd%%%$2,aa%%%aaa,ww
