from traits.api import HasTraits, Button, String
from traitsui.api import View, Item, HGroup
from matplotlib import pyplot as plt

class Analysis(HasTraits):

    inline_slice_number = String('')
    crossline_slice_number = String('')
    depth_slice_number = String('')
    inline_button = Button('Inline Plot')
    crossline_button = Button('Crossline Plot')
    depth_button = Button('Depth Plot')

    analysis_view = View(
        HGroup(
            Item('inline_slice_number', label='Inline slice number:'),
            Item('inline_button', show_label=False),
            label='Inline (X-Axis)'
        ),
        HGroup(
            Item('crossline_slice_number', label='Crossline slice number:'),
            Item('crossline_button', show_label=False),
            label='Crossline (Y-Axis)'
        ),
        HGroup(
            Item('depth_slice_number', label='Depth slice number:'),
            Item('depth_button', show_label=False),
            label='Depth (Z-Axis)'
        ),
        title='Planar Plots',
        resizable=True,
        buttons=['Cancel'],
    )

    def __init__(self, data):
        HasTraits.__init__(self)
        self.seismic_data = data

    def _inline_button_fired(self):
        if self.inline_slice_number == '' or int(self.inline_slice_number) > self.seismic_data.shape[2] or int(self.inline_slice_number) < 0:
            print("Invalid Slice Number")
            self.inline_slice_number = ''
            return
        inline_slice = self.seismic_data[int(self.inline_slice_number), :, :]
        plt.imshow(inline_slice)
        plt.title('Inline Slice: ' + self.inline_slice_number + ', Plane of Y and Z axes')
        plt.xlabel('Y-Axis')
        plt.ylabel('Z-Axis')
        plt.show()

    def _crossline_button_fired(self):
        if self.crossline_slice_number == '' or int(self.crossline_slice_number) > self.seismic_data.shape[1] or int(self.crossline_slice_number) < 0:
            print("Invalid Slice Number")
            self.crossline_slice_number = ''
            return
        crossline_slice = self.seismic_data[:, int(self.crossline_slice_number), :]
        plt.imshow(crossline_slice)
        plt.title('Crossline Slice: ' + self.crossline_slice_number + ', Plane of X and Z axes')
        plt.xlabel('X-Axis')
        plt.ylabel('Z-Axis')
        plt.show()

    def _depth_button_fired(self):
        if self.depth_slice_number == '' or int(self.depth_slice_number) > self.seismic_data.shape[0] or int(self.depth_slice_number) < 0:
            print("Invalid Slice Number")
            self.depth_slice_number = ''
            return
        depth_slice = self.seismic_data[:, :, int(self.depth_slice_number)]
        plt.imshow(depth_slice)
        plt.title('Depth Slice: ' + self.depth_slice_number + ', Plane of X and Y axes')
        plt.xlabel('X-Axis')
        plt.ylabel('Y-Axis')
        plt.show()