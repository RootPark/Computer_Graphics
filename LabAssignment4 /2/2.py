import glfw
from OpenGL.GL import *
import numpy as np

def render(M):
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	
	#draw coordinate
	glBegin(GL_LINES)
	glColor3ub(255,0,0)
	glVertex2fv(np.array([0.,0.]))
	glVertex2fv(np.array([1.,0.]))
	glColor3ub(0,255,0)
	glVertex2fv(np.array([0.,0.]))
	glVertex2fv(np.array([0.,1.]))
	glEnd()
	
	glColor3ub(255,255,255)
	
	#draw point p
	glBegin(GL_POINTS)
	p = (M @ np.array([0.5,0.,1.]))[:2]
	glVertex2fv(p)
	glEnd()
	
	#draw vector v
	glBegin(GL_LINES)
	v = (M @ np.array([0.5,0.,0.]))[:2]
	glVertex2fv(v)
	glVertex2fv(np.array([0.,0.]))
	glEnd()
	
def main():
	global M
	if not glfw.init():
		return
	window = glfw.create_window(480,480, "2018008313", None,None)
	
	if not window:
		glfw.terminate()
		return
	
	glfw.make_context_current(window)
	
	while not glfw.window_should_close(window):
		glfw.poll_events()
		
		t = glfw.get_time()
		M = np.array([[np.cos(t),-np.sin(t),np.cos(t)*0.5],[np.sin(t),np.cos(t),np.sin(t)*0.5],[0.,0.,1.]])
		render(M)
		
		glfw.swap_buffers(window)
		
	glfw.terminate()
	
if __name__ == "__main__":
	main()