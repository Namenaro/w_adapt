import matplotlib.pyplot as plt

def error(vals, val):
    errs = list([abs(x- val) for x in vals])
    return errs

def best_error(errs, index):
    # перебираем левее на начиная с ближайших индексов
    err = errs[index]
    i = index
    lefts_arr = []
    current_best_err = err
    while True:
        new_index = i-1
        if new_index<0:
            break
        new_err = errs[new_index]
        if new_err < current_best_err:
            current_best_err = new_err
        lefts_arr.append(current_best_err)
        i = new_index
    lefts_arr = list(reversed(lefts_arr))

    # перебираем левее на начиная с ближайших индексов
    i = index
    rights_arr = []
    current_best_err = err
    while True:
        new_index = i+1
        if new_index == len(errs):
            break
        new_err = errs[new_index]
        if new_err < current_best_err:
            current_best_err = new_err
        rights_arr.append(current_best_err)
        i = new_index

    best_errs_left_rigt = lefts_arr +[err]+ rights_arr
    return best_errs_left_rigt


def t1():
    vals = [3,2,1,2,3,4,4.2]
    index1 = 5
    val1 = 1.3


    # рисовашка:
    fig, ax = plt.subplots()
    ax.plot(vals, 'o-r', label='значения сенсоров')
    ax.set_ylim(bottom=0)
    ax.vlines(x=index1, ymin=0, ymax=val1)
    errs = error(vals, val1)
    ax.plot(errs, 'o-.g', label='абсолютная ошибка предсказания')

    ax.plot(best_error(errs, index1), 'o-.b', label='лучшая ошибка для областей')


    plt.legend()


if __name__ == '__main__':
    t1()
    plt.show()
