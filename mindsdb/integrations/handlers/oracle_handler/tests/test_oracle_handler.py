import unittest
from mindsdb.integrations.handlers.oracle_handler.oracle_handler import OracleHandler
from mindsdb.api.mysql.mysql_proxy.libs.constants.response_type import RESPONSE_TYPE


class OracleHandlerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kwargs = {
            "host": "127.0.0.1",
            "port": "1521",
            "user": "admin",
            "password": "password",
            "sid": "ORCL"
        }
        cls.handler = OracleHandler('test_oracle_handler', **cls.kwargs)

    def test_0_check_connection(self):
        assert self.handler.check_connection()

    def test_1_native_query_select(self):
        query = "SELECT * FROM DUAL"
        result = self.handler.native_query(query)
        assert result.type is RESPONSE_TYPE.TABLE

    def test_2_get_tables(self):
        tables = self.handler.get_tables()
        assert tables.type is not RESPONSE_TYPE.ERROR

    def test_4_get_columns(self):
        columns = self.handler.get_columns('customers')
        assert columns.type is not RESPONSE_TYPE.ERROR