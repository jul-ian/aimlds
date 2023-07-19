"""
Get the PUF CHIS data
"""

import os
import re
from tempfile import mkdtemp
from zipfile import ZipFile
import pandas as pd
data_dir = os.path.expanduser('~/Github/aimlds/data')
raw_dir = os.path.join(data_dir, 'raw')
proc_dir = os.path.join(data_dir, 'processed')

chis_zipfiles = [x for x in os.listdir(raw_dir) if re.search(r'.+sas.*\.zip$', x)]
chis_zipfiles = list(map(lambda s: os.path.join(raw_dir, s), chis_zipfiles))

temp_dir = mkdtemp()
for zipfile in chis_zipfiles:
    with ZipFile(zipfile) as file:
        sasfile = [x for x in file.namelist() if x.endswith('sas7bdat')]
        file.extract(sasfile[0], temp_dir)
        sasdf = pd.read_sas(os.path.join(temp_dir, sasfile[0]))
        outfname = os.path.dirname(sasfile[0]) + '.pkl'
        outfname = outfname.replace('_sas', '')
        sasdf.to_pickle(os.path.join(proc_dir, outfname))
        