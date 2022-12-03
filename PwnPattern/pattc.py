import argparse
from PwnPattern import PatternEngine

def pattc():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", dest="length", type=int, help="length of pattern", required=True)
    parser.add_argument("-o", dest="output", help="output file")
    parser.add_argument("-b", dest="bad_char", help="bad characters")
    args = parser.parse_args()

    engine = PatternEngine(bad=args.bad_char)
    payload = engine.create_pattern(args.length)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(payload)
    else:
        print(payload)