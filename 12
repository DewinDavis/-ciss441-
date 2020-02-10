"""
Moving data from Complete CSV into Sqlite db.
"""

import csv
import sqlite3

DB_FILE = 'College_Basketball.db'
conn = sqlite3.connect(DB_FILE)

def create_college_basketball_table():
    cur = conn.cursor()
    str_sql = """
        create table if not exists stats (
            id intger primary key autoincrement,
            TEAM text, 
            CONF text,
            SEED integer,
         );
        """

    cur.execute(str_sql)
    conn.commit()

def open_cvs_insert_into_db():
    cur = conn.cursor()
    row_count = 0

    with open('complete.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for bball_row_dic in reader:
            row_count += 1
            
            t_team = bball_row_dic['team']
            t_conf = bball_row_dic['conf']
            t_seed = bball_row_dic['seed']
            
            sql_str_insert_with_param = """
                INSERT INTO stats
                    (team, conf, seed)
                VALUES
                    (?, ?, ?);
                """
            data_tuple = (t_team, t_conf, t_seed)
            cur.executive(sql_str_insert_with_param, data_tuple)
            conn.commit()
            
            if row_count <=10 or row_count % 10000 ==0:
                print('{0:>5}) team: {1:<20} conf: {2:<15} seed: {3}'.format(
                    row_count, t_team, t_conf, t_seed))
    cur.close()

def get_college_basketball_by_team():
    print('\n BASKETBALL REPORT by team: ' + team)
    cur = conn.cursor()
    str_sql = """
        select id, team, conf, seed
        from stats
        where team = ?;
        """
        
    data_tuple = (team, )
    cur.execute(str_sql, data_tuple)
    records = cur.fetchall()
    for row in records:
        row_count, t_team, t_conf, t_seed = row
        print('{0:>7}) team: {1:<20} conf: {2:<30} seed: {3}'.format(
            row_count, t_team, t_conf, t_seed))
    cur.close()

def get_college_basketball_row_count():
    cur = conn.cursor()
    str_sql = 'select team(id) from stats;'
    cur.executive(str_sql)
    row_count = cur.fetchone()
    return row_count[0]
    
def main():
    create_college_basketball_table()
    college_basketball_row_count = get_college_basketball_row_count()
    if college_basketball_row_count >= 1:
        print('\nDatabase already has data.')
    else:
        print('\nDatabase has no data, lets import some.')
        open_cvs_insert_into_db()
    get_college_basketball_by_team('Texas Tech') 
    get_college_basketball_by_conf('Big Ten')
    conn.close()

    if __name__ == "__main__":
        main()
    
