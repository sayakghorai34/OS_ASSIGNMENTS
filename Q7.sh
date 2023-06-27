echo "Enter 3 numbers with space in between"
read a b c
l=$a
if [ $b -gt $l ]
then
    l=$b
fi
if [ $c -gt $l ]
then
    l=$c
fi
echo "Largest of $a,$b,$c is : $l"
