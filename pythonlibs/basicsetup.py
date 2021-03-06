from pprint import pprint
import os
import argcomplete, argparse
import yaml
import subprocess
import requests
import uuid
import time

WTL_DEV_KIT_PATH = os.environ.get("WTL_DEV_KIT_PATH")
WTL_DEV_KIT_REPOS_PATH = os.environ.get("WTL_DEV_KIT_REPOS_PATH")
WTL_DEV_KIT_BIN_PATH = os.environ.get("WTL_DEV_KIT_BIN_PATH")

WTL_DEV_KIT_TMP_PATH = WTL_DEV_KIT_PATH + "/tmp/"

config = {}

with open(WTL_DEV_KIT_PATH + "/config/config.yml") as fh:
    config['config'] = yaml.load(fh)

if os.path.isfile(WTL_DEV_KIT_PATH + "/config/repositories.yml"):
    with open(WTL_DEV_KIT_PATH + "/config/repositories.yml") as fh:
        config['repositories'] = yaml.load(fh)
else:
    with open(WTL_DEV_KIT_PATH + "/config/repositories.example.yml") as fh:
        config['repositories'] = yaml.load(fh)

os.environ['KEYCLOAK_URI'] = 'http://{host_ip}:9080'.format(host_ip=config['config']['host_ip'])
os.environ['COURSES_BACKEND_URI'] = 'http://{host_ip}:10000'.format(host_ip=config['config']['host_ip'])
os.environ['CHAPTERS_BACKEND_URI'] = 'http://{host_ip}:10001'.format(host_ip=config['config']['host_ip'])
os.environ['PAGES_BACKEND_URI'] = 'http://{host_ip}:10002'.format(host_ip=config['config']['host_ip'])
os.environ['COURSESSECURITY_BACKEND_URI'] = 'http://{host_ip}:10003'.format(host_ip=config['config']['host_ip'])
os.environ['PDF_BACKEND_URI'] = 'http://{host_ip}:10004'.format(host_ip=config['config']['host_ip'])
os.environ['MATH_BACKEND_URI'] = 'http://{host_ip}:10005'.format(host_ip=config['config']['host_ip'])
os.environ['COURSE_MIDTIER_URI'] = 'http://{host_ip}:11000'.format(host_ip=config['config']['host_ip'])
os.environ['MATH_MIDTIER_URI'] = 'http://{host_ip}:11001'.format(host_ip=config['config']['host_ip'])
os.environ['PWA_GATEWAY_URI'] = 'http://{host_ip}:12000'.format(host_ip=config['config']['host_ip'])
os.environ['MONGO_HOST'] = 'mongodb://{host_ip}:27017'.format(host_ip=config['config']['host_ip'])
os.environ['PUBLIC_KEYCLOAK_URI'] = 'http://localhost:9080'
os.environ['PUBLIC_PWA_GATEWAY_URI'] = 'http://localhost:12000'

parser = argparse.ArgumentParser()

argcomplete.autocomplete(parser)
args = parser.parse_args()

def get_services_to_manage():
    return [
        "shared-services",
        "courses-backend",
        "chapters-backend",
        "pages-backend",
        "coursessecurity-backend",
        "pdf-backend",
        "math-backend",
        "math-midtier",
        "course-midtier",
        "pwa-gateway",
        "frontend",
    ]
