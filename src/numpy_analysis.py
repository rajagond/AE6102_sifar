from traits.api import HasTraits, Button, String, Instance
from traitsui.api import View, Item, HGroup

class Display(HasTraits):
    string = String()
    view = View(Item('string', show_label=False, springy=True, style='custom'))

class analyser(HasTraits):
    coordinates = String('')
    inline_slice_number = String('')
    crossline_slice_number = String('')
    depth_slice_number = String('')
    coordinates_button = Button('Print Value')
    inline_button = Button('Print Data')
    crossline_button = Button('Print Data')
    depth_button = Button('Print Data')
    result = Instance(Display)

    view = View(
        HGroup(
            Item('coordinates', label='Comma Separated Indices:', style='custom'),
            Item('coordinates_button', show_label=False, style='custom'),
            label='Coordinates'
        ),
        HGroup(
            Item('inline_slice_number', label='Inline slice number:', style='custom'),
            Item('inline_button', show_label=False, style='custom'),
            label='Inline (X-Axis)'
        ),
        HGroup(
            Item('crossline_slice_number', label='Crossline slice number:', style='custom'),
            Item('crossline_button', show_label=False, style='custom'),
            label='Crossline (Y-Axis)'
        ),
        HGroup(
            Item('depth_slice_number', label='Depth slice number:', style='custom'),
            Item('depth_button', show_label=False, style='custom'),
            label='Depth (Z-Axis)'
        ),
    )

    def __init__(self, data, display):
        HasTraits.__init__(self)
        self.seismic_data = data
        self.result = display

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
        self.coordinates = ''
        self.result.string = str(self.seismic_data[int(x), int(y), int(z)])

    def _inline_button_fired(self):
        if self.inline_slice_number == '' or int(self.inline_slice_number) > self.seismic_data.shape[2] or int(self.inline_slice_number) < 0:
            print("Invalid Slice Number")
            self.inline_slice_number = ''
            return
        inline_slice = self.seismic_data[int(self.inline_slice_number), :, :]
        self.inline_slice_number = ''
        self.result.string = str(inline_slice)

    def _crossline_button_fired(self):
        if self.crossline_slice_number == '' or int(self.crossline_slice_number) > self.seismic_data.shape[1] or int(self.crossline_slice_number) < 0:
            print("Invalid Slice Number")
            self.crossline_slice_number = ''
            return
        crossline_slice = self.seismic_data[:, int(self.crossline_slice_number), :]
        self.crossline_slice_number = ''
        self.result.string = str(crossline_slice)

    def _depth_button_fired(self):
        if self.depth_slice_number == '' or int(self.depth_slice_number) > self.seismic_data.shape[0] or int(self.depth_slice_number) < 0:
            print("Invalid Slice Number")
            self.depth_slice_number = ''
            return
        depth_slice = self.seismic_data[:, :, int(self.depth_slice_number)]
        self.depth_slice_number = ''
        self.result.string = str(depth_slice)


class NumpyAnalysis(HasTraits):
    display = Instance(Display, ())
    analysis = Instance(analyser, ())

    def __init__(self, data):
        HasTraits.__init__(self)
        self.analysis = analyser(data, self.display)

    view = View(
        Item(
            'analysis',
            style='custom',
            show_label=False,
        ),
        Item(
            'display',
            style='custom',
            label='Result',
            show_label=True
        ),
        title='Numpy Analysis',
        resizable=True,
        buttons=['Cancel'],
    )