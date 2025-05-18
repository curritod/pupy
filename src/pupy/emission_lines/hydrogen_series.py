from ..constants import Rydberg_energy
from ..constants import Rydberg_H, h, c
from ..constants import electron_mass
from ..energy import eV

def rydberg_transition_energy(M, n1,n2):

	RM = 1/(1 + electron_mass/M)*Rydberg_energy

	Energy = RM * (1/n1**2 - 1/n2**2) * eV

	#Convert to meters
	wavelength = h*c / Energy
	
	return wavelength

def hydrogen_transition_energy(n1,n2):
	
	# Calculate energy in electron volts
	Energy = Rydberg_H * (1/n1**2 - 1/n2**2) * eV
	
	#Convert to meters
	wavelength = h*c / Energy
	
	return wavelength

#Lyman series
Lyman_alpha = hydrogen_transition_energy(1,2)
Lyman_beta  = hydrogen_transition_energy(1,2)
Lyman_gamma = hydrogen_transition_energy(1,3)

#Balmer series
Balmer_alpha = hydrogen_transition_energy(2,3)
Balmer_beta  = hydrogen_transition_energy(2,4)
Balmer_gamma = hydrogen_transition_energy(2,5)

Halpha = Balmer_alpha 
Hbeta  = Balmer_beta  
Hgamma = Balmer_gamma 

#Paschen Series
Paschen_alpha = hydrogen_transition_energy(3,4)
Paschen_beta  = hydrogen_transition_energy(3,5)
Paschen_gamma = hydrogen_transition_energy(3,6)

#Brackett Series
Brackett_alpha = hydrogen_transition_energy(4,5)
Brackett_beta  = hydrogen_transition_energy(4,6)
Brackett_gamma = hydrogen_transition_energy(4,7)

