# -*- coding:utf-8 -*-
'''
Created on 2014年2月16日

@author: xuer
'''
# 日期元件
import math
class JDate():
    def __init__(self):
        self.Y = 2000
        self.M = 1
        self.D = 1
        self.h = 12
        self.m = 0
        self.s = 0
        self.J2000 = 2451545  # 2000年前儒略日数(2000-1-1 12:00:00格林威治平时)
        self.dts = [-4000, 108371.7, -13036.80, 392.000, 0.0000, -500, 17201.0, -627.82, 16.170, -0.3413,
                    - 150, 12200.6, -346.41, 5.403, -0.1593, 150, 9113.8, -328.13, -1.647, 0.0377,
                    500, 5707.5, -391.41, 0.915, 0.3145, 900, 2203.4, -283.45, 13.034, -0.1778,
                    1300, 490.1, -57.35, 2.085, -0.0072, 1600, 120.0, -9.81, -1.532, 0.1403,
                    1700, 10.2, -0.91, 0.510, -0.0370, 1800, 13.4, -0.72, 0.202, -0.0193,
                    1830, 7.8, -1.81, 0.416, -0.0247, 1860, 8.3, -0.13, -0.406, 0.0292,
                    1880, -5.4, 0.32, -0.183, 0.0173, 1900, -2.3, 2.06, 0.169, -0.0135,
                    1920, 21.2, 1.69, -0.304, 0.0167, 1940, 24.2, 1.22, -0.064, 0.0031,
                    1960, 33.2, 0.51, 0.231, -0.0109, 1980, 51.0, 1.29, -0.026, 0.0032,
                    2000, 64.7, -1.66, 5.224, -0.2905, 2150, 279.4, 732.95, 429.579, 0.0158, 6000]  # 世界时与原子时之差计算表
    
    def int2(self, v):  # 取整数部分
        v = int(math.floor(v))
        if(v < 0):
            return v + 1
        else:
            return v
    
    def deltatT(self, y):  # 计算世界时与原子时之差,传入年
        d = self.dts
#         for i in range(0, 100):
#             if(y < d[i + 5] or i == 95):
#                 break
        i = 0
        while i < 100:
            if(y < d[i + 5] or i == 95):
                break
            i += 5
        t1 = (y - d[i]) / (d[i + 5] - d[i] - 0.0) * 10
        t2 = t1 * t1
        t3 = t2 * t1
        return d[i + 1] + d[i + 2] * t1 + d[i + 3] * t2 + d[i + 4] * t3
    
    def deltatT2(self, jd):  # 传入儒略日(J2000起算),计算UTC与原子时的差(单位:日)
        return self.deltatT(jd / 365.2425 + 2000) / 86400.0
    
    def toJD(self, UTC):  # 公历转儒略日,UTC=1表示原日期是UTC
        y = self.Y
        m = self.M
        n = 0  # 取出年月
        if (m <= 2):
            m += 12
            y -= 1
        if (self.Y * 372 + self.M * 31 + self.D >= 588829):  # 判断是否为格里高利历日1582*372+10*31+15
            n = self.int2(y / 100)
            n = 2 - n + self.int2(n / 4)  # 加百年闰
        n += self.int2(365.2500001 * (y + 4716))  # 加上年引起的偏移日数
        n += self.int2(30.6 * (m + 1)) + self.D  # 加上月引起的偏移日数及日偏移数
        n += ((self.s / 60 + self.m) / 60 + self.h) / 24 - 1524.5
        if (UTC): 
            return n + self.deltatT2(n - self.J2000)
        return n
    
    def setFromJD(self, jd, UTC):  # 儒略日数转公历,UTC=1表示目标公历是UTC
        # 测试
        # print self.Y,self.M,jd,UTC
        if (UTC):
            jd -= self.deltatT2(jd - self.J2000)
        jd += 0.5
        A = self.int2(jd)
        F = jd - A
        # D取得日数的整数部份A及小数部分F
        if (A > 2299161):
            D = self.int2((A - 1867216.25) / 36524.25)
            A += 1 + D - self.int2(D / 4)
        A += 1524  # 向前移4年零2个月
        self.Y = int(self.int2((A - 122.1) / 365.25))  # 年
        D = A - self.int2(365.25 * self.Y)  # 去除整年日数后余下日数
        self.M = int(self.int2(D / 30.6001))  # 月数
        self.D = int(D - self.int2(self.M * 30.6001))  # 去除整月日数后余下日数
        self.Y -= 4716
        self.M -= 1
        if (self.M > 12):
            self.M -= 12
        if (self.M <= 2):
            self.Y += 1
        # 日的小数转为时分秒
        F *= 24
        self.h = int(self.int2(F))
        F -= self.h
        F *= 60
        self.m = int(self.int2(F))
        F -= self.m
        F *= 60
        self.s = F
        # 测试
        # print self.s
        
    def setFromStr(self, s):  # 设置时间,参数例:"20000101 120000"或"20000101"
        self.Y = int(s[0:4])
        self.M = int(s[4:6])
        self.D = int(s[6:8])
        self.h = int(s[9:11])
        self.m = int(s[11:13])
        self.s = int(s[13:18])
        # 测试
        # print self.s
    
    def toStr(self):  # 日期转为串
        Y, M, D = "     " + str(self.Y), "0" + str(self.M), "0" + str(self.D)
        h, m, s = self.h, self.m, math.floor(self.s + 0.5)
        if (s >= 60):
            s -= 60
            m += 1
        if (m >= 60):
            m -= 60
            h += 1
        h = "0%s" % h
        m = "0%s" % m
        s = "0%s" % int(s)
        # 测试
        Y = Y[len(Y) - 5:]
        M = M[len(M) - 2:]
        D = D[len(D) - 2:]
        h = h[len(h) - 2:]
        m = m[len(m) - 2:]
        s = s[len(s) - 2:]
        return Y + "-" + M + "-" + D + " " + h + ":" + m + ":" + s
    
    def Dint_dec(self, jd, shiqu, int_dec):
        
