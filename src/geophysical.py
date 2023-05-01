from traits.api import HasTraits, Button, String
from traitsui.api import View, Item, HGroup, VGroup
import bruges as bg
from matplotlib import pyplot as plt

class GeoPhysicalAnalysis(HasTraits):

    x_axis = String('')
    y_axis = String('')
    z_axis = String('')
    envelope_button_x = Button('Reflection Strenth')
    envelope_button_y = Button('Reflection Strenth')
    envelope_button_z = Button('Reflection Strenth')
    phase_button_x = Button('Instantaneous Phase')
    phase_button_y = Button('Instantaneous Phase')
    phase_button_z = Button('Instantaneous Phase')
    frequency_button_x = Button('Instantaneous Frequency')
    frequency_button_y = Button('Instantaneous Frequency')
    frequency_button_z = Button('Instantaneous Frequency')

    analysis_view = View(
        HGroup(
            VGroup(
                HGroup(  
                    Item('x_axis', label='X-Axis:'),
                    Item('envelope_button_x', show_label=False),
                ),
                HGroup(
                    Item('y_axis', label='Y-Axis:'),
                    Item('envelope_button_y', show_label=False),
                ),
                HGroup(
                    Item('z_axis', label='Z-Axis:'),
                    Item('envelope_button_z', show_label=False),
                ),
            ),
            label='Reflection Strength'
        ),
        HGroup(
            VGroup(
                HGroup(
                    Item('x_axis', label='X-Axis:'),
                    Item('phase_button_x', show_label=False),
                ),
                HGroup(
                    Item('y_axis', label='Y-Axis:'),    
                    Item('phase_button_y', show_label=False),
                ),
                HGroup(
                    Item('z_axis', label='Z-Axis:'),
                    Item('phase_button_z', show_label=False),
                ),
            ),
            label='Instantaneous Phase'
        ),
        HGroup(
            VGroup(
                HGroup(
                    Item('x_axis', label='X-Axis:'),
                    Item('frequency_button_x', show_label=False),
                ),
                HGroup(
                    Item('y_axis', label='Y-Axis:'),
                    Item('frequency_button_y', show_label=False),
                ),
                HGroup(
                    Item('z_axis', label='Z-Axis:'),
                    Item('frequency_button_z', show_label=False),
                ),
            ),
            label='Instantaneous Frequency'
        ),
        title='Geophysical Analysis',
        resizable=True,
        width=600,
        buttons=['Cancel'],
    )

    def __init__(self, data):
        HasTraits.__init__(self)
        self.seismic_data = data
        self.envelope = None
        self.phase = None
        self.frequency = None

    def _envelope_button_x_fired(self):
        if self.envelope is None:
            self.envelope = bg.attribute.envelope(self.seismic_data.data)
        try:
            plt.imshow(self.envelope[int(self.x_axis),:,:].T, interpolation='bicubic')
            plt.show()
        except Exception as e:
            print('Error: Invalid Arguments', e)
        self.x_axis = ''

    def _envelope_button_y_fired(self):
        if self.envelope is None:
            self.envelope = bg.attribute.envelope(self.seismic_data.data)
        try:
            plt.imshow(self.envelope[:,int(self.y_axis),:].T, interpolation='bicubic')
            plt.show()
        except Exception as e:
            print('Error: Invalid Arguments', e)
        self.y_axis = ''
    
    def _envelope_button_z_fired(self):
        if self.envelope is None:
            self.envelope = bg.attribute.envelope(self.seismic_data.data)
        try:
            plt.imshow(self.envelope[:,:,int(self.z_axis)].T, interpolation='bicubic')
            plt.show()
        except Exception as e:
            print('Error: Invalid Arguments', e)
        self.z_axis = ''

    def _phase_button_x_fired(self):
        if self.phase is None:
            self.phase = bg.attribute.instantaneous_phase(self.seismic_data.data)
        try:
            plt.imshow(self.phase[int(self.x_axis),:,:].T, cmap='twilight_shifted', interpolation='bicubic')
            plt.show()
        except Exception as e:
            print('Error: Invalid Arguments', e)
        self.x_axis = ''
    
    def _phase_button_y_fired(self):
        if self.phase is None:
            self.phase = bg.attribute.instantaneous_phase(self.seismic_data.data)
        try:
            plt.imshow(self.phase[:,int(self.y_axis),:].T, cmap='twilight_shifted', interpolation='bicubic')
            plt.show()
        except Exception as e:
            print('Error: Invalid Arguments', e)
        self.y_axis = ''

    def _phase_button_z_fired(self):
        if self.phase is None:
            self.phase = bg.attribute.instantaneous_phase(self.seismic_data.data)
        try:
            plt.imshow(self.phase[:,:,int(self.z_axis)].T, cmap='twilight_shifted', interpolation='bicubic')
            plt.show()
        except Exception as e:
            print('Error: Invalid Arguments', e)
        self.z_axis = ''

    def _frequency_button_x_fired(self):
        if self.frequency is None:
            self.frequency = bg.attribute.instantaneous_frequency(self.seismic_data.data, dt=0.004)
        try:
            plt.imshow(self.frequency[int(self.x_axis),:,:].T, interpolation='bicubic', vmin=-10)
            plt.colorbar(shrink=0.75)
            plt.show()
        except Exception as e:
            print('Error: Invalid Arguments', e)
        self.x_axis = ''
    
    def _frequency_button_y_fired(self):
        if self.frequency is None:
            self.frequency = bg.attribute.instantaneous_frequency(self.seismic_data.dat, dt=0.004)
        try:
            plt.imshow(self.frequency[:,int(self.y_axis),:].T, interpolation='bicubic', vmin=-10)
            plt.colorbar(shrink=0.75)
            plt.show()
        except Exception as e:
            print('Error: Invalid Arguments', e)
        self.y_axis = ''

    def _frequency_button_z_fired(self):
        if self.frequency is None:
            self.frequency = bg.attribute.instantaneous_frequency(self.seismic_data.data, dt=0.004)
        try:
            plt.imshow(self.frequency[:,:,int(self.z_axis)].T, interpolation='bicubic', vmin=-10)
            plt.colorbar(shrink=0.75)
            plt.show()
        except Exception as e:
            print('Error: Invalid Arguments', e)
        self.z_axis = ''
