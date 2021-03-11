#!/bin/bash
mkdir temp
##################已经可以实现两个目录的比较
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
			if ! diff $1/$i $2/$i &> /dev/null ; then
				echo changeFile:$1/$i'>'$2/$i'$'
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




fileCount=0
if [[ -e $1 ]]; then
	unzip $1 -d temp &> /dev/null
	fileCount=1
fi
allDirForChangeName=($(ls -tr temp))
mv temp/{,0}${allDirForChangeName[0]}
if [[ -e $2 ]]; then
	unzip $2 -d temp &> /dev/null
	fileCount=2
fi
allDir=($(ls -tr temp))
if [ $fileCount -eq 1 ]; then
	dir1=temp/${allDir[0]}
	mkdir temp/2none
	dir2=temp/2none
	diffTwoDirAdd $dir2 $dir1
fi
if [ $fileCount -eq 2 ]; then
	dir1=temp/${allDir[0]}
	dir2=temp/${allDir[1]}
	diffTwoDirAdd $dir1 $dir2
	diffTwoDirDel $dir1 $dir2
fi

##################clear
rm -frv temp &> /dev/null