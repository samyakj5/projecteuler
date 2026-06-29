coin_values = [200, 100, 50, 20, 10, 5, 2, 1]
# coin_values = [5, 2, 1]
counted = {}

def coins(remaining_total, largest_coin_idx):
    if (remaining_total, largest_coin_idx) in counted:
        return counted[(remaining_total, largest_coin_idx)]
    if remaining_total == 0:
        counted[(remaining_total, largest_coin_idx)] = 1
        return 1
    if remaining_total < 0:
        return 0
    else:
        
        if largest_coin_idx + 1 < len(coin_values):
                y = (
                     coins(remaining_total - coin_values[largest_coin_idx], largest_coin_idx) + 
                     coins(remaining_total, largest_coin_idx + 1)
                     )
                counted[(remaining_total, largest_coin_idx)] = y
                return y
        else:
            y = (
                coins(remaining_total - coin_values[largest_coin_idx], largest_coin_idx)
                )
            counted[(remaining_total, largest_coin_idx)] = y
            return y

print(coins(200, 0))