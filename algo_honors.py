import mne
import numpy as np
import subprocess

row = 0
column = 0
data = [ [0]*14 for i in range(109)]
raw_data = [ [0]*14 for i in range(109)]
find_RECORDS = "find . -type f -name 'RECORDS.txt'"
find_files = subprocess.check_output("find . -name 'files'").strip()
found_RECORDS = subprocess.check_output(find_RECORDS).strip()
with open(found_RECORDS) as RECORDS:
    for line in RECORDS:
        data[column][row] = mne.io.read_raw_edf(find_files.decode() + "/" + line.rstrip())
        raw_data[column][row] = data[column][row].get_data()
        row += 1
        if row == 13:
            row = 0
            column += 1
            if column == 108:
                column = 0
        print(line.strip())
print(find_files.decode() + "/" + line)

data[1][1].compute_psd(fmax=50).plot()
data[1][1].plot(block=True, duration=60, n_channels=64)