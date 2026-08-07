class BasicColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

class Log:
    LOG_WARNINGS = True


    PREFIX = '[Nedit]:'
    WS_PREFIX = '[WSL/Nedit]:'

    def __get_prefix(i):
        match (i):
            case 0:
                return ''
            case 1:
                return Log.PREFIX
            case 2:
                return Log.WS_PREFIX


            case _:
                return ''

    @staticmethod
    def debug(msg: str, type: int = 0):
        print(f'{BasicColors.HEADER}{Log.__get_prefix(type)} {msg}{BasicColors.RESET}')

    @staticmethod
    def info(msg: str, type: int = 0):
        print(f'{BasicColors.OKCYAN}{Log.__get_prefix(type)} {msg}{BasicColors.RESET}')

    @staticmethod
    def success(msg: str, type: int = 0):
        print(f'{BasicColors.OKGREEN}{Log.__get_prefix(type)} {msg}{BasicColors.RESET}')

    @staticmethod
    def warn(msg: str, type: int = 0):
        print(f'{BasicColors.WARNING}{Log.__get_prefix(type)} {msg}{BasicColors.RESET}')

    @staticmethod
    def error(msg: str, type: int = 0):
        print(f'{BasicColors.FAIL}{Log.__get_prefix(type)} {msg}{BasicColors.RESET}')


