import taichi as ti
import numpy as np
import plb
import plb.engine.renderer
from plb.engine.primitive.primitives import Primitives
from plb.config import load
from plb.engine.renderer import Renderer
from plb.engine.primitive.primitives import Sphere

if __name__ == "__main__":
    ti.init()

    #cfg = load()
    #sphere1 = Sphere(radius=0.2)
    #sphere2 = Sphere(radius=0.1)
    #sphere3 = Sphere(radius=0.1)

    #render = Renderer(cfg.RENDERER, (sphere1, sphere2, sphere3))

    #sphere1.set_state(0, [0.1, 0.2, 0.2, 1, 0, 0,0])
    #sphere2.set_state(0, [0.9, 0.2, 0.2, 1, 0, 0,0])
    #sphere3.set_state(0, [0.5, 0.8, 0.6, 1, 0, 0,0])

    #x = np.random.random((10000, 3)) * 0.2 + np.array([0.5, 0.5, 0.5])

    #render.set_particles(x, np.zeros(10000,) + (255<<8) + 255)

    #img = render.render_frame(40, shape=1, primitive=1, target=0)
    #render.calc_heightmap()


    cfg = plb.envs.env.PlasticineEnv.load_varaints("rollingpin.yml", version=1)
    #cfg = load()

    renderer = plb.engine.renderer.Renderer(cfg.RENDERER)#, primitives=Primitives(cfg.PRIMITIVES))
    renderer.initialize()

    #renderer.build_sdf_from_particles()

    x = np.random.random((10000, 3)) * 0.2 + np.array([0.5, 0.5, 0.5])

    renderer.set_particles(x, np.zeros(10000,) + (255<<8) + 255)


    img = renderer.render_frame(40, shape=1, primitive=0, target=0)

    renderer.foo()

    gui = ti.GUI("window", (512, 512))
    while gui.running:
        gui.set_image(img)
        gui.show()

