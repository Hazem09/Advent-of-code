with open ("2022\input_day4.txt") as f:
    lines = f.readlines()

inter,inter_2 = 0,0
for line in lines:
    pair = line.split(",")
    pair_1,pair_2 = pair[0].split("-"), pair[1].split("-")

    pair_1_sections = [sec for sec in range(int(pair_1[0]),int(pair_1[1])+1)]
    pair_2_sections = [sec for sec in range(int(pair_2[0]),int(pair_2[1])+1)]
    pair_1_sections = set(pair_1_sections)
    pair_2_sections = set(pair_2_sections)
    if pair_1_sections.issubset(pair_2_sections) or pair_2_sections.issubset(pair_1_sections):
        inter +=1
    if len(pair_1_sections & pair_2_sections) > 0:
        inter_2 += 1


print(inter,inter_2)


#645 too high 
#424 right answer