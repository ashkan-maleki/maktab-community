def generate_code(model, prefix, length=5):
    prefix_length = len(prefix)
    number_length = length - prefix_length
    if number_length < 2:
        raise ValueError('length should be greater than prefix length by two')
    number = 10 ** (number_length-1) + 11
    count = model.objects.count()
    number += count
    from random import randrange
    return prefix + str(number) + str(randrange(10))
