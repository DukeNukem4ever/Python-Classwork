lines2016 = []
with open ('happiness-cantril-ladder.csv', encoding = 'utf-8') as f:
    #for line in f:
    lines = f.readlines()
    for line in lines:
        #print(line)
        cells = line.split(',')
        #print(cells)
        if cells[2] == '2016':
            lines2016.append(cells)
            
user_country = input("Your country: ")
found_answer = False
for line in lines2016:
    if line[0] == user_country:
        #print(line[3])
        value = float(line[3].strip())
        print(value)
        found_answer = True
        break
if not found_answer:
    print ("Sorry, I don't know")
