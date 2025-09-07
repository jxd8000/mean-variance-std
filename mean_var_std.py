import numpy as np

def calculate(list):
    
    # 检查输入是否为9个元素
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # 转换为3x3的numpy数组
    arr = np.array(list).reshape(3, 3)

    # 计算结果并存入字典
    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),   # 列方向的均值
            arr.mean(axis=1).tolist(),   # 行方向的均值
            arr.mean().item()            # 整个矩阵的均值
        ],
        'variance': [
            arr.var(axis=0).tolist(),
            arr.var(axis=1).tolist(),
            arr.var().item()
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            arr.std().item()
        ],
        'max': [
            arr.max(axis=0).tolist(),
            arr.max(axis=1).tolist(),
            arr.max().item()
        ],
        'min': [
            arr.min(axis=0).tolist(),
            arr.min(axis=1).tolist(),
            arr.min().item()
        ],
        'sum': [
            arr.sum(axis=0).tolist(),
            arr.sum(axis=1).tolist(),
            arr.sum().item()
        ]
    }



    return calculations