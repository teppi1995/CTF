for var in `seq 1 20000`
do
    if  readelf -r lib_${var}.so | grep "GLIBC_2.2.5"  >/dev/null; then
	:
    else
	echo find!${var}
    fi

done
