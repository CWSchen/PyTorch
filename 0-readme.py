
# 安装 ptorch
'''
python 3.5.可以在 windows上安装深度学习框架，
无论是TensorFlow还是Pytorch，都不支持python2，其中TF不支持3.6

https://www.lfd.uci.edu/~gohlke/pythonlibs/
有两个版本一个对应3.5一个对应3.6.然后下载以后，
在这个路径下 pip install "torch-0.3.0b0+591e73e-cp35-cp35m-win_amd64.whl"
(输入pip install 然后点击一下或多下tab，自动会有这个文件出现）

如果没有GPU，那其实安装已经结束了，但我相信大部分人，都是要gpu版本的。

去安装一下 cuda8+cudnn6. 或者 cuda9+cudnn7。我是前者，因为我装过TensorFlow只支持cuda8。
网上教程很多，不过坑，其实只有一个。安装cuda请选择自定义安装，只勾选cuda，其他一律不选！
然后英伟达驱动安装最新的低一版就可以（不放心最新版），驱动安装可以在cuda前也可以在cuda后。
至于cudnn，复制黏贴，很简单。下载不下来的话，可以联系我。

如果你在安装pytorch之前没有装cuda，那么你需要先  pip uninstall torch
然后再重新装一遍，测试的话：
然后，你们还可以试试具体案例（官方demo有的跑不起来，需要略作修改，可能是因为PyTorch版本更新太快的原因），
比如我写的一个训练好的ResNet：我的github，直接下载到一个文件夹下，
'''