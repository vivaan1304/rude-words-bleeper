import string
rude_words = open("list_of_words.txt").read().split("\n")

def bleeped(s):
    return "".join(len(s) * '*')
def is_rude(s):
    s = s.strip(string.punctuation).lower()
    if s in rude_words:
        return 1
    return 0


def count_rude_words(s):
    count = 0
    words = s.split(" ")
    words[-1] = words[-1].strip()
    for word in words: 
        isitrude = is_rude(word)
        if isitrude:
            count += 1
            print(f"found rude word : {word}")
    return count


def mark(s, edited_file):
    words = s.split(" ")
    words[-1] = words[-1].strip()
    final = []
    for word in words:
        isitrude = is_rude(word)
        if isitrude:
            final.append(bleeped(word))
        else:
            final.append(word)
    final[-1] = final[-1] + "\n"
    edited_file.write(" ".join(final))


def read_file(file_name):
    edited_file = open("edited.txt","w")
    with open(file_name) as file:
        total = 0
        for line in file:
            mark(line,edited_file)
            total += count_rude_words(line)
    if total > 0:
        print(f"found {total} rude word(s)")
    else:
        print("Found no rude words!")
    edited_file.close()

if __name__ == "__main__":
    read_file("read.txt")
