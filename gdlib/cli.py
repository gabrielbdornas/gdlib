import click
from gdlib.main import hello_world

@click.group()
def cli():
  """
    Conjunto de comandos criados no pacote
  """
  pass

# @cli.group()
# def sub_comandos():
#   pass

cli.add_command(hello_world)
