from traits.api import HasTraits, Button, String
from traitsui.api import View, Item, HGroup

class NumpyAnalysis(HasTraits):

    coordinates = String('')
    inline_slice_number = String('')
    crossline_slice_number = String('')
    depth_slice_number = String('')
    coordinates_button = Button('Print Value')
    inline_button = Button('Print Data')
    crossline_button = Button('Print Data')
    depth_button = Button('Print Data')

    numpy_analysis_view = View(
        HGroup(
            Item('coordinates', label='Comma Separated Indices:'),
            Item('coordinates_button', show_label=False),
            label='Coordinates'
        ),
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
        title='Numpy Analysis',
        resizable=True,
        buttons=['Cancel'],
    )

    def __init__(self, data):
        HasTraits.__init__(self)
        self.seismic_data = data

    def _coordinates_button_fired(self):
        x,y,z = self.coordinates.split(',')
        if int(x) > self.seismic_data.shape[0] or int(x) < 0:
            print("Invalid X Coordinate")
            return
        if int(y) > self.seismic_data.shape[1] or int(y) < 0:
            print("Invalid Y Coordinate")
            return
        if int(z) > self.seismic_data.shape[2] or int(z) < 0:
            print("Invalid Z Coordinate")
            return
        
        print(self.seismic_data[int(x), int(y), int(z)])

    def _inline_button_fired(self):
        if self.inline_slice_number == '' or int(self.inline_slice_number) > self.seismic_data.shape[2] or int(self.inline_slice_number) < 0:
            print("Invalid Slice Number")
            self.inline_slice_number = ''
            return
        inline_slice = self.seismic_data[int(self.inline_slice_number), :, :]
        print(inline_slice)

    def _crossline_button_fired(self):
        if self.crossline_slice_number == '' or int(self.crossline_slice_number) > self.seismic_data.shape[1] or int(self.crossline_slice_number) < 0:
            print("Invalid Slice Number")
            self.crossline_slice_number = ''
            return
        crossline_slice = self.seismic_data[:, int(self.crossline_slice_number), :]
        print(crossline_slice)

    def _depth_button_fired(self):
        if self.depth_slice_number == '' or int(self.depth_slice_number) > self.seismic_data.shape[0] or int(self.depth_slice_number) < 0:
            print("Invalid Slice Number")
            self.depth_slice_number = ''
            return
        depth_slice = self.seismic_data[:, :, int(self.depth_slice_number)]
        print(depth_slice)