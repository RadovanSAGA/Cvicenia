"""Cvicenia"""
# If,elif,else

y = 6
if y > 5:
    print('y je väčšie než 5')
else:
    print('y nieje väčšie ako 5')

z = 3

if z > 10:
    print('t je väčšie ako 10')

elif z > 5:
    print('z je väčšie ako 5, no je menšie alebo sa rovná 10')

else:
    print('z je menšie alebo je rovné 5')

# Loops

fruits = ['banana', 'strawberry', 'cherry']
for friuts in fruits:
    print(friuts)


count = 0 # Hodnota premennej count

while count < 5:  #
    print('Count is:', count) 
    count = count + 1 # Printnem Count a jeden count pridám neprestané ta slučka až kým nebude menšia ako 5 ako sme si na začiatku zadali

    print('Loop finished')








