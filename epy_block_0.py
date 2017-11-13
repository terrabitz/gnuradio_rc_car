"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


def convert_dir_to_num_dashes(dir_string):
    dir_to_dashes = {
        "UP": 10,
        "DOWN": 40,
        "LEFT": 64,
        "RIGHT": 58,
        "UP_LEFT": 34,
        "UP_RIGHT": 28,
        "DOWN_LEFT": 46,
        "DOWN_RIGHT": 52,
    }

    if dir_string not in dir_to_dashes.keys():
        raise KeyError('String ' + dir_string + ' is not an acceptable direction string')

    return dir_to_dashes[dir_string]

def convert_dir_booleans_to_dir_string(up, down, left, right, up_left, up_right, down_left, down_right):
    if up:
       return "UP"
    if down:
       return "DOWN"
    if left:
       return "LEFT"
    if right:
       return "RIGHT"
    if up_left:
       return "UP_LEFT"
    if up_right:
       return "UP_RIGHT"
    if down_left:
       return "DOWN_LEFT"
    if down_right:
       return "DOWN_RIGHT"

    return ""


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """The RC Car Controller for demonstrating basic smart replay attacks"""

    def __init__(self, sample_rate=1e6, symbol_length=532e-6, up=False, down=False, left=False, right=False, up_left=False, up_right=False, down_left=False, down_right=False):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='RC Car Controller',   # will show up in GRC
            in_sig=[],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.up = up
    	self.down = down
    	self.left = left
    	self.right = right
    	self.up_left = up_left
    	self.up_right = up_right
    	self.down_left = down_left
    	self.down_right = down_right

        symbol_repeats = int(sample_rate * symbol_length)

        long_dash = [1,1,1,0]
        short_dash = [1,0]

        self.long_dash_repeated = []
        for i in long_dash:
            self.long_dash_repeated.extend([i]*symbol_repeats)

        self.short_dash_repeated = []
        for i in short_dash:
            self.short_dash_repeated.extend([i]*symbol_repeats)

        self.current_tx_bits = []

    def _create_vector(self):
        dir_string = convert_dir_booleans_to_dir_string(self.up, self.down, self.left, self.right, self.up_left, self.up_right, self.down_left, self.down_right)
        num_dashes = convert_dir_to_num_dashes(dir_string)

        vector = self.long_dash_repeated*4 + self.short_dash_repeated*num_dashes
        return vector

    def _should_transmit(self):
        return self.up or self.down or self.left or self.right or self.up_left or self.up_right or self.down_left or self.down_right

    def work(self, input_items, output_items):
        """
        Output the proper bit stream depending on the current direction
        """
    	output_items[0].fill(0)
        len_output_items = len(output_items[0])
        if self._should_transmit():
            # print(output_items)
            # print(output_items[0])
            # output_items[0] = self._create_vector()
            while len(self.current_tx_bits) <= len_output_items:
                self.current_tx_bits.extend(self._create_vector())

            output_bits = self.current_tx_bits[0:len_output_items]
            # print(output_bits)
            self.current_tx_bits = self.current_tx_bits[len_output_items:]
            for index, bit in enumerate(output_bits):
                output_items[0][index] = bit
        else:
            del self.current_tx_bits[:]

        # print(output_items[0])
        return len(output_items[0])
