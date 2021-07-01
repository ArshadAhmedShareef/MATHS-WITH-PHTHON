#Questio:What kind of exception handling we faced when dealing with complex number And 
# ANSWER : We face error handling exception while dealing with complex number. 
#Code for it is:

try:
  a=complex(input('Enter complex number:'))
except ValueError:
    print('Invalid number')
