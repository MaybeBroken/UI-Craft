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

        self.obj0 = DirectButton(
            parent=self.aspect2d,
            pos=LPoint3f(-0.33, 0, 0.11),
            scale=LVecBase3f(0.0974074, 0, 0.0974074),
            color=(1, 1, 1, 1),
            relief=None,
            geom=None,
            image=self.loader.loadTexture("01/textures/button1.png"),
        )


if __name__ == "__main__":
    from direct.showbase.ShowBase import ShowBase

    base = ShowBase()
    base.setBackgroundColor(0, 0, 0, 1)
    base.accept("q", exit)
    frame.build(base)
    base.run()
