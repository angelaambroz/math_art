triangle_height = 10


for ix, row in enumerate(range(triangle_height)):
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

    print(row_vals)

