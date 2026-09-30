
def load_data():
    return [3, 17, 8, 25 , 6, 12, 25, 9, 14]

def filter_above(val,threshold=10):
    return [x for x in val if x>threshold]

def mean(values):
    return sum(values) / len(values)
print(mean(filter_above(load_data())))

if __name__ == '__main__':
    print('Самопроверка:', mean([1, 2, 3]))
