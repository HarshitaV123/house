import pgzrun

WIDTH=700
HEIGHT=700
TITLE="House"

def draw():
    screen.clear()
    screen.draw.line((200,100),(100,250),"pink")
    screen.draw.line((200,100),(300,250),"blue")
    screen.draw.line((300,250),(100,250),"green")
    rect=Rect((100,250),(200,300))
    screen.draw.rect(rect,"purple")
    screen.draw.line((100,500),(300,500),"purple")



pgzrun.go()


