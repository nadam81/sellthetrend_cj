from pathlib import Path

import click

from bs4 import BeautifulSoup
from loguru import logger

from squeezer import DATADIR

@click.command("drop-shipping")
@click.option("--html", help="Input HTML file.", type=Path, required=True)
def parse_drop_shipping(html: str) -> None:
    
    html_path = DATADIR / html

    # Read
    with html_path.open("r") as file:
        content = file.read()
    
    # Build soup
    logger.info("Parsing {}", html_path)
    soup = BeautifulSoup(content, "html.parser")

    # Prettify
    pretty = Path(DATADIR / f"{html.stem}_pretty.html")
    logger.info("Beautify and save output to {}", pretty)   
    with pretty.open("w") as file:
        file.write(soup.prettify())

    # Parse
    prods = soup.find_all("div", class_="product-list-box__content")

    with open("out.csv", "w") as fp:
        for prod in prods:
            prod_info = [x.strip() for x in str(prod).split("\n") if "<" not in x]

            logger.info("Item: {}", prod_info[0])
            prod_info = ",".join(prod_info)
            fp.write(f"{prod_info}\n")