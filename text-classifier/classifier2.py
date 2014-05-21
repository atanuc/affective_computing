import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import random

stop=stopwords.words('english')

stop.remove('not')

ste=PorterStemmer()

f=open("rt-polarity.neg","r")
negt=(f.read()).split(".")
f.close()
f=open("rt-polarity.pos","r")
post=(f.read()).split(".")
f.close()

print "good"

dicy=[]

i=0

for ln in negt:
    wrd=ln.split(' ')
    if(i%1000==0):
        print i,
    i+=1
    if(len(wrd)>3):
        for wd in wrd :
            t=ste.stem(wd)
            if wd.isalpha() and t not in dicy :
                if wd not in stop :
                    dicy.append(t)

print "\n"
    
for ln in post:
    if(i%1000==0):
        print i,
    i+=1
    wrd=ln.split(' ')
    if(len(wrd)>3):
        for wd in wrd:
            t=ste.stem(wd)
            if wd.isalpha() and t not in dicy :
                if wd not in stop :
                    dicy.append(t)

print len(dicy)

def valu(c,t):
    if c in dicy:
            if ('JJ' in t):
                return 1
            elif ('NN' in t):
                return 2
            elif ('RB' in t):
                return 3
            elif ('VB' in t):
                return 4
            else:
                return 0
cn=0

def fet(ln,cn):
    wrd=ln.split()
    lst=[]
    for w in wrd:
        if w.isalpha() and (len(w)>=1):
            lst.append(w)
    if(cn%1000==0):
        print cn,
    les={}
    for w in dicy:
        les["%s" % w]=0
    fg=1
    for i in range(0,len(lst)):
        t=ste.stem(lst[i])
        if t in dicy:
            if(lst[i] not in 'not'):
                les["%s" % t]+=(fg)
                fg=1
            else:
                fg*=(-1)
    return les

tgt=[]
vect=[]
i=0
for ln in negt:
    t=(fet(ln,cn))
    cn+=1
    vect.append((t,'0'))

for ln in post:
    t=(fet(ln,cn))
    cn+=1
    vect.append((t,'1'))

print "good"

random.shuffle(vect)
train,test=vect[0:9000],vect[10000:14000]

print "good"

clas = nltk.NaiveBayesClassifier.train(train)

print "good"

print nltk.classify.accuracy(clas, test)















            

        
