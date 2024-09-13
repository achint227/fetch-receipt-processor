from math import ceil
from uuid import uuid4

from fastapi import HTTPException

from .models import Receipt


def calculate_points(receipt: Receipt):

    points = 0

    # One point for every alphanumeric character in the retailer name.
    points += sum(1 for c in receipt.retailer if c.isalnum())

    # 5 points for every two items on the receipt.
    item_count = len(receipt.items)
    points += 5 * (item_count // 2)

    # 50 points if the total is a round dollar amount with no cents.
    if receipt.total[-2] == "00":
        points += 50

    # 25 points if the total is a multiple of 0.25.
    if float(receipt.total) % 0.25 < 1e-9:
        points += 25

    for item in receipt.items:
        # If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2
        # and round up to the nearest integer. The result is the number of points earned.
        if len(item.shortDescription.strip()) % 3 == 0:
            points += ceil(float(item.price) * 0.2)

    # 6 points if the day in the purchase date is odd.
    if receipt.purchaseDate.day % 2:
        points += 6

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    hour, minute = receipt.purchaseTime.hour, receipt.purchaseTime.minute
    if 16 < hour >= 14 and (minute > 0 or hour != 14):
        points += 10

    return points


def get_points(db, id):

    if id not in db:
        raise HTTPException(status_code=404, detail="Receipt with given id not found")

    return db[id]


def process_receipt(db, receipt: Receipt):

    points = calculate_points(receipt)
    uuid = uuid4()
    id = str(uuid)
    db[id] = points

    return id
