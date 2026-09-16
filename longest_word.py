sentence = "Python programming is very interesting"

word = ""
maximum = ""

for ch in sentence:
    if ch != " ":
        word += ch
    else:
        if len(word) > len(maximum):
            maximum = word
        word = ""

# Check the last word
if len(word) > len(maximum):
    maximum = word

print(maximum)