import numpy as np
from tkinter import filedialog as fd
from tkinter import Tk
from traits.api import HasTraits, Button, File, Instance, on_trait_change, Bool
from traitsui.api import View, Item, HGroup
from mayavi.core.ui.api import MlabSceneModel, SceneEditor, MayaviScene
from mayavi.tools.mlab_scene_model import MlabSceneModel
from analysis import *
from numpy_analysis import *
from animation import *

class SEGYAnalysis(HasTraits):

    # File Buttons
    open_file = Button(label='Open file...')
    file_path = File()
    clearFile = Button(label='Clear file')

    # Mlab Scene Model
    scene = Instance(MlabSceneModel, ())

    # Sesismic Data Specific Buttons
    zoom_in_button = Button('Zoom In', show_label=False)
    zoom_out_button = Button('Zoom Out', show_label=False)
    show_group = Bool(False)
    analysis_button = Button(label='Analysis...')
    numpy_analysis_button = Button(label='Numpy Analysis...')
    animation_button = Button(label='Animation...')

    traits_view = View(
        Item('scene', editor=SceneEditor(scene_class=MayaviScene),
             height=600, width=800, show_label=False),
        HGroup(
            'zoom_in_button', 
            'zoom_out_button',
            Item('analysis_button', show_label=False),
            Item('numpy_analysis_button', show_label=False),
            Item('animation_button', show_label=False),
            visible_when='show_group',
        ),
        Item('open_file'),
        Item('file_path', label='Selected file:', style='readonly'),
        Item('clearFile'),
        title='Seismic Data Visualization and Analysis',
        resizable=True,
        buttons=['Cancel'],
    )

    def __init__(self):
        HasTraits.__init__(self)
        self.seismic_data = None

    @on_trait_change('scene.activated')
    def update_plot(self):
        self.scene.mlab.clf()
        self.scene.mlab.test_contour3d()
        print('update_plot')

    def _open_file_fired(self):
        file_path = fd.askopenfilename()
        self.file_path = file_path
        if file_path != '':
            try:
                self.seismic_data = np.load(file_path)
                print(self.seismic_data.shape)
                self.scene.mlab.clf()
                self.scene.mlab.volume_slice(self.seismic_data, slice_index=0, plane_orientation='x_axes')
                self.scene.mlab.volume_slice(self.seismic_data, slice_index=0, plane_orientation='y_axes')
                self.scene.mlab.volume_slice(self.seismic_data, slice_index=0, plane_orientation='z_axes')
                self.show_group = True

            except Exception as e:
                print(e)
                self.scene.mlab.clf()
                self.scene.mlab.test_contour3d()
                self.seismic_data = None
                file_path = File()
                self.show_group = False          

    def _clearFile_fired(self):
        self.seismic_data = None
        self.file_path = ''
        self.scene.mlab.clf()
        self.scene.mlab.test_contour3d()
        self.show_group = False

    def _zoom_in_button_fired(self):
        self.scene.camera.zoom(1.3)
        self.scene.render()

    def _zoom_out_button_fired(self):
        self.scene.camera.zoom(0.7)
        self.scene.render()

    def _analysis_button_fired(self):
        analysis_traits = Analysis(self.seismic_data)
        analysis_traits.configure_traits()

    def _numpy_analysis_button_fired(self):
        numpy_analysis_traits = NumpyAnalysis(self.seismic_data)
        numpy_analysis_traits.configure_traits()

    def _animation_button_fired(self):
        animation_traits = Animation(self.seismic_data)
        animation_traits.configure_traits()

if __name__ == '__main__':

    root = Tk()
    root.withdraw()
    sa = SEGYAnalysis()
    sa.configure_traits()
    root.destroy()