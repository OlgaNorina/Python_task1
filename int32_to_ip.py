def int32_to_ip(a):
     b = f"{a:08x}"
     c=[b[i:i+2] for i in range(0, len(b), 2)]
     d=[int(s, 16) for s in c]
     e=[str(i) for i in d]
     return '.'.join(e)
      

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
