import json
import os
from distutils.dir_util import copy_tree
import uuid
import subprocess
import datetime
from os.path import expanduser
from reports import fine
import argparse
import sys
import yaml
import re

parser = argparse.ArgumentParser(description='Discover deep insights into multi-instance data differences.')
parser.add_argument('-c', '--config', help='location of configuration')

args = parser.parse_args()

if args.config is None:
  parser.print_help()
  sys.exit(1)

home = os.environ['STRAYTORCH_HOME']
fallback_output_home = expanduser("~") + "/.straytorch"

if args.config.endswith(".yaml") or args.config.endswith(".yml"):
  with open(args.config, 'r') as stream:
      try:
          report_config = yaml.safe_load(stream)
      except yaml.YAMLError as exc:
        print("invalid yaml in "+args.config+ ": "+str(exc))
        sys.exit(1)
else:
  print("unsupported file type: "+args.config)
  sys.exit(1)

def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

source_data = {}

number_of_columns = 0

columns_data = [
  {
      'header': 'Name',
      'name': 'key',
      'filter': { 
        'type': 'text',
        'showClearBtn': True
      },
      'ellipsis': True
  },
  {
    'header': 'Difference?',
    'name': 'difference',
    'width': 100,
    'align': 'center',
    'resizable': False,
    'filter': 'select'
  }
]

for filename in os.listdir('.'):
  match = re.match('(?P<name>.*).json', filename)
  if match:
    columns_data.append({
      'header': match.group('name'),
      'name':  match.group('name'),
      'align': 'center',
      'ellipsis': True,
      'filter': { 
        'type': 'text',
        'showClearBtn': True
      }
    })
    with open(filename) as f:
      data = json.load(f)
      source_data[os.path.splitext(filename)[0]] = flatten_json(data)
      number_of_columns += 1

data = {}
for env in source_data:
  for key in source_data[env]:
    value = source_data[env][key]
    if key in data:
      data[key][env] = value
    else:
      data[key] = { env: value }

report_type = report_config['report']['type']
if report_type == "fine":
  sorted_data = sorted(fine.report(data,number_of_columns), key=lambda k: k['key'].lower())
else:
  print(report_type + " is not a supported report type.")
  sys.exit(1)

if not 'grid' in report_config:
  report_config['grid'] = {}
if not 'bodyHeight' in report_config['grid']:
  report_config['grid']['bodyHeight'] = 'auto'

if "outputDirectory" in report_config['report']:
    output_dir = report_config['report']['outputDirectory']
else:
    output_dir = fallback_output_home + "/"+str(uuid.uuid4())

if not os.path.exists(output_dir):
    print("creating "+output_dir)
    os.makedirs(output_dir)

copy_tree(home + "/files", output_dir)

fin = open(home + "/templates/index.html", "rt")
fout = open(output_dir+"/index.html", "wt")
for line in fin:
    report_config
    l = line.replace('REPORT_NAME', report_config['report']['name']) 
    if report_config['report']['autoTimestamp']:
      l = l.replace('TIMESTAMP',  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    else:
      l = l.replace('TIMESTAMP', '')       
    fout.write(l)
fin.close()
fout.close()

text_file = open(output_dir+"/generated.js", "w")
if isinstance(report_config['grid']['bodyHeight'], int):
  text_file.write("const gridBodyHeight=%s\n" % report_config['grid']['bodyHeight'])
text_file.write('const columns=%s\n' % json.dumps(columns_data, indent=2))
text_file.write('const data=%s\n' % json.dumps(sorted_data, indent=2))
text_file.close()

print("report generated at "+output_dir)