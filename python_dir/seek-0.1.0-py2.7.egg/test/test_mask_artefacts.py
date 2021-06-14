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
Created on Jun 6, 2016

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

from ivy.utils.struct import Struct
from mock import patch
from seek.plugins import mask_artefacts
from datetime import datetime
import numpy as np


class TestMaskArtefactsPlugin(object):
    
    def test_frequency_masking(self):
        tod = np.ma.array(np.random.uniform(size=(10,100)),
                      mask=False)
        
        frequencies = np.arange(tod.shape[0])
        
        min_freq = 4
        max_freq = 6
        mask_freqs = ((min_freq, max_freq), )
        params = Struct(mask_freqs = mask_freqs)
        
        ctx = Struct(params = params,
                     tod_vx = tod,
                     tod_vy = tod,
                     frequencies = frequencies
                     )
        
        plugin = mask_artefacts.Plugin(ctx)
        plugin.mask_frequencies()
        
        assert np.all(tod.mask[min_freq:max_freq, :] == True)

    def test_mask_artefacts(self):
        data = np.random.uniform(size=(1,1000))
        tod = np.ma.array(data, mask=np.zeros_like(data, np.bool))
        time_axis = np.linspace(0, 24, 1000)

        params = Struct(artefacts_file = "")
        ctx = Struct(params = params,
                     tod_vx = tod,
                     tod_vy = tod,
                     time_axis = time_axis,
                     strategy_start = datetime(2015,12,26)
                     )
        
        with patch("seek.utils.load_file") as load_txt_mock:
            load_txt_mock.return_value = np.array([["2015-12-26", "09:00", "10:00"]])
            plugin = mask_artefacts.Plugin(ctx)
            plugin.mask_artefacts()
        
        assert np.all(ctx.tod_vx.mask[:, :int(1000/24*9)] == False)
        assert np.all(ctx.tod_vx.mask[:, int(1000/24*9):int(1000/24*10)] == True)
        assert np.all(ctx.tod_vx.mask[:, int(1000/24*10+1):] == False)
