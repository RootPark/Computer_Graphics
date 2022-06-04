import glfw
from OpenGL.GL import *
import numpy as np

gComposedM = np.array([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])

def render():
	pass
	
def key_callback(window, key, scancode, action, mods):
	global gComposedM
	if key == glfw.KEY_W:#Scale by 0.9 times in x direction
		if action == glfw.PRESS or action == glfw.REPEAT:
			gComposedM = np.array([[0.9,0.,0.],[0.,1.,0.],[0.,0.,1.]]) @gComposedM
			
	if key == glfw.KEY_E:#Scale by 1.1 times in x direction
		if action == glfw.PRESS or action == glfw.REPEAT:
			gComposedM = np.array([[1.1,0.,0.],[0.,1.,0.],[0.,0.,1.]]) @gComposedM
			
	if key == glfw.KEY_S:#Rotate by 10 degrees counterclockwise
		if action == glfw.PRESS or action == glfw.REPEAT:
			gComposedM = np.array([[np.cos(10*np.pi/180),-np.sin(10*np.pi/180),0.0],[np.sin(10*np.pi/180),np.cos(10*np.pi/180),0.0],[0.0,0.0,1.0]]) @gComposedM
			
	if key == glfw.KEY_D:#Rotate by 10 degrees clockwise
		if action == glfw.PRESS or action == glfw.REPEAT:
			gComposedM = np.array([[np.cos(-10*np.pi/180),-np.sin(-10*np.pi/180),0.0],[np.sin(-10*np.pi/180),np.cos(-10*np.pi/180),0.0],[0.0,0.0,1.0]]) @gComposedM
			
	if key == glfw.KEY_X:#Shear by a factor of -0.1 in x direction
		if action == glfw.PRESS or action == glfw.REPEAT:
			gComposedM = np.array([[1.,-0.1,0.],[0.,1.,0.],[0.,0.,1.]]) @gComposedM
			
	if key == glfw.KEY_C:#Shear by a factor of 0.1 in x direction
		if action == glfw.PRESS or action == glfw.REPEAT:
			gComposedM = np.array([[1.,0.1,0.],[0.,1.,0.],[0.,0.,1.]]) @gComposedM
			
	if key == glfw.KEY_R:#Reflection across x axis
		if action == glfw.PRESS or action == glfw.REPEAT:
			gComposedM = np.array([[1.,0.,0.],[0.,-1.,0.],[0.,0.,-1.]]) @gComposedM
			
	if key == glfw.KEY_1:#Reset
		if action == glfw.PRESS or action == glfw.REPEAT:
			gComposedM= np.array([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])
	
def main():
	if not glfw.init():
		return
	window = glfw.create_window(480,480, "2018008313",None,None)
	
	if not window:
		glfw.terminate()
		return
	
	glfw.set_key_callback(window,key_callback)
	
	glfw.make_context_current(window)
	
	while not glfw.window_should_close(window):
		
		glfw.poll_events()
				
		render(gComposedM);
		
		glfw.swap_buffers(window)
		
	glfw.terminate()
	

def render(T):
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
	
	#draw triangle
	glBegin(GL_TRIANGLES)
	glColor3ub(255,255,255)
	glVertex2fv( (T @ np.array([.0,.5,1.])) [:-1] )
	glVertex2fv( (T @ np.array([.0,.0,1.])) [:-1] )
	glVertex2fv( (T @ np.array([.5,.0,1.])) [:-1] )
	glEnd()
	
	
if __name__ =="__main__":
	main()