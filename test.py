from BSE import Exchange, Order
import itertools
import time

exchange = Exchange()

orderid_iter = itertools.count(start=1)
sign_iter_for_side = itertools.cycle([1, -1, -1, 1, 1, -1])
side_iter = ('Ask' if s > 0 else 'Bid' for s in sign_iter_for_side)

spread_values = [3, 2, 3, 2, 2, 2, 3, 2, 3, 4, 2, 2, 1, 2, 4, 5, 6, 4, 9, 5, 3, 2, 3, 2, 3, 3, 2, 2, 3, 2, 5, 2, 2, 2, 2, 2, 4, 2, 3, 6, 5, 6, 3, 2, 3, 5, 4]
spread_iter = itertools.cycle(spread_values)
sign_iter_for_price = itertools.cycle([1, -1, -1, 1, 1, -1])
price_iter = (int(1000 + sgn * delta) for (delta, sgn) in zip(spread_iter, sign_iter_for_price))

size_values = [2, 9, 5, 3, 3, 4, 10, 15, 1, 6, 13, 11, 4, 1, 5, 1, 3, 7, 9, 11, 13, 17, 19, 21, 27, 9, 103]
size_iter = itertools.cycle(size_values)

# Zip them all together
user_id = itertools.count(start=1)

lmt_order_info_iter = zip(orderid_iter, price_iter, size_iter, side_iter, user_id)

upper_limit = 6
order_info_lst = list(itertools.islice(lmt_order_info_iter, int(upper_limit)))

orders = [Order(trader_id, order_type, order_price, order_quantity, 0, qid=order_id) for (order_id, order_price, order_quantity, order_type, trader_id) in order_info_lst]



def time_n_vol_upper_limit(upper_limit):
    ob = Exchange()  # Initialize empty book
    order_info_lst = list(itertools.islice(lmt_order_info_iter, int(upper_limit)))
    orders = [Order(trader_id, order_type, order_price, order_quantity, 0, qid=order_id) for (order_id, order_price, order_quantity, order_type, trader_id) in order_info_lst]
    
    start_time = time.time()
    
    for order in orders:
        exchange.add_order(order, verbose=True)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    return elapsed_time

def time_n_vol_group_testing(test_sample):
    times = []
    vols = []
    cnt = 0
    
    for i in test_sample:
        t = time_n_vol_upper_limit(i)
        cnt += 1
        
        if cnt == 1:
            continue
        
        times.append(t)
        vols.append(i)
    
    with open('insert_cmp_python_y.txt', 'w') as f:
        for time in times:
            f.write(f"{time}\n")
            print(time)

    return [vols, times]


test_sample = [2500, 5000, 10000, 15000, 20000, 25000, 30000]
# test_sample = [2000, 4000]
ans = time_n_vol_group_testing(test_sample)
# user_id increment
# price integer



# # Define the order parameters
# trader_id = "T1"
# order_type = "Bid"  # or "Ask"
# order_price = 103
# order_quantity = 10
# current_time = 0
# qid = 1

# Create an order instance
# order1 = Order(trader_id, order_type, order_price, order_quantity, current_time, qid)

# # Submit the order to the exchange
# transaction_record = exchange.process_order2(current_time, order1, verbose=True)

# order2 = Order("T2", order_type, 105, 20, current_time, 2)
# exchange.process_order2(current_time, order2, verbose=True)
# order3 = Order("T3", order_type, 109, 20, current_time, 2)
# exchange.add_order(order3, verbose=True)
# order4 = Order("T4", order_type, 105, 20, 0, 2)
# exchange.process_order2(0, order4, verbose=True)

# print("exchange.bids.orders:", exchange.bids.orders['T2'])
