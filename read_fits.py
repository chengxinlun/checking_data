from astropy.io import fits
import numpy as np
import pickle


def read_fits():
    fit = fits.open('peak_vel_cat.fits')
    data_table = fit[1].data
    columns = fit[1].columns.names
    rmid = data_table["RMID"]
    for each in columns:
        if each == "RMID":
            continue
        file_name = "data/" + str(each) + ".pkl"
        file_out = open(file_name, "wb")
        pickle.dump(dict(zip(rmid, data_table[each])), file_out)
        file_out.close()
    fit.close()


read_fits()
