import happybase as hb
import csv

row_names = ['personal:hero', 'personal:power', 'professional:name', 'professional:xp', 'custom:color']

connection = hb.Connection()
powers = connection.table('powers')

with open('input.csv') as f:
    reader = csv.reader(f)
    for line in reader:
        payload = dict(zip(row_names, line[1:]))
        powers.put(line[0], payload)
