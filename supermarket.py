def queue_time(customers, n):
    queues = n *[0]
    while customers:
        next = customers.pop(0)
        # this could be optimized as we are exactly
        # one swap away from a sorted list at this point
        # so a dichotomy would yield a log(n) complexity instead
        queues.sort()
        # put the biggest customer is the shallowest queue
        queues[0] += next
    # we're done
    return max(queues)
