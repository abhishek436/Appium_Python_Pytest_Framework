from configparser import ConfigParser
def readConfig(section, key):
    config = ConfigParser()
    config.read("..\\Configuration_Data\\conf.ini")
    return config.get(section, key)