import glfw
from OpenGL.GL import *
import numpy as np

def render():
	global ls
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	
	#draw coordinates
	glBegin(GL_LINES)
	glColor3ub(255,0,0)
	glVertex2fv(np.array([0.,0.]))
	glVertex2fv(np.array([1.,0.]))
	glColor3ub(0,255,0)
	glVertex2fv(np.array([0.,0.]))
	glVertex2fv(np.array([0.,1.]))
	glEnd()
	
	glColor3ub(255,255,255)
	
	for i in range(len(ls)-1,0,-1):
		if ls[i] == 'Q': # translate by -0.1 in x direction
			glTranslatef(-0.1,0.,0.)
		elif ls[i] == 'E': # translate by 0.1 in x direction
			glTranslatef(0.1,0.,0.)
		elif ls[i] == 'A': # Rotate by 10 degrees counterclockwise
			glRotatef(10,0,0,1)
		elif ls[i] == 'D': # Rotate by 10 degrees clockwise
			glRotatef(-10,0,0,1)
	
	drawTriangle()
	
def drawTriangle():
	glBegin(GL_TRIANGLES)
	glVertex2fv(np.array([0.,.5]))
	glVertex2fv(np.array([0.,0.]))
	glVertex2fv(np.array([.5,0.]))
	glEnd()
	
def key_callback(window,key,scancode,action, mods):
	global ls
	if key == glfw.KEY_Q:
		if action == glfw.PRESS or action == glfw.REPEAT:
			ls.append('Q')
	elif key == glfw.KEY_E:
		if action == glfw.PRESS or action == glfw.REPEAT:
			ls.append('E')
	elif key == glfw.KEY_A:
		if action == glfw.PRESS or action == glfw.REPEAT:
			ls.append('A')
	elif key == glfw.KEY_D:
		if action == glfw.PRESS or action == glfw.REPEAT:
			ls.append('D')
	elif key == glfw.KEY_1:
		if action == glfw.PRESS or action == glfw.REPEAT:
			ls.clear()
	
def main():
	if not glfw.init():
		return
	window = glfw.create_window(480,480, "2018008313", None,None)
	
	if not window:
		glfw.terminate()
		return
	
	glfw.set_key_callback(window,key_callback)
	glfw.make_context_current(window)
	
	while not glfw.window_should_close(window):
		glfw.poll_events()
		
		render()
		
		glfw.swap_buffers(window)
		
	glfw.terminate()
	
if __name__ == "__main__":
	ls = list()
	main()