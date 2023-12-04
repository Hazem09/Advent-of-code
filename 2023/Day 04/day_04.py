
with open('Day 04\day_04.txt') as f:
    data = [line.strip('\n') for line in f.readlines()]
    
def part_1(data):
    total = 0
    for line in data:
        line = line.split(':')[1].strip(' ').split('|')
        winning_cards = set(line[0].split())
        cards = line[1].split()
        
        total_1 = sum(1 if card in winning_cards else 0 for card in cards if card)
        total += total_1 if total_1 == 0 else 2 ** (total_1 - 1)
    return print(total)
       
part_1(data)

def part_2(data):
    total_cards = [0]*len(data)
    for i,line in enumerate(data):
        total_cards[i] += 1
        cont = total_cards[i]
        
        card_num = int(line.split(':')[0].strip('Card '))
        line = line.split(':')[1].strip(' ').split('|')
        winning_cards = set(line[0].split())
        cards = line[1].split()
        num_of_winning_cards = sum(1 if card in winning_cards else 0 for card in cards if card)
        while cont > 0:
            for j in range(num_of_winning_cards):
                total_cards[card_num+j] += 1
            cont -= 1
    return print(sum(total_cards))

part_2(data)