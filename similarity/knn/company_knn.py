import numpy as np
from sklearn import neighbors
from similarity.util.company import Company


def dict2list(dic: dict):
    ''' 将字典转化为列表 '''
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst

def knn():
    # 1 - 10
    # [geo, region, country, bp_category, cross_buy, sellin_sum, bill_sum, contract_sum, machine_sum, loyalty, gp_size ]
    weight = [5, 6, 7, 8, 8, 10, 10, 10, 10, 10, 10, 10]
    data_list = Company().getCompany()

    for item in data_list:
        result = {}
        company_name = item[0]
        origin_geo = item[1]
        origin_region = item[2]
        origin_country = item[3]
        origin_bp_category = item[4]
        origin_cross_buy = item[5]
        origin_sellin_sum = item[6]
        origin_bill_sum = item[7]
        origin_contract_sum = item[8]
        origin_machine_sum = item[9]
        origin_loyalty = item[10]
        origin_gp_size = item[11]

        result_dict = {}
        data_list_copy = data_list[:]

        for tar in data_list_copy:
            tar_company = tar[0]
            geo = 0 if tar[1] == origin_geo else 9
            region = 0 if tar[2] == origin_region else 9
            country = 0 if tar[3] == origin_country else 9
            bp_category = 0 if tar[4] == origin_bp_category else 9
            cross_buy = 0 if tar[5] == origin_cross_buy else 9
            sellin_sum = float(tar[6] if tar[6] else 0) - float(origin_sellin_sum if origin_sellin_sum else 0)
            bill_sum = float(tar[7]) - float(origin_bill_sum)
            contract_sum = float(tar[8]) - float(origin_contract_sum)
            machine_sum = float(tar[9]) - float(origin_machine_sum)
            loyalty = 0 if tar[10] == origin_loyalty else 9
            gp_size = 0 if tar[11] == origin_gp_size else 9

            distance = (
                geo ** 2 / weight[0] + region ** 2 / weight[1]
                + country ** 2 / weight[2] + bp_category ** 2 / weight[3]
                + cross_buy ** 2 / weight[4] + sellin_sum ** 2 / weight[5]
                + sellin_sum ** 2 / weight[6] + sellin_sum ** 2 / weight[7]
                + bill_sum ** 2 / weight[7] + contract_sum ** 2 / weight[8]
                + machine_sum ** 2 / weight[9] + loyalty ** 2 / weight[10]
                + gp_size ** 2 / weight[11]
            ) ** 0.5

            result_dict[tar_company] = distance

        # print(result_dict)
        sorted_result_dict = sorted(dict2list(result_dict), key=lambda d: d[1])
        result[company_name] = sorted_result_dict[1:6]

        print(result)

if __name__ == "__main__":
    knn()