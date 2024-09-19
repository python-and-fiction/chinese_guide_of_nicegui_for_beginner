from nicegui import ui
import os

result = {}
with open(f'{os.path.dirname(os.path.abspath(__file__))}/result.txt') as f:
    result = eval(f.read())

icon_name_dict = result
icon_name_list = list(icon_name_dict.keys())
icon_name_dict_typed = {'':[],'o_':[],'r_':[],'s_':[],'sym_o_':[],'sym_r_':[],'sym_s_':[],}
for i in icon_name_list:
    for k in icon_name_dict[i]:
        icon_name_dict_typed[k].append(i)
        
type_name_map = {'':'Filled',
                 'o_':'Outline',
                 'r_':'Round',
                 's_':'Sharp',
                 'sym_o_':'Outline symbol',
                 'sym_r_':'Round symbol',
                 'sym_s_':'Sharp symbol',}

current_name = ''
current_type = ''

def all_show(icon_name = None,icon_type = None):
    with ui.card():
        ui.label(icon_name+':')
        with ui.column():
            with ui.row() as row1:
                label1= ui.label('This name has no filled icon.')
            with ui.row() as row2:
                label2= ui.label('This name has no styled icon.')
            with ui.row() as row3:
                label3= ui.label('This name has no symbol icon.')
            for prefix in icon_type:
                if prefix in ['o_','r_','s_']:
                    label2.set_text('Styled:')
                    with row2,ui.icon(prefix+icon_name, size='3em').on('click',lambda :(ui.clipboard.write(prefix+icon_name),ui.notify('name copied!'))):
                        ui.tooltip(prefix+icon_name).tailwind.font_size('sm')
                elif prefix in ['sym_o_','sym_r_','sym_s_']:
                    label3.set_text('Symbol:')
                    with row3,ui.icon(prefix+icon_name, size='3em').on('click',lambda :(ui.clipboard.write(prefix+icon_name),ui.notify('name copied!'))):
                        ui.tooltip(prefix+icon_name).tailwind.font_size('sm')
                else:
                    label1.set_text('Filled:')
                    with row1,ui.icon(prefix+icon_name, size='3em').on('click',lambda :(ui.clipboard.write(prefix+icon_name),ui.notify('name copied!'))):
                        ui.tooltip(prefix+icon_name).tailwind.font_size('sm')

def bigger_show(icon_name = None,icon_type = None):
    with ui.card():
        with ui.column():
            ui.label(icon_name+f' of {type_name_map[icon_type]}'+':')
            with ui.icon(icon_type+icon_name, size='10em').on('click',lambda :(ui.clipboard.write(icon_type+icon_name),ui.notify('name copied!'))):
                ui.tooltip(icon_type+icon_name).tailwind.font_size('sm')

def title():
    with ui.row():
        ui.link('all_type','/')
        ui.link('bigger_type','/bigger')
        ui.link('bigger_type_fisrt','/bigger_first')

@ui.page('/',title='all type')
def page_index():
    title()
    icon_name = ui.select(icon_name_list, value= current_name if (current_name in icon_name_list) else icon_name_list[0] ,label='icon name:', with_input=True).classes('w-64')

    @ui.refreshable
    def show():
        all_show(icon_name=icon_name.value,icon_type=icon_name_dict[icon_name.value])
    show()
    icon_name.on_value_change(show.refresh)
    icon_name.on_value_change(lambda e:globals().update({'current_name':e.sender.value}))

@ui.page('/bigger',title='bigger type')
def page_bigger():
    title()
    icon_name = ui.select(icon_name_list, value = current_name if (current_name in icon_name_list) else icon_name_list[0],label='icon name:', with_input=True).classes('w-64')

    @ui.refreshable
    def show():
        current_type_list = icon_name_dict[icon_name.value]
        icon_type_name = ui.select({ i:type_name_map[i] for i in current_type_list}, value= current_type if(current_type in current_type_list) else current_type_list[0] , label='icon type name:',with_input=True).classes('w-64')
        icon_type_name.bind_value_to(globals(),'current_type')

        @ui.refreshable
        def inner_show():
            bigger_show(icon_name=icon_name.value,icon_type=icon_type_name.value)

        inner_show()
        icon_type_name.on_value_change(inner_show.refresh)
    show()
    icon_name.on_value_change(show.refresh)
    icon_name.on_value_change(lambda e:globals().update({'current_name':e.sender.value}))

@ui.page('/bigger_first',title='bigger_type_fisrt')
def page_bigger_first():
    title()
    icon_type_name = ui.select(type_name_map, value=current_type,label='icon type name:', with_input=True).classes('w-64')
    icon_type_name.bind_value_to(globals(),'current_type')

    @ui.refreshable
    def show():
        current_name_list = icon_name_dict_typed[icon_type_name.value]
        icon_name = ui.select(current_name_list, value= current_name if current_name in current_name_list else current_name_list[0], label='icon name:',with_input=True).classes('w-64')

        @ui.refreshable
        def inner_show():
            bigger_show(icon_name = icon_name.value, icon_type= icon_type_name.value)

        inner_show()
        icon_name.on_value_change(inner_show.refresh)
        icon_name.on_value_change(lambda e:globals().update({'current_name':e.sender.value}))
    show()
    icon_type_name.on_value_change(show.refresh)

ui.run(native=True,title='Material Icons Search')
