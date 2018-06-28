"""
View more, visit my tutorial page: https://morvanzhou.github.io/tutorials/
My Youtube Channel: https://www.youtube.com/user/MorvanZhou

Dependencies:
torch: 0.1.11
numpy
"""
import torch

'''
https://pytorch.org/#pip-install-pytorch
http://www.sohu.com/a/136715469_473283
'''
import numpy as np
# details about math operation in torch can be found in: http://pytorch.org/docs/torch.html#math-operations
# convert numpy to tensor or vise versa
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()
print(
    '\nnumpy array:', np_data,  # [[0 1 2], [3 4 5]]
    '\ntorch tensor:', torch_data,  # 0  1  2 \n 3  4  5    [torch.LongTensor of size 2x3]
    '\ntensor to array:', tensor2array,  # [[0 1 2], [3 4 5]]
)


# abs
data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)  # 32-bit floating point
print(
    '\nabs',
    '\nnumpy: ', np.abs(data),  # [1 2 1 2]
    '\ntorch: ', torch.abs(tensor)  # [1 2 1 2]
)

# sin
print(
    '\nsin',
    '\nnumpy: ', np.sin(data),  # [-0.84147098 -0.90929743  0.84147098  0.90929743]
    '\ntorch: ', torch.sin(tensor)  # [-0.8415 -0.9093  0.8415  0.9093]
)

# mean
print(
    '\nmean',
    '\nnumpy: ', np.mean(data),  # 0.0
    '\ntorch: ', torch.mean(tensor)  # 0.0
)

# matrix multiplication
data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)  # 32-bit floating point
# correct method
print(
    '\nmatrix multiplication (matmul)',
    '\nnumpy: ', np.matmul(data, data),  # [[7, 10], [15, 22]]
    '\ntorch: ', torch.mm(tensor, tensor)  # [[7, 10], [15, 22]]
)
# incorrect method
print('tensor 转 np.array 前\n',tensor)
data = np.array(data)
tensor = np.array(tensor)
print('data\n',data)
print('tensor 转 np.array 后\n',tensor)
'''
注意：torch 做矩阵内积，需要 转 np.array，否则报错如下：
RuntimeError: Expected argument self to have 1 dimension(s),
but has 2 at d:\pytorch\pytorch\torch\csrc\generic\TensorMethods.cpp:25700
'''
print(
    '\nmatrix multiplication (dot)',
    '\nnumpy: ', data.dot(data),  # [[7, 10], [15, 22]]
    '\ntorch: ', tensor.dot(tensor)  # this will convert tensor to [1,2,3,4], you'll get 30.0
)