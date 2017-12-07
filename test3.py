list = []
while True:
    word = input ("Введите слово \n")
    print (word)
    if word =="":
        break
    else:
        list.append(word)
print ("End.")
print (list)

with open ("quotes.txt", "w", encoding = 'utf=8') as f:
    text = f.read()
    lines = text.splitlines()
    f.close()
    for word in list:
        if word
        print (word)
        print
