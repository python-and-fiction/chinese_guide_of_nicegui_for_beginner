import os

icon_name_dict = {}
map_name1 = {
    'materialiconstwotone': '',
    'materialicons': '',
    'materialiconsoutlined': 'o_',
    'materialiconsround': 'r_',
    'materialiconssharp': 's_',
}
map_name2 = {
    'materialsymbolsoutlined':'sym_o_', 
    'materialsymbolsrounded':'sym_r_', 
    'materialsymbolssharp':'sym_s_'
}

# main path:
sym_path = 'e:/Projects/material-design-icons-master/symbols/android'
src_path = 'e:/Projects/material-design-icons-master/src'
result_path = f'{os.path.dirname(os.path.abspath(__file__))}/result.txt'

# search name:
# https://fonts.google.com/icons?icon.set=Material+Icons
# source code link:
# https://github.com/google/material-design-icons/archive/master.zip

for names in os.listdir(src_path):
    for name in os.listdir(src_path+f'/{names}'):
        icon_name_dict.update({name: []})
        for typ in os.listdir(src_path+f'/{names}/{name}'):
            icon_name_dict[name].append(map_name1[typ])

for name in os.listdir(sym_path):
    if name not in icon_name_dict.keys():
        icon_name_dict.update({name: []})
    for typ in os.listdir(sym_path+f'/{name}'):
        icon_name_dict[name].append(map_name2[typ])

for k in icon_name_dict.keys():
    icon_name_dict[k] = list(set(icon_name_dict[k]))

with open(result_path, 'w') as f:
    f.write(str(icon_name_dict))
