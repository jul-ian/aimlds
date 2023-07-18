"""
Get the PUF CHIS data
"""

import os
import re
from zipfile import ZipFile
import pandas as pd

data_dir = os.path.expanduser('~/Github/aimlds/data/raw')
chis_zipfiles = [x for x in os.listdir(data_dir) if re.search(r'.+sas.*\.zip$', x)]

datadict = {}
for zipfile in chis_zipfiles:
    with ZipFile(os.path.join(data_dir, zipfile)) as file:
        sasfile = [x for x in file.namelist() if x.endswith('sas7bdat')]
        file.extract(sasfile[0], )
        sasdf = pd.read_sas(sasfile[0])
        datadict[re.sub(r'', r'', )]