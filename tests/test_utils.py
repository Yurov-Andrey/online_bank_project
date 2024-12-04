









import os

base_dir = os.path.dirname(os.path.dirname(__file__))
my_json = os.path.join(base_dir, 'data', 'operations.json')
print(processing_json_dict(my_json))