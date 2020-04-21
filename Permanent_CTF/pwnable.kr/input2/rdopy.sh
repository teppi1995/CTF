#!/bin/bash

echo -e "cat << 'EOT' | python <(cat -) ${@:2}\n$(cat ${1}|sed -e 's/\\/\\\\/g')\nEOT
