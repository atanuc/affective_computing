from nltk.stem.snowball import *
from nltk.corpus import stopwords
import re

stop=stopwords.words()
ste = SnowballStemmer("english")

dict={}
emo=["anger","disgust","fear","joy","sadness","surprise","neutral"]
wdemo={}

def inv(w):
    if w in "anger":
        return "fear"
    elif w in "joy":
        return "sadness"
    else:
        return "neutral"

   
a=open("emotion.txt","r")
st=a.read()
pq=re.split('\W+',st)
awd=[]
for wx in pq:
    if wx.isalpha():
        awd.append(ste.stem(wx.lower()))
        dict["%s" % wx]="neutral"
a.close()
emodict=set(awd)
    
stop.remove('not')

for w in emo[0:6]:
    print w
    a=open(w+".txt","r")
    #b=open(w+"2.txt","w")
    st=a.read()
    pq=re.split('\W+',st)
    awd=[]
    for wx in pq:
        if wx.isalpha() and len(wx)>=2:
            awd.append(ste.stem(wx.lower()))
    a.close()
    wdemo["%s" % w]=set(awd)

    for wd in wdemo["%s" % w]:
        #b.write(wd+"\n")
        dict["%s" % wd]=w
    #b.close()

while(1):
    c=raw_input("GIMME!\n")
    arr=c.split(' ')
    wds=[]
    for w in arr:
        if w.lower() not in stop:
            wds.append(ste.stem(w.lower()))
    
    cn={}
    for i in emo:
        cn["%s" % i]=0
    
    fg=1

    for w in wds:
        if w.lower() in 'not':
            fg=0
        if (w in dict.keys()) and (fg==1):
            cn[dict[w]]+=1
        elif (w in dict.keys()):
            cn[inv(dict[w])]+=1
            fg=1

    print wds
    
    tot=0    
    for c in emo[0:6]:
        tot+=cn["%s" % c]

    if tot==0:
        print "neutral","1"
    else:
        cn["neutral"]=1
        for c in emo[0:6]:
            print c,(cn["%s" % c]*1.0/tot)
            cn["neutral"]-=(cn["%s" % c]*1.0/tot)
        print "neutral",cn["neutral"]