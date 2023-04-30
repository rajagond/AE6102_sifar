from traits.api import HasTraits, Button, String
from traitsui.api import View, Item, HGroup

class GeoPhysicalAnalysis(HasTraits):

    analysis_view = View(
        title='GeoPhysical Analysis',
        resizable=True,
        buttons=['Cancel'],
    )

    def __init__(self, data):
        HasTraits.__init__(self)
        self.seismic_data = data