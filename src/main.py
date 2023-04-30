import numpy as np
from tkinter import filedialog as fd
from tkinter import Tk
from traits.api import HasTraits, Button, File, Instance, on_trait_change, Bool
from traitsui.api import View, Item, HGroup, VGroup, HSplit
from mayavi.core.ui.api import MlabSceneModel, SceneEditor, MayaviScene
from mayavi.tools.mlab_scene_model import MlabSceneModel
from analysis import *
from numpy_analysis import *
from animation import *
from volume_slice_analysis import *

class ProjectInformationDisplay(HasTraits):
    name = '3D Visualization and Analysis of Seismic Volumes'
    team_name = 'Sifar'
    team_members = 'Adarsh, Koustav, Raja'
    course_name = 'AE6102 (Spring 2022-2023)'

    view = View(
        HSplit(
            VGroup(
                Item('course_name', style='readonly', label='Course Name'),
                Item('name', style='readonly', label='Project Name'),
            ),
            VGroup(
                Item('team_name', style='readonly', label='Team Name'),
                Item('team_members', style='readonly', label='Team Members'),
            ),
            VGroup(),
        ),
        style = 'custom',
        title='Project Information',
        resizable=True,
    ) 

class SEGYAnalysis(HasTraits):

    # File Buttons
    open_data_file = Button(label='Open data file')
    data_file_path = File()
    open_label_file = Button(label='Open label file')
    label_file_path = File()
    show_button = Button(label='Show and Analyse')
    clearFile = Button(label='Clear file')

    # Project Information
    project = Instance(ProjectInformationDisplay, ())

    # Mlab Scene Model
    scene = Instance(MlabSceneModel, ())

    # Sesismic Data Specific Buttons
    zoom_in_button = Button('Zoom In', show_label=False)
    zoom_out_button = Button('Zoom Out', show_label=False)
    show_group = Bool(False)
    show_file = Bool(True)
    analysis_button = Button(label='Planar Plots')
    numpy_analysis_button = Button(label='Raw Data')
    animation_button = Button(label='Planar Animations')
    volume_slice_analysis_button = Button(label='Volume Slice Analysis')

    traits_view = View(
        Item('project', style='custom', show_label=False),
        Item('scene', editor=SceneEditor(scene_class=MayaviScene),
             height=600, width=800, show_label=False),
        HGroup(
            Item('zoom_in_button', show_label=False),
            Item('zoom_out_button', show_label=False),
            Item('volume_slice_analysis_button', show_label=False),
            Item('analysis_button', show_label=False),
            Item('numpy_analysis_button', show_label=False),
            Item('animation_button', show_label=False),
            visible_when='show_group',
        ),
        VGroup(
            HGroup(
                Item('open_data_file', show_label=True, style='simple', label='Data File'),
                Item('data_file_path', label='Selected file:', style='readonly'),
            ),
            HGroup(
                Item('open_label_file', show_label=True, style='simple', label='Label File'),
                Item('label_file_path', label='Selected file:', style='readonly'),
            ),
            Item('show_button', show_label=False, style='simple', label='Show File'),
            visible_when='show_file',
        ),
        Item('clearFile', show_label=False, style='custom', label='Clear File'),
        title='Seismic Data Visualization and Analysis',
        resizable=True,
        buttons=['Cancel'],
    )

    def __init__(self):
        HasTraits.__init__(self)
        self.seismic_data = None
        self.seismic_label = None
        self.data_file_path = 'None'
        self.label_file_path = 'None'


    @on_trait_change('scene.activated')
    def update_plot(self):
        self.scene.mlab.clf()
        self.scene.mlab.test_contour3d()

    def _open_data_file_fired(self):
        self.data_file_path = fd.askopenfilename()
        if self.data_file_path != '':
            try:
                self.seismic_data = np.load(self.data_file_path)

            except Exception as e:
                print(e)
                self.seismic_data = None
                self.data_file_path = 'None'
                self.show_group = False

    def _open_label_file_fired(self):
        self.label_file_path = fd.askopenfilename()
        if self.label_file_path != '':
            try:
                self.seismic_label = np.load(self.label_file_path)
            except Exception as e:
                print(e)
                self.seismic_label = None
                self.label_file_path = 'None'
                self.show_group = False   

    def _show_button_fired(self):
        self.scene.mlab.clf()
        if self.seismic_data is not None:
            self.scene.mlab.volume_slice(self.seismic_data, slice_index=0, plane_orientation='x_axes')
            self.scene.mlab.volume_slice(self.seismic_data, slice_index=0, plane_orientation='y_axes')
            self.scene.mlab.volume_slice(self.seismic_data, slice_index=0, plane_orientation='z_axes')
            self.scene.mlab.axes(xlabel='Inline', ylabel='Crossline', zlabel='Depth', nb_labels=5)
            self.show_group = True
            self.show_file = False
            if self.seismic_label is not None:
                self.scene.mlab.contour3d(self.seismic_label, contours=[3])
            self.scene.render()
            self.scene.mlab.view(azimuth=45, elevation=45, distance='auto')
        else:
            self.scene.mlab.clf()
            self.scene.mlab.test_contour3d()  

    def _clearFile_fired(self):
        self.seismic_data = None
        self.seismic_label = None
        self.data_file_path = 'None'
        self.label_file_path = 'None'
        self.scene.mlab.clf()
        self.scene.mlab.test_contour3d()
        self.show_group = False
        self.show_file = True

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

    def _volume_slice_analysis_button_fired(self):
        volume_slice_analysis_traits = VolumeSliceAnalysis(data=self.seismic_data)
        volume_slice_analysis_traits.configure_traits()

if __name__ == '__main__':

    root = Tk()
    root.withdraw()
    sa = SEGYAnalysis()
    sa.configure_traits()
    root.destroy()