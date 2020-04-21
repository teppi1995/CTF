for var in `seq 1 20000`
do
    if  grep "How do you find" lib_${var}.so  >/dev/null; then
	echo no
    else
	echo find!${var}
    fi

done
