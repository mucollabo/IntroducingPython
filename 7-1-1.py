def unicode_test(value):
    import  unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' %(value, name, value2))
    
unicode_test('A')

unicode_test('$')

unicode_test('\u00a2')

unicode_test('\u20ac')

unicode_test('\u2603')

unicode_test('\u00e9')

import unicodedata

print(unicodedata.name('\u00e9'))

print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))

place = 'cat\u00e9'
print(place)

place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)

u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
print(u_umlaut)

drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)

