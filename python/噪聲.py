import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise  # type: ignore

xpix, ypix = 100, 100
N = 1000
n = [1, 4, 16, 64]
noise_list: list[PerlinNoise] = []
for i in n:
    noise_list.append(PerlinNoise(octaves=i))

m: list[list[float]] = []
for i in range(xpix):
    t: list[float] = []
    for j in range(ypix):
        t.append(sum(noise_list[k]([i / xpix, j / ypix]) / n[k] * N for k in range(len(n))))
    m.append(t)

plt.imshow(m, cmap="gray")  # type: ignore
plt.show()  # type: ignore
