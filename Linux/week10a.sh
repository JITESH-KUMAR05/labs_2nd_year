echo "Enter basic salary"
read bsal

if [ $bsal -lt 1500 ]
then 
    gsal=$(( bsal + (10 * bsal / 100) + (90 * bsal / 100) ))
    echo "Gross salary is $gsal"
fi

if [ $bsal -ge 1500 ]
then
    gsal=$(( (98 * bsal / 100) + bsal + 500 ))
    echo "Gross salary is $gsal"
fi