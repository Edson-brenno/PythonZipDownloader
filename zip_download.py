import io
import pyping2
from urllib import request


class ZipDownload:
    def __init__(self):
        self.__link = None
        self.__filename = None

    def __is_link_valid(self, link) -> bool:
        total_response_ping = pyping2.ping(link)
        if total_response_ping[1] == 200:
            return True
        else:
            return False

    def perguntar_link(self) -> None:
        while True:
            try:
                link_inputed = str(input("Digite o link: "))
                # check if the link starts with http:// or https://
                if link_inputed.startswith("http://") or link_inputed.startswith("https://"):
                    # Check if the link is valid
                    if self.__is_link_valid(link_inputed):
                        self.__link = link_inputed
                        break
                    else:
                        # raise error
                        raise Exception("Link inválido")
                else:
                    # raise error
                    raise Exception("Error link invalido! O link deve comecar com http:// or https://")
            except Exception as e:
                print(e)
