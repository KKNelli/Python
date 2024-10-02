#A megadott listából készíts egy új listát, mely a 6 karakternél rövidebb elemeket tartalmazza. Az új lista legyen abc szerint rendezve.
#['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

fruits =['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
short_fruits = []
for i in fruits:
    if len(i) < 6:
        short_fruits.append(i)
short_fruits.sort()
print(short_fruits)