import read_config, os, alter_file
config = read_config.ReadConfig().config
print(config['test']['folder1'])
alter_file.alter("file1.txt", "測試", "python")