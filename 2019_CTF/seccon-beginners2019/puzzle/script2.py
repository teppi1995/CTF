# -*- coding: utf-8 -*-
#!/usr/bin/env python

from socket import *
from telnetlib import Telnet
from time import time, sleep
from sys import argv
from struct import pack, unpack
import pprint


pp = pprint.PrettyPrinter(indent=3)


def puzz_astar(start,end):
    """
    A* algorithm
    """
    front = [[heuristic_2(start), start]] #optional: heuristic_1
    expanded = []
    expanded_nodes=0
    while front:
        i = 0
        for j in range(1, len(front)):
            if front[i][0] > front[j][0]:
                i = j
        path = front[i]
        front = front[:i] + front[i+1:]
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in expanded: continue
        for k in moves(endnode):
            if k in expanded: continue
            newpath = [path[0] + heuristic_2(k) - heuristic_2(endnode)] + path[1:] + [k] 
            front.append(newpath)
            expanded.append(endnode)
        expanded_nodes += 1 
    print "Expanded nodes:", expanded_nodes
    print "Solution:"
    pp.pprint(path)
    return path

def moves(mat): 
    """
    Returns a list of all possible moves
    """
    output = []  

    m = eval(mat)   
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0); #blank space (zero)

    if i > 0:                                   
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
      output.append(str(m))
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
      
    if i < 2:                                   
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
      output.append(str(m))
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

    if j > 0:                                                      
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
      output.append(str(m))
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < 2:                                   
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
      output.append(str(m))
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]

    return output

def heuristic_1(puzz):
    """
    Counts the number of misplaced tiles
    """ 
    misplaced = 0
    compare = 0
    m = eval(puzz)
    for i in range(3):
        for j in range(3):
            if m[i][j] != compare:
                misplaced += 1
            compare += 1
    return misplaced

def heuristic_2(puzz):
    """
    Manhattan distance
    """  
    distance = 0
    m = eval(puzz)          
    for i in range(3):
        for j in range(3):
            if m[i][j] == 0: continue
            distance += abs(i - (m[i][j]/3)) + abs(j -  (m[i][j]%3));
    return distance



def read_until(s, c):
    ret = ""
    while 1:
        ret += s.recv(1)
        if ret.endswith(c):
            return ret        
        
HOST = "133.242.50.201"
PORT = 24912

def search_puzzle(s):
    _ = read_until(s, "----------------")
    _ = read_until(s, "| ")
    
    p = []
    for i in range(0,3):
        l_str = read_until(s, "\n").strip("  ").strip("|\n").split("|")
        l_int = [int(n) for n in l_str]
        print(l_int)
        
        p.append(l_int)
        
    print(p)
    puzzle = str(p)
    end = str([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    path = puzz_astar(puzzle,end)
        
    answer = ""
    coord0 = [-1, -1]
    for i in path:
        if (i != 0):
            i =  i.strip("[").strip("]").split("], [")
            y = 0
            for j in i:
                k = [int(n) for n in j.split(",")]
                if 0 in k:
                    x = k.index(0)
                    break
                y = y + 1

            if (coord0[0] == -1):
                coord0[0] = x 
                coord0[1] = y
            else:
                if (coord0[0] - x) == 1:
                    answer += "3,"
                    coord0[0] = x
                elif (coord0[0] - x) == -1:
                    answer += "1,"
                    coord0[0] = x
                    
                if (coord0[1] - y) == 1:
                    answer += "0,"
                    coord0[1] = y
                elif (coord0[1] - y) == -1:
                    answer += "2,"
                    coord0[1] = y
                    
            print(coord0)
            
    answer = answer[:-1]
    print(answer)
    
    s.sendall(answer + "\n")
    sleep(1)
    print(read_until(s, "\n"))

    
def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    for i in range(0, 100):
        search_puzzle(s)

    print(s.recv(100))
                
if __name__ == "__main__":
    main()
    
        

