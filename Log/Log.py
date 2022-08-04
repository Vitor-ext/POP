import logging

##################  Criando e COnfigurando Log   ####################

class Log ():

    Log_Format = "%(message)s - %(asctime)s - %(levelname)s "

    logging.basicConfig(filename ="bot.log",
                        filemode = "a",
                        format =Log_Format,
                        level = logging.INFO)

    logger = logging.getLogger()
