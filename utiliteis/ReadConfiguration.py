

from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("C:\\Users\\HP\\PycharmProjects\\AbhayRoshniPOM\\configuration\\config.ini")
    return config.get(category, key)
