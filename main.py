text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

wor = set(words)
longest_word = words[0]
shortest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

char_frequency = {}

for char in text:
    if char in char_frequency.keys():
        char_frequency[char] = char_frequency[char] + 1
    else:
        char_frequency[char] = 1

print("Количество разных слов:", len(wor))
print("Самое длинное слово:", longest_word)
print("Самое короткое слово:", shortest_word)

print("Частота символов:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")