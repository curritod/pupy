import numpy as np

c 			= 299792458			# m/s [1]
h 			= 6.62607015e-34	# J s [1]
hbar 		= h/(2*np.pi)		# J s			 
alpha 		= 1/137.035999084   # n.u. [1] 
G 			= 6.67430e-11 		# m^3 kg^-1 s^-2 [1]
Navogadro 	= 6.02214076e-23 	# mol-1 [1]
kB 			= 1.380649e-23		# J K^-1 [1]	

electron_charge	= 1.602176634e-19   # C [1]
electron_mass	= 9.1093837015e-31	# kg [1]
proton_mass     = 1.67262192369e-27 # kg [1] 

eps_0 = 8.8541878128e-12 # F m^-1

Rydberg_energy = 13.605693122994 # eV [1]
Rydberg_H = proton_mass/(electron_mass + proton_mass) * Rydberg_energy