def count_characters(input_text):
    char_counts = {}

    for char in input_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    total_count = sum(char_counts.values())
    print(type(total_count))
    print(type(char_counts))

    return total_count, char_counts

if __name__ == "__main__":
    text_to_analyze = f"Rana Universe"
    total_count , char_counts = count_characters(text_to_analyze)

    print(f"Total Characters Count is::: {total_count}")
    print(f'Individulas Characters Counts Are Below::: {char_counts}')

    # for char, count in char_counts.items():
    #     print (f"Character '{char}' occurs {count} times")
