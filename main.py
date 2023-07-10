import sys
from modules import awsInventory


def main(argv):
    eks = awsInventory.eks()
    eks.file = sys.argv[1]
    print(eks.inventory())    
    sys.exit()


if __name__ == "__main__":
	main(sys.argv[1:])
