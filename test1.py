list = []
with open ("quotes.txt", encoding = 'utf=8') as f:
    text = f.read()
    lines = text.splitlines()
    f.close()
    c1 = 0
    c2 = 0
    for line in lines:
        quote = line.split(". - ")
        quote_text = quote[0]
        n = len(quote_text)
        if n <= 10:
            list.append (element)
            c1+=1
        else:
            c2+=1
        print(len(quote_text))
        print(quote_text)
print ("Количество слов с длиной не больше 10: ")
print (c1)
print ("Количество слов с длиной больше 10: ")
print (c2)
