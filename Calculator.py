#Victoria W.

import sys

month1 = sys.argv[1]
month2 = sys.argv[2]
month3 = sys.argv[3]

try :
    year = int(month1) + int(month2) + int(month3)

Except :
    print('Error: All sales should be numeric')

Else :
    Year = int(month1) + int(month2) + int(month3)
    
    if year >= 140000 :
        Year = int(month1) + int(month2) + int(month3)
        print('Quarterly sales: $',month1,'$',month2,'$',month3)
		print('Total sales $',year)
		print('Sales high, excellent')
	Elif year > 40000 and year < 139999:
        Year = int(month1) + int(month2) + int(month3)
		print('Quarterly sales: $',month1,'$',month2,'$',month3)
		print('Total sales: $',year)
		print('Sales: medium')
	Elif year < 40000 :
        Year = int(month1) + int(month2) + int(month3)
        print('Quarterly sales: $',month1,'$',month2,'$',month3)
		print('Total sales $',year)
		print('Sales: low')
		print('Warning: Need to improve sales.')

