from traits.api import HasTraits, Range, Instance, on_trait_change, Array
from traitsui.api import View, Item, HGroup
from tvtk.pyface.scene_editor import SceneEditor
from mayavi.tools.mlab_scene_model import \
    MlabSceneModel
from mayavi.core.ui.mayavi_scene import MayaviScene
import numpy as np

seismic_data = np.load('../data/test.npy')


class ContourColoring(HasTraits):
    red = Range(0., 1., 0.5)
    green = Range(0., 1., 0.5)
    blue = Range(0., 1., 0.5)
    scene = Instance(MlabSceneModel, ())
    data = Array()

    def __init__(self):
        HasTraits.__init__(self)
        r = self.red
        b = self.blue
        g = self.green
        self.plot = self.scene.mlab.contour3d(self.data,
                                              color=(r, g, b))

    @on_trait_change('red,blue,green')
    def update_plot(self):
        r = self.red
        b = self.blue
        g = self.green
        self.plot.mlab_source.trait_set(scalars=(r, g, b))

    # the layout of the dialog created
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                HGroup(
        '_', 'R', 'G', 'B',
    ),
        resizable=True,
        title='Contour Coloring',
    )


coloring = ContourColoring(data=seismic_data)
coloring.configure_traits()
