
# coding: utf-8

# In[2042]:


#import data set
text = open("Data.txt","r").read()


# In[2043]:


#making list of lines as documents
documents = []

for r in text.split('\n'):
    documents.append( r )


# In[2044]:


documents


# In[2045]:


# Searching ball_number line using rex for example like = 1.1 , 2.1, 17.1
import re
ball = re.findall(r'\n([0-9].[1-6]|[1-2][0-9].[1-6])\n',text)
ball


# In[2046]:


#length of documents file = l
l = len(documents)
l


# In[2048]:


# main sentences which are important,
#(ball_no + immidiate commentry line) 
#sent = [ , , , , ,  .....]
sent = []
ball_no = []
for i in range(l):
    if documents[i] in ball:
        ball_no.append(documents[i])
        sentence = documents[i]+','+documents[i+1]
        print(sentence)
        sent.append(sentence)


# In[2049]:


sent.reverse()


# In[2050]:


# sent is list of all important commentry lines starting from 0.1 ball to last ball
sent[0]


# In[2051]:


x = len(sent)
x


# In[2052]:


# splitting each commentry present in sent list by comma seprated & storing it in line list
#line is list of list 
#line = [[],[],[].......]
line = []
for i in range(x):
    line.append(sent[i].split(','))
lx = len(line)
print(lx)
line[0] 


# In[2053]:


# Finding batsman and ballers
batsman = []
ballers = []
for i in range(lx):
    players = line[i][1].split('to')
    batsman.append(players[1])
    ballers.append(players[0])


# In[2054]:


batsman


# In[2055]:


line


# In[2056]:


# finding unique batsman and ballers
batsman = list(dict.fromkeys(batsman))
ballers = list(dict.fromkeys(ballers))
print(batsman)
print(ballers)


# In[2057]:


import pandas as pd


# In[2058]:


# making batsman dataFrame using pandas
myBatsman = pd.DataFrame(0, batsman, ['status', 'R', 'B', '4s', '6s', 'SR'])
myBatsman['status'] = 'not out'


# In[2059]:


myBatsman


# In[2060]:


myBatsman.loc[' Miller','status']


# In[2061]:


# making dataFrame for ballers
myBallers = pd.DataFrame(0, ballers, ['O', 'M', 'R', 'W', 'NB', 'WD', 'EC' , 'B'])
myBallers


# In[2062]:


extra = 0
wide  = 0
score = 0
wickets = 0
noBall = 0
b = 0
lb = 0
fall = []
for i in range(lx):
    ball_no = line[i][0]
    players = line[i][1].split('to')
    batsmanName = players[1]
    ballerName = players[0]
#     print(ball_no)
#     print(ballerName)
#     print(batsmanName)
    line[i][2] = line[i][2].lower()
