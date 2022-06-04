import glfw
from OpenGL.GL import*

primitive_type = GL_LINE_LOOP

def render():
	pass
	
def key_callback(window,key,scancode,action,mods):
	global primitive_type
	if key==glfw.KEY_1:
		if action==glfw.PRESS or action==glfw.REPEAT:
			primitive_type=GL_POINTS
	if key==glfw.KEY_2:
		if action==glfw.PRESS or action==glfw.REPEAT:
			primitive_type=GL_LINES
	if key==glfw.KEY_3:
		if action==glfw.PRESS or action==glfw.REPEAT:
			primitive_type=GL_LINE_STRIP
	if key==glfw.KEY_4:
		if action==glfw.PRESS or action==glfw.REPEAT:
			primitive_type=GL_LINE_LOOP
	if key==glfw.KEY_5:
		if action==glfw.PRESS or action==glfw.REPEAT:
			primitive_type=GL_TRIANGLES
	if key==glfw.KEY_6:
		if action==glfw.PRESS or action==glfw.REPEAT:
			primitive_type=GL_TRIANGLE_STRIP
	if key==glfw.KEY_7:
		if action==glfw.PRESS or action==glfw.REPEAT:
			primitive_type=GL_TRIANGLE_FAN
	if key==glfw.KEY_8:
		if action==glfw.PRESS or action==glfw.REPEAT:
			primitive_type=GL_QUADS
	if key==glfw.KEY_9:
		if action==glfw.PRESS or action==glfw.REPEAT:
			primitive_type=GL_QUAD_STRIP
	if key==glfw.KEY_0:
		if action==glfw.PRESS or action==glfw.REPEAT:
			primitive_type=GL_POLYGON
	
def main():
	
	if not glfw.init():
		return
	window = glfw.create_window(480,480,"2018008313",None,None)
	
	if not window:
		glfw.terminate()
		return
	
	glfw.set_key_callback(window,key_callback)
	
	glfw.make_context_current(window)
	
	while not glfw.window_should_close(window):
		
		glfw.poll_events()
		
		render(primitive_type)
		
		glfw.swap_buffers(window)
	
	glfw.terminate()
	
def render(T):
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	glBegin(T)
	glVertex2f(-0.5,0.5)
	glVertex2f(-0.5,-0.5)
	glVertex2f(0.5,-0.5)
	glVertex2f(0.5,0.5)
	glEnd()

if __name__ == "__main__":
	main()
		