import argparse
import os

if __name__ == '__main__':
    def file(w,name):
        w = input("введиите абсолютный путь: ")
        name = input("введите имя файла: ")
        for dirs, folder, files in os.walk(w):
            for file in files:
                if file == name:
                    path_file = os.path.join(dirs, file)
                    print(path_file, 'существует')


parser = argparse.ArgumentParser(
    description='my arg parser'
)
parser.add_argument(
    '-- w',
    dest='w',
    type=int,
    help='first int value'
)
parser.add_argument(
    '-- name',
    dest='name',
    type=int,
    help='first int value'
)



args = parser.parse_args()
print(args.name)

result = file(args.w, args.name)
print(result)