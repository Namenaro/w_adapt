import matplotlib.pyplot as plt

def error(vals, val):
    errs = list([abs(x- val) for x in vals])
    return errs

def t1():
    vals = [3,2,1,2,3,4,4.2]
    index1 = 2
    val1 = 1.3


    # рисовашка:
    fig, ax = plt.subplots()
    ax.plot(vals, 'o-r', label='значения сенсоров')
    ax.set_ylim(bottom=0)
    ax.vlines(x=index1, ymin=0, ymax=val1)
    ax.plot(error(vals, val1), 'o-.g', label='абсолютная ошибка предсказания')
    plt.legend()


if __name__ == '__main__':
    t1()
    plt.show()
