a = "aabbccaa"

repetitions = {}

for index, char in enumerate(a):
    if char in repetitions:
        repetitions[char].append(index)
    else:
        repetitions[char] = [index]

for char, indices in repetitions.items():
    print(f"Character '{char}' appears at indices: {indices}")
    break