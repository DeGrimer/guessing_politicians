import json

with open('db.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    print(text['политики'])
for man in text['политики']:
    print(man['имя'])