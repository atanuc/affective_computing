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
posit=(f.read()).split(".")
f.close()

f=open("score1.txt","r")
txt=f.read()
lin=txt.split("\n")
f.close()

print "good"

fdicy=[]

i=0

for ln in lin:
    wts=ln.split()
    if (len(wts)>2) and ('_' not in wts[1]) and (len(wts[1])<11):
        fdicy.append(wts[0]+"-"+wts[1])

print len(fdicy)

def valu(c,t):
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
            
tgt=[]
vect=[]

stn=""

cn=0

sdicy=[]

for ln in negt:
    wrd=ln.split(' ')
    for w in wrd:
        if w.isalpha():
            sdicy.append("r-"+w)
            sdicy.append("a-"+w)
            sdicy.append("n-"+w)
            sdicy.append("v-"+w)

print len(sdicy)

mdicy=list(set(fdicy)&set(sdicy))

print len(mdicy)

for ln in negt[0:5000]:
    wrd=ln.split(' ')
    if(cn%100==0):
        print cn,
    cn+=1
    lst=[]
    for wd in wrd:
        if wd.isalpha() and (len(wd)>=1):
            lst.append(wd)
    post=nltk.pos_tag(lst)
    les={}
    for w in mdicy:
        les["%s" % w]=0
    if(len(wrd)>3):
        for wd in wrd :
            for i in range(0,len(lst)):
                if(lst[i].lower() not in 'not'):
                    nstn=""
                    w=lst[i].lower()
                    t=valu(w,post[i][1])
                    if(t==1):
                        nstn=("a-"+stn+w)
                    elif(t==2):
                        nstn=("n-"+stn+w)
                    elif(t==3):
                        nstn=("r-"+stn+w)
                    elif(t==4):
                        nstn=("v-"+stn+w)
                    if nstn in mdicy:
                        les["%s" % nstn]+=1
                    stn=""
                else:
                    stn=stn+"not-"
    vect.append(les)
    tgt.append('0')

print "\n"
    
for ln in posit[0:5000]:
    wrd=ln.split(' ')
    if(cn%100==0):
        print cn,
    cn+=1
    lst=[]
    for wd in wrd:
        if wd.isalpha() and (len(wd)>=1):
            lst.append(wd)
    post=nltk.pos_tag(lst)
    les={}
    for w in mdicy:
        les["%s" % w]=0
    if(len(wrd)>3):
        for wd in wrd :
            for i in range(0,len(lst)):
                if(lst[i].lower() not in 'not'):
                    nstn=""
                    w=lst[i].lower()
                    t=valu(w,post[i][1])
                    if(t==1):
                        nstn=("a-"+stn+w)
                    elif(t==2):
                        nstn=("n-"+stn+w)
                    elif(t==3):
                        nstn=("r-"+stn+w)
                    elif(t==4):
                        nstn=("v-"+stn+w)
                    if nstn in mdicy:
                        les["%s" % nstn]+=1
                    stn=""
                else:
                    stn=stn+"not-"
    vect.append(les)
    tgt.append('1')

cn=0

"""def fet(ln,cn):
    wrd=ln.split()
    lst=[]
    for w in wrd:
        if w.isalpha() and (len(w)>=1):
            lst.append(w)
    #post=nltk.pos_tag(lst)
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
    for w in dicy:
        t=ste.stem(w)
        les["%s" % ("n-"+w)]=0
        les["%s" % ("a-"+w)]=0
        les["%s" % ("r-"+w)]=0
        les["%s" % ("v-"+w)]=0
    for i in range(0,len(lst)):
        if(lst[i] not in 'not'):
            t=valu(lst[i],post[i][1])
            if(t==1):
                les["%s" % ("a-"+w)]+=1
            elif(t==2):
                les["%s" % ("n-"+w)]+=1
            elif(t==3):
                les["%s" % ("r-"+w)]+=1
            elif(t==4):
                les["%s" % ("v-"+w)]+=1
        else:
            t=valu(lst[i],post[i][1])
            if(t==1):
                les["%s" % ("a-"+w)]-=1
            elif(t==2):
                les["%s" % ("n-"+w)]-=1
            elif(t==3):
                les["%s" % ("r-"+w)]-=1
            elif(t==4):
                les["%s" % ("v-"+w)]-=1
    return les"""

data=[]

for i in range(0,len(vect)):
    t=(vect[i],tgt[i])
    data.append(t)

print "good",len(data)

random.shuffle(data)

train,test=data[0:5000],data[5000:10000]

print "good"

clas = nltk.NaiveBayesClassifier.train(train)

print "good"

print nltk.classify.accuracy(clas, test)















            

        
