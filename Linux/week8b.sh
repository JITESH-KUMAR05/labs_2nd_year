# shell script that accepts one or more file name as argument and converts all of them to uppercase, provided they exist in the current directory
if [ $# -eq 0 ]
then
    echo "No arguments provided"
    exit 1
fi
for file in $@; do
    if [ -f $file ]
    then
        mv $file `echo $file | tr '[a-z]' '[A-Z]'`
    else
        echo "$file does not exist"
    fi
done