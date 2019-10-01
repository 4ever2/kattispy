x = [int(a) for a in input().split(" ")]
y = input()

x.sort()

out = ""

for c in y:
    if c == "A":
        if out == "":
            out += str(x[0])
        else:
            out += " " + str(x[0])
    elif c == "B":
        if out == "":
            out += str(x[1])
        else:
            out += " " + str(x[1])
    elif c == "C":
        if out == "":
            out += str(x[2])
        else:
            out += " " + str(x[2])

print(out)
