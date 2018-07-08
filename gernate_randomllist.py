from random import randint


def mixer(liste):
    scrambled = []
    while len(liste) > 0:
        ind = randint(0, len(liste) - 1)
       # print(ind)
        scrambled.append(liste[ind])
        del liste[ind]
    return scrambled


if __name__ == "__main__":
    liste = list(range(15))
    list_to_scramble = liste.copy()

    print('liste            before= ' + str(liste))
    print('list_to_scramble before= ' + str(list_to_scramble))

    scrambled = mixer(list_to_scramble)

    print('liste            after 1 = ' + str(liste))
    print('list_to_scramble after 1 = ' + str(list_to_scramble))

    list_to_scramble = liste.copy()
    scrambled = mixer(list_to_scramble)

    print('liste            after 2 = ' + str(liste))
    print('list_to_scramble after 2 = ' + str(list_to_scramble))

    print('scrambled = ' + str(scrambled))
