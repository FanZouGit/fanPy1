from multiprocessing import Pool

def test(num):
    return num*num

if __name__ == '__main__':
    p = Pool(processes=20,)
    data = p.map(test,[i for i in range(20,)])
    p.close()
    print(data)
    

