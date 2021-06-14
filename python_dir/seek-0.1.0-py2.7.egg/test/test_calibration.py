# SEEK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# SEEK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with SEEK.  If not, see <http://www.gnu.org/licenses/>.

'''
Created on Jan 7, 2015

@author: seehars
'''
import numpy as np
from ivy.utils.struct import Struct
from seek.plugins import calibration
import os

DATA_PATH = 'res/data'

class TestCalibrationPlugin(object):
    
    def setup(self):
        current_path = os.path.dirname(__file__)
        params = Struct(flux_calibration = "default",
                        gain_file_default=os.path.join(os.path.join(current_path, DATA_PATH),'gain_null.dat'))
        self.ctx = Struct(params = params)
        
    def testCalibration(self):
        calib = calibration.Plugin(self.ctx)
        calib()
        assert self.ctx.params.gain_file_default

