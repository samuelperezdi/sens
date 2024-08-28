import requests
import argparse
from src.data import get_data

def run():
    url = 'http://cda.cfa.harvard.edu/csccli/retrieve'

    file_path = './output/'
    filename = 'stack_ids.txt'

    number_of_identifiers = 0
    number_of_identifiers_per_request = 3

    packageset = ''
    
    # The file below contains the list of detection IDs
    separator = ''
    with open(filename, 'r') as input:
        # read header line and ignore it
        input.readline()
    
        while True:
            line = input.readline()
            if '' == line:
                break
            line = line.rstrip()

            number_of_identifiers += 1
        
            # Here we specify which datatypes to download
            packageset += separator + line + '/sensity/b'
            separator = ','
            #packageset += separator + line + '/rmf/b'
            #separator = ','
            #packageset += separator + line + '/arf/b'
            #separator = ','
        
            if 0 == number_of_identifiers % number_of_identifiers_per_request:
                retrieve(url, packageset, int(number_of_identifiers / number_of_identifiers_per_request), file_path)

                packageset = ''
                separator = ''
            
                # Print progress with
                # the current set thresholds of S/N, etc.
                #print(number_of_identifiers)
        

        if 0 != number_of_identifiers % number_of_identifiers_per_request:
            retrieve(url, packageset, int(number_of_identifiers / number_of_identifiers_per_request)+1, file_path)

    return 1

def retrieve(url, packageset, idx, file_path):
    # This function retrieves the data and saves them in tarballs
    print("retrieving: ", packageset)
    response = requests.get(url, params={
        'version': 'rel2.1',  # Current version of the CSC
        'packageset': packageset
    })
    
    with open(file_path+f'package.{idx}.tar', 'wb') as output:
        output.write(response.content)
    print('created ', file_path+f'package.{idx}.tar')
    return 1

def main():
    parser = argparse.ArgumentParser(description='process stack_ids for retrieving sens maps')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # get_data command
    get_data_parser = subparsers.add_parser('get_data', help='get the data based on your separation and theta')
    get_data_parser.add_argument('--separation', type=float, required=True, help='Separation threshold')
    get_data_parser.add_argument('--theta_min', type=float, required=True, help='Minimum theta value')
    get_data_parser.add_argument('--theta_max', type=float, required=True, help='Maximum theta value')

    # retrieve command (placeholder)
    retrieve_parser = subparsers.add_parser('retrieve', help='Retrieve data')

    args = parser.parse_args()

    if args.command == 'get_data':
        get_data(args.separation, [args.theta_min, args.theta_max])
    elif args.command == 'retrieve':
        run()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
