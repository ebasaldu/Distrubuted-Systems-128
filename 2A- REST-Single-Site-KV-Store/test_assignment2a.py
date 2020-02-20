################### 
# Course: CMPS128
# Date: Spring 2019
# Assignment: #2A
# Author: Reza NasiriGerdeh
# Email: rnasirig@ucsc.edu
###################

import unittest
import subprocess
import requests
import sys
import random
import time

hostname = 'localhost'  # Windows and Mac users can change this to the docker vm ip
portNumber = '8082'
baseUrl = 'http://' + hostname + ":" + portNumber

class TestHW2(unittest.TestCase):

    def test_a_get_nonexisting_key(self):
        response = requests.get( baseUrl + '/key-value-store/subject1')
        responseInJson = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(responseInJson['doesExist'], False)
        self.assertEqual(responseInJson['message'], 'Error in GET')
        self.assertEqual(responseInJson['error'], 'Key does not exist')

    def test_b_delete_nonexisting_key(self):
        response = requests.delete( baseUrl + '/key-value-store/subject1')
        responseInJson = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(responseInJson['doesExist'], False)
        self.assertEqual(responseInJson['message'], 'Error in DELETE')
        self.assertEqual(responseInJson['error'], 'Key does not exist')


    def test_c_put_nonexistent_key(self):
        response = requests.put(baseUrl + '/key-value-store/' + "subject1", json={'value': "Data Structures"})
        responseInJson = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(responseInJson['message'], 'Added successfully')
        self.assertEqual(responseInJson['replaced'], False)


    def test_d_get_after_put_nonexisting_key(self):
        response = requests.get( baseUrl + '/key-value-store/subject1')
        responseInJson = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseInJson['doesExist'], True)
        self.assertEqual(responseInJson['message'], 'Retrieved successfully')
        self.assertEqual(responseInJson['value'], 'Data Structures')

    def test_e_put_existent_key(self):
        response = requests.put(baseUrl + '/key-value-store/' + "subject1", json={'value': "Distributed Systems"})
        responseInJson = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseInJson['message'], 'Updated successfully')
        self.assertEqual(responseInJson['replaced'], True)

    def test_f_get_after_put_existing_key(self):
        response = requests.get( baseUrl + '/key-value-store/subject1')
        responseInJson = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseInJson['doesExist'], True)
        self.assertEqual(responseInJson['message'], 'Retrieved successfully')
        self.assertEqual(responseInJson['value'], 'Distributed Systems')


    def test_g_delete_existing_key(self):
        response = requests.delete( baseUrl + '/key-value-store/subject1')
        responseInJson = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseInJson['doesExist'], True)
        self.assertEqual(responseInJson['message'], 'Deleted successfully')

    def test_h_get_after_delete_existing_key(self):
        response = requests.get( baseUrl + '/key-value-store/subject1')
        responseInJson = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(responseInJson['doesExist'], False)
        self.assertEqual(responseInJson['message'], 'Error in GET')
        self.assertEqual(responseInJson['error'], 'Key does not exist')

    def test_i_put_key_too_long(self):
        tooLongKey = '6TLxbmwMTN4hX7L0QX5_NflWH0QKfrTlzcuM5PUQHS52___lCizKbEMxLZHhtfww3KcMoboDLjB6mw_wFfEz5v_TtHqvGOZnk4_8aqHga79BaHXzpU9_IRbdjYdQutAU0HEuji6Ny1Ol_MSaBF4JdT0aiG_N7xAkoPH3AlmVqDN45KDGBz7_YHrLnbLEK11SQxZcKXbFomh9JpH_sbqXIaifqOy4g06Ab0q3WkNfVzx7H0hGhNlkINf5PF12'
        value = "haha"
        response = requests.put( baseUrl + '/key-value-store/' + tooLongKey, json={'value': value})

        responseInJson = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(responseInJson['message'], 'Error in PUT')
        self.assertEqual(responseInJson['error'], 'Key is too long')

    def test_j_put_key_with_no_value(self):
        response = requests.put(baseUrl + '/key-value-store/subject1', json={})
        responseInJson = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(responseInJson['message'], 'Error in PUT')
        self.assertEqual(responseInJson['error'], 'Value is missing')

if __name__ == '__main__':
    unittest.main()
