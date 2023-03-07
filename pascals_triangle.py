
def draw_pascal(height: int = 25, odds: bool = False, fours: bool = False) -> None:
    """
    Pascal's Patterns from the 'This is Not a Math Book', pp. 32-33
    """
    tri = []

    for ix, row in enumerate(range(height)):
        row_length = ix + 1
        row_vals = [0] * row_length
        row_vals[0] = 1
        row_vals[-1] = 1

        if ix == 0:
            previous_row = row_vals
        else:
            for val_ix, val in enumerate(row_vals):
                if val_ix != 0 and val_ix != row_length-1:
                    row_vals[val_ix] = previous_row[val_ix - 1] + previous_row[val_ix]
                else:
                    continue
            previous_row = row_vals

        if odds:
            row_vals = ["#" if x % 2 == 0 else "." for x in row_vals]
        elif fours:
            row_vals = ["#" if x % 4 == 0 or x % 6 == 0 else "." for x in row_vals]
        else:
            row_vals = [str(x) for x in row_vals]

        tri.append([" ".join(row_vals)])


    max_length = len(tri[-1][0])

    for row in tri:
        row = row[0]
        white_space = " " * int((max_length - len(row))/2)
        print(f"{white_space}{row}{white_space}")


TEST_HEIGHT = 25
draw_pascal(TEST_HEIGHT)
draw_pascal(50, odds=True)
draw_pascal(50, fours=True)
