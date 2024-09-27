# shell script that takes a command line argument and report on whether it is a directory, a file, or something else
echo "Enter filename or directory name: "
read name
if [ -d $name ]
then
    echo "It is a directory"
elif [ -f $name ]
then
    echo "It is a file"
else
    echo "It is something else"
fi