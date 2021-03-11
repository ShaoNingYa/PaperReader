#!/bin/bash
diffTwoDirAdd(){
	for i in $(ls $2) 
	do
		 # echo $dir1/$i
		if [[ ! -a $1/$i ]]; then
			# echo $1/$i 不是目录
			if [[ -d $2/$i ]]; then
				echo addDir:$2/$i'$'
			else
				echo addFile:$2/$i'$'
			fi
		else
			if [[ ! -d $2/$i ]]; then
				if ! diff $1/$i $2/$i &> /dev/null ; then
					echo changeFile:$1/$i'>'$2/$i'$'
				fi
			fi
		fi
		if [[ -d $2/$i ]]; then
			diffTwoDirAdd $1/$i $2/$i
		fi
	done
}


diffTwoDirDel(){
	for i in $(ls $1) 
	do
		if [[ ! -a $2/$i ]]; then
			# echo $1/$i 不是目录
			if [[ -d $1/$i ]]; then
				echo delDir:$1/$i'$'
			else
				echo delFile:$1/$i'$'
			fi
		fi
		if [[ -d $1/$i ]]; then
			diffTwoDirDel $1/$i $2/$i
		fi
	done
}
# diffTwoDirAdd $getDirPath_1 $getDirPath_2
# diffTwoDirDel $getDirPath_1 $getDirPath_2


# getDirPath_1=$(dirname $1)/temp
# getDirPath_2=$(dirname $2)/temp
# # echo $getDirPath_1
# # echo $getDirPath_2
# # common_static/codeSavePosition/test1/test01/temp
# # common_static/codeSavePosition/test2/test02/temp
# if [[ ! -d ${getDirPath_1} ]]; then
# 	# echo ${getDirPath_1} no exists
# 	mkdir ${getDirPath_1}
# 	unzip $1 -d ${getDirPath_1} &> /dev/null
# fi
# if [[ ! -d ${getDirPath_2} ]]; then
# 	# echo ${getDirPath_2} no exists
# 	mkdir ${getDirPath_2}
# 	unzip $2 -d ${getDirPath_2} &> /dev/null
# fi

fileCount=0
getDirPath_1=temp
getDirPath_2=temp
if [[ -e $1 ]]; then
	getDirPath_1=$(dirname $1)/temp
	if [[ ! -d ${getDirPath_1} ]]; then
		# echo ${getDirPath_1} no exists
		mkdir ${getDirPath_1}
		unzip $1 -d ${getDirPath_1} &> /dev/null
	fi
	fileCount=1
fi
if [[ -e $2 ]]; then
	getDirPath_2=$(dirname $2)/temp
	if [[ ! -d ${getDirPath_2} ]]; then
		# echo ${getDirPath_1} no exists
		mkdir ${getDirPath_2}
		unzip $2 -d ${getDirPath_2} &> /dev/null
	fi
	fileCount=2
fi
if [ $fileCount -eq 1 ]; then
	mkdir temp
	diffTwoDirAdd $getDirPath_2 $getDirPath_1
fi
if [ $fileCount -eq 2 ]; then
	diffTwoDirAdd $getDirPath_1 $getDirPath_2
	diffTwoDirDel $getDirPath_1 $getDirPath_2
fi

##################clear
rm -frv temp &> /dev/null