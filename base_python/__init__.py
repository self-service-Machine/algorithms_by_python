# import argparse
#
# if __name__ == '__main__':
#     paraser = argparse.ArgumentParser()
#     parent_parser = argparse.ArgumentParser(add_help=False)
#     paraser.add_argument("-a", "--allinone_uuid", help="allinone_uuid")


import argparse


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()