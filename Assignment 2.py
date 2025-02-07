def setup():
    size(400, 400)
    background(255)  #white background
    draw_painting()

def draw_painting():
    stroke(0)  #black lines
    stroke_weight(12)
        
#(x, y, width, height) for each rectangle

    #large red square (top-right)
#     fill(223, 66, 48)
    fill(random(0, 255), random(0, 255), random(0, 255))
    rect(120, 0, 280, 280)

    #blue rectangle (bottom-left)
#     fill(76, 103, 179)
    fill(random(0, 255), random(0, 255), random(0, 255))
    rect(0, 280, 120, 120)

    #small yellow square (bottom-right)
#     fill(240, 233, 124)
    fill(random(0, 255), random(0, 255), random(0, 255))
    rect(350, 350, 50, 50)

    #white areas (background)
    fill(255)
    rect(0, 0, 120, 130)  #top-left
    rect(0, 130, 120, 150)  #mid-left
    rect(120, 280, 230, 120)  #bottom-center

    #black thick lines (x, y to x, y)
    stroke_weight(12)
    line(120, 0, 120, 400)  #vertical left line
    line(350, 280, 350, 400)  #vertical right line
    line(0, 280, 400, 280)  #horizontal bottom line
    line(0, 141, 120, 141)  #mid horizontal line
    line(350, 345, 400, 345)  #small bottom-right line
    
def key_pressed(e):
    pressed_key = e.get_key()
    if pressed_key == 's':
        save('Assignment2-Sketch.jpg')

run_sketch()

