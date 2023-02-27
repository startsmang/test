def maoPao(dataset):
    n  = len(dataset)
    for i  in range(n-1):
        for j in range(n-i-1):
            if dataset[j] > dataset[j+1]:
                dataset[j] ,dataset[j+1] = dataset[j+1],dataset[j]
    return dataset

if __name__ == '__main__':
    dataset = [185,22,373,41,53,652,73,84]
    a = maoPao(dataset)
    print(a)
