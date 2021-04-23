"""InfluxDB Helper."""

from influxdb import InfluxDBClient


class InfluxDBHelper:

    INFLUXDB_HOST = "YOUR_HOST_OR_IP"
    INFLUXDB_PORT = 8086
    INFLUXDB_DATABASE = "YOUR_DB"
    INFLUXDB_USERNAME = "YOUR_USER"
    INFLUXDB_PASSWORD = "YOUR_PWD"

    def __init__(self):
        self.influxdb_client = InfluxDBClient(
            host=self.INFLUXDB_HOST,
            port=self.INFLUXDB_PORT,
            username=self.INFLUXDB_USERNAME,
            password=self.INFLUXDB_PASSWORD,
            database=None,
        )
        databases = self.influxdb_client.get_list_database()
        if self.INFLUXDB_DATABASE not in [x["name"] for x in databases]:
            self.influxdb_client.create_database(self.INFLUXDB_DATABASE)
        self.influxdb_client.switch_database(self.INFLUXDB_DATABASE)

    def _send_sensor_data_to_influxdb(self, sensor_data):
        json_body = [
            {
                "measurement": sensor_data["measurement"],
                "tags": {"location": sensor_data["location"]},
                "fields": {"value": sensor_data["value"]},
            }
        ]
        self.influxdb_client.write_points(json_body)


if __name__ == "__main__":
    print("Starting main()...")
    idh = InfluxDBHelper()
