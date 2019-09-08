def char_count(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


filename = input('File name is: ')
with open(filename) as f:
    text = f.read().lower()


pairs = []
for char in 'abcdefghijklmnopqrstuvwxyz':
    perc = 100 * char_count(text, char) / len(text)
    pairs.append(round(perc, 2))
    pairs.append(char)


new_pairs = []
for i in range(0, len(pairs) - 1, 2):
    new_pairs.append(pairs[i])
new_pairs.sort(reverse = True)


findict = {}
for i in new_pairs:
    for o in pairs:
        if o == i and not pairs[pairs.index(o) + 1] in findict:
            findict[pairs[pairs.index(o) + 1]] = o
            pairs[pairs.index(o)] = 101


for i in findict:
    print(i, '-', findict[i])
