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

    info = []
    for prod in prods:
        prod_info = [x.strip() for x in str(prod).split("\n") if "<" not in x]
        prod_info = ",".join(prod_info)
        info.append(prod_info)
    
    logger.info("Num rows: {}", len(info))

    i = 0
    out = []
    while i < len(info):
        row = info[i]
        next_row = info[i+1]

        logger.info("Iteration {}\n  {}\n  {}", i, row, next_row)

        if row[0] != next_row[0]:
            logger.error("Row misatch")

        out.append(",".join([row, next_row]))

        i = i + 2

    with open("out.csv", "w") as fp:
        for prod_info in out:
            fp.write(f"{prod_info}\n")