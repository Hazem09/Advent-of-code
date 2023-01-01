from itertools import zip_longest
from functools import cmp_to_key

lines =[]

with open ("input_day13.txt") as f:
    for line in f:
        if line != "\n":
            lines.append(eval(line.strip("\n")))

def compare_int(left,right):
    if left < right:
        return "right_order"
    elif left == right:
        return "ok"
    else: 
        return "wrong_order"


def compare_nones(left,right):
    if left == None and right == None:
        return "ok"
    elif left == None:
        return "right_order"
    elif right == None:
        return "wrong_order"



def compare_lists(left,right):
    for l,r in zip_longest(left,right):
        if isinstance(l,int) and isinstance(r,int):
            yield compare_int(l,r)
        elif isinstance(l, list) and isinstance(r, list):
            yield from compare_lists(l,r)
        elif isinstance(l, int) and isinstance(r ,list):
            yield from compare_lists([l],r)
        elif isinstance(l, list) and isinstance(r, int):
            yield from compare_lists(l,[r])
        else:
            yield compare_nones(l,r)

right_pairs=0

for i, (left, right) in enumerate(zip(lines[:-1:2],lines[1::2]), start=1):
    for result in compare_lists(left,right):
        if result=="right_order":
            right_pairs += i
            break
        elif result == "wrong_order":
            break
        else:
            continue






print(right_pairs,)

