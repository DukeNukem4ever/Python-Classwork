quotes = []
f = open ("quotes.txt", encoding = 'utf=8')
amount = 0
for s in f:
    i = s.find("разум")
    if i > -1:
        amount += 1
print ("Количество цитат, в которых употребляется слово 'Разум': ", amount)
f.close()
#for line in quotes:
#    value = float(line[3].strip())
#    print (value)
