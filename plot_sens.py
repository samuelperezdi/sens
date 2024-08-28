import os
import sys
import glob
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import simple_norm

def plot_sensitivity_map(fits_id, output_folder='figures'):
    # create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # find the corresponding sens file
    sens_file = glob.glob(f'fits/*{fits_id}*sens*.fits.gz')
    if not sens_file:
        print(f"No sensitivity map found for fits_id: {fits_id}")
        return
    sens_file = sens_file[0]

    # read the fits file
    with fits.open(sens_file) as hdul:
        data = hdul[0].data

    # create the plot
    plt.figure(figsize=(10, 8))
    norm = simple_norm(data, 'log', percent=99)
    plt.imshow(data, cmap='inferno', norm=norm, origin='lower')
    plt.colorbar(label='Sensitivity')
    plt.title(f'Sensitivity Map: {os.path.basename(sens_file)}')

    # save the plot
    output_file = os.path.join(output_folder, f'{fits_id}_sens.pdf')
    plt.savefig(output_file)
    plt.close()

    print(f"Sensitivity map saved as {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python plot_sens.py <fits_id>")
        sys.exit(1)
    
    fits_id = sys.argv[1]
    plot_sensitivity_map(fits_id)