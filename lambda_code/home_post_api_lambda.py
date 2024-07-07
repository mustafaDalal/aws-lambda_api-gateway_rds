import json, pymysql, os

# Configuration for your MySQL database

def lambda_handler(event, context):
  
    rds_host = os.getenv('RDS_HOST')
    rds_port = int(os.getenv('RDS_PORT'))
    rds_user = os.getenv('RDS_USER')
    rds_password = os.getenv('RDS_PASSWORD')
    rds_db_name = os.getenv('RDS_DB_NAME')
    rds_table_name = os.getenv('RDS_TABLE_NAME')

    
 
    # Parse the incoming request body
    request_body = json.loads(event['body'])

    # Extract data from request body
    amount = int(request_body.get('amount', 0))
    timestamp = int(request_body.get('timestamp', 0))
    
    print("amount : ", amount)
    print("timestamp : ", timestamp)

    # Establish a connection to the database
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
            # SQL query to insert data into table
            sql = "INSERT INTO expenses_table (amount, timestamp) VALUES (%s, %s)"
            cursor.execute(sql, (amount, timestamp))
            connection.commit()
        
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Data inserted successfully'})
            }
    except Exception as e:
        print(f"Error inserting data: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to insert data'})
        }
    finally:
        connection.close()  # Close database connection
