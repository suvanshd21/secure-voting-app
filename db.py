import sqlite3, json
from sqlite3 import Error

def create_connection(database):
    try:
        conn = sqlite3.connect(database, isolation_level=None, check_same_thread = False)
        conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
        print("connection established")
        return conn
    except Error as e:
        print(e)

def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    c.execute(create_table_sql)

def select_all_candidates(conn):
    try:
        c = conn.cursor()
        sql_select_all = """
            SELECT * FROM candidates;
        """
        rows = c.execute(sql_select_all).fetchall()
        #return(json.dumps(rows))
        return(rows)
    except Error as e:
        print(e)

def select_candidate(conn,cand_id):
    try:
        c = conn.cursor()
        sql = """
            SELECT * FROM candidates WHERE id={0};
        """.format(cand_id)
        rows = c.execute(sql).fetchone()
        #return(json.dumps(rows))
        return(rows)
    except Error as e:
        print(e)

def insert_candidate(conn,insert_candidate_sql):
    try:
        c = conn.cursor()
        c.execute(insert_candidate_sql)
        print("Inserted Candidate")
    except Error as e:
        print(e)

def insert_user(conn,insert_user_sql):
    try:
        c = conn.cursor()
        c.execute(insert_user_sql)
        print("Inserted User")
    except Error as e:
        print(e)

def select_user(conn, voter_id, phone_number=None):
    try:
        c = conn.cursor()
        sql = """
            SELECT * FROM users WHERE voter_id = "{0}" AND phone_number = "{1}";
        """.format(voter_id,phone_number)
        if phone_number is None:
            sql = """
            SELECT * FROM users WHERE voter_id = "{0}";
            """.format(voter_id)
        return c.execute(sql).fetchone()
    except Error as e:
        print(e)

def update_vote(conn,cand_id):
    try:
        c = conn.cursor()
        sql = "UPDATE candidates SET votes = votes + 1 WHERE id = '{0}';".format(cand_id)
        c.execute(sql)
        print("Updated Vote")
    except Error as e:
        print(e)

def update_user(conn,voter_id,cand_id):
    try:
        c = conn.cursor()
        sql = "UPDATE users SET candidate_id = '{0}' WHERE voter_id = '{1}';".format(cand_id,voter_id)
        c.execute(sql)
        print("Updated User")
    except Error as e:
        print(e)

def main():
    database = "./pythonsqlite.db"
    conn = create_connection(database)
    sql_candidates_table = """ 
        CREATE TABLE IF NOT EXISTS candidates (
            id integer PRIMARY KEY,
            name varchar(225) NOT NULL,
            party varchar(225) NOT NULL,
            votes integer NOT NULL Default 0
        ); 
    """
    create_table(conn,sql_candidates_table)
    sql_users_table = """ 
        CREATE TABLE IF NOT EXISTS users (
            voter_id varchar(10) PRIMARY KEY,
            phone_number varchar(10) NOT NULL,
            name varchar(225) NOT NULL,
            candidate_id integer,
            foreign key(candidate_id) references candidates(id)
        ); 
    """
    create_table(conn,sql_users_table)
    # sql_insert_user="""
    # INSERT INTO users(voter_id,phone_number,name) VALUES(
    # "DEL1234567",
    # "9873940022",
    # "Suvansh Dutta"
    # )
    # """
    # insert_user(conn,sql_insert_user)
    # sql_insert_user="""
    # INSERT INTO users(voter_id,phone_number,name) VALUES(
    # "VEL1234567",
    # "9873940022",
    # "Suvansh Dutta"
    # )
    # """
    # insert_user(conn,sql_insert_user)
    # sql_insert_user="""
    # INSERT INTO users(voter_id,phone_number,name) VALUES(
    # "BEL1234567",
    # "9873940022",
    # "Suvansh Dutta"
    # )
    # """
    # insert_user(conn,sql_insert_user)
    # sql_insert_user="""
    # INSERT INTO users(voter_id,phone_number,name) VALUES(
    # "KOL1234567",
    # "9790650345",
    # "Souradeep Bhattacharya"
    # )
    # """
    # insert_user(conn,sql_insert_user)
    # sql_insert_user="""
    # INSERT INTO users(voter_id,phone_number,name) VALUES(
    # "VOL1234567",
    # "9790650345",
    # "Souradeep Bhattacharya"
    # )
    # """
    # insert_user(conn,sql_insert_user)
    # sql_insert_user="""
    # INSERT INTO users(voter_id,phone_number,name) VALUES(
    # "BOL1234567",
    # "9790650345",
    # "Souradeep Bhattacharya"
    # )
    # """
    # insert_user(conn,sql_insert_user)
    # sql_insert_user="""
    # INSERT INTO users(voter_id,phone_number,name) VALUES(
    # "DEL1234567",
    # "9873940022",
    # "Suvansh Dutta"
    # )
    # """
    # insert_user(conn,sql_insert_user)
    # sql_insert_user="""
    # INSERT INTO users(voter_id,phone_number,name) VALUES(
    # "HYD1234567",
    # "9652840525",
    # "Debdeep Mohanty"
    # )
    # """
    # insert_user(conn,sql_insert_user)
    # sql_insert_user="""
    # INSERT INTO users(voter_id,phone_number,name) VALUES(
    # "VYD1234567",
    # "9652840525",
    # "Debdeep Mohanty"
    # )
    # """
    # insert_user(conn,sql_insert_user)
    # sql_insert_user="""
    # INSERT INTO users(voter_id,phone_number,name) VALUES(
    # "BYD1234567",
    # "9652840525",
    # "Debdeep Mohanty"
    # )
    # """
    # insert_user(conn,sql_insert_user)


if __name__ == '__main__':
    main()