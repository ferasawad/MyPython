# define height and width for the draw board.
height = 500
width  = 500

# define the number of soldiers
soldiers = 22
killing_order = 2

"""
define a function called drawPoints to draw the points
corresponding to soldiers and/or labels.
     n: the number of soldiers (n = soldiers)
     r: radius of the point (default = 15)
     R: radius of the circular path (default = 175)
     label: display numbering for soldiers (default = false)
"""

def drawPoint(iter = 0, n = soldiers, r = 15, R = 175, label = True, p_color = green):
    
    # the angle corresponding to each soldier
    theta = iter * TWO_PI / n
        
    # the parametric equation of circle with center
    # (height/2, width/2) and radius R
    x = height / 2 + R * cos(theta)
    y = width / 2 + R * sin(theta)
        
    # draw the points of soldiers with labeling
    fill(76, 153, 0)
    if p_color == red:
        stroke(255,0,0)
        fill(75)
    ellipse(x,y,r,r)
    if label == True:
        x = x + 35 * cos(theta)
        y = y + 35 * sin(theta)
        textSize(20)
        fill(255, 255, 51)
        text(iter+1, x-10, y+10)
        

def setup():
    
    # define the screen size
    size(height, width)
    # define the screen background (BLACK)
    background(75)
    
    for iter in range(soldiers):
        drawPoint(iter)

# define the Josephus function iterator
# Rosetta Code

p = list(range(soldiers))
k = killing_order
i, j = 0, 0
seq = []

def draw():
    global i, j
    frameRate(5)
    saveFrame("fawad-####.jpg")
    if len(p) > 0:
        j = (j+k-1) % len(p)
        i = p.pop(j)
        seq.append(i+1)
        if len(seq) < soldiers:
            drawPoint(iter = i, p_color=red)
    else:
        noLoop()
        print 'The number of soldiers:', soldiers
        print 'The order of killing:', killing_order
        print 'The soldiers killed in the following sequence:\n', seq[:-1]
        print "The Survived soldier: ", seq[-1]
