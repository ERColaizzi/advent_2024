# for each row
#check up/down all
#
#
# for each i < i+1 and i+2 all i range -2
#
#
#
#



file = open(r"C:\Users\ercol\Documents\programming\advent_2024\day2\input.txt", 'r')

#print(file.read())

count=0
way=''
line=[]

for row in file:
    line = row.split()
    for i in range(len(line)):
        if all(line[i]<=line[i+1]):
            way = up
#         elif line[i]>=line[i:]:
#             way = down
#         else:
#             break
#     
print(way)



