import turtle as tt

tt.shape('turtle')
tt.speed(0)
tt.pu()
tt.goto(0, -50)
tt.pd()
tt.color('Yellow')


def semicircle (f):
    i = 0
    while i < 150 :
        tt.fd( 0.7 * f )
        tt.lt( 180- ((300-2) * 180 / 300))
        i += 1
def circle(f):
    i = 0
    tt.pu()
    tt.pd()
    while i < 300 :
        tt.fd( 0.7 * f )
        tt.lt( 180- ((300-2) * 180 / 300))
        i += 1


tt.begin_fill(), circle(2), tt.end_fill()
tt.pu(), tt.goto(25, 30), tt.color('blue'), tt.begin_fill(), circle(0.3), tt.end_fill()
tt.pu(), tt.goto(-25, 30), tt.begin_fill(), circle(0.3), tt.end_fill(), tt.pu()
tt.goto(8, 14), tt.pd(),  tt.lt(90), tt.color('black'), tt.begin_fill(), semicircle(0.2), tt.fd(20), semicircle(0.2), tt.fd(20), tt.end_fill()
tt.width(6), tt.lt(180), tt.color('red'), tt.pu(), tt.goto(-39, 0), tt.pd(), semicircle(1.2)


    
