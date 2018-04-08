import happybase as hb

connection = hb.Connection()

powers = connection.table('powers')

def printrow(table, row_id, **args):
    row = powers.row(row_id)
    outlist = []
    for a in args:
        outlist.append('%s: %s' % (a, row[a]))
    print(', '.join(outlist))

printrow(powers, 'row1', 'hero', 'power', 'name', 'xp', 'color')
