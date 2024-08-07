#!/usr/bin/bash

files_dir="./files/"
py_script="./merge.py"

file_array=()

for file in "$files_dir"*
do 
	if [ -f "$file" ] && [[ "$file" == *.pdf || "$file" == *.PDF ]]; then
		file_array+=("$file")	
	fi
done

python "$py_script" "${file_array[@]}"