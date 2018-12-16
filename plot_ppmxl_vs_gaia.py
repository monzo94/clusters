import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


DEG_TO_MAS = 3600000.  # 1 deg = 3600000 mas


def load_data():
    with fits.open('ivanov_2_ppmxl.fits') as hdul:
        ppxml_data = hdul[1].data

    gaia_data = np.genfromtxt('ivanov_2_gaiadr2.csv', skip_header=1, delimiter=',', unpack=True)
    return ppxml_data, gaia_data


def plot_positions(ppxml_data, gaia_data):
    plt.figure(0, figsize=(12, 6))
    plt.clf()
    plt.title('PPMXL vs Gaia DR2 positions')

    # PPMXL
    plt.subplot(121)
    plt.plot(ppxml_data['raj2000'], ppxml_data['dej2000'], 'k.', markersize=4)
    plt.errorbar(ppxml_data['raj2000'], ppxml_data['dej2000'],
                 xerr=ppxml_data['e_raepRA'], yerr=ppxml_data['e_deepDE'],
                 linestyle='', color='lightblue', marker='', zorder=0)
    plt.xlabel('ra (deg)')
    plt.ylabel('dec (deg)')

    # Gaia DR2 (filtering by G <= 19)
    plt.subplot(122)
    plt.plot(gaia_data[0], gaia_data[2], 'k.', markersize=4)
    # ra and dec errors are in mas, not deg
    plt.errorbar(gaia_data[0], gaia_data[2],
                 xerr=gaia_data[1] / DEG_TO_MAS, yerr=gaia_data[3] / DEG_TO_MAS,
                 linestyle='', color='lightblue', marker='', zorder=0)
    plt.xlabel('ra (deg)')
    plt.ylabel('dec (deg)')

    plt.tight_layout()

    plt.show()
    plt.close()


def plot_motions(ppxml_data, gaia_data):
    plt.figure(0, figsize=(12, 6))
    plt.clf()
    plt.title('PPMXL vs Gaia DR2 proper motions')

    # PPMXL
    plt.subplot(121)
    plt.plot(ppxml_data['pmRA'], ppxml_data['pmDE'], 'k.', markersize=4)
    plt.errorbar(ppxml_data['pmRA'], ppxml_data['pmDE'],
                 xerr=ppxml_data['e_pmRA'], yerr=ppxml_data['e_pmDE'],
                 linestyle='', color='lightblue', marker='', zorder=0)
    plt.xlabel('pmra (deg/yr)')
    plt.ylabel('pmdec (deg/yr)')
    plt.xlim(-0.00001, 0.00001)
    plt.ylim(-0.00001, 0.00001)

    # Gaia DR2
    plt.subplot(122)
    # In Gaia DR2, pmra and pmdec is given in mas/yr, so convert it to deg/yr
    plt.plot(gaia_data[4] / DEG_TO_MAS, gaia_data[6] / DEG_TO_MAS, 'k.', markersize=4)
    plt.errorbar(gaia_data[4] / DEG_TO_MAS, gaia_data[6] / DEG_TO_MAS,
                 xerr=gaia_data[5] / DEG_TO_MAS, yerr=gaia_data[7] / DEG_TO_MAS,
                 linestyle='', color='lightblue', marker='', zorder=0)
    plt.xlabel('pmra (deg/yr)')
    plt.ylabel('pmdec (deg/yr)')
    plt.xlim(-0.00001, 0.00001)
    plt.ylim(-0.00001, 0.00001)

    plt.tight_layout()

    plt.show()
    plt.close()


def main():
    ppxml_data, gaia_data = load_data()
    plot_positions(ppxml_data, gaia_data)
    plot_motions(ppxml_data, gaia_data)


if __name__ == "__main__":
    main()
