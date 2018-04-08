import happybase as hb

# cols 'personal:hero', 'personal:power', 'professional:name', 'professional:xp', 'custom:color'

connection = hb.Connection()

powers = connection.table('powers')

def printrow(table, row_id, *args):
    row = powers.row(row_id)
    outlist = []
    for a in args:
        outlist.append('%s: %s' % (a, row[a]))
    print(', '.join(outlist))

printrow(powers, 'row1', 'personal:hero', 'personal:power', 'professional:name', 'professional:xp', 'custom:color')
