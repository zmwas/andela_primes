
def generate_prime_numbers(end_number):
    not_prime = []
    output = []
    if type(end_number)!=int:
        raise TypeError
    for i in range(2,end_number):
        for j in range(2,i):
            if i%j ==0:
                not_prime.append(i)
    for i in range(2,end_number):
        if i not in not_prime:
            output.append(i)
    return output


print(generate_prime_numbers(10))
