
# Script igg.py yang telah dikonversi ke Python 2
from multiprocessing.dummy import Pool as ThreadPool
import urlparse
import requests
import json

def example():
    print "Script ini sekarang berjalan di Python 2"
    username = raw_input("Masukkan username: ")
    print "Username yang dimasukkan: {}".format(username)

example()
