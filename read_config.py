from configparser import ConfigParser, ExtendedInterpolation
class ReadConfig():
    def __init__(self):
        cfg = ConfigParser(interpolation=ExtendedInterpolation())
        cfg.read('config.ini', encoding='utf-8')
        self.config = cfg


if __name__ == "__main__":
    config = ReadConfig().config
    config.sections()
    print(config.sections())

    path = config['default']['logic_root']+config['logic']['PlateLogic']
    print(path)

    print(config['test']['folder1'])