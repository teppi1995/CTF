#!/usr/bin/python
# -*- Coding: utf-8 -*-


def main():
    array_a = [70,152,195,284,475,612,791,896,810,850,737,1332,1469,1120,1470,832,1785,2196,1520,1480,1449]

    answer = ""
    for i, c in enumerate(array_a):
        answer += chr(c // (i + 1))

    print(answer)
    
if __name__ == "__main__":
    main()
    
