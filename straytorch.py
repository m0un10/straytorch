import json
import os
from distutils.dir_util import copy_tree
import uuid
import subprocess
import datetime
from os.path import expanduser
from reports import fine

home = os.environ['STRAYTORCH_HOME']
fallback_output_home = expanduser("~") + "/.straytorch"

report_config = {
    'report': {
        'name': 'Environment Difference Report',
        'autoTimestamp': True,
        'outputDirectory': 'output',
        'type': 'fine',
    },
}

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

for filename in os.listdir('.'):
  if filename.endswith(".json"):
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
  os.exit(1)

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

# TODO: generate the load.js 

text_file = open(output_dir+"/generated.js", "w")
text_file.write('const data=%s' % json.dumps(sorted_data, indent=2))
text_file.close()

print("report generated at "+output_dir)