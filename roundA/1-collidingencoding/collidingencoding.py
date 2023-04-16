def has_collision(mapping, words):
    encodings = set()  # create a set
    for word in words:  # use a for loop to iterate over words
        encoding = ''.join(str(mapping[letter]) for letter in word)
        print("encoding", encoding)
        if encoding in encodings:
            return True
        encodings.add(encoding)
    return False


t = int(input())
for i in range(1, t+1):
    mapping = input().split()
    print("mapping after split", mapping)
    mapping = {chr(ord('A') + i): int(mapping[i]) for i in range(26)}
    print("mapping after code", mapping)
    n = int(input())
    words = [input().strip() for _ in range(n)]
    if has_collision(mapping, words):
        print(f"Case #{i}: YES")
    else:
        print(f"Case #{i}: NO")
