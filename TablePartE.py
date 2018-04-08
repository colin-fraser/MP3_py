import happybase as hb


connection = hb.Connection()
powers = connection.table('powers')

for key, data in powers.scan():
    print('Found: %s, %s' % key, data)