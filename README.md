# USACO Guide Progress Fixer
A simple program restore your problem progress on usaco.guide from your activity.

一个简单的恢复 USACO 做题进度的工具。

可能中国用户更会遇到，在 Firebase 上登陆有时会有网络错误，造成一些奇怪的后果，比如提示 local progress override，导致做题记录丢失。

但是我发现做题记录不见了，活动和时间戳还保留着，在下载的 userdata 中，可以以此为依据改写 json 恢复做题记录。

用 Python 编写，单文件代码，没有可维护性，没有延展性，但是使用比较方便。

rsj

Jan/19/2022
