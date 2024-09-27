# pipe your /etc/passwd file to this script to get the home directories
{
    if (match($0, /:\/home\//) > 0) {
        split($0, fields, ":")
        print fields[6]
    }
}