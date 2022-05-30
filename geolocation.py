# -*- coding: utf-8 -*-
"""
Created on Sun May 29 22:16:42 2022

@author: apisl
"""


import geocoder
g = geocoder.ip('me')

print(g.latlng)
print(g.city)
