'''
GUI application using traitsui to display a plot from file input
'''

import numpy as np
from tkinter import filedialog as fd
from tkinter import Tk
from traits.api import HasTraits, Button, File, Instance, on_trait_change
from traitsui.api import View, Item
from mayavi.core.ui.api import MlabSceneModel, SceneEditor, MayaviScene
from mayavi.tools.mlab_scene_model import MlabSceneModel

class SEGYAnalysis(HasTraits):

    open_file = Button(label='Open file...')
    file_path = File()
    clearFile = Button(label='Clear file')
    scene = Instance(MlabSceneModel, ())
    traits_view = View(
                        Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                            height=600, width=800, show_label=False),
                        Item('open_file'),
                        Item('file_path', label='Selected file:', style='readonly'),
                        Item('clearFile'),
                        title='File Input Mayavi',
                        resizable=True,
                        buttons =  [ 'Cancel'],
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
                self.scene.mlab.clf()
                self.scene.mlab.volume_slice(self.seismic_data, slice_index=0, plane_orientation='x_axes')
                self.scene.mlab.volume_slice(self.seismic_data, slice_index=0,  plane_orientation='y_axes') 
                self.scene.mlab.volume_slice(self.seismic_data, slice_index=0, plane_orientation='z_axes')

            except Exception as e:
                print(e)
                self.scene.mlab.clf()
                self.scene.mlab.test_contour3d()
                self.seismic_data = None    
                file_path = File()

    def _clearFile_fired(self):
        self.seismic_data = None
        self.file_path = ''
        self.scene.mlab.clf()
        self.scene.mlab.test_contour3d()

if __name__ == '__main__':

    root = Tk()
    root.withdraw()
    sa = SEGYAnalysis()
    sa.configure_traits()
    root.destroy()