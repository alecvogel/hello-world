def vowelCount():
    phrase = input('Enter a phrase: ')
    phrase = phrase.lower()
    a = phrase.count('a')
    e = phrase.count('e')
    i = phrase.count('i')
    o = phrase.count('o')
    u = phrase.count('u')
    print('a, e, i, o, and u apprear, respectively, ' + str(a) + ', ' + str(e) + ', ' + str(i) + ', ' + str(o) + ', ' + str(u) + ' times.')

vowelCount()
