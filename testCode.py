from kirbyClass import *
from crossingClass import *
from joinClass import *
from strandClass import *
from componentClass import *

#fixed PD diagrams:

#unknot w/ an R1:
knot=component(2,-1)
y=strand(knot)
z=strand(knot,y,y)
y.set_pred(z)
y.set_succ(z)
x=crossing(y,y,z,z)
y.set_pred_con(x)
z.set_pred_con(x)
y.set_succ_con(x)
z.set_succ_con(x)
unknot_r1=Kirby([x], [])


# trefoil
tr = component(2, 3)
a = strand(tr)
b = strand(tr, a)
c = strand(tr, b)
d = strand(tr, c)
e = strand(tr, d)
f = strand(tr, e, a)
a.set_pred(f)
a.set_succ(b)
b.set_succ(c)
c.set_succ(d)
d.set_succ(e)
e.set_succ(f)
c1 = crossing(a, e, b, d)
c2 = crossing(e, c, f, b)
c3 = crossing(c, a, d, f)
trefoil = Kirby([c1, c2, c3], [])
trefoil.rename_all()
trefoil.set_all_cons()

   #print('trefoil: \n' + str(trefoil) + '\n')

#unknot
unknt = component(2, 0)
x = strand(unknt)
#y = strand(unknt, x, x)
j1 = join(x, x)
#j2 = join(y, x)
x.set_pred(x)
x.set_succ(x)
x.set_pred_con(j1)
x.set_succ_con(j1)
#y.set_pred_con(j1)
#y.set_succ_con(j2)
unknot = Kirby([], [j1])
#unknot.set_all_cons()

#print('unknot: \n' + str(unknot) + '\n')

#unknot w/ r2
kt=component(2,0)
k=strand(kt)
l=strand(kt,k)
m=strand(kt,l)
n=strand(kt,m,k)
k.set_pred(n)
k.set_succ(l)
l.set_succ(m)
m.set_succ(n)
cr1=crossing(k,k,n,l)
cr2=crossing(m,l,n,m)
k.set_pred_con(cr1)
k.set_succ_con(cr1)
l.set_pred_con(cr1)
l.set_succ_con(cr2)
m.set_pred_con(cr2)
m.set_succ_con(cr2)
n.set_pred_con(cr2)
n.set_succ_con(cr1)
unknot_r2=Kirby([cr1, cr2],[])

#another unknot but w two joins this time!
ukt=component(2,0)
o=strand(ukt)
p=strand(ukt,o,o)
o.set_pred(p)
o.set_succ(p)
jn1=join(o,p)
jn2=join(p,o)
o.set_pred_con(jn1)
o.set_succ_con(jn2)
p.set_pred_con(jn2)
p.set_succ_con(jn1)
unknot2=Kirby([],[jn1,jn2])

mc=component(2,0)
ma=strand(mc)
mb=strand(mc,ma,ma)
ma.pred=mb
ma.succ=mb
md=crossing(mb,ma,ma,mb)
for i in [ma,mb]:
   i.set_pred_con(md)
   i.set_succ_con(md)
me=Kirby([md],[])


#disjoint trefoil and unknot
tr_u=Kirby([c1,c2,c3],[j1])

#two disjoint trefoils
trr=component(2,3)
aa=strand(trr)
bb=strand(trr,aa)
cc=strand(trr,bb)
dd=strand(trr,cc)
ee=strand(trr,dd)
ff=strand(trr,ee,aa)
aa.set_pred(ff)
aa.set_succ(bb)
bb.set_succ(cc)
cc.set_succ(dd)
dd.set_succ(ee)
ee.set_succ(ff)
c4=crossing(aa,ee,bb,dd)
c5=crossing(ee,cc,ff,bb)
c6=crossing(cc,aa,dd,ff)
aa.set_pred_con(c6)
aa.set_succ_con(c4)
bb.set_pred_con(c4)
bb.set_succ_con(c5)
cc.set_pred_con(c5)
cc.set_succ_con(c6)
dd.set_pred_con(c6)
dd.set_succ_con(c4)
ee.set_pred_con(c4)
ee.set_succ_con(c5)
ff.set_pred_con(c5)
ff.set_succ_con(c6)
two_trefoils=Kirby([c1,c2,c3,c4,c5,c6],[])

