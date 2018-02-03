def write (fopen):

    fopen.write('P3\n')
    fopen.write('500 500\n')
    fopen.write('255\n')

    for r in range (0,500):
        for c in range (0,500):
            fopen.write('255 0 ' + str(r) + ' ')
        fopen.write('\n')

def main():
    f = open('hw1.ppm', 'w')
    write(f)
    f.close

main()
