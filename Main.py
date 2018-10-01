from argparse import ArgumentParser
import subprocess
from subprocess import Popen, PIPE
from os import listdir
from os.path import isfile, join
import time
import psutil


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-prog', dest="prog", required=True)
    parser.add_argument('-test', dest="test", required=True)
    parser.add_argument('-time', dest="time", type=int, default=-1, required=False)
    parser.add_argument('-mem', dest="mem", type=int, default=-1, required=False)
    args = parser.parse_args()
    print('vars args', vars(args))

    inFiles = [join(args.test, f) for f in listdir(args.test) if isfile(join(args.test, f)) & f.endswith(".in")]
    ansFiles = [join(args.test, f) for f in listdir(args.test) if isfile(join(args.test, f)) & f.endswith(".ans")]

    #print(infiles)
    #print(ansfiles)

    out = []
    outReal = []
    outTime = []
    outMem = []

    for a in ansFiles:
        f = open(a)
        outReal.append(f.read())

    for i in inFiles:
        f = open(i)
        start = time.time()
        p = psutil.Popen("python " + args.prog, stdout=PIPE, stdin=f)
        t = p.memory_info()
        out.append(p.stdout.read().decode())
        end = time.time()

        outMem.append(t[3])
        outTime.append(end-start)
    
    out = [s.replace("\r", "") for s in out]

    for i in range(len(out)):
        a = out[i]
        b = outReal[i]
        t = outTime[i]
        m = outMem[i]
        print("Testing input " + inFiles[i])
        if a == b:
            if args.time >= 0:
                if t > args.time:
                    print("\tTest took too long")
                    print("\tTime: " + str(t))
                    continue
            
            if args.mem >= 0:
                if m > args.mem:
                    print("\tTest used too much memory")
                    print("\tMemory: " + str(m))
                    continue

            print("\tTest succeeded")
        else:
            print("\tTest failed")
            print("\tExpected: " + b)
            print("\tReceived: " + a)



    print(out)
    print(outReal)
    print(outTime)
    print(outMem)