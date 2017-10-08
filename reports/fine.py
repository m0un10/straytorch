def set_colour(o, c='red'):
  o["_attributes"] = {
    "className": {
      "row": [c]
    }
  }

def report(in_data, number_of_columns):
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