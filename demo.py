import glfw
import OpenGL
import time
from OpenGL.GL import *

def main():
    demo = Demo()
    demo.run()

class Demo:
    windowID = None

    def run(this):
        this.init()
        while not glfw.window_should_close(this.windowID): 
            this.update()
            this.render()
        
    def init(this):
        if not glfw.init():
            return
        this.windowID = glfw.create_window(640, 480, "Test", None, None)
        glfw.show_window(this.windowID)
        glfw.make_context_current(this.windowID)
        glfw.swap_interval(1)
        glClearColor(0, 0, 0, 1);


    def update(this):
        glfw.poll_events()

    def render(this):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glfw.swap_buffers(this.windowID)


if __name__ == '__main__':
    main()
    
