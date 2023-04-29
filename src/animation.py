import numpy as np
from mayavi import mlab
from traits.api import HasTraits, Range, Instance, Button, Bool
from traitsui.api import View, Item, HGroup
from mayavi.core.ui.api import MlabSceneModel, SceneEditor, MayaviScene
from os.path import join
from os import makedirs, remove
import imageio


class Animation(HasTraits):
    animation_scene = Instance(MlabSceneModel, ())    
    inline_animate_button = Button('Animate')
    crossline_animate_button = Button('Animate')
    depth_animate_button = Button('Animate')
    save_inline_animation_button = Button('Save Inline Animation')
    save_crossline_animation_button = Button('Save Crossline Animation')
    save_depth_animation_button = Button('Save Depth Animation')
    loading = Bool(False)

    animation_view = View(
        Item('animation_scene', 
            editor=SceneEditor(scene_class=MayaviScene), 
            show_label=False),
        HGroup(
            Item('inline_animate_button', show_label=False),
            label='Inline Animation (X-Axis)',
            visible_when='loading == False'
        ),
        HGroup(
            Item('crossline_animate_button', show_label=False),
            label='Crossline (Y-Axis)',
            visible_when='loading == False'
        ),
        HGroup(
            Item('depth_animate_button', show_label=False),
            label='Depth (Z-Axis)',
            visible_when='loading == False'
        ),
        HGroup(
            Item('save_inline_animation_button', show_label=False),
            Item('save_crossline_animation_button', show_label=False),
            Item('save_depth_animation_button', show_label=False),
            visible_when='loading == False'
        ),
        Item('loading', show_label=True),
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

    @mlab.animate(delay=30)
    def inline_animate(self):
        self.time = 0
        while True:
            self.time += 1
            if self.time == self.seismicdata.shape[0]:
                self.time = 0
            self.animation_scene.mlab.clf()
            self.animation_scene.mlab.imshow(self.seismicdata[self.time, :, :])
            yield

    @mlab.animate(delay=30)
    def crossline_animate(self):
        self.time = 0
        while True:
            self.time += 1
            if self.time == self.seismicdata.shape[1]:
                self.time = 0
            self.animation_scene.mlab.clf()
            self.animation_scene.mlab.imshow(self.seismicdata[:, self.time, :])
            yield
    
    @mlab.animate(delay=30)
    def depth_animate(self):
        self.time = 0
        while True:
            self.time += 1
            if self.time == self.seismicdata.shape[2]:
                self.time = 0
            self.animation_scene.mlab.clf()
            self.animation_scene.mlab.imshow(self.seismicdata[:, :, self.time])
            yield

    def _save_inline_animation_button_fired(self):
        makedirs('../animations', exist_ok=True)
        print("Saving inline animation")
        print("Creating Frames......")

        self.loading = True
        writer = imageio.get_writer(join('../animations', 'inline.mp4'), fps=15)
        for i in range(self.seismicdata.shape[0]):
            self.animation_scene.mlab.clf()
            self.animation_scene.mlab.imshow(self.seismicdata[i, :, :])
            self.animation_scene.mlab.savefig(join('../animations', 'inline_%d.png' % i))
            writer.append_data(imageio.imread(join('../animations', 'inline_%d.png' % i)))
            remove(join('../animations', 'inline_%d.png' % i))

        writer.close()
        self.loading = False
        print("Done saving inline animation")

    def _save_crossline_animation_button_fired(self):
        makedirs('../animations', exist_ok=True)
        print("Saving crossline animation")
        print("Creating Frames......")

        self.loading = True
        writer = imageio.get_writer(join('../animations', 'crossline.mp4'), fps=15)
        for i in range(self.seismicdata.shape[1]):
            self.animation_scene.mlab.clf()
            self.animation_scene.mlab.imshow(self.seismicdata[:, i, :])
            self.animation_scene.mlab.savefig(join('../animations', 'crossline_%d.png' % i))
            writer.append_data(imageio.imread(join('../animations', 'crossline_%d.png' % i)))
            remove(join('../animations', 'crossline_%d.png' % i))

        writer.close()
        self.loading = False
        print("Done saving crossline animation")

    def _save_depth_animation_button_fired(self):
        makedirs('../animations', exist_ok=True)
        print("Saving depth animation")
        print("Creating Frames......")

        self.loading = True
        writer = imageio.get_writer(join('../animations', 'depth.mp4'), fps=15)
        for i in range(self.seismicdata.shape[2]):
            self.animation_scene.mlab.clf()
            self.animation_scene.mlab.imshow(self.seismicdata[:, :, i])
            self.animation_scene.mlab.savefig(join('../animations', 'depth_%d.png' % i))
            writer.append_data(imageio.imread(join('../animations', 'depth_%d.png' % i)))
            remove(join('../animations', 'depth_%d.png' % i))
        
        writer.close()
        self.loading = False
        print("Done saving depth animation")