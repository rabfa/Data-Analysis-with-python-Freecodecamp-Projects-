import numpy as np

def calculate(l):
    if len(l) != 9:
        raise ValueError('List must contain nine numbers.')

    flatten = np.array(l)
    x = flatten.reshape(3, 3)
    
    summary = {
        'mean': [x.mean(axis=0).tolist(), x.mean(axis=1).tolist(), flatten.mean().tolist()],
        'variance': [x.var(axis=0).tolist(), x.var(axis=1).tolist(), flatten.var().tolist()],
        'standard deviation': [x.std(axis=0).tolist(), x.std(axis=1).tolist(), flatten.std().tolist()],
        'max': [x.max(axis=0).tolist(), x.max(axis=1).tolist(), flatten.max().tolist()],
        'min': [x.min(axis=0).tolist(), x.min(axis=1).tolist(), flatten.min().tolist()],
        'sum': [x.sum(axis=0).tolist(), x.sum(axis=1).tolist(), flatten.sum().tolist()]
    }
    
    return summary

l = [0, 1, 2, 3, 4, 5, 6, 7, 8]  
#l = [2,6,2,8,4,0,1,5,7]
calculate(l)



