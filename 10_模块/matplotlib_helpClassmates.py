from matplotlib import get_backend, pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
#encoding='gbk'
# from matplotlib import font_manager
 
# my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
 
x = [1,2,3,4,5,6,7,8,9,10]
 
y = [-70.2,-73.3,-75.1,-75.4,-77.6,-83.1,-88.4,-86.2,-84.4,-88.1]

# plt.xlabel("Disstance（m）")
# plt.ylabel("RSSI值")
# color可以百度颜色代码
# plt.plot(x,y)
 
#绘制网格
plt.grid(alpha=0.6,linestyle=':')

 
#展示
# plt.show()
from scipy.interpolate import make_interp_spline
 # 插值法，50表示插值个数，个数>=实际数据个数，一般来说差值个数越多，曲线越平滑
x_new = np.linspace(min(x),max(x),50) 
 
y_smooth = make_interp_spline(x, y)(x_new)
 
plt.plot(x_new, y_smooth)
plt.xlabel("Disstance(m)")
plt.ylabel("RSSI")
plt.ylim(-70.0,-90.0)
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d m'))
 
plt.show()