import json, boto3, os, pymysql

def lambda_handler(event, context):
    
    # TODO implement
  
    print("The incoming data is", json.dumps(event))
    
    return connectToDatabaseAndTable()
    
def connectToDatabaseAndTable():
    rds_host = os.getenv('RDS_HOST')
    rds_port = int(os.getenv('RDS_PORT'))
    rds_user = os.getenv('RDS_USER')
    rds_password = os.getenv('RDS_PASSWORD')
    rds_db_name = os.getenv('RDS_DB_NAME')
    rds_table_name = os.getenv('RDS_TABLE_NAME')

    
    connection = pymysql.connect(
        host=rds_host,
        port=rds_port,
        user=rds_user,
        password=rds_password,
        db=rds_db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            # Execute query
            cursor.execute("SELECT * FROM expenses_table")
            rows = cursor.fetchall()
            
            print("Number of total rows : ", rows )
        
        return {
            "statusCode": 200,
            "body": rows
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
    
    finally:
        connection.close()