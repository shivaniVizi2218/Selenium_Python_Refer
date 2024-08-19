import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
# config.read('../../Configurations/config.ini')

class ReadConfig:
    @staticmethod
    def getapplicationuRL():
        url = config.get('common info', 'baseURL')
        return url


class ReadprodConfig:
    @staticmethod
    def getproduRL():
        url1 = config.get('common info', 'prod_url')
        return url1


class  ReadEOSurlConfig:
    @staticmethod
    def getEOSuRL():
        url2 = config.get('common info', 'eos_baseUrl2')
        return url2


class ReadEOStesturlConfig:
    @staticmethod
    def getEOStestuRL():
        url3 = config.get('common info', 'eos_baseUrl1')
        return url3
class  ReadEOSdbConfig:
    @staticmethod
    def getEOSdb_server():
        server = config.get('common info', 'db_server')
        return server

    @staticmethod
    def getEOSdb_database():
        database = config.get('common info', 'db_database_commonDB')
        return database

    @staticmethod
    def getEOSdb_user():
        user = config.get('common info', 'db_user')
        return user

    @staticmethod
    def getEOSdb_pass():
        password = config.get('common info', 'db_pass')
        return password