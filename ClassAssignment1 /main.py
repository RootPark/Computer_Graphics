import glfw
from OpenGL.GL import *
import numpy as np
from OpenGL.GLU import *

#First set angle
angleAzimuth = np.radians(45)
angleElevation = np.radians(45)

projectionMode = False

left = False
right = False

#First set distance
distance = 2
orthoPoint = 1

mouse_x = 0
mouse_y = 0

rotate_xz = 0
rotate_y = 0


def render():
    global projectionMode, angleAzimuth, angleElevation, distance, rotate_y, rotate_xz
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )

    glLoadIdentity()
    
    #Choose projection mode
    #First start with perspective
    if projectionMode == False:
        gluPerspective(45,1,0.1,10)
        gluLookAt(distance * np.sin(angleAzimuth) * np.cos(angleElevation), distance * np.sin(angleElevation), distance * np.cos(angleAzimuth) * np.cos(angleElevation),0,0,0, 0,.1,0)
    else:
        glOrtho(-orthoPoint,orthoPoint,-orthoPoint,orthoPoint,-orthoPoint*2,orthoPoint*2)
        gluLookAt(.1 * np.sin(angleAzimuth) * np.cos(angleElevation), .1* np.sin(angleElevation), .1*np.cos(angleAzimuth) * np.cos(angleElevation), 0,0,0, 0,.1,0)

    glTranslatef(rotate_xz,-rotate_y,-rotate_xz)
    drawFrame()
    drawRectangulerGrid()
    drawUnitCube()


def drawUnitCube():
    glBegin(GL_QUADS)
    glColor3ub(255,100,200)
    glVertex3f(0.2, 0.2, -0.2)
    glVertex3f(-0.2, 0.2, -0.2)
    glVertex3f(-0.2, 0.2, 0.2)
    glVertex3f(0.2, 0.2, 0.2)
    
    glVertex3f(0.2, -0.2, 0.2)
    glVertex3f(-0.2, -0.2, 0.2)
    glVertex3f(-0.2, -0.2, -0.2)
    glVertex3f(0.2, -0.2, -0.2)
    
    glVertex3f(0.2, 0.2, 0.2)
    glVertex3f(-0.2, 0.2, 0.2)
    glVertex3f(-0.2, -0.2, 0.2)
    glVertex3f(0.2, -0.2, 0.2)
    
    glVertex3f(0.2, -0.2, -0.2)
    glVertex3f(-0.2, -0.2, -0.2)
    glVertex3f(-0.2, 0.2, -0.2)
    glVertex3f(0.2, 0.2, -0.2)
    
    glVertex3f(-0.2, 0.2, 0.2)
    glVertex3f(-0.2, 0.2, -0.2)
    glVertex3f(-0.2, -0.2, -0.2)
    glVertex3f(-0.2, -0.2, 0.2)
    
    glVertex3f(0.2, 0.2, -0.2)
    glVertex3f(0.2, 0.2, 0.2)
    glVertex3f(0.2, -0.2, 0.2)
    glVertex3f(0.2, -0.2, -0.2)
    glEnd()
    
    
def drawRectangulerGrid():
    glBegin(GL_LINES)
    glColor3ub(255,255,255)
    for i in range(10):
        glVertex3fv(np.array([(i+1)*0.1,0.,1.0]))
        glVertex3fv(np.array([(i+1)*0.1,0.,-1.0]))
        glVertex3fv(np.array([1.0,0.,(i+1)*0.1]))
        glVertex3fv(np.array([-1.0,0.,(i+1)*0.1]))
    for i in range(10):
        glVertex3fv(np.array([-(i+1)*0.1,0.,1.0]))
        glVertex3fv(np.array([-(i+1)*0.1,0.,-1.0]))
        glVertex3fv(np.array([1.0,0.,-(i+1)*0.1]))
        glVertex3fv(np.array([-1.0,0.,-(i+1)*0.1]))
    glEnd()
        
    
def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([-1.,0.,0.]))
    glVertex3fv(np.array([1.,0.,0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0.,-1.,0.]))
    glVertex3fv(np.array([0.,1.,0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0.,0.,-1.]))
    glVertex3fv(np.array([0.,0.,1.]))
    glEnd()
    
    
    
#When v key press, change projection mode 
def key_callback(window, key, scancode, action, mods):
    global projectionMode
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_V:
            projectionMode = not projectionMode
            
            
            
def cursor_callback(window, xpos, ypos):
    global left, right, angleAzimuth, angleElevation, mouse_x, mouse_y, rotate_xz, rotate_y
    if left == True:
        angleAzimuth += np.radians(-0.5* (xpos - mouse_x) * 0.01)
        angleElevation += np.radians(-0.5* (ypos - mouse_y) * 0.01)
    
    if right == True:
        rotate_xz +=0.001 * (xpos - mouse_x) * 0.01
        rotate_y +=0.001 * (ypos - mouse_y) * 0.01
        

def button_callback(window, button, action, mod):
    global left, right, mouse_x, mouse_y
    if button == glfw.MOUSE_BUTTON_LEFT:
        if action == glfw.PRESS:
            mouse_x, mouse_y = glfw.get_cursor_pos(window)
            left = True
        elif action == glfw.RELEASE:
            left = False
            
    elif button == glfw.MOUSE_BUTTON_RIGHT:
        if action == glfw.PRESS:
            mouse_x, mouse_y =glfw.get_cursor_pos(window)
            right = True
        elif action == glfw.RELEASE:
            right = False

def scroll_callback(window, xoffset, yoffset):
    global distance, orthoPoint
    if yoffset == 1:
        distance -= .05
        orthoPoint -= .05
    elif yoffset == -1:
        distance += .05
        orthoPoint += .05


def main():
    if not glfw.init():
        return
    window = glfw.create_window(1000,1000,"ClassAssignment1", None,None)
    
    if not window:
        glfw.terminate()
        return
    
    glfw.set_key_callback(window, key_callback)
    glfw.set_mouse_button_callback(window, button_callback)
    glfw.set_cursor_pos_callback(window, cursor_callback)
    glfw.set_scroll_callback(window,scroll_callback)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
    