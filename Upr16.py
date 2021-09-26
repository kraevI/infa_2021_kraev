import turtle as tt
tt.shape('turtle')
tt.color('Coral')
tt.width(3)
tt.pu()
tt.bk(220)
tt.pd()
def zero():
    tt.fd(40), tt.lt(90), tt.fd(80), tt.lt(90), tt.fd(40), tt.lt(90), tt.fd(80), tt.lt(90), tt.fd(40)
def one():
    tt.pu(), tt.lt(90), tt.fd(40), tt.pd(), tt.rt(45), tt.fd(40* 2**0.5), tt.rt(135), tt.fd(80), tt.lt(90)
def two():
    tt.pu(), tt.lt(90), tt.fd(80), tt.pd(), tt.rt(90), tt.fd(40), tt.rt(90), tt.fd(40), tt.rt(45), tt.fd(40* 2**0.5), tt.lt(135), tt.fd(40)
def three():
    tt.pu(), tt.lt(90), tt.fd(80), tt.pd(), tt.rt(90), tt.fd(40), tt.rt(135),tt.fd(40* 2**0.5), tt.lt(135), tt.fd(40), tt.rt(135), tt.fd(40* 2**0.5),
    tt.pu(), tt.lt(135), tt.fd(40)
def four():
    tt.pu(), tt.lt(90), tt.fd(80), tt.lt(180), tt.pd(), tt.fd(40), tt.lt(90), tt.fd(40), tt.lt(90), tt.fd(40), tt.rt(180), tt.fd(80), tt.lt(90)
def five():
    tt.fd(40), tt.lt(90), tt.fd(40), tt.lt(90), tt.fd(40), tt.rt(90), tt.fd(40), tt.rt(90), tt.fd(40), tt.pu(), tt.rt(90), tt.fd(80), tt.lt(90)
def six():
    tt.fd(40), tt.lt(90), tt.fd(40), tt.lt(90), tt.fd(40), tt.lt(90), tt.fd(40), tt.bk(40), tt.lt(135), tt.fd(40* 2**0.5), tt.pu(), tt.rt(135)
    tt.fd(80), tt.lt(90)
def seven():
    tt.lt(90), tt.fd(40), tt.rt(45), tt.fd(40* 2**0.5), tt.lt(135), tt.fd(40), tt.pu(), tt.lt(120), tt.fd((40**2 + 80**2)**0.5), tt.lt(60)
def eight():
    tt.fd(40), tt.lt(90), tt.fd(80), tt.lt(90), tt.fd(40), tt.lt(90), tt.fd(80), tt.bk(40), tt.lt(90), tt.fd(40), tt.rt(90), tt.fd(40), tt.lt(90)
def nine():
    tt.lt(45), tt.fd(40* 2**0.5), tt.lt(45), tt.fd(40), tt.lt(90), tt.fd(40), tt.lt(90), tt.fd(40), tt.lt(90), tt.fd(40), tt.pu()
    tt.rt(90), tt.fd(40), tt.lt(90)
def number(n):
    if n==0: zero()
    elif n==1: one()
    elif n==2: two()
    elif n==3: three()
    elif n==4: four()
    elif n==5: five()
    elif n==6: six()
    elif n==7: seven()
    elif n==8: eight()
    elif n==9: nine()
A = list(map(int, input().split()))
for i in A:
    number(i)
    tt.pu()
    tt.fd(40)
    tt.pd()
