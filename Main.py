from argparse import ArgumentParser
import subprocess
from subprocess import Popen, PIPE
from os import listdir
from os.path import isfile, join
import time


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-prog', dest="prog", required=True)
    parser.add_argument('-test', dest="test", required=True)
    parser.add_argument('-time', dest="time", type=int, required=False)
    args = parser.parse_args()
    print('vars args', vars(args))

    inFiles = [join(args.test, f) for f in listdir(args.test) if isfile(join(args.test, f)) & f.endswith(".in")]
    ansFiles = [join(args.test, f) for f in listdir(args.test) if isfile(join(args.test, f)) & f.endswith(".ans")]

    #print(infiles)
    #print(ansfiles)

    out = []
    outReal = []
    outTime = []

    for a in ansFiles:
        f = open(a)
        outReal.append(f.read())

    for i in inFiles:
        f = open(i)
        out.append(Popen("python " + args.prog, stdout=PIPE, stdin=f).stdout.read().decode())
    
    out = [s.replace("\r", "") for s in out]

    for i in range(len(out)):
        a = out[i]
        b = outReal[i]
        print("Testing input " + inFiles[i])
        if a == b:
            print("\tTest succeeded")
        else:
            print("\tTest failed")
            print("\tExpected: " + b)
            print("\tReceived: " + a)



    print(out)
    print(outReal)