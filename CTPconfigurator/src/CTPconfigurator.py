'''
Created on Aug 31, 2017

@author: paul
'''

from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import csv

ENV = Environment(loader=FileSystemLoader('.'))

with open("CTP.yaml") as _:
    config = yaml.load(_)

trainAssetToNetwork = csv.DictReader(open("CTPassetToNetwork.csv"))

trainVars = {}

trainVars['TRAIN']  = int(sys.argv[1])
trainVars['SIDE']  = sys.argv[2].upper()

for car in trainAssetToNetwork:
    car['Asset'] = int(car['Asset'])
    car['Network'] = int(car['Network'])
    if car['Asset'] == trainVars['TRAIN']:
        trainVars['IPV4'] = car['Network']

config.update(trainVars)

template = ENV.get_template("CTP-template.text")

print template.render(config)
