import click
import keyinput
from gameplay import GamePlay


@click.command()
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.option('--col', prompt='Number of column',
              help='Number of column', default=100)
@click.option('--row', prompt='Number of row',
              help='Number of row', default=20)
def start_game(name, col, row):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f"Hello {name}!")
    click.echo("Welcome to Snaky")
    gameplay = GamePlay(col, row)

    score, msg = gameplay.start()

    click.echo(f"Wow.. {name}: {msg}")
    click.echo(f"Your score is {score}")


if __name__ == '__main__':
    print("starting")
    start_game()
