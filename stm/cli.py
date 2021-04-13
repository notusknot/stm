import click
import os
import shutil
import json

stm_dir_var = ''



def append_value(dict_obj, key, value):
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = value

@click.group()
def cli():
    pass
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@click.command()
@click.argument('stm_dir')
def set_dir(stm_dir):
    try:
        stm_dir_var = stm_dir
        print(stm_dir_var)
    except:
        raise Exception('There has been an error in the system')
    

with open(base_dir+"/themes.json", "r") as read_file:
    themes = json.load(read_file)


@click.command()
def list():
    click.echo('\nAvailable themes:\n')
    for loop in themes:
        click.echo(loop)

@click.command()
@click.argument('name', nargs=1)
@click.argument('path', nargs=-1)
def add(name, path):
    themes[name] = path
    path_destination = str(path).split(':')[0]
    path_location = str(path).split(':')[1]
    with open("themes.json", "w") as write_file:
            json.dump(themes, write_file)

@click.command()
@click.argument('theme')
def load(theme):
    flag = 0
    for loop in themes:
        if theme == loop:
            flag = 1
            break
        else:
            flag = 2
    if flag == 1:
        for s in themes[theme]:
            if s.count(':') != 1:
                raise ValueError
            file_destination, file_location = s.split(':')
            shutil.copy(file_location,file_destination)
        click.echo('\nSuccess. Make sure to reload your window manager')
    elif flag == 2: 
        click.echo('\nThis theme is not registered')

cli.add_command(list)
cli.add_command(add)
cli.add_command(load)
cli.add_command(set_dir)

