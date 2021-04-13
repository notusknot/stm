import click
import shutils
import json

with open("themes.json", "r") as read_file:
    themes = json.load(read_file)

class Context:
    def __init__(self, theme):
        self.theme = theme

@click.command()
@click.option("-t", "--theme", type=str, help="Choose a theme to load")
@click.pass_context
def cli(ctx, theme):
    ctx.obj = Context(theme)
    click.echo(ctx.obj.theme)
