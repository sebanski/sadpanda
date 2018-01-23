'''
testing for sadpanda.structs.datastore.py
'''

import unittest

from sadpanda.structs.datastore import DataStore

class DataStoreTest(unittest.TestCase):
    def setUp(self):
        self.datastore = DataStore()

    def tearDown(self):
    	pass

    def test_empty_datastore(self):
    	self.assertEqual(self.datastore.datastore, [])

    def test_add_item(self):
    	item = "this is a random value being added into the datastore."
    	self.datastore.add_item(item)
    	self.assertEqual(self.datastore.get_previous_item(), item)

    #def test_has_age_in_dog_years(self):
    #    self.assertEqual(self.person.dog_years, self.person.age / 7)

