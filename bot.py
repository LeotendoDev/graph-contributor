import os
import random

for i in range(1, 365):
    for j in range(0, random.randint(1, 10)):
        day = str(i) + ' days ago'
        with open('test.txt', 'a') as file:
            file.write(day)
        os.system('git add .')
        os.system(f'git commit -m --date={day} -m "Commit!"')

os.system('git push -u origin master')
