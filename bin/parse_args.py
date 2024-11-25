import argparse
import os
import sys
from datetime import datetime, timedelta

def parse_args(prog, description):
    parser = argparse.ArgumentParser(description=description, prog=prog, epilog='The data will be first loaded to a Flat File')
    parser.add_argument('-s', required=True, metavar='SECTION', dest='section', help='The section name of configuration file, which will be used to get the object information.')    
    parser.add_argument('-a', '--asset', required=True, type=str, help='The asset name which will be used to get the object information.')
    parser.add_argument('-sd', '--startdate', required=False, default=(datetime.now() - timedelta(days=5)).strftime('%Y-%m-%dT%H:%M:%SZ'), type=str, help='The Start date which will be use to get the object information. Default Start date is today minus three days')    
    parser.add_argument('-ed', '--enddate', required=False, default=datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'), type=str, help='The End date which will be use to get the object information. Default End date is current datetime')
    parser.add_argument('-it', '--interval', required=False, default='m30', type=str, choices=['m1', 'm5', 'm15', 'm30', 'h1', 'h2', 'h6', 'h12', 'd1'], help='The interval which will be use to get the object information. Default interval is m30, m = minute, h = hour and d = day.')                
    parser.add_argument('-l', required=False, default='info', metavar='LOG_LEVEL', dest='log_level', choices=['info', 'debug', 'warning', 'error'], help='Logging level, "info" by default.')
    parser.add_argument('-p', required=False, metavar='CONFIG_FILE', dest='config_file', default='config.ini', help='The configuration file to be used. If not specified, the program will try to find it with "./config.ini"')
    parser.add_argument('--print_log', required=False, dest='print_log', action='store_true', help='Whether print the log to console. False by default')

    
    args = vars(parser.parse_args())
     
    # Check the if the configuration file exists
    file_name = args.get('config_file')
    dirname = os.path.dirname(file_name)
    
    if not dirname:
        abslute_path = os.path.abspath(sys.argv[0])
        args['config_file'] = os.path.join(os.path.dirname(abslute_path), 'config.ini')
    elif not os.path.isdir(dirname): 
        raise FileNotFoundError('No such directory {}'.format(dirname))
    elif not os.path.isfile(file_name):
        raise FileNotFoundError('No such file {}'.format(file_name))
    
    if not os.path.isfile(args['config_file']):
        raise FileNotFoundError(f'Cannot find config file {file_name}')
    
    return args


if __name__ == '__main__':
    print(parse_args('test', 'This is a test'))
