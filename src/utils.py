def print_float(nbr: float, length, fill_end=True):
    nbr = round(nbr, length-(len(str(int(nbr)))+1))
    assert len(str(nbr)) <= length, f"{len(str(nbr))} n'est pas inférieur ou égal à {length}"
    nbr_splited = str(nbr).split('.')
    if fill_end and len(nbr_splited) > 1:
        nbr_splited[1] += '0' * (length - len(str(nbr)))
        return '.'.join(nbr_splited)
    else:
        return '0' * (length - len(str(nbr))) + '.'.join(nbr_splited)


if __name__ == '__main__':
    def main():
        print(print_float(12.3, 7))
    main()
