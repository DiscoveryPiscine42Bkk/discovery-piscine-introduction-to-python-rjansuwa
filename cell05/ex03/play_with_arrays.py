#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array =[]
seen = set()
for number in original_array:
    if number > 5:
        result = number + 2
        if result not in seen:
            new_array.append(result)
            seen.add(result)
print(original_array)
print(new_array)