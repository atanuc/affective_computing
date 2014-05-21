import nltk

f=open("score1.txt","r")
txt=f.read()
lin=txt.split("\n")

aposlist={}
rposlist={}
vposlist={}
nposlist={}
aneglist={}
nneglist={}
vneglist={}
rneglist={}
dicy=[]

for l in lin:
    wds=l.split(' ')
    if(len(wds)>3):
        dicy.append(wds[1])
        aposlist["%s" % wds[1]]=0
        aneglist["%s" % wds[1]]=0
        nposlist["%s" % wds[1]]=0
        nneglist["%s" % wds[1]]=0
        rposlist["%s" % wds[1]]=0
        rneglist["%s" % wds[1]]=0
        vposlist["%s" % wds[1]]=0
        vneglist["%s" % wds[1]]=0
        
for l in lin:
    wds=l.split(' ')
    if(len(wds)>3):
        t=wds[0]
        if(t in 'a'):
            aposlist["%s" % wds[1]]=float(wds[2])
            aneglist["%s" % wds[1]]=float(wds[3])
        elif(t in 'r'):
            rposlist["%s" % wds[1]]=float(wds[2])
            rneglist["%s" % wds[1]]=float(wds[3])
        elif(t in 'n'):
            nposlist["%s" % wds[1]]=float(wds[2])
            nneglist["%s" % wds[1]]=float(wds[3])
        elif(t in 'v'):
            vposlist["%s" % wds[1]]=float(wds[2])
            vneglist["%s" % wds[1]]=float(wds[3])

f.close()

def valu(c,t):
    val=(0,0)
    if c in dicy:
            if ('JJ' in t):
                val=(aposlist["%s" % tt],aneglist["%s" % tt])
            elif ('NN' in t):
                val=(nposlist["%s" % tt],nneglist["%s" % tt])
            elif ('RB' in t):
                return 0
            elif ('VB' in t):
                val=(vposlist["%s" % tt],vneglist["%s" % tt])
    return val

while(1):
    st=raw_input("GIMME : ")
    wds=st.split()
    post=nltk.pos_tag(wds)
    psum=0
    nsum=0
    a=0
    b=0
    fg=0
    for i in range(0,len(wds)):
        t=post[i][1]
        tt=(post[i][0].lower())
        if tt in dicy and fg==1:
            tup=valu(tt,t)
            if(tup!=0):
                psum+=(2*(a-b)*tup[0])
                nsum+=(2*(a-b)*tup[1])
                fg=0
            else:
                a+=rposlist["%s" % tt]
                b+=rneglist["%s" % tt]
        elif tt in dicy:
            tup=valu(tt,t)
            if(tup!=0):
                psum+=(tup[0])
                nsum+=(tup[1])
            else:
                a=rposlist["%s" % tt]
                b=rneglist["%s" % tt]
                fg=1

    tot=psum+nsum 
    print psum/tot,nsum/tot        

