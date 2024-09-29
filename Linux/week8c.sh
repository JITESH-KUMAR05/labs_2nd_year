# shell script that determines that period for which a specified user has been logged in
username=$1
current_login=`who | grep $username | wc -l`
if [ -z $username ]
then
    echo "No username provided"
    exit 1
else
    echo "user $username is currently logged in"
    echo "$current_login"
fi
echo "Last login session for $username"
last $username | head -n 1
