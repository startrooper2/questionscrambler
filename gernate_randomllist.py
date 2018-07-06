from random import randint

liste = list(range(15))
order = []
while len(liste) > 0:
    ind = randint(0, len(liste) - 1)
    print(ind)
    order.append(liste[ind])
    del liste[ind]

print('liste = ' + str(liste))
print('order = ' + str(order))
