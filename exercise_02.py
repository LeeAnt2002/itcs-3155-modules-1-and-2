def suffixfinder(w, w2):
    if w2.endswith(w):
        print('True')

    elif w.endswith(w2):
        print('True')
    else:
        print('False')


w = input ('Enter a string: ')
w2 = input ('Enter another string: ')
suffixfinder(w, w2)
