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
Created on Nov 9, 2015

author: jakeret
'''
from __future__ import print_function, division, absolute_import, unicode_literals

from pkg_resources import resource_filename

import numpy as np

import hide

# GAIN_PATH = "data/gain_template_7m_FFT_ADU_K.dat"
GAIN_PATH = "data/gain_template_7m_FFT_phase_switch_ADU_K.dat"
BACKGROUND_PATH = "data/background_template_7m_FFT_ADU.dat"
NOISE_PATH = "data/noise_template_7m_FFT_ADU.dat"
RFI_PATH = "data/rfi_template_7m_FFT_ADU.dat"
SCHEDULE_PATH = "data/full_scan_schedule.txt"

def get_gain(frequencies):
    path = resource_filename(hide.__name__, GAIN_PATH)
    data = np.loadtxt(path)
    freq = data[:,0]
    gain = data[:,1]
    
    tod_gain = np.interp(frequencies, freq, gain)
    return tod_gain

def get_background(frequencies, el_model):
    path = resource_filename(hide.__name__, BACKGROUND_PATH)
    data = np.loadtxt(path)
    freq = data[:,0]
    bg_ = data[:,1]
    bg = np.interp(frequencies, freq, bg_).reshape(-1,1)
    bg_model = lambda el: bg * np.polyval(el_model, el)
    return bg_model

def get_noise_params(frequencies):
    path = resource_filename(hide.__name__, NOISE_PATH)
    data = np.loadtxt(path)
    freq = data[:,0]
    white_noise_scale_ = data[:,1]
    color_noise_amp_ = data[:,2]
    color_noise_beta_ = data[:,3]
    
    white_noise_scale = np.interp(frequencies, freq, white_noise_scale_)
    color_noise_amp = np.interp(frequencies, freq, color_noise_amp_)
    color_noise_beta = np.interp(frequencies, freq, color_noise_beta_)
    return white_noise_scale, color_noise_amp, color_noise_beta 

def get_rfi_params(frequencies):
    path = resource_filename(hide.__name__, RFI_PATH)
    data = np.loadtxt(path)
    freq = data[:,0]
    rfifrac_ = data[:,1]
    rfiamplitude_ = data[:,2]
    rfifrac = np.interp(frequencies, freq, rfifrac_)
    rfiamplitude = np.interp(frequencies, freq, rfiamplitude_)
    return rfifrac, rfiamplitude 
    
def convert_frequencies(frequencies):
    """
    :param frequencies: true frequencies
    :returns freq: true frequencies
    """
    return frequencies

def get_schedule():
    return resource_filename(hide.__name__, SCHEDULE_PATH)