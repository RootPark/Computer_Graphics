import glfw
from OpenGL.GL import *
import numpy as np
from OpenGL.GLU import *
import math

#First set angle
angleAzimuth = np.radians(45)
angleElevation = np.radians(45)

projectionMode = False

left = False
right = False

#First set distance
distance = 10
orthoPoint = 1

mouse_x = 0
mouse_y = 0

rotate_xz = 0
rotate_y = 0

shadingMode = False
solidMode = False

gVertexArraySeparate = None

hierarchicalMode = False


def render():
    global projectionMode, angleAzimuth, angleElevation, distance, rotate_y, rotate_xz, hierarchicalMode, solidMode
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    
    
    if solidMode == False:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glLoadIdentity()
        
    if projectionMode == False:
        gluPerspective(45,1,0.1,50)
        gluLookAt(distance * np.sin(angleAzimuth) * np.cos(angleElevation), distance * np.sin(angleElevation), distance * np.cos(angleAzimuth) * np.cos(angleElevation),0,0,0, 0,1,0)
        
    else:
        glOrtho(-orthoPoint,orthoPoint,-orthoPoint,orthoPoint,-orthoPoint,orthoPoint)
        gluLookAt(.1 * np.sin(angleAzimuth) * np.cos(angleElevation), .1* np.sin(angleElevation), .1*np.cos(angleAzimuth) * np.cos(angleElevation), 0,0,0, 0,1,0)

    glTranslatef(rotate_xz,-rotate_y,-rotate_xz)
    drawFrame()
    drawRectangulerGrid()
    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    
    glEnable(GL_NORMALIZE)  
    glEnable(GL_RESCALE_NORMAL)
    
    glPushMatrix()
    lightPos0 = (10.,10.,10.,1.)
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos0) 
    glPopMatrix()
    
    glPushMatrix()
    lightPos1 = (-5.,-7.,-5.,1.)
    glLightfv(GL_LIGHT1, GL_POSITION, lightPos1)
    glPopMatrix()
    
    
    lightColor0 = (1.,0.,0.,1.)
    lightColor1 = (0.,1.,0.,1.)
    ambientLightColor = (.1,.1,.1,1.)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightColor0)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lightColor0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLightColor)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, lightColor1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, lightColor1)
    glLightfv(GL_LIGHT1, GL_AMBIENT, ambientLightColor)
    
    if hierarchicalMode == False:
        objectColor = (0.5,0.5,0.5,1.)
        specularObjectColor = (1.,1.,1.,1.)
        glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE,objectColor)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SHININESS,10)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR,specularObjectColor)
        if gVertexArraySeparate is not None:
            drawObject()
    else:
        t = glfw.get_time()
        
        
        #cake
        objectColor = (1,1,1,1)
        specularObjectColor = (1.,1.,1.,1.)
        glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE,objectColor)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SHININESS,10)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR,specularObjectColor)
        
        drop_callback_path("./objEX/cake.obj")
        glPushMatrix()
        glTranslatef(0.,0.1,0.)
        glColor3ub(255,255,255)
        drawObject()
        
        #person
        glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE,objectColor)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SHININESS,10)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR,specularObjectColor)
        
        drop_callback_path("./objEX/human.obj")
        glPushMatrix()
        glScale(0.5,0.5,0.5)
        glRotate(t*(180/np.pi),0,1,0)
        glTranslate(10,0,0)
        drawObject()
        glPopMatrix()
        
        #number 5
        glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE,objectColor)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SHININESS,10)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR,specularObjectColor)
        
        drop_callback_path("./objEX/number5.obj")
        glPushMatrix()
        glScale(0.1,0.1,0.1)
        glRotate(t*(180/np.pi),0,1,0)
        glTranslate(6,5,0)
        drawObject()
        
        
        # number 1
        glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE,objectColor)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SHININESS,10)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR,specularObjectColor)
        
        drop_callback_path("./objEX/number1.obj")
        glPushMatrix()
        glRotate(90 + 45 * np.sin(2 * t),45,1,0)
        glTranslate(2,2,2)
        drawObject()
        glPopMatrix()


        #number 8
        glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE,objectColor)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SHININESS,10)
        glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR,specularObjectColor)
        
        drop_callback_path("./objEX/number8.obj")
        glPushMatrix()
        glRotate(90 + 45 * np.sin(2 * t),45,1,0)
        glTranslate(4,4,4)
        drawObject()
        glPopMatrix()
        
        glPopMatrix()
        

    
def drawObject():
    global gVertexArraySeparate
    VARR = gVertexArraySeparate
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glNormalPointer(GL_FLOAT, 6*VARR.itemsize, VARR)
    glVertexPointer(3, GL_FLOAT, 6*VARR.itemsize, ctypes.c_void_p(VARR.ctypes.data + 3*VARR.itemsize))
    glDrawArrays(GL_TRIANGLES, 0, int(VARR.size/6))
    
    
