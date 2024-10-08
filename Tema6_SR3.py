#Tema6_SR3

from collections import Counter

def top_3(s):
    count = Counter(map(int, s))

    most_common = count.most_common(3)

    result = dict(sorted(most_common, key=lambda x: x[0]))

    return result


sequence = "123124324323632462362164326234324"
result = top_3(sequence)

print(result)