import pyqtgraph as pg
import numpy as np


class FrequencyGraph:
    def __init__(self):
        self.plot_widget = pg.PlotWidget()

        self.legend = pg.LegendItem(offset=(-10, 2))
        self.legend.setParentItem(self.plot_widget.plotItem)
        # self.legend.hide()

        self.plot_widget.plotItem.setTitle("DFT Magnitude Plot")
        self.plot_widget.plotItem.setLabel(axis="left", text="|F(f)|")  # \u03C9
        self.plot_widget.plotItem.setLabel(axis="bottom", text="f", units="HZ")
        self.plot_widget.plotItem.showGrid(x=True)

        self.original_pen = pg.mkPen(color='w', width=2)
        self.modified_pen = pg.mkPen(color='orange', width=2)

    def draw_magnitudes(self, original_spectrum, modified_spectrum, frequencies, scale="linear"):
        self.plot_widget.plotItem.clear()
        self.legend.clear()

        if scale == "linear":
            self.apply_linear_scale()
        else:
            self.apply_audiogram_scale()
        # self.draw_impulses(np.abs(original_spectrum), frequencies, self.original_pen, scale)
        self.draw_impulses(np.abs(modified_spectrum), frequencies, self.modified_pen, scale)

    def apply_linear_scale(self):
        axis = self.plot_widget.plotItem.getAxis('bottom')
        axis.setTicks(None)
        axis.setStyle(showValues=True)
        self.plot_widget.plotItem.setLogMode(x=False, y=False)
        self.plot_widget.setLimits(xMin=None, xMax=None)
        self.plot_widget.plotItem.setLabel(axis="left", text="|F(f)|")

    def apply_audiogram_scale(self):
        self.plot_widget.plotItem.setLogMode(x=True)

        ticks = [125, 250, 500, 1000, 2000, 4000, 8000]
        log_ticks = [(np.log10(f), str(f)) for f in ticks]
        axis = self.plot_widget.plotItem.getAxis('bottom')
        axis.setTicks([log_ticks])

        self.plot_widget.setLimits(xMin=np.log10(20), xMax=np.log10(20_000))
        self.plot_widget.plotItem.showGrid(x=True, y=True)
        self.plot_widget.plotItem.setLabel(axis="left", text="|F(f)| (dB)")

    def draw_impulses(self, magnitudes, frequencies, pen, scale):
        if pen == self.original_pen:
            name = "Original Signal Components"
        else:
            name = "Modified Signal Components"

        if scale == "audiogram":
            # get only positive frequencies and their respective magnitudes from the frequencies of the DFT
            mask = frequencies > 0
            frequencies = frequencies[mask]
            magnitudes = magnitudes[mask]
            log_frequencies = np.log10(frequencies)
            log_magnitudes = 20 * np.log10(magnitudes)
            x_data = frequencies
            y_data = log_magnitudes
        else:
            x_data = frequencies
            y_data = magnitudes

        impulse_item = pg.PlotDataItem(x=x_data, y=y_data, pen=pen)

        self.plot_widget.addItem(impulse_item)

        self.legend.addItem(impulse_item, name)
