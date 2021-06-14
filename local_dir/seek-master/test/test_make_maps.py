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
Created on Mar 20, 2015

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

from ivy.utils.struct import Struct

import numpy as np
import healpy as hp

from seek import Coords
from seek.plugins import make_maps

class TestMakeMapsPlugin(object):
    
    def test_make_map(self):
        params = Struct(map_maker = "seek.mapmaking.healpy_mapper",
                        nside = 2, 
                        variance=False
                        )
        
        npix = hp.nside2npix(params.nside)
        ind = 1
        theta, phi = hp.pix2ang(params.nside, ind)
        dec = np.pi * .5 - theta
        ra = phi
        times = np.array([[0,0,0,ra,dec],[0,0,0,ra,dec]])
        rfi_mask = np.array([[False, False]], dtype = bool)
        tod_vx = np.ma.array([[1., 2.]], mask=rfi_mask)
        tod_vy = np.ma.array([[2., 4.]], mask=rfi_mask)
        
        frequencies = np.array([1420.40575177])
        ctx = Struct(params = params,
                     frequencies = frequencies,
                     times = times,
                     tod_vx = tod_vx,
                     tod_vy = tod_vy,
                     coords = Coords(times[:,-2], times[:,-1], None, None, None)
                     )
        
        plugin = make_maps.Plugin(ctx)
        plugin()
        
        assert len(ctx.map_idxs) == 3
        assert ctx.maps[0] == tod_vx.sum()
        assert ctx.maps[1] == tod_vy.sum()
        assert ctx.counts[0] == tod_vx.shape[1]
        assert ctx.counts[1] == tod_vy.shape[1]        
        
        
        
        