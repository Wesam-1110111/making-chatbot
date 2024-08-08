import sys
from wel import welcome
from colors import Colors

USER = 'admin'
PASS = '1234'

def check(user, passwd):
	if user == USER and passwd == PASS:
		welcome()
	else:
		print(f'\n{Colors.red}user name or password is wrong{Colors.end}\n')

try:
	check(sys.argv[1], sys.argv[2])
except IndexError:
	print(f'{Colors.yellow}please enter your: User name and your Password{Colors.end}')
	print('try: python [file_name.py] [User_name] [Password]')