echo 'Enter array limit'
read limit
echo 'Enter elements'
n=1
while [ $n -le $limit ]
do
    read num
    eval arr$n=$num
    n=`expr $n + 1`
done
echo 'Enter key element'
read key
low=0
high=$n
found=0
while [ $found -eq 0 -a $high -gt $low ]
do
    temp=`expr $low + $high`
    
    if [ `expr $temp / 2` -eq 0 ]
    then
        temp=`expr $temp + 1`
        mid=`expr $temp / 2`
    else
        temp=`expr $temp - 1`
        mid=`expr $temp / 2`
        

    fi

    eval t=$arr$mid
    if [ $key -eq $t ]
    then
        found=1
    elif [ $key -lt $t ]
    then
        high=`expr $mid - 1`

    else
        low=`expr $mid + 1`
    fi
done
if [ $found -eq 0 ]
then
    echo 'Unsuccessful search'
else
    echo 'Successful search'
fi
