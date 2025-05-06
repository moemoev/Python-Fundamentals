dict1 = {'shards': 5, 'motes': 9, 'fragments': 9}

for key, val in sorted(dict1.items(), key=lambda kvp: (kvp[1], kvp[0]), reverse=True):
    print(f"{key}: {val}")
