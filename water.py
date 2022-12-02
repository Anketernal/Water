#получение и зашумление сигналов
import common
import numpy as np
#import turtle as t
import matplotlib.pyplot as plt

class Water(common.Common):
    def get_signal(self,r,phi):
        time = np.arange (0,self.Tc,1/self.fd)
        signal_Left = np.random.randn(time.size)/10 #по нормальнома закону создаём сигнал
        signal_Right = np.random.randn(time.size) / 10

        delay = r/1500 #секунды
        dt = self.d/1500*np.sin(phi/180.0*np.pi)
        for i in range (time.size):#добавляем к сигналу шум
            if time[i] > delay and time[i] < delay+self.ti:
                signal_Left [i] += np.sin(2*np.pi*self.fs*time[i])
                signal_Right [i] += np.sin(2*np.pi*self.fs*(time[i]-dt))


        print(2 * np.pi * self.fs * dt * 180 / np.pi)  #выводим исходную фазу
        plt.plot(time, signal_Left, time, signal_Right)
        plt.show()
        return ((time, signal_Left, signal_Right))

