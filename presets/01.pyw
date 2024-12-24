from direct.gui.DirectGui import *
from panda3d.core import (
    LVecBase3f,
    LPoint3f,
    LVecBase4f,
    LPoint4f,
    ConfigVariableString,
)
ConfigVariableString("notify-level", "fatal").setValue("fatal")

class frame:
    def build(self):
        ...

        self.obj0 = DirectFrame(
            parent=self.aspect2d,
            pos=LPoint3f(0, 0, 0),
            scale=LVecBase3f(0.241852, 0, 0.241852),
            color=(1, 1, 1, 1),
            relief=None,
            geom=None,
            image=self.loader.loadTexture("01/textures/frame2.png"),
        )

        self.obj2 = DirectFrame(
            parent=self.aspect2d,
            pos=LPoint3f(-0.56, 0, 0.48),
            scale=LVecBase3f(0.241852, 0, 0.241852),
            color=(1, 1, 1, 1),
            relief=None,
            geom=None,
            image=self.loader.loadTexture("01/textures/frame2.png"),
        )


if __name__ == "__main__":
    from direct.showbase.ShowBase import ShowBase

    base = ShowBase()
    base.setBackgroundColor(0, 0, 0, 1)
    base.accept("q", exit)
    frame.build(base)
    base.run()