def drawRectangulerGrid():
    glBegin(GL_LINES)
    glColor3ub(255,255,255)
    for i in range(50):
        glVertex3fv(np.array([(i+1)*0.2,0.,10]))
        glVertex3fv(np.array([(i+1)*0.2,0.,-10]))
        glVertex3fv(np.array([10,0.,(i+1)*0.2]))
        glVertex3fv(np.array([-10,0.,(i+1)*0.2]))
    for i in range(50):
        glVertex3fv(np.array([-(i+1)*0.2,0.,10]))
        glVertex3fv(np.array([-(i+1)*0.2,0.,-10]))
        glVertex3fv(np.array([10,0.,-(i+1)*0.2]))
        glVertex3fv(np.array([-10,0.,-(i+1)*0.2]))
    glEnd()
        
    
def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([-10.,0.,0.]))
    glVertex3fv(np.array([10.,0.,0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0.,-10.,0.]))
    glVertex3fv(np.array([0.,10.,0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0.,0.,-10.]))
    glVertex3fv(np.array([0.,0.,10.]))
    glEnd()
    
    
#When v key press, change projection mode 
def key_callback(window, key, scancode, action, mods):
    global projectionMode, shadingMode, solidMode, hierarchicalMode
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_V:
            projectionMode = not projectionMode
        if key == glfw.KEY_S:
            shadingMode = not shadingMode
        if key == glfw.KEY_Z:
            solidMode = not solidMode
        if key == glfw.KEY_H:
            hierarchicalMode = not hierarchicalMode
            gVertexArraySeparate = None
            
            
            
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
        distance -= .5
        orthoPoint -= .5
    elif yoffset == -1:
        distance += .5
        orthoPoint += .5

def drop_callback(window, path):
    global gVertexArraySeparate
    file = open(path[0])
    
    vertex_arr = []
    vertex_normal_arr = []
    result = []
    
    count3 = 0
    count4 = 0
    countn = 0
    
    while True:
        line = file.readline()
        if not line:
            break
        
        if line.startswith('#'):
            continue
        
        splitedLine = line.split()
        
        if len(splitedLine) == 0:
            continue
        
        if splitedLine[0] == 'v':
            vertex_arr.append((float(splitedLine[1]),float(splitedLine[2]),float(splitedLine[3])))
            
        elif splitedLine[0] == 'vn':
            vertex_normal_arr.append((float(splitedLine[1]),float(splitedLine[2]),float(splitedLine[3])))
                        
        elif splitedLine[0] == 'f':
            if len(splitedLine) == 4:
                count3 += 1
            elif len(splitedLine) == 5:
                count4 += 1
            elif len(splitedLine) > 5:
                countn += 1
                
            for i in range(1, len(splitedLine)-1):
                element = splitedLine[1].split('/')
                result.append(vertex_normal_arr[int(element[2])-1])
                result.append(vertex_arr[int(element[0])-1])
                for j in range(0,2):
                    element = splitedLine[i+j].split('/')
                    result.append(vertex_normal_arr[int(element[2])-1])
                    result.append(vertex_arr[int(element[0])-1])
        else:
            continue
        
    file.close()
    gVertexArraySeparate = np.array(result, 'float32')
    
    print(file)
        
    print("File Name : ",str(path[0].split('/')[-1]))
    print("Total number of Faces : ",len(vertex_normal_arr))
    print("Number of faces with 3 vertices : ",count3)
    print("Number of faces with 4 vertices : ",count4)
    print("Number of faces with more than 4 vertices : ",countn)
    

def drop_callback_path(path):
    global gVertexArraySeparate
    file = open(path, "r")
    
    vertex_arr = []
    vertex_normal_arr = []
    result = []
    
    while True:
        line = file.readline()
        if not line:
            break
        
        if line.startswith('#'):
            continue
        
        splitedLine = line.split()
        
        if len(splitedLine) == 0:
            continue
        
        if splitedLine[0] == 'v':
            vertex_arr.append((float(splitedLine[1]),float(splitedLine[2]),float(splitedLine[3])))
            
        elif splitedLine[0] == 'vn':
            vertex_normal_arr.append((float(splitedLine[1]),float(splitedLine[2]),float(splitedLine[3])))
            
        elif splitedLine[0] == 'f':

            for i in range(1, len(splitedLine)-2):
                element = splitedLine[1].split('/')
                result.append(vertex_normal_arr[int(element[2])-1])
                result.append(vertex_arr[int(element[0])-1])
                for j in range(0,2):
                    element = splitedLine[i+j].split('/')
                    result.append(vertex_normal_arr[int(element[2])-1])
                    result.append(vertex_arr[int(element[0])-1])
        else:
            continue
        
    file.close()
    gVertexArraySeparate = np.array(result,'float32')
    
def main():
    if not glfw.init():
        return
    window = glfw.create_window(1000,1000,"ClassAssignment2", None,None)
    
    if not window:
        glfw.terminate()
        return
    
    glfw.set_key_callback(window, key_callback)
    glfw.set_mouse_button_callback(window, button_callback)
    glfw.set_cursor_pos_callback(window, cursor_callback)
    glfw.set_scroll_callback(window,scroll_callback)
    glfw.set_drop_callback(window,drop_callback)
    
    glfw.make_context_current(window)
    glfw.swap_interval(1)
    

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)
        
    glfw.terminate()

if __name__ == "__main__":
    main()
    