import numpy as np
import matplotlib.pyplot as plt

def result(data_missing, data_tr, imp, prefix = ''):
    rm_true = []
    lstat_true = []
    rad_true = []
    crim_true = []
    ptr_true = []

    rm_imp = []
    lstat_imp = []
    rad_imp = []
    crim_imp = []
    ptr_imp = []

    rmidx = np.where(data_missing['RM'].isnull()==True)[0]
    lsidx = np.where(data_missing['LSTAT'].isnull()==True)[0]
    raidx = np.where(data_missing['RAD'].isnull()==True)[0]
    cridx = np.where(data_missing['CRIM'].isnull()==True)[0]
    ptidx = np.where(data_missing['PTRATIO'].isnull()==True)[0]

    for i in rmidx:
        rm_true.append(data_tr.loc[i,'RM'])
        rm_imp.append(imp.loc[i, prefix+'RM'])

    for i in lsidx:
        lstat_true.append(data_tr.loc[i,'LSTAT'])
        lstat_imp.append(imp.loc[i,prefix+'LSTAT'])

    for i in raidx:
        rad_true.append(data_tr.loc[i,'RAD'])
        rad_imp.append(imp.loc[i,prefix+'RAD'])

    for i in cridx:
        crim_true.append(data_tr.loc[i,'CRIM'])
        crim_imp.append(imp.loc[i,prefix+'CRIM'])

    for i in ptidx:
        ptr_true.append(data_tr.loc[i,'PTRATIO'])
        ptr_imp.append(imp.loc[i,prefix+'PTRATIO'])

    plt.figure(figsize = (30,4))
    plt.subplot(1, 5, 1)

    x = np.linspace(min(rm_true), max(rm_true))
    plt.scatter(rm_true, rm_imp)
    plt.plot(x, x, 'r--')


    plt.subplot(1, 5, 2)

    x = np.linspace(min(lstat_true), max(lstat_true))
    plt.scatter(lstat_true, lstat_imp)
    plt.plot(x, x, 'r--')


    plt.subplot(1, 5, 3)

    x = np.linspace(min(rad_true), max(rad_true))
    plt.scatter(rad_true, rad_imp)
    plt.plot(x, x, 'r--')


    plt.subplot(1, 5, 4)

    x = np.linspace(min(crim_true), max(crim_true))
    plt.scatter(crim_true, crim_imp)
    plt.plot(x, x, 'r--')


    plt.subplot(1, 5, 5)

    x = np.linspace(min(ptr_true), max(ptr_true))
    plt.scatter(ptr_true, ptr_imp)
    plt.plot(x, x, 'r--')
    plt.show()