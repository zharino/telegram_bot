from telegram.ext import Updater


class TelegramServer:
    TOKEN = '1728249539:AAHOBVN1BN1N2ghKsObhzBDio3_j6Axvdf0'

    def __init__(self):
        self.client = Updater(token=self.TOKEN, use_context=True)


if __name__ == '__main__':
    pass
