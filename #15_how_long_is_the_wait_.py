import numpy as np

deli_worker = 1

deli_queue = 0

arriving_customers_hour = 30
serving_customers_hour = 40

seconds_hour = 3600
opening_hours = 10
opening_seconds = opening_hours * seconds_hour
idle_time = 0
max_queue_len = 0

avg_people_in_queue = 0

for i in range(opening_seconds):
    deli_queue += np.random.poisson(arriving_customers_hour / 3600)

    if deli_queue > max_queue_len:
        max_queue_len = deli_queue

    if deli_queue > 0:
        deli_queue -= np.random.poisson(serving_customers_hour / 3600)
    else:
        idle_time += 1

    avg_people_in_queue += deli_queue

idle_time /= opening_seconds
avg_people_in_queue /= opening_seconds

disp = "simulation ran for {} seconds, {} worker(s) had a max queue of {} and an average of {} people. The percentage of idle time is {}"

# format.(opening_seconds, deli_worker, max_queue_len, avg_people_in_queue, idle_time / opening_seconds)

print(disp.format(opening_seconds, deli_worker,
      max_queue_len, avg_people_in_queue, idle_time))
