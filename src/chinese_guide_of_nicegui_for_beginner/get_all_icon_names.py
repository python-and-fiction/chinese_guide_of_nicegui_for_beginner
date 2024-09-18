#!/usr/bin/env python3
import json

import httpx,os

FAMILIES = {
    'Material Icons': ('', ''),
    'Material Icons Outlined': ('_outlined', 'o_'),
    'Material Icons Round': ('_round', 'r_'),
    'Material Icons Sharp': ('_sharp', 's_'),
    'Material Symbols Outlined': ('_sym_outlined', 'sym_o_'),
    'Material Symbols Rounded': ('_sym_round', 'sym_r_'),
    'Material Symbols Sharp': ('_sym_sharp', 'sym_s_'),
}
FAMILY_SET = set(FAMILIES)

response = httpx.get('https://fonts.google.com/metadata/icons?incomplete=1&key=material_symbols')
with (f'{os.path.dirname(os.path.abspath(__file__))}/result.txt').open('w') as f:
    for icon in json.loads(response.text[4:])['icons']:
        for family in FAMILY_SET.difference(icon['unsupported_families']):
            name = f'{icon["name"]}{FAMILIES[family][0]}'.upper()
            if not name.isidentifier():
                name = f'_{name}'
            value = f'{FAMILIES[family][1]}{icon["name"]}'
            f.write(f"{value}\n")
""" 
icon_name_dict = {}
file = f'{os.path.dirname(os.path.abspath(__file__))}/result.txt'
result_path = f'{os.path.dirname(os.path.abspath(__file__))}/result.txt'

s_name = []
o_name = []
r_name = []
sym_s_name = []
sym_o_name = []
sym_r_name = []
name = []

with open(file) as f:
    for i in f.readlines():
        i = i.strip('\n')
        if i.startswith('s_'):s_name.append(i)
        elif i.startswith('r_'):r_name.append(i)
        elif i.startswith('o_'):o_name.append(i)
        elif i.startswith('sym_s_'):sym_s_name.append(i)
        elif i.startswith('sym_r_'):sym_r_name.append(i)
        elif i.startswith('sym_o_'):sym_o_name.append(i)
        else:name.append(i)

for i in name:
    if i not in icon_name_dict.keys():
        icon_name_dict.update({i: []})
    icon_name_dict[i].append('')

for i in o_name:
    i = i[2:]
    if i not in icon_name_dict.keys():
        icon_name_dict.update({i: []})
    icon_name_dict[i].append('o_')

for i in r_name:
    i = i[2:]
    if i not in icon_name_dict.keys():
        icon_name_dict.update({i: []})
    icon_name_dict[i].append('r_')

for i in s_name:
    i = i[2:]
    if i not in icon_name_dict.keys():
        icon_name_dict.update({i: []})
    icon_name_dict[i].append('s_')

for i in sym_o_name:
    i = i[6:]
    if i not in icon_name_dict.keys():
        icon_name_dict.update({i: []})
    icon_name_dict[i].append('sym_o_')

for i in sym_r_name:
    i = i[6:]
    if i not in icon_name_dict.keys():
        icon_name_dict.update({i: []})
    icon_name_dict[i].append('sym_r_')

for i in sym_s_name:
    i = i[6:]
    if i not in icon_name_dict.keys():
        icon_name_dict.update({i: []})
    icon_name_dict[i].append('sym_s_')


with open(result_path, 'w') as f:
    f.write(str(icon_name_dict)) """