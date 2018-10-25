
#Write data Influx Database

from influxdb import InfluxDBClient

influxdb_ip='172.16.0.80'
influxdb_port=8086
influxdb_username='root'
influxdb_password='Aruba123!'
influxdb_db_name='example'

def write_data_db(data):
    client = InfluxDBClient(influxdb_ip, influxdb_port, influxdb_username, influxdb_password,influxdb_db_name)
    client.create_database(influxdb_db_name)
    client.write_points(data, time_precision='s')