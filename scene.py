# Victoria Tisdale
# 2/24/15

from math import pi, sin, cos

from pyglet.gl import *
import pyglet

from shapelib import vec
import shapelib

try:
    # Try and create a window with multisampling (antialiasing)
    config = Config(sample_buffers=1, samples=4, 
                    depth_size=16, double_buffer=True,)
    window = pyglet.window.Window(resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
    # Fall back to no multisampling for old hardware
    window = pyglet.window.Window(resizable=True)

@window.event
def on_resize(width, height):
    # Override the default on_resize handler to create a 3D projection
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60., width / float(height), .1, 1000.)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

def update(dt):
    global rx, ry, rz
    rx += dt * 1
    ry += dt * 80
    rz += dt * 30
    rx %= 360
    ry %= 360
    rz %= 360
pyglet.clock.schedule(update)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    #zoom out
    glTranslatef(0, 0, -20)
    
    #rotate around the z-axis
    glRotatef(0, 0, 0, 1)
    #rotate around the y-axis
    glRotatef(0, 0, 1, 0)
    #rotate around the x-axis
    glRotatef(0, 1, 0, 0)
    
    
    #small trio from right to left
    glPushMatrix()
    glTranslatef(5, 0, 9)
    glRotatef(90, 1, 0, 0)
    mushroom00.draw(0.545, 0.000, 0.545)
    glPopMatrix()


    glPushMatrix()
    glTranslatef(3, -1, 8)
    glRotatef(90, 1, 0, 0)
    mushroom01.draw(0.545, 0.000, 0.645)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(2, 0, 6)
    glRotatef(90, 1, 0, 0)
    mushroom02.draw(0.545, 0.000, 0.545)
    glPopMatrix()
    
    
    #large middle (in back of trio)
    glPushMatrix()
    glTranslatef(5, 14, -40)
    glRotatef(90, 1, 0, 0)
    mushroom03.draw(0.541, 0.169, 0.886)
    glPopMatrix()
    
    
    #large front right
    glPushMatrix()
    glTranslatef(17, 9, -6)
    glRotatef(90, 1, 0, 0)
    mushroom04.draw(0.641, 0.169, 0.886)
    glPopMatrix()
    
    #skinny back
    glPushMatrix()
    glTranslatef(-10, 13, -70)
    glRotatef(90, 1, 0, 0)
    mushroom05.draw(0.402, 0.200, 0.702)
    glPopMatrix()
    
    #large backs from left to right
    glPushMatrix()
    glTranslatef(-25, 33, -80)
    glRotatef(90, 1, 0, 0)
    mushroom07.draw(0.294, 0.000, 0.510)
    glPopMatrix()
    
    
    glPushMatrix()
    glTranslatef(30, 33, -80)
    glRotatef(90, 1, 0, 0)
    mushroom07.draw(0.294, 0.000, 0.410)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(50, 33, -80)
    glRotatef(90, 1, 0, 0)
    mushroom07.draw(0.194, 0.000, 0.310)
    glPopMatrix()

    #large front left
    glPushMatrix()
    glTranslatef(-13, 5, 3)
    glRotatef(90, 1, 0, 0)
    mushroom06.draw(0.641, 0.169, 0.886)
    glPopMatrix()
    
    #little front left
    glPushMatrix()
    glTranslatef(-3, -2, 14)
    glRotatef(90, 1, 0, 0)
    mushroom08.draw(0.641, 0.169, 0.886)
    glPopMatrix()

    #grass
    
    #background grass
    glPushMatrix()
    glTranslatef(-36, -4.5, -40)
    glRotatef(75, 0, 1, 0)
    grass05.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-34, -4.5, -40)
    glRotatef(90, 0, 1, 0)
    grass06.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-33, -4.5, -40)
    glRotatef(55, 0, 1, 0)
    grass05.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-31, -4.5, -40)
    glRotatef(75, 0, 1, 0)
    grass07.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-28, -4.5, -40)
    glRotatef(75, 0, 1, 0)
    grass06.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-26, -4.5, -40)
    glRotatef(55, 0, 1, 0)
    grass06.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-25, -4.5, -40)
    glRotatef(75, 0, 1, 0)
    grass05.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-23, -4.5, -40)
    glRotatef(75, 0, 1, 0)
    grass06.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-21, -4.5, -40)
    glRotatef(55, 0, 1, 0)
    grass07.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-20, -4.5, -40)
    glRotatef(75, 0, 1, 0)
    grass05.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    #-------
    #diagonal grass from left to right

    glPushMatrix()
    glTranslatef(-13, -4.5, -30)
    glRotatef(60, 0, 1, 0)
    grass06.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-5, -3, -4)
    glRotatef(75, 0, 1, 0)
    grass01.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-4, -3, -5)
    glRotatef(75, 0, 1, 0)
    grass00.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-3, -3, -2)
    glRotatef(55, 0, 1, 0)
    grass00.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2, -3, -10)
    glRotatef(35, 0, 1, 0)
    grass01.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1, -3, 0)
    glRotatef(55, 0, 1, 0)
    grass00.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, -3, 0)
    glRotatef(75, 0, 1, 0)
    grass00.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2, -3, 0)
    glRotatef(45, 0, 1, 0)
    grass00.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(2.5, -3, 7)
    glRotatef(65, 0, 1, 0)
    grass03.draw(0.545, 0.9, 0.545)
    glPopMatrix()


    glPushMatrix()
    glTranslatef(3.5, -3, 7.5)
    glRotatef(35, 0, 1, 0)
    grass03.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3, -2, 12)
    glRotatef(55, 0, 1, 0)
    grass02.draw(0.545, 0.9, 0.545)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(3.5, -2.5, 12.5)
    glRotatef(25, 0, 1, 0)
    grass03.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4, -3, 13)
    glRotatef(90, 0, 1, 0)
    grass02.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(5, -3, 12)
    glRotatef(45, 0, 1, 0)
    grass00.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(6, -3, 12)
    glRotatef(45, 0, 1, 0)
    grass02.draw(0.545, 0.9, 0.545)
    glPopMatrix()


    #front grass right to left

    glPushMatrix()
    glTranslatef(-.75, -6.5, 14)
    glRotatef(35, 0, 1, 0)
    grass00.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.5, -5, 14)
    glRotatef(45, 0, 1, 0)
    grass00.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2, -6, 14)
    glRotatef(45, 0, 1, 0)
    grass00.draw(0.545, 0.9, 0.545)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.5, -7, 14)
    glRotatef(25, 0, 1, 0)
    grass00.draw(0.545, 0.9, 0.545)
    glPopMatrix()

