import argparse
from PwnPattern import PatternEngine

def patts():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", dest="length", type=int, help="length of pattern", required=True)
    query = parser.add_mutually_exclusive_group(required=True)
    query.add_argument("-q", dest="query", help="hex value of eip(0x01020304)")
    query.add_argument("-qc", dest="query_char", help="ascii value of eip(AABC)")
    parser.add_argument("-b", dest="bad_char", help="bad characters")
    args = parser.parse_args()

    engine = PatternEngine(bad=args.bad_char)
    payload = engine.create_pattern(args.length)

    if args.query_char:
        query_pattern = args.query_char
    else:
        try:
            query_pattern = bytes.fromhex(args.query).decode('iso-8859-1')
        except ValueError as e:
            print("unable to parse {args.query} as heximal, missing leading zero or try '-qc'?")
            return

    offset = payload.find(query_pattern)
    if offset == -1:
        print("pattern not found in payload")
    else:
        print(f"pattern found with offset {offset} in payload")