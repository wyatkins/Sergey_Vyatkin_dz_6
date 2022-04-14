PRICE_FILE = "./bakery.csv"


if __name__ == "__main__":

    import sys

    if len(sys.argv[1:]) != 2:
        sys.exit(1)

    pos = sys.argv[1]
    new_price = sys.argv[2]

    if not (pos.isdigit() and new_price.replace(".", "").isdigit()):
        sys.exit(1)

    pos = int(pos)
    new_price = float(new_price)

    with open(PRICE_FILE, "r+", encoding="utf-8") as price_list:

        skip_chars = 0

        for _ in range(pos-1):

            try:
                skip_chars += len(next(price_list))
            except StopIteration:
                print("out of index")
                sys.exit(1)