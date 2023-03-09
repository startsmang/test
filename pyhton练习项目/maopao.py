def maoPao(dataset):
    n = len(dataset)
    for i in range(0,n):
        for j in range(0,n-1):
            if dataset[j] > dataset[j+1]:
                dataset[j], dataset[j+1] = dataset[j+1],dataset[j]
    return dataset
if __name__ == '__main__':
    dataset =  [5,2,31,4,3,6,71,18,9,70]
    maoPao(dataset)
    print(dataset)