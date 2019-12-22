import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

def animate(X, Y, dt, figsize=(2,2), time_label_func=None):
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    line, = ax.plot([], [], 'o-', lw=2)
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    if time_label_func is None:
        def time_label_func(i):
            return 'time = %.1fs' % (i*dt)
    def init():
        print('here1')
        line.set_data([], [])
        time_text.set_text('')
        return line, time_text

    def addline(i):
        print('here2')
        thisx = [X[i], X[i+1]]
        thisy = [Y[i], Y[i+1]]
        print(thisx, thisy)
        line.set_data(thisx, thisy)
        time_text.set_text(time_label_func(i))
        return line, time_text
    
    return animation.FuncAnimation(
        fig, addline, np.arange(1, len(Y)-1),
        interval=1, blit=True, init_func=init)
