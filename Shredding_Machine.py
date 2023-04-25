import re

file = open(r"C:\Users\grifb\OneDrive\Documents\Shredder\Text_holder.txt", "r")

read_file = str(file.read())

print("whole file:", read_file)


# find_optical_system = re.search(".*Optical System.*", read_file).group(0)
try:
    find_materials = re.search(".*Wetted Surface Materials.*", read_file).group(0)
except:
    find_materials = "None"
try:
    find_EF = re.search(".*Flow rate.*", read_file).group(0)
except:
    find_EF = "None"
try:
    find_CE = re.search(".*Counting efficiency.*", read_file).group(0)
except:
    find_CE = "100%"
try:
    find_DW = re.search(".*Dimensions.*", read_file).group(0)
except:
    find_DW = "None"
try:
    find_SR = re.search(".*Size Range.*", read_file).group(0)
except:
    find_SR = "None"
try:
    find_ECO = re.search(".*Environmental Conditions Operating.*", read_file).group(0)
except:
    find_ECO = "None"
try:
    find_MPNC = re.search(".*Concentration Limit.*", read_file).group(0)
except:
    find_MPNC = "None"
try:
    find_USC = re.search(".*Standard Channel Sizes.*", read_file).group(0)
except:
    find_USC = "None"
try:
    find_P = re.search(".*Power External Supply:.*", read_file).group(0)
except:
    find_P = "None"
try:
    find_SPR = re.search(".*Sample Pressure.*", read_file).group(0)
except:
    find_SPR = "None"
try:
    find_LS = re.search(".*Light Source.*", read_file).group(0)
except:
    find_LS = "None"
try:
    find_LPC = re.search(".*Laser classification .*", read_file).group(0)
except:
    find_LPC = "None"
try:
    find_LD = re.search(".*Light detector.*", read_file).group(0)
except:
    find_LD = "None"
try:
    find_MST = re.search(".*Measurable sample types.*", read_file).group(0)
except:
    find_MST = "None"
try:
    find_OS = re.search(".*Optical system.*", read_file).group(0)
except:
    find_OS = "None"
try:
    find_FCR = re.search(".*False count rate.*", read_file).group(0)
except:
    find_FCR = "None"
try:
    find_PAP = re.search(".*Purge air port.*", read_file).group(0)
except:
    find_PAP = "None"
try:
    find_SIO = re.search(".*Sample Inlet/Outlet Connection.*", read_file).group(0)
except:
    find_SIO = "None"
try:
    find_STR = re.search(".*Sample Temperature.*", read_file).group(0)
except:
    find_STR = "None"
try:
    find_SFR = re.search(".*Sampling flow rate.*", read_file).group(0)
except:
    find_SFR = "None"
try:
    find_SetR = re.search(".*Size range.*", read_file).group(0)
except:
    find_SetR = "None"
try:
    find_SizR = re.search(".*Resolution.*", read_file).group(0)
except:
    find_SizR = "None"
try:
    find_A = re.search(".*Accessories.*", read_file).group(0)
except:
    find_A = "None"
try:
    find_C = re.search(".*Calibration.*", read_file).group(0)
except:
    find_C = "None"
try:
    find_FO = re.search(".*Factory option.*", read_file).group(0)
except:
    find_FO = "None"
try:
    find_O = re.search(".*Options.*", read_file).group(0)
except:
    find_O = "None" 

try:
    find_1 = re.search(".*Channels.*", read_file).group(0)
except:
    find_1 = "None" 

try:
    find_2 = re.search(".*Zero Count.*", read_file).group(0)
except:
    find_2 = "None" 

try:
    find_3 = re.search(".*Enclosure.*", read_file).group(0)
except:
    find_3 = "None" 

try:
    find_4 = re.search(".*Weight.*", read_file).group(0)
except:
    find_4 = "None" 

try:
    find_5 = re.search(".*Communication Protocol.*", read_file).group(0)
except:
    find_5 = "None" 

try:
    find_6 = re.search(".*Sample Volume.*", read_file).group(0)
except:
    find_6 = "None" 

replaced_materials = find_materials.replace("Wetted Surface Materials ", "")
replaced_EF = find_EF.replace("Flow rate (ml/min) ", "")
replaced_CE = find_CE.replace("Counting efficiency ", "")
replaced_DW = find_DW.replace("Dimensions ", "")
replaced_SR = find_SR.replace("Size Range", "")
replaced_ECO = find_ECO.replace("Environmental Conditions Operating ", "")
replaced_MPNC = find_MPNC.replace("Concentration Limit ", "")
replaced_USC = find_USC.replace("Standard Channel Sizes ", "")
replaced_P = find_P.replace("Power External Supply: ", "")
replaced_SPR = find_SPR.replace("Sample Pressure ", "")
replaced_LS = find_LS.replace("Light source ", "")
replaced_LPC = find_LPC.replace("Laser classification ", "")
replaced_LD = find_LD.replace("Light detector ", "")
replaced_MST = find_MST.replace("Measurable sample types ", "")
replaced_OS = find_OS.replace("Optical system ", "")
replaced_FCR = find_FCR.replace("False Count Rate ", "")
replaced_PAP = find_PAP.replace("Purge air port ", "")
replaced_SIO = find_SIO.replace("Sample Inlet/Outlet Connection ", "")
replaced_STR = find_STR.replace("Sample Temperature ", "")
replaced_SFR = find_SFR.replace("Sampling flow rate ", "")
replaced_SetR = find_SetR.replace("Channel sizes ", "")
replaced_SizR = find_SizR.replace("Resolution ", "")
replaced_A = find_A.replace("Accessories ", "")
replaced_C = find_C.replace("Calibration ", "")
replaced_FO = find_FO.replace("Factory option ", "")
replaced_O = find_O.replace("Options ", "")
replaced_1 = find_1.replace("Channels ", "")
replaced_2 = find_2.replace("Zero Count ", "")
replaced_3 = find_3.replace("Enclosure ", "")
replaced_4 = find_4.replace("Weight ", "")
replaced_5 = find_5.replace("Communication Protocol ", "")
replaced_6 = find_6.replace("Sample Volume ", "")

print(replaced_materials)
print(replaced_EF)
print(replaced_CE)
print(replaced_DW)
print(replaced_SR)
print(replaced_ECO)
print(replaced_MPNC)
print(replaced_USC)
print(replaced_P)
print(replaced_SPR)
print(replaced_LS)
print(replaced_LPC)
print(replaced_LD)
print(replaced_MST)
print(replaced_OS)
print(replaced_FCR)
print(replaced_PAP)
print(replaced_SIO)
print(replaced_STR)
print(replaced_SFR)
print(replaced_SetR)
print(replaced_SizR)
print(replaced_A)
print(replaced_C)
print(replaced_FO)
print(replaced_O)
print(replaced_1)
print(replaced_2)
print(replaced_3)
print(replaced_4)
print(replaced_5)


