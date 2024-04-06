


# take input from the user using input function
name = input('enter:')

print(name)

x = 3 

# use index operator 
w = name[x - 1]
print(w)

print(name[3])

print(len(name))



index = 0 
while index < len(name):
    letter = name[index]
    print(index, letter)
    index = index + 1 

#for loop is more better than for loop compare above while loop with for loop
#the iteration variable is completely taken care of by the for loop

for letter in name:
    print(index,letter)

#looping and counting


count = 0 
for letter in name:
    if letter == 'a':
        count = count + 1
print(count)



