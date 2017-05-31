import pprint
import numpy as np
import matplotlib.pyplot as plt


def fill_missing_values_to_zero(df):

    df = df.fillna(np.nan).dropna(axis=0, how='all')
    df = df.dropna(axis=1, how='all')
    pprint.pprint("shape: " + str(df.shape))
    df = df.drop('_id.$oid', axis=1)
    df = df.fillna(0)
    df2 = df.ix[:, 0:10]
    del df['droidmon.api.dalvik_system_DexFile_loadDex']
    del df['droidmon.api.android_util_Base64_encode']
    del df['droidmon.api.dalvik_system_DexFile_openDexFile']
    del df['droidmon.api.android_webkit_WebView_setWebViewClient']
    del df['droidmon.api.java_io_Fiie_exists']
    del df['droidmon.api.libcore_io_IoBridge_opee']
    del df['droidmon.api.dalvik_system_DexFile_dalvik_system_DexFile']
    del df['droidmon.api.javax_crypto_Cipher_doFinal']
    del df['droidmon.api.android_location_Location_getLatitude']
    del df['droidmon.api.java_net_ProxySelectorImpl_select']
    #plot_corr(df)
    return df


def plot_corr(df,size=10):
    '''Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot'''

    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.show()






