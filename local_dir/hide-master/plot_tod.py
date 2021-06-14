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
Created on August 1, 2018

author: Lucas Olivari
'''

import matplotlib.pyplot as plt
import h5py
import numpy as np

####################################################################
#### EXAMPLE OF HOW TO HANDLE HDF5 FILES
####################################################################

with h5py.File("./2018/01/01/bingo_tod_horn_0_20180101_000000.h5", "r") as fp:
    tod = fp["P/Phase1"].value
    time = fp["TIME"].value

print np.mean(tod), np.std(tod)

plt.imshow(tod, aspect="auto",
           extent=(time[0], time[-1],960, 1260))#, cmap="gist_earth")#, norm=matplotlib.colors.LogNorm())
plt.colorbar()
plt.ylabel(r'$\mathrm{Frequency}\,\mathrm{(MHz)}$', fontsize=12)
plt.xlabel(r'$\mathrm{Time}\,\mathrm{(s)}$', fontsize=12)
plt.savefig("tod.png")
plt.close()

