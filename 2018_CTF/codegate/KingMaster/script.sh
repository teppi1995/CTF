for var in `seq 10000 99999`
do
    echo $var
    echo 1 $var | nc 110.10.147.104 13152
done
