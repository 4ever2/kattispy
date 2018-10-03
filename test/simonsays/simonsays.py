# Exercise for https://open.kattis.com/problems/simonsays

n = int(input())


final_string = ""
i = 0

while(i<n):
    line = input()
    if line[0:10] == "Simon says":
        print(line[10:len(line)])
    i = i+1