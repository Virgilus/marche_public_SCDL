#-*- coding: utf-8 -*-
# coding: utf8

from goodtables import validate
import pprint

report = validate('../exemples/exemple_marche_public.csv', schema='marche_public_SCDL.json')
pprint.pprint(report)