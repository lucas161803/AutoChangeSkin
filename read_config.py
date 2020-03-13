import configparser
config = configparser.ConfigParser()
config.read('config.ini')
config.sections()
print(config.sections())

path = config['default']['logic_root']+config['logic']['PlateLogic']
print(path)