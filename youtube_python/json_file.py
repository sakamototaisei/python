import json

with open('youtube_python/sample.json', 'r') as f:
    data = json.load(f)
    print(data)