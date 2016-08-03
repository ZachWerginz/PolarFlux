from zaw_coord import CRD
import kpvt_class
#import sunpy.wcs
import numpy as np
import uncertainties.unumpy as unp
import timeit

start = timeit.default_timer()

mdi = CRD('MDI\\fd_M_96m_01d.1222.0005.fits')
kpvt = CRD('512c_eo000_C1_19771001_2048.fits')
#spmg = CRD('spmg_eo100_C1_19920421_1700.fits')
#hmi = CRD('HMI\\hmi.M_720s.20100504_214800_TAI.1.magnetogram.fits')

#Heliographic testing
# lonh, lath = mdi.heliographic(mdi.im_raw.data)
# print ( "Array Latitude = %s Longitude = %s " %(lath[52,650], lonh[52,650]) )
# lonh, lath = mdi.heliographic(52,650)
# print ( "Coordinate Latitude = %s Longitude = %s " %(lath, lonh) )

#mdi.heliographic(mdi.im_raw.data)
# print ( "Array Latitude = %s Longitude = %s " %(lath[511,511], lonh[511,511]) )
# lonh, lath = mdi.heliographic(511, 511)
# print ( "Coordinate Latitude = %s Longitude = %s " %(lath, lonh) )


#print( sunpy.wcs.convert_hpc_hg(0*mdi.im_raw.scale[0].value, 0*mdi.im_raw.scale[1].value, b0_deg = mdi.im_raw.meta['B0'], l0_deg = mdi.im_raw.meta['L0']) )


#LOS testing
# corr = mdi.los_corr(x.im_raw.data)

#print( "Raw field = %s " %mdi.im_raw.data[750,750])
#print( "Corrected field = %s " %corr[750, 750])

#Element of Area testing
#areapix = mdi.area(238,238)
#print("%e" %areapix.value)
#print(mdi.eoa(52, 650))
#area = mdi.eoa(x.im_raw.data)
#print(area[52, 650])

#Magnetic flux testing
# fluxpix = mdi.magnetic_flux(238, 238)
# flux = mdi.magnetic_flux(x.im_raw.data)
# print(flux[750,750])
#print(area.nansum())

#MDI
lonh, lath = mdi.heliographic()
mdi.eoa()
mdi.magnetic_flux(unc=True)
mdi.mflux_corr_unc
vpc = np.where(np.logical_and(np.logical_and(np.logical_and(np.less(mdi.rg, mdi.rsun), np.greater(mdi.lath, 70.0)),np.isfinite(unp.nominal_values(mdi.im_corr_unc))),np.isfinite(mdi.area)))
print (vpc)
print( "Polar sum")
print( np.nansum(mdi.mflux_corr_unc[vpc]))
print("Raw fields")
print(mdi.im_raw_unc[vpc])
print("Corrected fields")
print(mdi.im_corr_unc[vpc])
print("Area")
print(mdi.area[vpc])
print("Corrected Flux")
print(mdi.mflux_corr_unc[vpc])

print (np.nansum(mdi.area))



#KPVT
#kpvt.heliographic(kpvt.im_raw.data)
#kpvt.los_corr(kpvt.im_raw.data)
#kpvt.eoa(kpvt.im_raw.data)
#kpvtflux = kpvt.magnetic_flux(kpvt.im_raw.data)
#print(np.nanmax(kpvt.area))
#print(kpvt.area.shape)
#print(np.nansum(kpvt.area))
#print(np.nanmax(kpvt.mflux_corr))

#SPMG
# spmg.heliographic(spmg.im_raw.data)
# spmg.los_corr(spmg.im_raw.data)
# spmgarea = spmg.eoa(spmg.im_raw.data)
# spmg.magnetic_flux(spmg.im_raw.data)
# #print(np.nanmax(spmgarea))
# print(spmgarea.nansum())

#HMI
#hmi.heliographic(hmi.im_raw.data)
#hmi.los_corr(hmi.im_raw.data)
#hmiarea = hmi.eoa(hmi.im_raw.data)
#hmi.magnetic_flux(hmi.im_raw.data)
#print(np.nansum(hmi.area))


stop = timeit.default_timer()
print ("Time = ", stop - start)