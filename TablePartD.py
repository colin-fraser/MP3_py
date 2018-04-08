import happybase as hb

connection = hb.Connection()

powers = connection.table('powers')

row = powers.row('row1')
print(row)