"""
Read some part of some file.
"""
import argparse

LINE_LEN = 4

parser = argparse.ArgumentParser(description="Process some args.")
parser.add_argument("start", type=int)
parser.add_argument("end", type=int)
parser.add_argument("filename", type=str)

args = parser.parse_args()

shift = args.start * LINE_LEN
amount = (args.end - args.start) * LINE_LEN
filename = args.filename


with open(filename, "r") as f:
    f.seek(shift)
    print(f"thread {number}: {f.read(amount)}")
