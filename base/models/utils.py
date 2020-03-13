def generate_code(model, prefix, length=5):
    prefix_length = len(prefix)
    number_length = length - prefix_length
    number = 10 ** (number_length-1)
    count = model.objects.count()
    number += count
    from random import randrange
    return prefix + str(number) + str(randrange(10))
