# Encodes the given URL

# To test:
# python urlencode.py 'https://some.where?q=query&filter="here is"&and=2,4,13.5'

import sys
import urllib.parse

def main():
    if len(sys.argv) != 2:
        print("Usage: python urlencode.py '<string>'")
        sys.exit(1)

    input_string = sys.argv[1]
    encoded_string = urllib.parse.quote(input_string)
    print(encoded_string)

if __name__ == "__main__":
    main()

