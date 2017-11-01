#!/usr/bin/python3
import os


# converts data with decimal delimiters same as csv's delimiters to . delimiter based on my best guess

def convert(path, file):
    with open(path + '/' + file, 'r') as src:
        with open(path + '/converted_' + file, 'w') as dest:
            dest.write('\'time\',\'angle\',\'omega\'\n')
            for line in src:
                line = line.split(',')
                if len(line) > 9:
                    dest.write(line[0] + '.' + line[1] + ',' +
                               line[3] + '.' + line[4] + ',' +
                               line[5] + '.' + line[6] + '\n')


for root, dirs, files in os.walk('.'):
    for file in files:
        path = '/'.join(root.split(os.sep))
        if file[-4:] == '.csv':
            convert(path, file)
