def second_index(string, entry_str):
    if string.count(entry_str) > 1:
        second_entry_index = string.find(entry_str, string.find(entry_str) + len(entry_str))
        return second_entry_index
    return None


print(second_index("sims","s"))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))
print(second_index("Hello, hello", "lo"))