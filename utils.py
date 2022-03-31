from settings import CONNECTION #settings must be git ignored!!
import logging
import datetime
import psycopg2
import os

def get_connection():
    conn = psycopg2.connect(CONNECTION)
    with conn.cursor() as cursor:
        cursor.execute(f"set application_name = 'energy_extract'")
    return conn

class bfe_console_formatter(logging.Formatter):
    def __init__(self):
        fmttext =  '%(levelname)-8s ESI number: %(energylabel_serial_identifier)-9s %(message)s'

        # invocation_id is set in environment by recent systemd services (232+ according to the internet)
        # as the journald already timestamps messages, only prepend the message with time if it seems like
        # we are called directly
        if 'INVOCATION_ID' not in os.environ:
            fmttext =  '%(asctime)s ' + fmttext

        self.fmt = logging.Formatter(fmt=fmttext, datefmt='%Y-%m-%d %H:%M:%S')

    def format(self, record):
        # ensure bfe_nr is in the record (set it to '' if needed), as our format string depends on it
        try:
            ESI = int(getattr(record, 'energylabel_serial_identifier'))
        except:
            ESI = ''

        record.ESI = ESI

        # let the standard formatter do it's job
        return self.fmt.format(record)


class log_db_handler(logging.Handler):
    def __init__(self, run_id):
        logging.Handler.__init__(self)
        self.run_id = run_id
        self.conn = psycopg2.connect(CONNECTION)
        self.conn.autocommit = True

    def emit(self, record):
        # call with logger.info(msg, extra={'energylabel_serial_identifier':311151948})
        try:
            esi = int(getattr(record, 'energylabel_serial_identifier', None))
        except:
            esi = None

        created_on = datetime.datetime.fromtimestamp(record.created)
        sql = """INSERT INTO
                    test1.run_logger
                        (run_id, created_on, energylabel_serial_identifier, log_level, log_leveltext, message)
                    VALUES
                        (%s, %s, %s, %s, %s, %s)"""
        with self.conn.cursor() as cur:
            cur.execute(sql, [self.run_id, created_on, esi, record.levelno, str(record.levelname), record.msg])


def get_logger(debug):
    sql_select_runid = """select MAX(run_id) 
                          from test1.run_logger 
                          rl limit 1"""
    with get_connection() as conn:
        with conn.cursor() as cur:
           cur.execute(sql_select_runid)
           run_id = cur.fetchone()[0]
    if not run_id:
        run_id = 1
    else:
        run_id += 1
    if debug:
        run_id = -1
    logger = logging.getLogger('')
    dbh = log_db_handler(run_id)
    dbh.setFormatter(logging.Formatter('%(levelname)-8s %(message)s'))
    logger.addHandler(dbh)
    logger.setLevel('INFO')
    ch = logging.StreamHandler()
    ch.setFormatter(bfe_console_formatter())
    ch.setLevel('INFO')
    logger.addHandler(ch)
    return logger


