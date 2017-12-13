
import numpy as np
from matplotlib import pyplot as plt
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

def randomwalk(dims=(256, 256), n=20, sigma=5, alpha=0.95, seed=1):
    r, c = dims
    gen = np.random.RandomState(seed)
    pos = gen.rand(2, n) * ((r,), (c,))
    old_delta = gen.randn(2, n) * sigma
    while True:
        delta = (1. - alpha) * gen.randn(2, n) * sigma + alpha * old_delta
        pos += delta
        for ii in xrange(n):
            if not (0. <= pos[0, ii] < r):
                pos[0, ii] = abs(pos[0, ii] % r)
            if not (0. <= pos[1, ii] < c):
                pos[1, ii] = abs(pos[1, ii] % c)
        old_delta = delta
        yield pos

def run(niter=1000):
    fig, ax = plt.subplots(1, 1)
    ax.set_aspect('equal')
    ax.set_xlim(0, 255)
    ax.set_ylim(0, 255)
    ax.hold(True)
    rw = randomwalk()
    x, y = rw.next()
    plt.show(False)
    plt.draw()
    points = ax.plot(x, y, 'o')[0]
    for ii in xrange(niter):
        x, y = rw.next()
        points.set_data(x, y)
        fig.canvas.draw()
    plt.close(fig)


if __name__ == '__main__':
    run()
