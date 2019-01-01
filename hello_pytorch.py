import torch
import torchvision

def main():
    print("Hello PyTorch")
    print("torch.__version__", torch.__version__)
    print("torchvision.__version__", torchvision.__version__)

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # Assume that we are on a CUDA machine, then this should print a CUDA device:
    print("device", device)

    x = torch.empty(5, 3)
    print("torch.empty(5, 3)", "\n", x)

if __name__ == '__main__':
    main()