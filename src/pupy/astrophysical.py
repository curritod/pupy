import numpy as np
from .prefixes import *
from .constants import G,c

#Units
astronomical_unit   = 149597870700 # m [1]

parsec              = (3600*180/np.pi)*astronomical_unit
microparsec         = micro*parsec
miliparsec          = mili*parsec
kiloparsec          = kilo*parsec
megaparsec          = mega*parsec
gigaparsec          = giga*parsec

#The sun!
Msun = 1.98841e30 	# kg [1]
Rsun = 6.957e8		# m  [1]
Tsun = 5772			# K  [1]
Lsun = 3.828e26		# W  [1]

#The earth!
Mearth = 5.97217e24 # kg [1]
Rearth = 6.3781e6	# m  [1]

#The planets! - needs to be cross checked!
mercury_radius      = 2.4397 # m [Wikipedia]
venus_radius        = 6.0518 # m [Wikipedia] 
moon_radius         = 1.7374 # m [Wikipedia]
mars_radius         = 3.3895 # m [Wikipedia]
jupiter_radius      = 69.911 # m [Wikipedia]
saturn_radius       = 58.232 # m [Wikipedia]
uranus_radius       = 25.362 # m [Wikipedia] 
neptune_radius      = 24.622 # m [Wikipedia]

mercury_mass    = 3.285e23	# m [Wikipedia]
venus_mass    	= 4.867e24	# m [Wikipedia]
moon_mass       = 7.346e22	# m [Wikipedia]
mars_mass		= 6.417e23	# m [Wikipedia]
jupiter_mass    = 1.898e27	# m [Wikipedia]
saturn_mass     = 5.683e26	# m [Wikipedia]
uranus_mass     = 8.681e25	# m [Wikipedia]
neptune_mass    = 1.024e26	# m [Wikipedia]

#The galaxy - to be completed!



#The center of the galaxy
R0  = 8277.09055*parsec 	# m  [Stefan Gillessen]
Mbh = 4.297017427e6*Msun	# kg [Stefan Gillessen]
Rg  = G*Mbh/c**2 
