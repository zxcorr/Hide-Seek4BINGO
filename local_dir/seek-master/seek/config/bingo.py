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
Created on October, 2018

author: Lucas Olivari

Config file that specifies parameters specific for the FFT spectrometer.
'''

from __future__ import print_function, division, absolute_import, unicode_literals

from ivy.plugin.parallel_plugin_collection import ParallelPluginCollection

####################################################################
#### THIS IS THE CONFIGURATION FILE THAT WILL PRODUCE BINGO MAPS
####################################################################

# ==================================================================
# LIST OF PLUGINGS THAT SEEK (IVY) WILL RUN  -- THEY ARE LOCATED IN
# THE PLUGINS DIRECTORY -- FEEL FREE TO ADD OR REMOVE PLUGINS
# ==================================================================
plugins = ["seek.plugins.find_nested_files",
           "seek.plugins.calibration",
            "seek.plugins.initialize",
# comment out everything below when doing calibration-only analysis
           ParallelPluginCollection([
#                                     "seek.plugins.load_preprocessed_data",
                                    "seek.plugins.load_data",
                                    "seek.plugins.pre_process_tod",
                                    "seek.plugins.process_coords",
                                    "seek.plugins.post_process_tod",
                                    "seek.plugins.restructure_tod",
                                     ],
                                     "seek.plugins.map_file_paths",
                                     "seek.plugins.reduce_map_indicies"
                                     ),
            ParallelPluginCollection(["seek.plugins.create_maps"],
                                     "seek.plugins.map_indicies",
                                     "seek.plugins.reduce_maps"),
            "seek.plugins.write_maps",
            "ivy.plugin.show_stats",
            ]

# ==================================================================
# GENERAL
# ==================================================================
#seed = 1
verbose = True
cpu_count = 1
backend = "sequential"

# ==================================================================
# OUTPUT
# ==================================================================
overwrite = True            # True if file should be overwritten
map_name
        # map file name format -- it will be written by run_seek.py

# ==================================================================
# TELESCOPE
# ==================================================================

#-----------------
# BINGO
#-----------------
telescope_latitude = -7.0
telescope_longitude = -38.
telescope_elevation = 0.   # altitude

# ==================================================================
# DATA LOADING
# ==================================================================
file_prefix = "/home/otobone/Documentos/ic/projeto_karin/resultados/TOD/freq_bingo/drectangular_2d/"                # location of the tod data
strategy_start = "2018-01-01-00:00:00"      # survey start time. Format YYYY-mm-dd-HH:MM:SS
strategy_end   = "2018-01-03-23:59:59"      # survey end time. Format YYYY-mm-dd-HH:MM:SS
file_date_format = "%Y%m%d_%H%M%S"          # Format of date part of file name
integration_time = 1                       # no of pixel to use for integration in time (axis=1)
max_frequency = 1260.
min_frequency = 980.
integration_frequency = 1                   # no of pixel to use for integration in freq (axis=0)

# ==================================================================
# FILE INPUT
# ==================================================================

data_file_prefix
                # First part of data file name -- it will be written by run_seek.py
data_file_suffix = ".h5"         # Suffix of file name
file_type = "hdf5"
coord_prefix
            # prefix of coord file -- it will be written by run_seek.py
chunk_size = 1                   # number of files to be grouped together

### TO DISCOVER
ref_channel_freq = 0.
###            

# ---------------------------
# FFT SPECTROMETER
# ---------------------------
spectrometer = "fake_bingo_spectrometer"
m9703a_mode = "phase_switch"                # FFT spectrometer accusition mode -- In the future, this must be updated to BINGO real specifications
spectral_kurtosis = False                   # True if spectral kurtosis masking should be used
accumulations = 146484                      # number of spectrum accumulations -- Warning: I do not know from where this number comes from.
accumulation_offset = 0                     # SEL_Curtosis_Range (default: P_Select 0) 

# ==================================================================
# MAP MAKING
# ==================================================================
map_maker = "seek.mapmaking.simple_mapper" # choose the map-making algorithm
nside = 128                                 # choose the HEALPix nside             
variance = False

# ==================================================================
# CALIBRATION
# ==================================================================
flux_calibration = "default"              # calibration mode: default, flat, data
gain_file_default
                # Gain template to be used on the default mode -- it will be written by run_seek.py

# ----------------------------------------------------------------
# BACKGROUND MODEL -- AS DEFAULT, IT IS NOT IN THE LIST OF PLUGINS
# IT MAY BE EASIER TO REMOVE IT AT THE COMPONENT SEPARATION STEP
# ----------------------------------------------------------------
background_model = "median" # model: median or smooth

# ==================================================================
# RFI CLEANING -- AS DEFAULT, IT IS NOT IN THE LIST OF PLUGINS
# ==================================================================
cleaner = "seek.mitigation.sum_threshold"

# ---------------------------
# FREQUENCY MASKING 
# ---------------------------
mask_freqs = ()             # choose the frequencies to be masked

# ---------------------------
# SUM THRESHOLD
# ---------------------------
chi_1 = 6                    # First threshold value 
sm_kernel_m = 40             # Smoothing, kernel window size in axis=1
sm_kernel_n = 20             # Smoothing, kernel window size in axis=0
sm_sigma_m = 15              # Smoothing, kernel sigma in axis=1
sm_sigma_n = 7.5             # Smoothing, kernel sigma in axis=0
struct_size_0 = 3            # size of struct for dilation on freq direction [pixels]
struct_size_1 = 7            # size of struct for dilation on time direction [pixels]

eta_i = [0.5, 0.55, 0.62, 0.75, 1]

# ==================================================================
# POSTPROCESSING
# ==================================================================
store_intermediate_result = True         # Flag if data, mask etc should be written to file
post_processing_prefix =".cache"         # Prefix used
