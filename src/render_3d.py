import numpy as np

from traits.api import HasTraits, Instance, Array, \
    on_trait_change
from traitsui.api import View, Item, VGroup, Group, HGroup

from tvtk.api import tvtk
from tvtk.pyface.scene import Scene

from mayavi import mlab
from mayavi.core.api import PipelineBase, Source
from mayavi.core.ui.api import SceneEditor, MayaviScene, \
                                MlabSceneModel

class Display3D(HasTraits):
    scene3d = Instance(MlabSceneModel, ())

    view = View(
       Item('scene3d', editor=SceneEditor(scene_class=MayaviScene),
             height=600, width=800, show_label=False),
    )

    def __init__(self, data):
        HasTraits.__init__(self)
        self.seismic_data = data

    @on_trait_change('scene3d.activated')
    def display_scene3d(self):
        source = mlab.pipeline.scalar_field(self.seismic_data)
        mlab.pipeline.volume(source, figure=self.scene3d.mayavi_scene)
        mlab.axes(xlabel='inline', ylabel='crossline', zlabel='depth', nb_labels=5)
        mlab.outline()
        self.scene3d.mlab.view(40, 50)
        
