import itertools
hosts = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10']
groups = ['G1', 'G1', 'G2', 'G2', 'G3', 'G3', 'G4', 'G4', 'G4', 'G4']
'''
G1, H1
G2, H2
G3, H3
'''
d = {}
for i in range(len(hosts)):
    d[hosts[i]] = groups[i]
print(d)

res = []

for key, value in d.items():
    full_list = list(itertools.chain.from_iterable(res))
    if value not in full_list:
        i = 0
        if len(res) == 0:
            res.append(list())
        res[i].extend([key, value])

    elif value in full_list and key not in full_list:
        i += 1
        if len(res) == i:
            res.append(list())
        res[i].extend([key, value])

print(res)


