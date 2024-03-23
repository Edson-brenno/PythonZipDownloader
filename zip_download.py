import io
from urllib import request


class ZipDownload:
    def __init__(self):
        self.__link = None
        self.__filename = None

    def perguntar_link(self) -> None:
        while True:
            try:
                link_inputed = str(input("Digite o link: "))
                if link_inputed.startswith("http://") or link_inputed.startswith("https://"):
                    self.__link = link_inputed
                    break
                else:
                    raise Exception("Error link invalido! O link deve comecar com http:// or https://")
            except Exception as e:
                print(e)

    def validar_link(self):

        if self.__link.startswith("http://") or self.__link.startswith("https://"):
            pass
        else:
            pass
