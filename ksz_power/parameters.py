import numpy as np

#######################################
########### System settings ###########
#######################################
n_threads = 1
folder = './'
outroot = folder+"/kSZ_power_spectrum"  # root of all output files
debug = True
late_time = True #if you want to compute the late-time component of the kSZ too

##########################
#### Cosmo parameters ####
##########################
h = 0.6774000
Om_0 = 0.309
Ol_0 = 0.691
Ob_0 = 0.049
obh2 = Ob_0 * h**2
och2 = (Om_0 - Ob_0) * h**2
A_s = 2.139e-9
n_s = 0.9677
T_cmb = 2.7255
Yp = 0.2453
Xp       = 1-Yp
mh       = 1.67e-24 #gr
rhoc = 1.879e-29 *h**2 #gr cm-3
nh = Xp*Ob_0*rhoc/mh *1e6  # m-3
s_T = 6.6524616e-29     # sigma_thomson in m^2
xe_recomb = 1.7e-4

AU = 149597870.7       # Astronomical Unit in [km]
Mpckm = 1e6 * AU / np.tan(1. / 3600. * np.pi / 180.)  # one Mpc in [km]
Mpcm = Mpckm * 1e3

T_CMB=2.7260 #K
T_CMB_uK=T_CMB*1e6  

###################
#### Constants ####
###################
s_T = 6.6524616e-29     # sigma_thomson in SI units [m^2]
c = 299792458.          # speed of light in SI units [m.s-1]
AU = 149597870.7       # Astronomical Unit in [km]
Mpckm = 1e6 * AU / np.tan(1. / 3600. * np.pi / 180.)  # one Mpc in [km]
Mpcm = Mpckm * 1e3                          # one Mpc in [m]

#######################################
###### REIONISATION PARAMETERS ########
#######################################

# parameters for reionisation history
zend = 5.5
zre = 7.
z_early = 20.

# reionisation of Helium
HeliumI = True
HeliumII = False
fH = 1.
if HeliumI:
	not4 = 3.9715 #eta
	fHe = Yp/(not4*(1-Yp))
	fH=1+fHe
helium_fullreion_redshift = 3.5
helium_fullreion_start = 5.0
helium_fullreion_deltaredshift = 0.5

# parameters for Pee
alpha0 = 3.7
kappa = 0.10

#########################################
#### Settings for C_ells computation ####
#########################################
### linear ell range for kSZ C_ells
ell_min_kSZ = 1.
ell_max_kSZ = 10000.
n_ells_kSZ = 60
if debug:
	n_ells_kSZ = 2	

########################################
#### Integration/precision settings ####
########################################
### Settings for theta integration
num_th = 50
th_integ = np.linspace(0.000001,np.pi*0.999999,num_th)
mu = np.cos(th_integ)#cos(k.k')
### Settings for k' (=kp) integration
# k' array in [Mpc-1] - over which you integrate
min_logkp = -5.
max_logkp = 1.5
dlogkp = 0.05
kp_integ = np.logspace(
    min_logkp,
    max_logkp,
    int((max_logkp - min_logkp) / dlogkp) + 1
)
### Settings for z integration
z_min = 0.0015
z_piv = 1.
z_max = 20.
dlogz = 0.05
dz = 0.05
if late_time:
    z_integ = np.concatenate(
        (
            np.logspace(np.log10(z_min),np.log10(z_piv),int((np.log10(z_piv) - np.log10(z_min)) / dlogz) + 1),
            np.arange(z_piv,10.,step=dz),
            np.arange(10,z_max+0.5,step=0.5)
        )
    )
else:
    z_integ = np.concatenate(
        (np.arange(zend-1.,10.,step=dz),
         np.arange(10,z_max+0.5,step=0.5))
    )

### Setting for P(k) computation
kmin_pk = 10**min_logkp
kmax_pk = 10**max_logkp
nk_pk = 10001
### ell range for TT, EE, TE C_ells
ell_max_CMB = 2000

