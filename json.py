import json

print(json.dumps([1, 'simple', 'list']))

with open('file1') as f:
    json.dump(x, f)
    #To decode the object again, if f is a text file object which has been opened for reading:
    x = json.load(f)
    print(x)