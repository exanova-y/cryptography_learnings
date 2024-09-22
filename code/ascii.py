# msg = "english manipulates minds"
# msg_ascii = [ord(c) for c in msg]
# print(msg_ascii)

def is_prime(number):
    if number < 2:
        return False
    # make sure this is int, not float
    for i in range(2, int((number)**0.5)+1):
        if number%i==0:
            return False
    return True


print(is_prime(7), is_prime(10), is_prime(144))