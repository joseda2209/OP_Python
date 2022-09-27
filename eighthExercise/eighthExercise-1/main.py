
def main():
    archive = open('./demo.txt', 'w')
    archive.write("this is the first line of my archive")
    archive.close()

    archive = open('./demo.txt', 'r')
    print(f'el archivo tiene escrito:\n ${archive.read()}')
    archive.close()

if __name__ == '__main__':
    main()