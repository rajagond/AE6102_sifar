'''
GUI application using traitsui to display a plot generated by mayavi
'''

from traits.api import HasTraits, Instance, on_trait_change, Button, observe
from traitsui.api import View, Item, HGroup, UItem, ButtonEditor, CancelButton, OKButton, Action
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, SceneEditor
from mayavi.core.ui.engine_view import EngineView
import numpy as np
import argparse

class TraitsUI(HasTraits):
    # The scene Model
    scene = Instance(MlabSceneModel, ())

    # update the plot button
    # update_plot_button = Button(label='Update Plot')

    # Action to perform when the button is pressed
    upp = Action(name="Update Plot", action="update_plot_button_clicked")

    traits_view = View(
                Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=1000, width=750, show_label=False
                    ),
                # HGroup(
                #     UItem('update_plot_button', editor=ButtonEditor(label='Update Plot')),
                # ),
                buttons = [OKButton, CancelButton, upp],
                resizable=True,
                scrollable=True)
    
    def __init__(self, **traits):
        HasTraits.__init__(self, **traits)
        self.curent_plot = 1
        self.seismic_data = np.load('../data/test.npy')



    @on_trait_change('scene.activated')
    def update_plot(self):
        self.scene.mlab.clf()
        if self.curent_plot == 1:
            self.scene.mlab.test_contour3d()
            self.curent_plot = 2
        elif self.curent_plot == 2:
            self.scene.mlab.test_points3d()
            self.curent_plot = 3
        else :
            self.scene.mlab.volume_slice(self.seismic_data, slice_index=0, plane_orientation='x_axes')
            self.scene.mlab.volume_slice(self.seismic_data, slice_index=1,  plane_orientation='y_axes') 
            self.scene.mlab.volume_slice(self.seismic_data, slice_index=2, plane_orientation='z_axes') 
            self.curent_plot = 1

        print('update_plot')

    def update_plot_button_clicked(self, event):
        self.update_plot()
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mayavi', action='store_true')
    args = parser.parse_args()
    if args.mayavi:
        t = TraitsUI()
        t.configure_traits()