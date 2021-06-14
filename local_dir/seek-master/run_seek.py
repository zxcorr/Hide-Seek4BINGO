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
Created on October 1, 2018

author: Lucas Olivari
'''

import numpy as np
import os

####################################################################
#### THIS IS THE SCRIPT THAT WILL RUN HIDE FOR EACH HORN
####################################################################

# ==================================================================
# CHOOSE NUMBER OF HORNS
# ==================================================================

number_horns = 28

# ==================================================================
# CHOOSE BINGO MODEL
# ==================================================================

bingo_model = 1 # either 1 or 2

# ==================================================================
# CHOOSE DESTINATION AND WORKING PATHS
# ==================================================================

destination_path = "/usr/local/lib/python2.7/dist-packages/seek-0.1.0-py2.7.egg/seek/config/" #'~/anaconda2/lib/python2.7/site-packages/seek-0.1.0-py2.7.egg/seek/config/' # change to your destination (the place where your hide package is located within your python repository)
out_path = "/home/otobone/Documentos/ic/projeto_karin/resultados/healpix_seek/drectangular/0d/"
working_path = os.getcwd() + "/seek/config/"   #'/home/lucas/Documentos/work/seektest/seek/seek/config/' # change to your working path

# ==================================================================
# SETTING THE CONFIG FILES FOR EACH HORN
# ==================================================================

dfile_short = 'bingo_horn'

for i in range(0, number_horns):
    destination = open(working_path + 'bingo_horn_' + str(i) + '.py', 'w')
    source = open(working_path + 'bingo.py', 'r')
    for line in source:
        if line == 'map_name\n':
            destination.write('map_name = "'+ out_path + 'bingo_maps_horn_' + str(i) + '.hdf"' + '\n')    #destination.write('map_name = "bingo_maps_horn_' + str(i) + '.hdf"' + '\n')
                             # map file name for each horn -- output

        elif line == 'data_file_prefix\n':
            destination.write('data_file_prefix = "bingo_tod_horn_' + str(i) + '_"' + '\n') 
                             # tod file name for each horn -- input     

        elif line == 'coord_prefix\n':
            destination.write('coord_prefix = "coord_bingo_' + str(i) + '_"' + '\n') 
                             # coordinates file name for each horn -- input

        elif line == 'gain_file_default\n':
            if bingo_model == 1:
                destination.write('gain_file_default = "data/gain_template_fake_bingo_model_1_' + str(i) + '.dat"' + '\n') 
                             # gain template used for each horn
            elif bingo_model == 2:
                destination.write('gain_file_default = "data/gain_template_fake_bingo_model_2_' + str(i) + '.dat"' + '\n') 
                             # gain template used for each horn
            
        else:
            destination.write(line)	
    source.close()
    destination.close()

# ==================================================================
# SETTING AND RUNNING SEEK
# ==================================================================

for i in range(0, number_horns):
    os.system('sudo cp ' + working_path + 'bingo_horn_' + str(i) + '.py' + ' ' + destination_path)	 
    os.system('seek seek.config.' + dfile_short + '_' + str(i)) # run seek
