from dataclasses import dataclass


@dataclass
class OrderLine:
    orderid: str
    sku: str
    qty: int
