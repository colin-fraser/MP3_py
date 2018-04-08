import happybase as hb

connection = hb.Connection()

connection.create_table('powers', {'personal': {}, 'professional': {}, 'custom': {}})
connection.create_table('food', {'nutrition': {}, 'taste': {}})