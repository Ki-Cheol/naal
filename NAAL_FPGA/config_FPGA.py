  
import os
import sys

import logging
import configparser
import logging
import numpy as np

configfile_name ="NAAL_config"


logger = logging.getLogger(__name__)            

if sys.platform.startswith('win'):
    config_dir = os.path.expanduser(os.path.join("~", ".nengo"))
else:
    config_dir = os.path.expanduser(os.path.join("~", ".config", "nengo"))

install_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
nengo_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir))
examples_dir = os.path.join(install_dir, "examples")

print(nengo_dir)
print(install_dir)

print(examples_dir)

#fpga_config = \
#    {'NAAL': os.path.join(nengo_dir, 'data', configfile_name),
#     'system': os.path.join(install_dir, 'fpga_config'),
#     'user': os.path.join(config_dir, "fpga_config"),
#     'project': os.path.abspath(os.path.join(os.curdir, 'fpga_config'))}
     
fpga_config = \
    {'NAAL': os.path.join(nengo_dir, 'data', configfile_name),
     'system': os.path.join(install_dir, configfile_name),
     'user': os.path.join(config_dir, "fpga_config"),
     'project': os.path.abspath(os.path.join(os.curdir, configfile_name))}

print(fpga_config)

FPGA_CONFIG_FILES = [fpga_config['NAAL'],
                     fpga_config['system'],
                     fpga_config['user'],
                     fpga_config['project']]


#config = configparser.ConfigParser()
##os.chdir(FPGA_CONFIG_FILES[3])
#config.read(FPGA_CONFIG_FILES[3])
#try :
#    host_config = config['host']
#except Exception as ex:
#    print('config_FPGA config error',ex)
#    exit()


def Is_FPGABOAD(fgpaboad_name):
    try :

        config = configparser.ConfigParser()
        config.read(FPGA_CONFIG_FILES[3])
        fpga_config = config[fgpaboad_name]
    except Exception as ex:
        print('config_FPGA config error',ex)
        exit()
    return fpga_config


def config_parser(key,value):
    config = configparser.ConfigParser()
    config.read(FPGA_CONFIG_FILES[3])
    try :
        key_config = config[key]
    except Exception as ex:
        print('config_FPGA config error',ex)
        exit()
    return key_config[value]


    




