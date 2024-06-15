text = f"""Rana Universe"""

char_counts = {}


for char in text:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

total_count = 0
for char, count in char_counts.items():
    print(f"Character Name'{char}' & it Occurs {count} times.")
    total_count += count

print(f"\nTotal character count: {total_count}")
