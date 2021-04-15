import mysql.connector
import json

class DB_Bing:
    # BING_COVID TABLE_SCHEMA
    # ['nid', 'state', 'country', 'last_update', 'lat', 'lng', 'confirmed', 'deaths', 'recovered', 'posted_date']

    mydb = None
    TEST_TABLE_NAME = "bing_covid_temp"
    PROD_TABLE_NAME = "bing_covid"
    db_connector = DatabaseSingleton.getInstance()

    def connect(): 
        db_connector.connect()

        

    def select():
        db_connector.select()


    def insert(data_dict, target_table="test"):
        table_name = PROD_TABLE_NAME if target_table == "prod" else TEST_TABLE_NAME
        mycursor = mydb.cursor()
        sql = "INSERT INTO {} (state, country, last_update, lat, lng, confirmed, deaths, recovered, posted_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE state = %s, country = %s, confirmed = %s, deaths = %s, recovered = %s".format(
            table_name
        )
        val = (
            data_dict["state"],
            data_dict["country"],
            data_dict["last_update"],
            data_dict["lat"],
            data_dict["lng"],
            data_dict["confirmed"],
            data_dict["deaths"],
            data_dict["recovered"],
            data_dict["posted_date"],
            data_dict["state"],
            data_dict["country"],
            data_dict["confirmed"],
            data_dict["deaths"],
            data_dict["recovered"],
        )
        print("SQL query: ", sql, val)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as ex:
            print(ex)
            print("Record not inserted")
