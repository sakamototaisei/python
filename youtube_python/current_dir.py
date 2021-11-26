import os

for curDir, dirs, files in os.walk('.'):
    for file in files:
        print(f'{curDir}/{file}')