# write a shell script that accepts a filename, starting and ending line numbers as arguments and displays all the lines between the given line numbers.

if [ $# -ne 3 ]
then
    echo "Usage: $0 filename start_line end_line"
    exit 1
fi

file=$1
snum=$2
enum=$3
sed -n "${snum},${enum}p" "$file"