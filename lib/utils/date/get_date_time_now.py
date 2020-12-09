import datetime

datetime = datetime.datetime.now()


# Função que realiza a capptura da data e hora atual ou somente da data atual
def get_date_time_now(date_time):
    if date_time:
        return datetime.strftime('%d-%m-%Y_%H_%M_%S')
    elif datetime is False:
        return datetime.strftime('%d-%m-%Y')
