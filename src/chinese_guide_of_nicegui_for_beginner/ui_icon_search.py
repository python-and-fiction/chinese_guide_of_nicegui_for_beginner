from nicegui import ui
import os

result = {}
with open(f'{os.path.dirname(os.path.abspath(__file__))}/result.txt') as f:
    result = eval(f.read())

icon_name_list = list(result.keys())


with ui.row():
    icon_name = ui.select(icon_name_list, value='3d_rotation',label='icon name:', with_input=True).classes('w-64')
    zoom_spec = ui.switch().tooltip('show bigger icon')

@ui.refreshable
def icon_type():
    icon_prefix = ui.select(result[icon_name.value], value=result[icon_name.value][0], label='icon type:').classes('w-64')
    icon_prefix.bind_visibility_from(zoom_spec,'value')
    @ui.refreshable
    def icon_type_card():
        with ui.card().bind_visibility_from(zoom_spec,'value'):
            with ui.icon(icon_prefix.value+icon_name.value, size='10em'):
                    ui.tooltip(icon_prefix.value+icon_name.value).tailwind.font_size('xl')
    icon_type_card()
    icon_prefix.on_value_change(icon_type_card.refresh)

icon_type()


@ui.refreshable
def demo():
    with ui.card().bind_visibility_from(zoom_spec,'value',lambda x:not x):
        ui.label(icon_name.value+':')
        with ui.row():
            for i in sorted(result[icon_name.value]):
                with ui.icon(i+icon_name.value, size='3em'):
                    ui.tooltip(i+icon_name.value).tailwind.font_size('sm')

demo()
icon_name.on_value_change(demo.refresh)
icon_name.on_value_change(icon_type.refresh)

ui.run(native=True,title='Material Icons Search')
