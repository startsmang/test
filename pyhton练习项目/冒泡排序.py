# def bobbleShort(dataset):
#     # 获取数据的长度
#
#     arr =[1,1,23,35,36,388,33333,58]
#     n = len(dataset)
#          # 遍历整个数组的元素
#     for i in range(n):
#      for j in range(0,n-1):
#          if dataset[j] > dataset[j+1]:
#           dataset [j] , dataset[j+1] = dataset[j+1],dataset[j]
#     return dataset
#
#
#
# if __name__ == '__main__':
#      dataset = [1,23,35,36,388,33333,58]
#      bobbleShort(dataset)
#      print(dataset)


































def maopao(dataset):
    n  = len(dataset)
    for i in range(n):
        for j in range(0,n-1):
            if dataset[j] <  dataset[j+1]:
                dataset[j],dataset[j+1] = dataset[j+1] ,dataset[j]
    return dataset

if __name__ == '__main__':
    dataset = [1,2,3,4,5,6,99999,55,56]
    maopao(dataset)
    print(dataset)