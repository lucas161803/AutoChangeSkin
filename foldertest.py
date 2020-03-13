import read_config, os
config = read_config.ReadConfig().config
print(config['test']['folder1'])