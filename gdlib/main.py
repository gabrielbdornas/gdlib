import click

@click.command()
def hello_world():
  print('Olá Mundo')

if __name__ == '__main__':
  hello_world()

