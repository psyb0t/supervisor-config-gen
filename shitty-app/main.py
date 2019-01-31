from time import sleep, strftime, localtime

def main():
    while True:
        print('Fuck! Look at the fucking time: %s' % str(strftime('%H:%M:%S', localtime())))
        sleep(10)

if __name__ == '__main__':
	main()
