def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each 
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list 
    of which item(s) are in each bag.
    """
    # Your code here
    n = len(items)
    for i in xrange(3**n):
        bag1 = []
        bag2 = []
        for j in xrange(n):
            fc = (i // 3**j) % 3
            if fc == 1:
                bag1.append(items[j])
            elif fc == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

