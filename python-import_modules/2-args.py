#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv.pop(0)

    args_len = len(argv)
    plural_args = '' if args_len == 1 else 's'
    punctuation_args = '.' if args_len == 0 else ':'

    print(f'{args_len} argument{plural_args}{punctuation_args}')

    if args_len > 0:
        for i in range(args_len):
            print(f'{i+1}: {argv[i]}')
