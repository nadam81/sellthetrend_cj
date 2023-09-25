from dataclasses import dataclass
from pathlib import Path

import click

from bs4 import BeautifulSoup
from loguru import logger

from squeezer import DATADIR

@click.command("drop-shipping")
@click.option("--html", help="Input HTML file.", type=Path, required=True)
@click.option("--date", help="Date in YYYY-MM-DD format.", type=str, required=True)
def parse_drop_shipping(html: str, date: str) -> None:
    
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
    all_content = []
    for prod in soup.find_all("div", class_="product-list-box__content"):
        content = [x.strip() for x in str(prod).split("\n") if "<" not in x]
        all_content.append(content)
    
    logger.info("Num rows: {}", len(all_content))

    # Each product takes two rows in the all_content array
    # The first row is useful, the second one not
    # Let's get rid of the second row
    all_content = all_content[0::2]

    logger.info("Num products: {}", len(all_content))

    with open("raw.csv", "w") as fp:
        for prod_info in all_content:
            fp.write(f"{prod_info}\n")

    cards = []
    for x in all_content:
        card = ProductCard(
            name=x[0].replace("&amp;", ""),
            reviews=x[1].replace("Reviews: ", ""),
            price=x[7].replace("$", ""),
            daily_inc_percent=x[11].replace("+", ""),
            daily_inc_value=x[12].replace(" Lists", "").replace("+", ""),
            total_lists=x[15].replace(" Lists", "").replace("+", "")
        )
        cards.append(card)

    with open("out.csv", "w") as fp:
        fp.write("name;reviews;price;daily_inc_percent;daily_inc_value;total_lists;date\n")
        for card in cards:
            fp.write(f"{card.to_csv()};{date}\n")

    logger.info("Saved results in out.csv")


@dataclass
class ProductCard:
    name: str
    reviews: str
    price: str
    daily_inc_percent: str
    daily_inc_value: str
    total_lists: str

    def to_csv(self):
        return ";".join(
            [
                self.name,
                self.reviews,
                self.price,
                self.daily_inc_percent,
                self.daily_inc_value,
                self.total_lists
            ]
        )
