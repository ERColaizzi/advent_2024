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


for row in file:
    line = row.split()
    for i in range(len(line)-2):
        if line[i]<line[i+1] and line[i]<line[i+2]:
            True
        else:
            break
        count=count+1

print(count)



