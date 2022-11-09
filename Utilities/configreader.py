from configparser import ConfigParser


def ConfigReader(section, Key):
    config = ConfigParser()
    config.read("C:\\Users\\e3t\\Downloads\\SPRINT2\\SPRINT2\\ConfigurationData\\config.ini")
    return config.get(section, Key)