def setup():
    # One-time GL setup
    glClearColor(0.678, 0.800, 0.184, 1)
    glColor3f(1, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)

    # Uncomment this line for a wireframe view
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # Simple light setup.  On Windows GL_LIGHT0 is enabled by default,
    # but this is not the case on Linux or Mac, so remember to always 
    # include it.
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    glLightfv(GL_LIGHT0, GL_POSITION, vec(.5, .5, 1, 0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, vec(.5, .5, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(1, 1, 1, 1))
    glLightfv(GL_LIGHT1, GL_POSITION, vec(1, 0, .5, 0))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, vec(.5, .5, .5, 1))
    glLightfv(GL_LIGHT1, GL_SPECULAR, vec(1, 1, 1, 1))

    # glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0.0, 0.5, 0.3, 1))
    # glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0.5, 0.5, 0.5, 1))
    # glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
    # glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)



setup()
# tube = shapelib.ConicalCylinder(64, 2, 1.5, 1)
mushroom00 = shapelib.Mushroom4(.25, 2, 2.5, .25)
mushroom01 = shapelib.Mushroom5(.25, 1, 1.5, .2)
mushroom02 = shapelib.Mushroom3(.25, 2, 2.5, .2)

#large mushroom in background
mushroom03 = shapelib.Mushroom3(4, 20, 20, 4)

mushroom04 = shapelib.Mushroom3(3, 15, 15, 2)

mushroom05 = shapelib.Mushroom3(3, 15, 20, 1)

#massive mushroom in back left
mushroom07 = shapelib.Mushroom3(5, 25, 40, 5)

mushroom06 = shapelib.Mushroom3(3, 10, 15, 2)

mushroom08 = shapelib.Mushroom5(.25, 1.5, 2.5, .35)

grass00 = shapelib.Triangle(1,4)
grass01 = shapelib.Triangle(.75,3.5)
grass02 = shapelib.Triangle(.5,3)
grass03 = shapelib.Triangle(.5,2)
grass05 = shapelib.Triangle(2,8)
grass06 = shapelib.Triangle(2,6)
grass07 = shapelib.Triangle(2,4)


rx = ry = rz = 0
pyglet.app.run()
# glEnd()
