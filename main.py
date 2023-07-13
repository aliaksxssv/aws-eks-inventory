import sys, getopt
import configparser
from modules import awsInventory, logger


def main(argv):

    short_opts = ""
    long_opts = ""

    try:
        opts, args = getopt.getopt(argv, short_opts, long_opts)
    except getopt.error as err:
        logger.write(str(err), 'debug')
        sys.exit()      

    if "help" in args:
        print("Use cloud.ini file in the config folder to setup cloud environments")
        sys.exit()

    config_file = './config/cloud.ini'
    config = configparser.ConfigParser()
    config.read(config_file)

    # AWS inventory
    if config['aws']['profile'] != '':
        try:
            ec2 = awsInventory.ec2()
            ec2.aws_profile = config['aws']['profile']
            print(ec2.inventory())
        except Exception as e:
            logger.write(str(e), 'debug')
            print(e)

    #if "eks" in aws_scope.split(","):
    #    eks = awsInventory.eks()
    #    eks.file = sys.argv[1]
    #    print(eks.inventory())    


if __name__ == "__main__":
	main(sys.argv[1:])
