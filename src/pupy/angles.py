import numpy as np

# Degree <-> radian
deg_to_rad = np.pi/180
rad_to_deg = 1/deg_to_rad

# Radian <-> arcsecond
rad_to_as = (180/np.pi)*60*60
as_to_rad = 1/rad_to_as

# Radian <-> miliarcsecond
rad_to_mas = (180/np.pi)*60*60*1e3
mas_to_rad = 1/rad_to_mas

# Radians <-> microas
rad_to_microas = (180/np.pi)*60*60*1e6
microas_to_rad = 1/rad_to_microas

# arcsecond <-> degree
as_to_deg = as_to_rad*rad_to_deg
deg_to_as = 1/as_to_deg

# miliarcsecond <-> degree
mas_to_deg = mas_to_rad*rad_to_deg
deg_to_mas = 1/mas_to_deg

# microarcsecond <-> degree
microas_to_deg = microas_to_rad*rad_to_deg
deg_to_microas = 1/microas_to_deg
