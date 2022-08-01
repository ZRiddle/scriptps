import csv
from dataclasses import dataclass
from typing import List

RETURN_CHAR = "\r"


@dataclass
class Order:
    """Base class for a single order"""
    id: str
    design: str
    name_on_label: str
    address_street: str
    address_city_state: str
    address_zip: str

    def __post_init__(self):
        self.name_on_label = self.name_on_label.strip()
        self.address_street = self.address_street.strip()
        self.address_city_state = self.address_city_state.strip()
        self.address_zip = self.address_zip.strip()

    def get_filename(self) -> str:
        """Get filename for saving"""
        return self.id + "_" + self.name_on_label.replace(" ", "-") + ".png"

    def get_address_text(self, is_single_line: bool, separator: str = "·") -> str:
        if is_single_line:
            return f"{self.address_street} {separator} {self.address_city_state} {self.address_zip}"
        else:
            # Multi-line
            return f"{self.address_street}{RETURN_CHAR}{self.address_city_state}{RETURN_CHAR}{self.address_zip}"

    def __repr__(self):
        return f"[Order #{self.id}][{self.design}] {self.name_on_label} | {self.get_address_text(True)}"


def load_orders(filepath: str) -> List[Order]:
    """Load all orders"""
    with open(filepath, 'r') as csvfile:
        _rows = csv.reader(csvfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rows = [row for row in _rows]

    all_orders = []
    for row in rows[1:]:
        all_orders.append(
            Order(
                id=row[0],
                design=row[3],
                name_on_label=row[4],
                address_street=row[5],
                address_city_state=row[6],
                address_zip=row[7],
            )
        )

    return all_orders
