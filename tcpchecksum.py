def ip_to_bytes(ip: str) -> bytes:
    numbers = ip.split('.')
    return big_endian_int_from_str(numbers[0]) + big_endian_int_from_str(numbers[1]) + big_endian_int_from_str(numbers[2]) + big_endian_int_from_str(numbers[3])


def big_endian_int_from_str(value):
    return int(value).to_bytes(1, byteorder="big")


print(ip_to_bytes("192.168.1.1"))
