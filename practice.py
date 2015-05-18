#!/usr/bin/python
######################
""""This is how
to do
multi-line comments"""

print ("it's nice " + 'to be "or not to be"')
# it's nice to be "or not to be"
print ('where aren\'t you?')
# where aren't you?
print ('hello\nworld')
# hello
# world
print ('''hello
\tworld''')
# hello
# 	world
print ('go to \\news')
# go to \news
######################
def nikoprint():
  print 'hello'
  print 'world'
  print '!'
nikoprint()
#
def routerupgrade(router):
  toupgrade = ['bx01', 'bx02', 'bx03']
  if router in toupgrade:
    print 'start upgrade on %s' % router
  else:
    print 'stop upgrading on %s' % router
routerupgrade('cx01')
routerupgrade('bx03')
#
def function(x, y, z):
   print x + y + z
function(1, 2, 3)
#
def function_input(x, y, z):
   return x + y - z
a = function_input(1, 2, 3)
print 'input %s' % a
######################
"""From the directory where the .py file is, run <python nikoprint.py>:
hello
world
!
stop upgrading on cx01
start upgrade on bx03
6
input 0"""
######################
name = raw_input("What is your name?")
What is your name?Niko
quest = raw_input("What is your quest?")
What is your quest?Art
color = raw_input("What is your favorite color?")
What is your favorite color?Blue

print "Ah, so your name is %s, your quest is %s, " "and your favorite color is %s." % (name, quest, color)
'Ah, so your name is Niko, your quest is Art, and your favorite color is Blue.'
######################
meal = 44.50
tax = 6.75/100
tip = 15.0/100
meal = meal + meal * tax
total = meal + meal * tip

print total
54.6293125
######################
# FU = 'Function is Universal'
# 'datetime' is a function

from datetime import datetime
now = datetime.now()

print '%s-%s-%s' % (now.year, now.month, now.day)
2015-5-18

print '%s/%s/%s' % (now.month, now.day, now.year)
5/18/2015

print '%s:%s:%s' % (now.hour, now.minute, now.second)
13:43:50
######################
