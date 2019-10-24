import json
with open("json",'r+') as f:
    json.dump([1, 'simple', 'list'],f)
    x = json.load(f)
    print(x)
