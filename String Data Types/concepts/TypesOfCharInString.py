#  To show the types of chars present in a string

"""""
isalnum()    to check all characters are alphanumerics ore not  (a-z,A-Z,0 to 9)
isdigit()    to check all characters are only digits only(0 to 9)
isalpha()    to check all characters are only alpha(a-z or A to Z)
islower()    to check all characters presented in the str are in lowercase,  string can contain anytype of char
isupper()    to check all characters are in uppercase, string can contain anytype of char
istitle()    to check all characters are in title case, string can contain anytype of char
isspace()    to check all characters are spaces only

"""
print('amarnath12ADDWWEd'.isalnum())
print('amarnenvnA'.isalpha())
print('123456'.isdigit())
print('1234sdfgh'.islower())
print('1234UPPER'.isupper())
print('Thhsdwehd'.istitle())
print('    '.isspace())