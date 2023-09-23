import click

from squeezer import __version__
from squeezer.scripts import parse_drop_shipping

def _main() -> None:
    """Define entrypoint commands."""

    @click.group(chain=True)
    @click.version_option(__version__)
    def entry_point() -> None:
        """Squeezer entrypoint."""

    entry_point.add_command(parse_drop_shipping)

    entry_point()

if __name__ == "__main__":
    _main()