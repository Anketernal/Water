#обработка сигнала(направление и расстояние до цели)
import numpy  as np
import common

class Sonar(common.Common):
    def get_coordinats(self,signal_Left,signal_Right):
        spectrum_Left = np.fft.fft(signal_Left)
        spectrum_Right = np.fft.fft(signal_Right)

        n = spectrum_Left.size
        spectrum_Left[int(n/2):] = 0#сбрасываем у массива половину спектра отрицательную
        spectrum_Right[int(n/2):] = 0#сбрасываем у массива половину спектра отрицательную
        signal_Left = np.fft.ifft(spectrum_Left)#возвращаемся через обратное преобразование Фурье в область ...
        signal_Right = np.fft.ifft(spectrum_Right)

        z_Left = np.abs(np.fft.ifft(spectrum_Left))
        sigma = np.sqrt( ( np.sum(np.sqrt(z_Left))/n) )#уровень порога обноружения
        detection_level = np.where(z_Left>=sigma) #превышения порога

        print (detection_level)
        distance = ((detection_level[0][0])/self.fd) *1500 #определение дистанции через деление на частоту дискреизации и домножение на скорость звука
        print(distance)

        phi_Left = np.angle(signal_Left)
        phi_Right = np.angle(signal_Right)
        dphi = phi_Right - phi_Left  # разность фаз

        dphi[np.where(dphi > np.pi)] -= 2 * np.pi  # возвращаем фи в диапазон
        dphi[np.where(dphi < -np.pi)] += 2 * np.pi
        dphi_mean = sum(dphi) / dphi.size  # среднее значение фи
        print(dphi_mean)#выводим значение угла
        peleng = np.arcsin((self.c * dphi_mean) / (2 * np.pi * self.fs * self.d))

        print(peleng * (180 / np.pi))#вывод полученного угла в градусах



