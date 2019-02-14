#!/bin/sh

DIR=".git"

if [ -d "$DIR" ]; then
	if [ $# -eq 0 ]; then
		echo "No commit comment supplied. Exit"
		exit 0
	fi
	make fclean
	git add .
	git commit -m "$1"
	git push
else
	echo "Go to the root of the project."
fi
exit 0
