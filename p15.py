
"""Problem 15: How Long is the Wait

Simulation of a queue in a deli store using FCFS principle.

The customers in the queue are served by a number of "workers". The
arrival of customers are modeled as Poisson process with a fixed
rate. The service time of the workers are also simulated as a Poisson
process with a fixed rate.

This simulation attempts to answer the following questions:

1) What is the average time (wait+service) for a customer?
2) What is the maximum time for a customer?
3) What is the average length of the waiting queue?
4) What is the maximum length of the waiting queue?
5) What fraction of time is spent idle by the clerk(s)?
"""
import numpy as np


def simulate(workers, opening_seconds, customers_rate, service_rate):
    queue = []
    queue_max = 0

    customer_total_amount = 0
    customer_total_time = 0
    customer_max_time = 0
    num_customers = 0

    idle_time = 0

    for i in range(opening_seconds):
        customer_total_amount += len(queue)
        if len(queue) > queue_max:
            queue_max = len(queue)

        queue = [waiting_time + 1 for waiting_time in queue]
        arrival = np.random.poisson(lam=customers_rate)
        if arrival != 0:
            queue.append(0)

        if len(queue) > 0:
            serve = np.random.poisson(lam=service_rate)
            if serve > 0:
                customer_time = queue[0]
                if customer_time > customer_max_time:
                    customer_max_time = customer_time
                customer_total_time += customer_time
                queue.pop(0)
                num_customers += 1
        else:
            idle_time += 1

    average_time_spent = customer_total_time / num_customers
    average_length_queue = customer_total_amount / opening_seconds
    percent_no_customers = idle_time / opening_seconds

    print("average wait time {}".format(average_time_spent))
    print("max wait time {}".format(customer_max_time))
    print("average queue length {}".format(average_length_queue))
    print("maximum queue length {}".format(queue_max))
    print("idle time {}".format(percent_no_customers))


def main():
    arriving_customers_hour = 30
    serving_customers_hour = 40

    seconds_hour = 3600
    opening_hours = 10
    opening_seconds = opening_hours * seconds_hour

    simulate(1, opening_seconds, arriving_customers_hour /
             seconds_hour, serving_customers_hour / seconds_hour)


if __name__ == '__main__':
    main()
