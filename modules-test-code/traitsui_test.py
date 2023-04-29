'''
sample gui application using traitsui to display a plot generated by mayavi
'''

from traits.api import HasTraits, Instance, on_trait_change
from traitsui.api import View, Item, CancelButton, OKButton, Action
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, SceneEditor
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
             height=250, width=300, show_label=False
             ),
        # HGroup(
        #     UItem('update_plot_button',
        #          editor=ButtonEditor(label='Update Plot')),
        # ),
        buttons=[OKButton, CancelButton, upp],
        resizable=True)

    def __init__(self, **traits):
        HasTraits.__init__(self, **traits)
        self.curent_plot = 1

    @on_trait_change('scene.activated')
    def update_plot(self):
        self.scene.mlab.clf()
        if self.curent_plot == 1:
            self.scene.mlab.test_contour3d()
            self.curent_plot = 2
        else:
            self.scene.mlab.test_points3d()
            self.curent_plot = 1
        print('update_plot')

    def update_plot_button_clicked(self, event):
        self.update_plot()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()
    if args.test:
        t = TraitsUI()
        t.configure_traits()
