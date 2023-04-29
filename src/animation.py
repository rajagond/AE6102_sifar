import numpy as np
from mayavi import mlab
from traits.api import HasTraits, Range, Instance, Button
from traitsui.api import View, Item, HGroup
from mayavi.core.ui.api import MlabSceneModel, SceneEditor, MayaviScene


class Animation(HasTraits):
    scene = Instance(MlabSceneModel, ())    
    inline_animate_button = Button('Animate Inline')
    crossline_animate_button = Button('Animate Crossline')
    depth_animate_button = Button('Animate Depth')

    animation_view = View(
        Item('scene', editor=SceneEditor(scene_class=MayaviScene), show_label=False),
        HGroup(
            Item('inline_animate_button', show_label=False),
            label='Inline (X-Axis)'
        ),
        HGroup(
            Item('crossline_animate_button', show_label=False),
            label='Crossline (Y-Axis)'
        ),
        HGroup(
            Item('depth_animate_button', show_label=False),
            label='Depth (Z-Axis)'
        ),
        title='Animation',
        resizable=True,
        buttons=['Cancel'],
    )

    def __init__(self, data):
        HasTraits.__init__(self)
        self.seismicdata = data
        self.time = -1

    def _inline_animate_button_fired(self):
        if self.seismicdata.shape[0] == 1:
            print("Cannot animate inline, only one inline slice")
            return
        self.inline_animate()

    def _crossline_animate_button_fired(self):
        if self.seismicdata.shape[1] == 1:
            print("Cannot animate crossline, only one crossline slice")
            return
        self.crossline_animate()

    def _depth_animate_button_fired(self):
        if self.seismicdata.shape[2] == 1:
            print("Cannot animate depth, only one depth slice")
            return
        self.depth_animate()

    @mlab.animate(delay=100)
    def inline_animate(self):
        self.time = 0
        while True:
            self.time += 1
            if self.time == self.seismicdata.shape[0]:
                self.time = 0
            self.scene.mlab.clf()
            self.scene.mlab.imshow(self.seismicdata[self.time, :, :])
            yield

    @mlab.animate(delay=100)
    def crossline_animate(self):
        self.time = 0
        while True:
            self.time += 1
            if self.time == self.seismicdata.shape[1]:
                self.time = 0
            self.scene.mlab.clf()
            self.scene.mlab.imshow(self.seismicdata[:, self.time, :])
            yield
    
    @mlab.animate(delay=100)
    def depth_animate(self):
        self.time = 0
        while True:
            self.time += 1
            if self.time == self.seismicdata.shape[2]:
                self.time = 0
            self.scene.mlab.clf()
            self.scene.mlab.imshow(self.seismicdata[:, :, self.time])
            yield
