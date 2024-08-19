from json import dumps
from logging import Logger
from random import random
from uuid import uuid4
#from clients.people.base_client import BaseClient
#from config import BASE_URI
#import utilities.file_reader
import utilities
from Base.custom_code import Custom_code
from utilities.CustomLogger import custlogger

from eospageObjects.file_reader import FileReader


class CreatePackage(Custom_code):
    LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base_url = "http://uat.nextgen.lasership.com/json/reply/Package[]"

    # def create_person(self, body=None):
    #     last_name, response = self.__create_person_with_unique_last_name(body)
    #     return last_name, response

    def create_package(self, body=None):

        if body is None:
            print("body is None")
            # last_name = f'User {str(uuid4())}'
            payload = dumps({
                'fname': 'New',
                'lname': "barcode"
            })
        else:
            barcode = body['barcode']
            payload = dumps(body)

        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        }
        request = utilities.request.APIRequest

        response = self.request.post(self.base_url, payload, self.headers)
        return response

    def create_data_in_package_payload(self):
        payload = FileReader.read_file('create_package.json')

        random_no = random.randint(1000, 50000)
        barcode = f'1LSCXNU{random_no}'

        payload['Barcode'] = barcode
        print('barcode:'+barcode)
        yield payload
        return payload

