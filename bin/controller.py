import os
import sys 
import shutil
from datetime import datetime, timedelta

from config import Config
from parse_args import parse_args
from logger import set_logger
from assets import get_asset, get_asset_history, dict_to_json

def main():
    args = parse_args('Coincap_controller', 'Downloading Crypto currency data using CoinCap API.')
    
    # Read the Configuration file
    config_parser = Config(args.get('config_file'))
    config_var = config_parser.get(args['section'])
    
    # Logging level setup
    log_domain = 'CoinCap_{}'.format(args['section'] + '_' + args.get('asset'))
    logger = set_logger(args.get('log_level'), log_domain, print_log=args['print_log'], log_path = config_var.get('log_path'))
    logger.debug("args: {}".format(args))

    try:     
        # Makes data directory if not exists
        if os.path.exists(config_var.get('file_path')):
            if not os.listdir(config_var.get('file_path')):
                logger.info(f"No files in directory: {config_var.get('file_path')}")
            elif len(os.listdir(config_var.get('file_path'))) >= 10:
                shutil.make_archive(config_var.get('archive_path') + str(datetime.now().strftime("%Y%m%d%H%M%S")),
                                    'zip',
                                    config_var.get('file_path')
                                    )
                logger.info(f"Archived files in directory: {config_var.get('file_path')}")
                shutil.rmtree(config_var.get('file_path'))
        os.makedirs(config_var.get('file_path'), exist_ok=True)
       
        # Executing CoinCap API Session
        logger.info("Executing CoinCap Session...")

        if args.get('section') in ('ASSET','EXCHANGES','MARKETS','RATES'):
            response_json = get_asset(key=config_var.get('api_key'),
                                      url=config_var.get('base_url') + args.get('asset'),
                                      encoding=config_var.get('accepted_encoding')
                                      )         
        elif args.get('section') == 'ASSET_HISTORY':
            response_json = get_asset_history(key=config_var.get('api_key'), 
                                              url=config_var.get('base_url') + args.get('asset') + "/history", 
                                              encoding=config_var.get('accepted_encoding'),
                                              start=args.get('startdate'), #.isoformat() + "Z",
                                              end=args.get('enddate'), #.isoformat() + "Z",
                                              interval=args.get('interval')
                                              )
        elif args.get('section') == 'ASSET_MARKETS':
            response_json = get_asset(key=config_var.get('api_key'), 
                                      url=config_var.get('base_url') + args.get('asset') + "/markets", 
                                      encoding=config_var.get('accepted_encoding')
                                      )
        if "Error:" in response_json:
            logger.info(f"{response_json}")
        elif response_json is None:
            logger.info('Error: None Object returned')
        else:
            dict_to_json(response_json, config_var.get('file_path') + args.get('asset') + config_var.get('file_name'))

        logger.info('Data Collection Complete.' + '\n' + 'Execution Complete.')

        sys.exit(0)

    except Exception as e:
        logger.info(f"Error: {str(e)}")    
        sys.exit(1)

if __name__ == '__main__':
    main()