x=int(input("enter no of teams"))
scores={}
score_compare=list(scores.values())
l=[]
for j in range(0,x):
    key=(chr(65+j))
    l.append(chr(65+j))
    scores[key]=0

print("teams are {}".format(l[0::]))
h={ '3':'''q1) Simplify :150 ÷ (6 + 3 x 8) - 5
 1) 2
 2) 5
 3) 0
 4) None of these''',
'2':'''q2) what is x in 7x+2=30
1) 3
2) 4
3) 1
4) 5''',
   '2': '''q3) A clock seen through a mirror, shows quarter past three. What is the correct time shown by the clock?
 1. 3.15
 2. 8.45
 3. 9.15
 4. 9.45 ''',
   '2':'''q4) Tom was not at school on Saturday last. He was first absent for four days before that. Today is Monday, the 31st of October. When was Tom first absent? Give the day and date.
 1. Monday, Oct. 24
 2. Tuesday, Oct. 25
 3. Wednesday, Oct. 26
 4. Thursday, Oct. 27 ''',
   '1': '''q5) Fill in the blanks; 4, 6, 12, 14, 28, 30, (?)
 1. 60
 2. 62
 3. 64
 4. 32''',
   '4':'''q6) Each edge of a cube is increased by 50%. What will be the percent increase in its volume?
 1. 50 %
 2. 150 %
 3. 133 ¼ %
 4. 237 ½ % ''',
   '2':''' q7) In the following series a wrong number is given. Find out that number.
4, 5, 10, 18, 34, 59, 95
 1. 5
 2. 10
 3. 18
 4. 34''',
   '3':''' q8)A clock reads 4:30. If the minute hand points East, in what direction will the hour hand point?
 1. North
 2. North-West
 3. North-East
 4. South-East''',
   '2':''' q9) 45% of 640 + 64% of 450 = ? % of 1440
 1. 54
 2. 40
 3. 45
 4. 50)  ''',
   '4':''' q10) The wages of 10 workers for a six-day week is $ 1200. What are the one day’s wages of 4 workers?
 1. $ 40
 2. $ 32
 3. $ 80
 4. $ 24 '''}


a=list((h.keys()))
#print(a)

ind=0
for k in h.values():
    print(k)
    c=input('enter answer:')

    if c[1] == a[ind]:
        
        print('that is correct')
        scores[c[0]]+=(ind+1)
        print("scoreboard:")
        for i in (scores):
            print(i, scores[i])
    #print('scoreboard: {}'.format(scores))
    else:
        print('that is incorrect, sorry')
        
        print("scoreboard:")
        for i in (scores):
            print(i, scores[i])
    ind+=1

f=max(scores.values())
for key, value in scores.items():
    if f == value:
        print (key , 'wins')

