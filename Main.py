from argparse import ArgumentParser
import subprocess
from subprocess import Popen, PIPE


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-prog', dest="prog", required=True)
    args = parser.parse_args()
    print('vars args', vars(args))

    f = open("test.in")

    print(Popen("python " + args.prog, stdout=PIPE, stdin=f).stdout.read())
    f.seek(0)
    print(f.read())