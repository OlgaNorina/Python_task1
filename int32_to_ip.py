def int32_to_ip(int32):
     hex_str = f"{int32:08x}"
     hex_str_list = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
     int_list = [int(s, 16) for s in hex_str_list]
     dec_str_list = [str(i) for i in int_list]
     return '.'.join(dec_str_list)
      

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
