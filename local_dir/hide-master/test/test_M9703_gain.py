# HIDE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# HIDE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with HIDE.  If not, see <http://www.gnu.org/licenses/>.


'''
Created on Mar 2, 2015

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals
from ivy.utils.struct import Struct

import numpy as np
from mock import patch
from hide.spectrometer import M9703A

def test_M9703A():
    frequencies = np.arange(980, 1300)
    tod_vx = np.ones((len(frequencies), 100))
    
    # constant elevation model
    params = Struct(elevation_model = [1])
    ctx = Struct(params=params,
                 tod_vx=tod_vx,
                 frequencies = frequencies)
    
    gain_ = np.linspace(0, 10, len(ctx.frequencies))
    with patch("numpy.loadtxt") as load_txt_mock:
        load_txt_mock.return_value = np.vstack([ctx.frequencies, gain_,
                                                2*gain_, 3*gain_]).T
    
        gain = M9703A.get_gain(frequencies)
        bg = M9703A.get_background(frequencies, params.elevation_model)(0)
        wn_scale, cn_amp, cn_beta = M9703A.get_noise_params(frequencies)
        frac, amp = M9703A.get_rfi_params(frequencies)
    
    assert np.all(gain_ == gain)
    assert np.all(bg == gain.reshape(-1,1))
    assert np.all(wn_scale == gain)
    assert np.all(cn_amp == 2*gain)
    assert np.all(cn_beta == 3*gain)
    assert np.all(frac == gain)
    assert np.all(amp == 2*gain)
    
    