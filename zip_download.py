import io
import pyping2
from urllib import request


class ZipDownload:
    def __init__(self):
        self.__link = None
        self.__filename = None
        self.__output_file = None

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
                if ((link_inputed.startswith("http://") and link_inputed.endswith(".zip")) or
                        (link_inputed.startswith("https://") and link_inputed.endswith(".zip")) or
                        (link_inputed.startswith("http://") and link_inputed.endswith(".zip/")) or
                        (link_inputed.startswith("https://") and link_inputed.endswith(".zip/"))):
                    # Check if the link is valid
                    if self.__is_link_valid(link_inputed):
                        # Posicao .zip e da ultima barra
                        posicao_ponto_zip = link_inputed.find(".zip")
                        posicao_ultima_barra = link_inputed.rfind("/", 0,
                                                                  len(link_inputed) - 2 if link_inputed.endswith(
                                                                      "/") else len(link_inputed))
                        # Seta nome arquivo
                        self.__filename = link_inputed[posicao_ultima_barra + 1:posicao_ponto_zip]
                        # Seta link
                        self.__link = link_inputed
                        break
                    else:
                        # raise error
                        raise Exception("Link inválido")
                else:
                    # raise error
                    raise Exception("Error link invalido! \n O link deve comecar com http:// or https:// e possuir um "
                                    "arquivo .zip")
                # check if the link starts with http:// or https://
            except Exception as e:
                print(e)
