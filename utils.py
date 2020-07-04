import os 
import sys 
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display
import ipywidgets as widgets
from emoji import UNICODE_EMOJI


dataset_names = os.listdir('data')

resample_human = {'w':'Week', 'm':'Month', 'd':'Day', 'h':'Hour'}

def list_has_emoji(s):
    return len([x for x in s if x in UNICODE_EMOJI])

data_sel = widgets.Dropdown(
    options=[x.split('.')[0] for x in dataset_names],
    description='Dataset:',
    disabled=False,
)

resample_slider = widgets.SelectionSlider(
    options=['m', 'w', 'd'],
    description='Resample:',
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True
)
