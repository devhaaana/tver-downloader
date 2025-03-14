import time
import logging
import warnings
warnings.filterwarnings(action='ignore')

from tver import *

def execution_time_log(filepath='execution_time.log', mode='update'):
    if mode == 'update':
        logging.basicConfig(
            filename = filepath,
            level = logging.INFO,
            format = '%(message)s'
        )
        # recent_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        recent_time = datetime.now().strftime("%a %b %d %H:%M:%S")
        logging.info(f"[Last login] {recent_time}")
        
    elif mode == 'read':
        try:
            with open(filepath, 'r') as file:
                lines = file.readlines()
                if lines:
                    return lines[-1].strip()
                else:
                    return None
        except FileNotFoundError:
            return None
        
def start_program():
    last_execution_time = execution_time_log(filepath='execution_time.log', mode='read')
    
    sep_bar = f'==========================================================='
    tab = '    '
    tver_ascii = f'''
{sep_bar}
{tab}████████╗██╗   ██╗███████╗██████╗ ██████╗ ██╗   ██╗
{tab}╚══██╔══╝██║   ██║██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
{tab}   ██║   ██║   ██║█████╗  ██████╔╝██████╔╝ ╚████╔╝ 
{tab}   ██║   ╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔═══╝   ╚██╔╝  
{tab}   ██║    ╚████╔╝ ███████╗██║  ██║██║        ██║   
{tab}   ╚═╝     ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝        ╚═╝   

{tab}Copyright 2025. devhaaana All rights reserved.
'''
    print(convert_text_color(text=f'{tver_ascii}', color='green'))
    if last_execution_time != None:
        print(convert_text_color(text=f'{tab}{last_execution_time}', color='green'))
    print(convert_text_color(text=f'{sep_bar}', color='green'))
    execution_time_log(filepath='execution_time.log', mode='update')

def main():
    start_time = time.time()
    start_program()
    downloader = Tver_Downloader()
    downloader.run_process()
    print(f"Execution Time: {time.time() - start_time:.4f} sec")


if __name__ == "__main__":
    main()