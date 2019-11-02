import json

import requests


class Net(object):

    @staticmethod
    def create_order_data(product_id, product_sku_id, buy_nums, activity_id):
        data = {}

        data['product_id'] = product_id
        data['product_sku_id'] = product_sku_id
        data['buy_nums'] = buy_nums
        data['activity_id'] = activity_id
        return data

    @staticmethod
    def create_order(product_id, product_sku_id, buy_nums, activity_id, headers):
        url = 'https://billeslook.com/api/order/buy_direct?origin_type=1'

        data = Net.create_order_data(product_id, product_sku_id, buy_nums, activity_id)

        print(json.dumps(data))
        response = requests.post(url, data=data, headers=headers, verify=False)
        return response


    @staticmethod
    def create_order_confirm(order_sn, address_id, purchaser_identity_card, purchaser_name, user_coupon_id, pay_type,
                      customer_comments):
        data = {}

        data['order_sn'] = order_sn
        data['address_id'] = address_id
        data['purchaser_identity_card'] = purchaser_identity_card
        data['purchaser_name'] = purchaser_name
        data['user_coupon_id'] = user_coupon_id
        data['pay_type'] = pay_type
        data['customer_comments'] = customer_comments
        return data

    @staticmethod
    def confirm_order(order_sn, address_id, purchaser_identity_card, purchaser_name, user_coupon_id, pay_type,
                      customer_comments,headers):
        url = 'https://billeslook.com/api/order/confirm?origin_type=1'
        data = Net.create_order_confirm(order_sn, address_id, purchaser_identity_card, purchaser_name, user_coupon_id, pay_type,
                      customer_comments)

        print(json.dumps(data))
        response = requests.post(url, data=data, headers=headers, verify=False)
        return response

