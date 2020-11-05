import hashlib


def get_hash(path):
    with open(f'{path}', 'rb') as file:
        for line in file:
            yield hashlib.md5(line).hexdigest()

if __name__ == '__main__':
    print(__name__)