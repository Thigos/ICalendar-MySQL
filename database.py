import mysql.connector
import log

def open_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="db_calendar"
        )

        return connection, connection.cursor()
    
    except mysql.connector.Error as error:
        log.e(f'Erro na Conexão Com o BD: {error}')

        return False, False

def db_write(dict):
    connection, cursor = open_connection()
    sql = "INSERT INTO tb_calendar (`uidCalendar`,`summaryCalendar`,`descriptionCalendar`,`dtEndCalendar`,`categoriesCalendar`) VALUES (%s, %s, %s, %s, %s)"
    
    if connection != False and cursor != False:
        try:
            for key in dict:
                event = dict[key]
                
                values = (event['UID'], event['SUMMARY'], event['DESCRIPTION'], event['DTEND'], event['CATEGORIES'])

                cursor.execute(sql, values)
                connection.commit()

        except mysql.connector.errors.DatabaseError as error:
            log.e(f'Erro na Gravação do BD: {error}')

        else:
            log.s('Calendário Salvo no Banco de Dados')

        finally:
            cursor.close()
            connection.close()
        
        
