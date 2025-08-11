
def count_jewels(jewels: str, stones: str) -> int:
    counter = 0

    for stone in stones:
        if stone in jewels:
            counter += 1
    return counter

print(count_jewels("aA", "aAAbbbb"))

print(count_jewels("ZZ", "zzz"))

print(count_jewels("aAB", "aAAaABbbABAbbabAbajdsknbj"))