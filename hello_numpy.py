import numpy as np

def main():
    print("Hello NumPy")
    print("np.__version__", np.__version__)
    # np.random.seed(42)
    # print(np.random.get_state())
    print(np.random.random(1))

if __name__ == '__main__':
    np.random.seed(42)
    main()
    # print(np.random.random(1))
