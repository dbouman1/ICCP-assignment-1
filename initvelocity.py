## Import libraries
import numpy as np
## Import functions
from normalize_momentum import normalize_momentum
## Define function
def initvelocity( N, T):
	velocity = np.zeros((N,3),dtype=float) 	# Initialize velocity array
	## Assign velocity from uniform random number
	for ii in xrange(0,N):
		velocity[ii,0] = np.sqrt(-2*np.log(np.random.random()))
		velocity[ii,1] = np.sqrt(-2*np.log(np.random.random()))
		velocity[ii,2] = np.sqrt(-2*np.log(np.random.random()))
	velocity = normalize_momentum(N, velocity,T)

	return velocity;