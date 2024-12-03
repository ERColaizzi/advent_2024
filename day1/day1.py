# init statement here
#day 1 part 1


#thoughts
#split lines
#create two listss
#order lists
# for i in L1/L2 compare
#distance is abs from L1 to L2 and add to running total 

list1=[]
list2=[]
distance = 0


with open('C:\\Users\\ercol\\Documents\\programming\\advent_2024\\day1\\input.txt', 'r') as file:
    for line in file:
        list1.append((line.split()[0]))
        list2.append((line.split()[1]))



list1.sort()
list2.sort()


for i in range(len(list1)):
    distance = distance + abs(int(list1[i]) - int(list2[i]))

print("the distance is:",distance)
    
