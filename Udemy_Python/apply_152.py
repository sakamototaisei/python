# json
import json


j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

print(j)
print('--------------')
# jsonフォーマットにするには json.dumps()
print(json.dumps(j))


#ファイルに書き込み
with open('test.json', 'w') as f:
    json.dump(j, f)