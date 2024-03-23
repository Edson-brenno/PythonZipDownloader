import io
from urllib import request


class ZipDownload:
    def __init__(self):
        self.__link = None
        self.__filename = None
    def perguntar_link(self) -> None:
        link_inputed = str(input("Digite o link: "))
        if self.__link.startswith("http://") or self.__link.startswith("https://"):
            pass
        else:
            pass
    def validar_link(self):

        if self.__link.startswith("http://") or self.__link.startswith("https://"):
            pass
        else:
            throw
