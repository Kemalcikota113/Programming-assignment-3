import os

def read_file(path):
    lst = []
    with open(path, "r", encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            lst.append(line)
        return lst

    

def get_words(row):
    return row.lower()


def save_words(path, words):
    with open(path, "w", encoding='utf-8') as file:
        for c in words:
            file.write(c + " ")

        

signs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "'", '-']
    

home = os.getcwd()
path = "E:\\1DV501\\large_texts\\holy_grail.txt"

rows = read_file(path)
print(f"\nRead {len(rows)} lines from file {path}")


words = []
for row in rows:
    w = get_words(row)  # "1    ! 03alpe01 It's a rip off."

    temp = w.split()        # [1, !, 03alpe01, It's, a, rip, off.]

    for i in range(len(temp)):
        if temp[i].endswith("."):
          temp[i] = temp[i].removesuffix(".")
        if temp[i].endswith(","):
          temp[i] = temp[i].removesuffix(",")
        if temp[i].endswith("?"):
          temp[i] = temp[i].removesuffix("?")
        if temp[i].endswith("!"):
          temp[i] = temp[i].removesuffix("!")
        if temp[i].endswith(":"):
            temp[i] = temp[i].removesuffix(":")

        if set(temp[i]).issubset(set(signs)):
            words.append(temp[i])   # [It's, a, rip, off] gets appended

outpath = home + f"output_{len(words)}_words.txt"
save_words(outpath,words)
print(f"Saved {len(words)} words in file {outpath}") 

# switching to next file

path = "E:\\1DV501\\large_texts\\eng_news_100k-sentences.txt"

rows = read_file(path)
print(f"\nRead {len(rows)} lines from file {path}")


words = []
for row in rows:
    w = get_words(row)  # "1    ! 03alpe01 It's a rip off."

    temp = w.split()        # [1, !, 03alpe01, It's, a, rip, off.]

    for i in range(len(temp)):
        if temp[i].endswith("."):
          temp[i] = temp[i].removesuffix(".")
        if temp[i].endswith(","):
          temp[i] = temp[i].removesuffix(",")
        if temp[i].endswith("?"):
          temp[i] = temp[i].removesuffix("?")
        if temp[i].endswith("!"):
          temp[i] = temp[i].removesuffix("!")
        if temp[i].endswith(":"):
            temp[i] = temp[i].removesuffix(":")

        if set(temp[i]).issubset(set(signs)):
            words.append(temp[i])   # [It's, a, rip, off] gets appended

outpath = home + f"output_{len(words)}_words.txt"
save_words(outpath,words)
print(f"Saved {len(words)} words in file {outpath}") 
