info = "Cal. Abs.:2022-12-14","Cal. Due Date:2024-12","Cal. Lin.:not applicable","Cal. Misc.:2022-12-14","Cal. Refl.:2022-12-14","Cal. S-Para.:not applicable","Cal. S-Para. (User):not applicable","Cal. Temp.:not applicable","Coupling:AC","Function:Power Terminating","Impedance:50","Manufacturer:Rohde & Schwarz","MaxFreq:1.8e+10","MaxPower:0.2","MinFreq:8000","MinPower:1e-10","Resolution:5e-07","SPD Mnemonic:","SW Build:02.40.22081101","Sensor Name:NRP18A-101753","Serial:101753","Stock Number:1424.6815K02","Technology:3-Path Diode","TestLimit:0.160 dB","TestLimit pd:0.160 dB","Type:NRP18A","Uptime:2642",""
info = list(info)
del info[len(info) - 1]


data = {}
for item in info:
    key = item.split(':')
    data[key[0]] = key[1]

print(data['MaxFreq'], data['MinFreq'])
