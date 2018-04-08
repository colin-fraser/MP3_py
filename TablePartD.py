import happybase as hb

# cols 'personal:hero', 'personal:power', 'professional:name', 'professional:xp', 'custom:color'

connection = hb.Connection()

powers = connection.table('powers')

def printrow(table, row_id, *args):
    row = powers.row(row_id)
    outlist = []
    for a in args:
        rowname = (a.split(b':')[1]).decode('utf-8')
        outlist.append('%s: %s' % (rowname, row[a]))
    print(', '.join(outlist))

printrow(powers, 'row1', b'personal:hero', b'personal:power', b'professional:name', b'professional:xp', b'custom:color')
