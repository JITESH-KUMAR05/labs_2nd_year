# interactive grep script that ask for a word and a filename and tells how many lines the word appears in the file
echo "Enter the pattern you are looking for: "
read pattern
echo "Enter the filename you are searching: "
read filename
echo "Searching for $pattern in $filename"
echo "Selected Records are :"
grep -n $pattern $filename
echo "Number of lines the word appears in the file: "
grep -c $pattern $filename
