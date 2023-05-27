#Mod değeri en çok görünen değerdir. 'mode()' En çok görünen sayıyı bulmak için SciPy yöntemini kullanılır.

from scipy import stats

speed = [1,2,3,3,4,5,6,7,8,33,0]

x = stats.mode(speed)

print(x)