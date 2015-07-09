#!/usr/local/bin/python2.7
# encoding: utf-8

from itertools import chain, combinations, count, cycle, groupby, ifilterfalse
from telnetlib import theNULL

def unique_everseen(iterable):
    """Yield unique elements, preserving order.
        >>> list(unique_everseen('AAAABBBCCDAABBB'))
        ['A', 'B', 'C', 'D']
        >>> list(unique_everseen('ABBCcAD', str.lower))
        ['A', 'B', 'C', 'D']
    """
    for element, new in zip(iterable, iterable[1:]) :
        print element, new
        if element == new:
            iterable.remove(new)
    print iterable
            
    
print unique_everseen(['12','ABC','ABC','ABC','ABC','abc','abc','cde'])  
# list(unique_everseen('ABBCcAD', str.lower)) 

print "Done"             