import MySQLdb
import json


class Constants:
    host = 'localhost'
    user = 'root'
    password = 'root123'
    database = 'cbi_report'
    port = 3306

    # host = '10.120.193.105'
    # user = 'cbi'
    # password = 'cbi123#@!'
    # database = 'cbi_crawler'
    # port = 3306


class Company:
    def getCompany(self):
        conn = MySQLdb.connect(Constants.host, Constants.user, Constants.password, db=Constants.database, charset="utf8")
        cursor = conn.cursor()
        try:
            sql = """
                select bp_name, geo, region, country_code, bp_category, cross_buy,
                sellin_sum, bill_sum, contract_sum, machine_sum,loyalty, gp_size
                from cbi_bp_search limit 100
            """
            cursor.execute(sql)
            results = cursor.fetchall()
            data_list = []
            for item in results:
                data_list.append(item)

            return data_list

        except Exception as e:
            print(e)
        finally:
            conn.close()


if __name__ == "__main__":
    company = Company()
    company.getCompany()
