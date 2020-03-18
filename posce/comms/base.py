'''
Click base group function.
'''

import click

from posce.items import Book

@click.group()
@click.option('--dire', envvar='POSCE_DIR', hidden=True)
@click.option('--ext',  envvar='POSCE_EXT', hidden=True)
@click.pass_context
def group(ctx, dire, ext):
    '''
    Posce: a note-taking toolkit for your command line.
    See github.com/posce/posce for help and issues.
    '''

    ctx.obj = Book(dire, ext)
