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
            Item('coordinates', label='Comma Separated Indices:', style='text'),
            Item('coordinates_button', show_label=False, style='custom'),
            label='Coordinates'
        ),
        HGroup(
            Item('inline_slice_number', label='Inline slice number:', style='text'),
            Item('inline_button', show_label=False, style='custom'),
            label='Inline (X-Axis)'
        ),
        HGroup(
            Item('crossline_slice_number', label='Crossline slice number:', style='text'),
            Item('crossline_button', show_label=False, style='custom'),
            label='Crossline (Y-Axis)'
        ),
        HGroup(
            Item('depth_slice_number', label='Depth slice number:', style='text'),
            Item('depth_button', show_label=False, style='custom'),
            label='Depth (Z-Axis)'
        ),
    )

    def __init__(self, data, display):
        HasTraits.__init__(self)
        self.seismic_data = data
        self.result = display

    def _coordinates_button_fired(self):
        try:
            x,y,z = self.coordinates.split(',')
            self.coordinates = ''
            self.result.string = str(self.seismic_data[int(x), int(y), int(z)])
        except:
            self.result.string = str("Invalid Coordinates")
            self.coordinates = ''

    def _inline_button_fired(self):
        try:    
            inline_slice = self.seismic_data[int(self.inline_slice_number), :, :]
            self.inline_slice_number = ''
            self.result.string = str(inline_slice)
        except:
            self.result.string = str("Invalid Inline Slice Number")
            self.inline_slice_number = ''

    def _crossline_button_fired(self):
        try:
            crossline_slice = self.seismic_data[:, int(self.crossline_slice_number), :]
            self.crossline_slice_number = ''
            self.result.string = str(crossline_slice)
        except:
            self.result.string = str("Invalid Crossline Slice Number")
            self.crossline_slice_number = ''

    def _depth_button_fired(self):
        try:
            depth_slice = self.seismic_data[:, :, int(self.depth_slice_number)]
            self.depth_slice_number = ''
            self.result.string = str(depth_slice)
        except:
            self.result.string = str("Invalid Depth Slice Number")
            self.depth_slice_number = ''


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
        title='Raw Data Analysis',
        resizable=True,
        buttons=['Cancel'],
        width=600,
    )