import logging

logger = logging

logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%m/%d/%y-%I:%M:%S %p',
                   handlers=[
                       logging.FileHandler("Capa_Datos.log"),
                       logging.StreamHandler()
                   ]
                )

if __name__ == "__main__":
    logging.warning("Mensaje a nivel Warning")
    logging.info("Mensaje a nivel Info")
    logging.debug("Mensaje a nivel Debug")
    logging.debug("Mensaje a nivel Error")
