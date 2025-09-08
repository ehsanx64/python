#!/usr/bin/env python3

# A simple example on base64 package in standard library

import base64

plain = "password"
encoded = ""
decoded = ""

encoded = base64.b64encode(plain.encode("utf-8"))
decoded = base64.b64decode(encoded.decode("utf-8"))

print("Plain text:    ", plain)
print("Base64 encoded:", encoded)
print("Base64 decoded:", decoded)
