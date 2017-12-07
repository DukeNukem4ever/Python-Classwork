with open ("quotes.txt", encoding = 'utf=8') as f:
    text = f.read()
    lines = text.splitlines()
    f.close()
    c1 = 0
    c2 = 0
    for line in text.split(" "):
        for word in line.split(" "):
            n = len(word)
            if n <= 10:
                c1+=1
            else:
                c2+=1
            print(len(word))
            print(word)
print ("Количество слов с длиной не больше 10: ")
print (c1)
print ("Количество слов с длиной больше 10: ")
print (c2)
