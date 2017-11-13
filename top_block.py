#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Nov 13 12:45:57 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import SimpleXMLRPCServer
import epy_block_0
import osmosdr
import sip
import sys
import threading
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.up_right = up_right = False
        self.up_left = up_left = False
        self.up = up = False
        self.target_rate = target_rate = 1e6
        self.target_freq = target_freq = 49.86e6
        self.symbol_length = symbol_length = 532e-6
        self.right = right = False
        self.left = left = False
        self.interpolation = interpolation = 10
        self.down_right = down_right = False
        self.down_left = down_left = False
        self.down = down = False

        ##################################################
        # Blocks
        ##################################################
        _up_right_push_button = Qt.QPushButton("up_right")
        self._up_right_choices = {'Pressed': True, 'Released': False}
        _up_right_push_button.pressed.connect(lambda: self.set_up_right(self._up_right_choices['Pressed']))
        _up_right_push_button.released.connect(lambda: self.set_up_right(self._up_right_choices['Released']))
        self.top_layout.addWidget(_up_right_push_button)
        _up_left_push_button = Qt.QPushButton("up_left")
        self._up_left_choices = {'Pressed': True, 'Released': False}
        _up_left_push_button.pressed.connect(lambda: self.set_up_left(self._up_left_choices['Pressed']))
        _up_left_push_button.released.connect(lambda: self.set_up_left(self._up_left_choices['Released']))
        self.top_layout.addWidget(_up_left_push_button)
        _up_push_button = Qt.QPushButton("up")
        self._up_choices = {'Pressed': True, 'Released': False}
        _up_push_button.pressed.connect(lambda: self.set_up(self._up_choices['Pressed']))
        _up_push_button.released.connect(lambda: self.set_up(self._up_choices['Released']))
        self.top_layout.addWidget(_up_push_button)
        _right_push_button = Qt.QPushButton("right")
        self._right_choices = {'Pressed': True, 'Released': False}
        _right_push_button.pressed.connect(lambda: self.set_right(self._right_choices['Pressed']))
        _right_push_button.released.connect(lambda: self.set_right(self._right_choices['Released']))
        self.top_layout.addWidget(_right_push_button)
        _left_push_button = Qt.QPushButton("left")
        self._left_choices = {'Pressed': True, 'Released': False}
        _left_push_button.pressed.connect(lambda: self.set_left(self._left_choices['Pressed']))
        _left_push_button.released.connect(lambda: self.set_left(self._left_choices['Released']))
        self.top_layout.addWidget(_left_push_button)
        _down_right_push_button = Qt.QPushButton("down_right")
        self._down_right_choices = {'Pressed': True, 'Released': False}
        _down_right_push_button.pressed.connect(lambda: self.set_down_right(self._down_right_choices['Pressed']))
        _down_right_push_button.released.connect(lambda: self.set_down_right(self._down_right_choices['Released']))
        self.top_layout.addWidget(_down_right_push_button)
        _down_left_push_button = Qt.QPushButton("down_left")
        self._down_left_choices = {'Pressed': True, 'Released': False}
        _down_left_push_button.pressed.connect(lambda: self.set_down_left(self._down_left_choices['Pressed']))
        _down_left_push_button.released.connect(lambda: self.set_down_left(self._down_left_choices['Released']))
        self.top_layout.addWidget(_down_left_push_button)
        _down_push_button = Qt.QPushButton("down")
        self._down_choices = {'Pressed': True, 'Released': False}
        _down_push_button.pressed.connect(lambda: self.set_down(self._down_choices['Pressed']))
        _down_push_button.released.connect(lambda: self.set_down(self._down_choices['Released']))
        self.top_layout.addWidget(_down_push_button)
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer(('localhost', 8080), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=interpolation,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	target_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(target_rate*interpolation)
        self.osmosdr_sink_0.set_center_freq(target_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.epy_block_0 = epy_block_0.blk(sample_rate=target_rate, symbol_length=symbol_length, up=up, down=down, left=left, right=right, up_left=up_left, up_right=up_right, down_left=down_left, down_right=down_right)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.osmosdr_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_up_right(self):
        return self.up_right

    def set_up_right(self, up_right):
        self.up_right = up_right
        self.epy_block_0.up_right = self.up_right

    def get_up_left(self):
        return self.up_left

    def set_up_left(self, up_left):
        self.up_left = up_left
        self.epy_block_0.up_left = self.up_left

    def get_up(self):
        return self.up

    def set_up(self, up):
        self.up = up
        self.epy_block_0.up = self.up

    def get_target_rate(self):
        return self.target_rate

    def set_target_rate(self, target_rate):
        self.target_rate = target_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.target_rate)
        self.osmosdr_sink_0.set_sample_rate(self.target_rate*self.interpolation)

    def get_target_freq(self):
        return self.target_freq

    def set_target_freq(self, target_freq):
        self.target_freq = target_freq
        self.osmosdr_sink_0.set_center_freq(self.target_freq, 0)

    def get_symbol_length(self):
        return self.symbol_length

    def set_symbol_length(self, symbol_length):
        self.symbol_length = symbol_length

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right
        self.epy_block_0.right = self.right

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left
        self.epy_block_0.left = self.left

    def get_interpolation(self):
        return self.interpolation

    def set_interpolation(self, interpolation):
        self.interpolation = interpolation
        self.osmosdr_sink_0.set_sample_rate(self.target_rate*self.interpolation)

    def get_down_right(self):
        return self.down_right

    def set_down_right(self, down_right):
        self.down_right = down_right
        self.epy_block_0.down_right = self.down_right

    def get_down_left(self):
        return self.down_left

    def set_down_left(self, down_left):
        self.down_left = down_left
        self.epy_block_0.down_left = self.down_left

    def get_down(self):
        return self.down

    def set_down(self, down):
        self.down = down
        self.epy_block_0.down = self.down


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
