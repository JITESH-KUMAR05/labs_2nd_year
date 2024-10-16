write a shell script to find the length of a string and extract sub string from a string
echo "Enter any string "
read str
n=${#str}
echo "Length of the string is $n"
echo "Enter the staring postion of the string "
read m
echo "Enter the ending postion of the string "
read o
echo $str | cut -c $m-$o