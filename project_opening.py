import water
import sonar

water = water.Water()
(time,signal_Left,signal_Right) = water.get_signal(500,30)

distance = sonar.Sonar().get_coordinats(signal_Left,signal_Right)#определяем расстояние
#если используем один раз можем сразу писать sonar.Sonar(). ... и т.п

