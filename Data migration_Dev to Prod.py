import snowflake.connector

# Connectio string
conn = snowflake.connector.connect(
                user='pashminamulchandani',
                password='Hexa@1234567',
                account='vc42987.ap-south-1.aws',
                warehouse='COMPUTE_WH',
                database='PROD',
                schema='public'
                )

# Create cursor
cur = conn.cursor()

# Execute SQL statement: Create a table in prod
cur.execute("Create or replace table Student_PROD(ROLLNo int PRIMARY KEY,NAME VARCHAR(200))")

# Execute SQL statement: Transfer data from dev to prod
cur.execute("Insert into Student_PROD select * from DEV.PUBLIC.Student_DEV")

