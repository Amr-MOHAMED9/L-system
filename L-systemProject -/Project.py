'''The code will requires a txt file written in the format given in in the txt file sent with project or in the report to work'''

from turtle import *
l=[]
f= open('filename.txt','r')
for i in f:
    l. append(i)
def dicho_prepare(l):
    a=[]
    for i in l:
        a.append(i.split('=',1))
    a=a[:-1]
        
    o=[]
    oo=[]
    for i in a:
        o.append(i[0])
        oo.append([i[1]])
    y=[]
    for i in oo:
        for k in i:
           y.append(k)  
    y[0]=y[0][2:-3]
    y[1]= y[1][4:-3]
    y[2]=y[2][:-3]
    dicho=dict(zip(o,y))
    return dicho

dicho=dicho_prepare(l)

def system(dicho,axiom):
    s=""

    for i in axiom:
        if i=='a':
            s+=dicho['rules ']
        elif i=='b':
            s+=dicho['"b']
        else:
            s+=i
    return s

def final_ax(dicho,level,axiom):
    s=axiom
    for i in range (level):
        s=system(dicho,s)
    return s
ax=final_ax(dicho,int(dicho['level ']),dicho['axiom '])
cpt=0
for i in range (len(ax)):
    if ax[i]=='a':
        pd();fd(int(dicho['size ']))
        cpt+=1
    if ax[i]=='b':
        pu(); fd(60)
        cpt+=1
    if ax[i]=='-':
        left(int(dicho['angle ']))
        cpt+=1
    if ax[i]=='+':
        right(int(dicho['angle ']))
        cpt+=1
    if ax[i]=='*':
        right(180)
        cpt+=1
    if ax[i]=='[':
        x,y=position()
        cpt+=1
    if ax[i]==']':
        goto(x,y)
        cpt+=1
exitonclick()