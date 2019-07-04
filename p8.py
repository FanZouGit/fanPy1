from multiprocessing import Process

def test(num):
    print(num*num, num+1)

print(__name__)
if __name__ == '__main__':
    for i in range(5):
        p = Process(target=test,args=(i,))
        p.start()
    

