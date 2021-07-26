import matplotlib.pyplot as plt

from common.menu import print_menu
"""모두의데이터분석 62p참고."""
"""
list 값은 y축이고, x축은 0~1까지 자동으로 증가한다 
"""
def plot_show():
    plt.title("plotting")
    plt.plot([10,20,30,40])
    plt.show()

"""
첫번째 리스트가 x축 두번째 리스트가 y축이다.
"""
def plot_two_list_show():
    plt.plot([10, 20, 30, 40],[1000, 3 ,355, 3])
    plt.show()

def plot_label():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40], label='asc')
    plt.plot([40, 30, 10, 10], label='desc')
    plt.legend()
    plt.show()
def plot_marker():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40],'r.--', label='circle')
    plt.plot([40, 30, 10, 10],'g^' ,label='triangle up')
    plt.legend()
    plt.show()
def scatter():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40], 'r.', label='circle')
    plt.plot([40, 30, 10, 10], 'g^', label='triangle up')
    plt.legend()
    plt.show()
