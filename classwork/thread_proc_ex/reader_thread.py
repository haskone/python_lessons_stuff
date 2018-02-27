"""
Read some part of some file.
"""
import argparse
import os
from threading import Thread

LINE_LEN = 3

parser = argparse.ArgumentParser(description="Process some args.")
parser.add_argument("threads", type=int)
parser.add_argument("filename", type=str)

args = parser.parse_args()

filename = args.filename
file_size = os.path.getsize(filename)

threads = args.threads


def run_it(start, end, filename, number):
    shift = start * LINE_LEN
    lines = end - start
    amount = (end - start) * LINE_LEN
    with open(filename, "r") as f:
        f.seek(shift)
        # for _ in range(lines): 
        # print(f"thread {number}: {f.readline()}")
        # pass
        # print(f"thread {number}: {f.read(amount)}")

block_size = file_size // threads
for number in range(threads):
    start_read = number * block_size
    print(f"thread num {number}, {start_read}, {start_read + block_size}")
    t = Thread(target=run_it,
               args=(start_read,
                     start_read + block_size,
                     filename,
                     number))
    t.start()
