'''
Created on Jun 20, 2013

This file contains the classes that represent objects in the Google datastore

@author: Robert Tseng
'''

import model
from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop

class PersonModel(ndb.Model):
    """Model a person in the google datastore"""
    person = msgprop.MessageProperty(model.Person, indexed_fields=['name'])