#         算出:jd转到当地UTC后,UTC日数的整数部分或小数部分
#         基于J2000力学时jd的起算点是12:00:00时,所以跳日时刻发生在12:00:00,这与日历计算发生矛盾
#         把jd改正为00:00:00起算,这样儒略日的跳日动作就与日期的跳日同步
#         改正方法为jd=jd+0.5-deltatT+shiqu/24
#         把儒略日的起点移动-0.5(即前移12小时)
#         式中shiqu是时区,北京的起算点是-8小时,shiqu取8
        u = jd + 0.5 - self.deltatT2(jd) + shiqu / (24 - 0.0)
        if (int_dec):
            return int(math.floor(u))  # 返回整数部分
        else:
            return u - math.floor(u)  # 返回小数部分
    
    def d1_d2(self, d1, d2):  # 计算两个日期的相差的天数,输入字串格式日期,如:"20080101"
        d1 = str(d1)
        d2 = str(d2)
        Y = self.Y
        M = self.M
        D = self.D
        h = self.h
        m = self.m
        s = self.s  # 备份原来的数据
        self.setFromStr(d1[0:8] + " 120000")
        jd1 = self.toJD(0)
        self.setFromStr(d2[0:8] + " 120000")
        jd2 = self.toJD(0)

        self.Y = Y
        self.M = M
        self.D = D
        self.h = h
        self.m = m
        self.s = s  # 还原
        if (jd1 > jd2):
            return int(math.floor(jd1 - jd2 + .0001))
        else:
            return -int(math.floor(jd2 - jd1 + .0001))

        
        
if __name__ == "__main__" :  
    jDate = JDate()
    jDate.setFromJD(2457072.50653, 1)
    print jDate.Dint_dec(20000, 8, 8)
    print jDate.toJD(2014)
    print jDate.deltatT(2014)
    print jDate.setFromStr("20000101 120000")
    print jDate.d1_d2('20080201', '20090302')
    print jDate.toStr()
    print math.pi
    s = 3.141592653589793
    print 3.141592653589793
    print s - 0.0
#     测试
#     print 3.0/6
#     print 3 - 0.0
#     print 1 / 3
#     print 1 / 3.0
        
        
        
    
