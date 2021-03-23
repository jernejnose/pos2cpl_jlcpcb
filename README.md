# pos2cpl_jlcpcb
Python tool that converts footprint positions file (.pos) from KiCad to component placement list (.csv) file as specified on JLCPCB.

## Usage

### Export file from KiCad
You can generate POS file by clicking File -> Fabrication Outputs -> Footprint Position (.pos) File. Set format to `ASCII`, units to `Millimeters` and files to `Separate files for front and back` Select output directory and then clikc Generate Position File.

### Convert file
Go to your export directory and run `python3 pos2cpl.py input.pos output.csv`
