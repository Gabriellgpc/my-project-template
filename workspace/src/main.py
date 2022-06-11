import argparse

def parser_opt():
    parser = argparse.ArgumentParser()
    opt = parser.parser_opt()
    return opt

def main(opt):
    print('Hello, world')

if __name__ == '__main__':
    opt = parser_opt()
    main(opt)