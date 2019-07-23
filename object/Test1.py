def test(injry):
    __injry=injry if injry>=50 else 50
    # __injry=injry>50?injry:50
    print(__injry)


def main():
    test(40)


if __name__ == '__main__':
    main()