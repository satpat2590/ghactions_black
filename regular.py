new_tuple = ("Apple", "Jeffrey", "Bananas", "Steven", "Grapes", "Satyam")

mapping = {y: new_tuple[idx + 1] for idx, y in enumerate(new_tuple) if idx % 2 == 0}

print(mapping)

for key, val in mapping.items():
    if "a" in key.lower():
        print(val)


vals = [1, 2, 3, 4, 5, 6, 3, 4, 5, 3, 65, 56, 78, 7, 8, 9]

print([x for x in vals if x % 2 == 1])
