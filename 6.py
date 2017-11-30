#def hello(user1, age):
#    print ('Hello, ' + user1 + '!')
    #print (user2.title())
    #print (user3.title())
#    if age > 10:
#        print ("older than 10")
#    else:
#        print(age)
#    sum_=0
#    for i in range(16):
#        sum_ +=1
#    print (sum_)
#    #print (gl)

#gl = 100
    
#hello("Anna", 15)
#print (sum_)

#def hello(user1,age):
#    print("Hello, " + user1 + "!")
#    if age>10:
#        print("older than 10")
#    else:
#        print(age)
#        new_name = user1.title()
#        return user1.title()

#user_title = hello ("ann",10)
#print (user_title)

#def hello(user1):
#    print ("hello, " + user1 + "")
#    return user1.title()
#
#user_title = hello('ann')
#print(user_title)

def hello(user1):
    '''

    '''
    print("hello, " + user1 + "!")
    return uesr1.title

def elements(word):
    ''' '''
    for l in word:
        print(l)
    print(len(word))

def tokenize(sentence):
    words = sentence.split()
    return words

sent = 'functions are useful'

tok_result = tokenize(sent)
print(tok_result)

for w in tok_result:
    print (w.upper())

def lines_div(fname):
    '''открыть файл, прочесть, разделить на строки, вернуть минимальную длину строки в символах'''
    with open(fname, encoding = 'utf8') as f:
        lines_raw = f.readlines()
    lines_lengths = []
    for line in lines_raw:
        clear_line = line.strip()
        if clear_line:
            print(len(clear_line), clear_line)
            lines_lengths.append(len(clear_line))
    return min(lines_lengths)

min_1 = lines_div ('dovlatov2.txt')
print(min_1)

#lines = lines_div('hse.txt')
#els = sent.split()
#elements(els)
