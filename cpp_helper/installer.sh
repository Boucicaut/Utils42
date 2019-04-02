#!/bin/bash

mkdir ~/.script_cpp
cp cpp_helper.py ~/.script_cpp/.

echo -n "Which terminal are you using on this device?"
DEFAULT="bash"
echo -n " [zsh|bash]
[$DEFAULT] >>>"
read -r term
if [[ $term == "zsh" ]]; then
    rc="zshrc"
else
    rc="bashrc"
fi

echo "alias cpp-init=\"python3 ~/script_cpp/cpp_helper.py\"" >> ~/.$rc

echo "Restart your terminal please: source ~/.$rc"
echo "Then to execute the helper use \"cpp-init [class1] [class2]\""
echo "@blefeuvr & @ cmaxime"
