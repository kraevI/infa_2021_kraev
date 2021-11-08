from random import randint

print('Введите Ваше имя:')
name = input()

output = open('scores', 'r+')
s = output.readlines()
c = []
for k in range(0, len(s)):
    a = s[k]
    b = a.split()
    for i in b:
        if(i.isdigit()):
            c.append(int(i))
score = randint(50, 100)
p = len(s)
for i in range(len(c)-1, -1, -1):
    if score >= c[i]:
        p = i
c.insert(p, score)
s.insert(p, 'Имя: '+str(name)+'    Результат: '+str(score)+'\n')

output.seek(0)
for i in range(0, len(s)):
    output.write(str(s[i]))

output.close()