#     print(line[i][2])
    
    # If ball is wide
    if line[i][2] == ' wide':
        wide = wide + 1
        score = score +1
        myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 1
        myBallers.loc[ballerName,'WD'] = myBallers.loc[ballerName,'WD'] + 1
    
    # If ball is no ball
    elif line[i][2] == ' no ball':
        noball = noball + 1
        score = score +1
        myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 1
        myBallers.loc[ballerName,'NB'] = myBallers.loc[ballerName,'NB'] + 1
    
    # If ball is legal and 4 runs
    elif line[i][2] == ' four' or line[i][2] == ' 4' or line[i][2] == ' 4 runs':
        myBatsman.loc[batsmanName,'4s'] = myBatsman.loc[batsmanName,'4s'] + 1
        myBatsman.loc[batsmanName,'R'] = myBatsman.loc[batsmanName,'R'] + 4
        myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName,'B'] + 1  
        
        myBallers.loc[ballerName,'B'] = myBallers.loc[ballerName,'B'] + 1
        myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 4
        score = score +4
        
    # If ball is legal and 6 runs
    elif line[i][2] == ' six' or line[i][2] == ' 6' or line[i][2] == ' 6 runs':
        myBatsman.loc[batsmanName,'6s'] = myBatsman.loc[batsmanName,'6s'] + 1
        myBatsman.loc[batsmanName,'R'] = myBatsman.loc[batsmanName,'R'] + 6
        myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName,'B'] + 1
        
        myBallers.loc[ballerName,'B'] = myBallers.loc[ballerName,'B'] + 1
        myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 6
        score = score +6
    
    # If ball is legal and 1 runs
    elif line[i][2] == ' 1 run' or line[i][2] == ' 1':
        myBatsman.loc[batsmanName,'R'] = myBatsman.loc[batsmanName,'R'] + 1   
        myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName,'B'] + 1
        
        myBallers.loc[ballerName,'B'] = myBallers.loc[ballerName,'B'] + 1
        myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 1
        score = score +1
        
    # If ball is legal and 2 runs    
    elif line[i][2] == ' 2 runs' or line[i][2] == ' 2 run' or line[i][2] == ' 2':
        myBatsman.loc[batsmanName,'R'] = myBatsman.loc[batsmanName,'R'] + 2 
        myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName,'B'] + 1
        
        myBallers.loc[ballerName,'B'] = myBallers.loc[ballerName,'B'] + 1
        myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 2
        score = score +2
    
    # If ball is legal and 3 runs
    elif line[i][2] == ' 3 runs' or line[i][2] == ' 3 run' or line[i][2] == ' 3':
        myBatsman.loc[batsmanName,'R'] = myBatsman.loc[batsmanName,'R'] + 3
        myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName,'B'] + 1
        
        myBallers.loc[ballerName,'B'] = myBallers.loc[ballerName,'B'] + 1
        myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 3
        score = score +3
    
    # If ball is legal and 5 runs
    elif line[i][2] == ' 5 runs' or line[i][2] == ' 5 run' or line[i][2] == ' 5':
        myBatsman.loc[batsmanName,'R'] = myBatsman.loc[batsmanName,'R'] + 5
        myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName,'B'] + 1
        
        myBallers.loc[ballerName,'B'] = myBallers.loc[ballerName,'B'] + 1
        myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 5
        score = score +5
    
    # If ball is legal and no runs
    elif line[i][2] == ' no run' or line[i][2] == ' no':
        myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName,'B'] + 1 
        
        myBallers.loc[ballerName,'B'] = myBallers.loc[ballerName,'B'] + 1
    
    # If ball is legal and leg byes
    elif line[i][2] == ' leg byes' or line[i][2] == ' leg bye' or line[i][2] == ' lb':
        myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName,'B'] + 1        
        myBallers.loc[ballerName,'B'] = myBallers.loc[ballerName,'B'] + 1
                        
        if line[i][3] == ' four' or line[i][3] == ' 4' or line[i][3] == ' 4 runs':
            lb = lb + 4
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 4
            score = score +4

        if line[i][3] == ' six' or line[i][3] == ' 6' or line[i][3] == ' 6 runs':
            lb = lb + 6
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 6
            score = score +6

        if line[i][3] == ' 1 run' or line[i][3] == ' 1':
            lb = lb + 1
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 1
            score = score +1

        if line[i][3] == ' 2 runs' or line[i][3] == ' 2 run' or line[i][3] == ' 2':
            lb = lb + 2
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 2
            score = score +2

        if line[i][3] == ' 3 runs' or line[i][3] == ' 3 run' or line[i][3] == ' 3':
            lb = lb + 3
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 3
            score = score +3

        if line[i][3] == ' 5 runs' or line[i][3] == ' 5 run' or line[i][3] == ' 5':
            lb = lb + 5
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 5
            score = score +5
    
    # If ball is legal and bye
    elif line[i][2] == ' byes' or line[i][2] == ' bye':
        myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName,'B'] + 1
        myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 1
                
        if line[i][3] == ' four' or line[i][3] == ' 4' or line[i][3] == ' 4 runs':
            b = b + 4
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 4
            score = score +4

        if line[i][3] == ' six' or line[i][3] == ' 6' or line[i][3] == ' 6 runs':
            b = b + 6
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 6
            score = score +6

        if line[i][3] == ' 1 run' or line[i][3] == ' 1':
            b = b + 1
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 1
            score = score +1

        if line[i][3] == ' 2 runs' or line[i][3] == ' 2 run' or line[i][3] == ' 2':
            b = b + 2
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 2
            score = score +2

        if line[i][3] == ' 3 runs' or line[i][3] == ' 3 run' or line[i][3] == ' 3':
            b = b + 3
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 3
            score = score +3

        if line[i][3] == ' 5 runs' or line[i][3] == ' 5 run' or line[i][3] == ' 5':
            b = b + 5            
            myBallers.loc[ballerName,'R'] = myBallers.loc[ballerName,'R'] + 5
            score = score +5
    
    # If ball is legal and out 
    else:
        myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName,'B'] + 1
        myBallers.loc[ballerName,'B'] = myBallers.loc[ballerName,'B'] + 1
        add = str(score) + '-' + str(wickets) + '('+ batsmanName + ',' + ball_no + ')'
        fall.append(add)
        
        content = line[i][2].split('!')
        print(content[0])
        if content[0] == ' out bowled':
            myBatsman.loc[batsmanName,'status'] = 'b ' + ballerName 
            myBallers.loc[ballerName,'W'] = myBallers.loc[ballerName,'W'] + 1
            wickets = wickets +1
        elif content[0] == ' run out':
            myBatsman.loc[batsmanName,'status'] = 'run out'
            wickets = wickets +1
        else:
            content2 = content[0].split('by')
            myBatsman.loc[batsmanName,'status'] = 'c ' + content2[1] + ' b ' + ballerName 
            myBallers.loc[ballerName,'W'] = myBallers.loc[ballerName,'W'] + 1
            wickets = wickets +1
    
    myBatsman.loc[batsmanName,'SR'] = int((myBatsman.loc[batsmanName,'R'] / myBatsman.loc[batsmanName,'B']) * 100)
    myBallers.loc[ballerName,'O'] = myBallers.loc[ballerName,'B']/6
    myBallers.loc[ballerName,'EC'] = myBallers.loc[ballerName,'R']/myBallers.loc[ballerName,'O']
    


# In[2063]:


myBatsman


# In[2067]:


myBallers


# In[2069]:


# calculating total extras
extra =lb + b + noBall + wide


# In[2076]:


print('SCORECARD')
print(myBatsman)
print('\nExtras\t\t'+ str(extra) + '(b ' + str(b) +', lb '+ str(lb) +', w '+ str(wide) +', nb '+ str(noBall) + ')')
print('\nTotal\t\t'+ str(score) + ' ('+ str(wickets)+ ' wkts, '+ str(myBallers['O'].sum()) +' Ov)\n' )
print(*fall, sep='  ')
print('\n')
print(myBallers.iloc[:,:-1])

