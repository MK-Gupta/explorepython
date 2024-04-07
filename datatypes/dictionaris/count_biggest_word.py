



fname = input('Enter file name: ')
handle = open(fname)


counts = dict()

for line in handle:
    print(line)
    words = line.split()
    print(words)
    for word in words:
        print(word)
        counts[word] = counts.get(word,0) + 1
        print(counts)

bigcount = None
bigword = None

for word, count in counts.items():
    print(word)
    print(count)
    if bigcount is None or count > bigcount:
        print(bigcount)
        print(bigword)
        bigword = word
        bigcount = count

print(bigword, bigcount)