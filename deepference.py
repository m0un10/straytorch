import json
import os
from distutils.dir_util import copy_tree
import uuid
import subprocess
import datetime

user_home = "/Users/craigbarr"
deepference_home = user_home + "/work/m0un10-closed/deepference"
output_home = user_home + "/.deepference"

report_config = {
    'report': {
        'name': "Environment Difference Report",
        'autoTimestamp': True
    }
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

##### Reports

def set_colour(o, c='red'):
  o["_attributes"] = {
    "className": {
      "row": [c]
    }
  }

def format_flat(in_data):
  data = []
  for key in in_data:
    obj = {
      "key": key
    }
    difference = False
    compare_value = None
    for env in in_data[key]:
      value = in_data[key][env]
      if compare_value is None:
        compare_value = value
      if value != compare_value:
        difference = True
      obj[env] = value
    if difference:
      set_colour(obj, 'yellow')
      obj['difference'] = "Inconsistent"
    elif len(in_data[key]) < number_of_columns:
      set_colour(obj, 'red')
      obj['difference'] = "Missing"
    else:
      obj['difference'] = "None"
    data.append(obj)
  return data

# Different Report
sorted_data = sorted(format_flat(data), key=lambda k: k['key'].lower())

output_dir = output_home + "/"+str(uuid.uuid4())
copy_tree(deepference_home + "/files", output_dir)

fin = open(deepference_home + "/templates/index.html", "rt")
fout = open(output_dir+"/index.html", "wt")
for line in fin:
    report_config
    l = line.replace('REPORT_NAME', report_config['report']['name']) 
    if report_config['report']['autoTimestamp']:
        l = l.replace('TIMESTAMP',  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))       
    fout.write(l)
fin.close()
fout.close()

# TODO: generate the load.js 

text_file = open(output_dir+"/generated.js", "w")
text_file.write('const data=%s' % json.dumps(sorted_data, indent=2))
text_file.close()

print("report generated at "+output_dir)
subprocess.Popen("/usr/bin/python -m SimpleHTTPServer", cwd=output_dir, shell=True)