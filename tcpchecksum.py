def ip_to_bytes(ip: str) -> bytes:
    numbers = ip.split('.')
    return big_endian_int_from_str(numbers[0]) + big_endian_int_from_str(numbers[1]) + big_endian_int_from_str(
        numbers[2]) + big_endian_int_from_str(numbers[3])


def big_endian_int_from_str(value):
    return int(value).to_bytes(1, byteorder="big")


def ip_pseudo_header(src_ip: str, dst_ip: str, tcp_length: int) -> bytes:
    return ip_to_bytes(src_ip) + ip_to_bytes(dst_ip) \
        + (0).to_bytes(1, byteorder="big") \
        + (6).to_bytes(1, byteorder="big") \
        + tcp_length.to_bytes(4, byteorder="big")


print(ip_pseudo_header("255.0.255.1", "127.255.0.1", 3490))
