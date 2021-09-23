

from werkzeug.datastructures import Headers
from pip._vendor import requests
import json
import time
from requests.auth import HTTPBasicAuth
import pygeohash as pgh
from datetime import datetime
from enum import Enum
from flask import Flask, json,request, jsonify
from typing import List
from datetimerange import DateTimeRange
import pymongo
from pymongo import MongoClient
import dns
from bson import json_util

headers= {'X-M2M-Origin': 'act_test_prod', 'X-M2M-RI': str(int(time.time())), 'content-Type': 'application/vnd.onem2m-res+json;ty=4',
        'Accept': 'application/json'}











