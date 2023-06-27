echo "Enter Series Length:"
read len
currSum=1
preSum=0
Sum=0
echo "Result----------------------------------------------------------"
echo $preSum
echo $currSum
while [ $len -gt 1 ]
do
Sum=`expr $preSum + $currSum`
preSum=$currSum
currSum=$Sum
echo $Sum
len=`expr $len - 1`
done



