#I tried the stupid way first, where you replace the powerful letters with correspending letter in order,
#for example 'K with B, Q with C, etc.. so after the finding the type of your hand, you can just sort it
# but i found this solution in the reddit, it's just smarter x)



def eval(line):
    hand, bid = line.split()
    hand = hand.translate(str.maketrans('TJQKA', face))
    best = max(type(hand.replace('0', r)) for r in hand)
    return best, hand, int(bid)

def type(hand):
    return sorted(map(hand.count, hand), reverse=True)

for face in 'ABCDE', 'A0CDE':
    print(sum(rank * bid for rank, (*_, bid) in
        enumerate(sorted(map(eval, open('2023\Day 07\day_07.txt'))), start=1)))