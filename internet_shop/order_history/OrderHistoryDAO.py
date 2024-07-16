from sqlalchemy import select

from base.BaseDAO import BaseDAO
from .models import OrderHistory
from products.models import Products
from database import session_maker


class OrderHistoryDAO(BaseDAO):
    @classmethod
    def find_all_orders(cls) -> list:
        orders = cls.find_all(OrderHistory)
        products = cls.find_all(Products)
        products_dict = {}
        for product in products:
            products_dict[product.id] = product.product_name
        result = []
        for order in orders:
            info = {
                'id': order.id,
                'product': products_dict[order.product],
                'date': order.date,
                'quantity': order.quantity,
                'full_cost': order.full_cost,
                'client': order.client,
            }
            result.append(info)
        return result
    

    @classmethod
    def find_order_by_id(cls, id: int) -> list:
        orders = cls.find_by_id(OrderHistory, id)
        if not orders:
            return None
        products = cls.find_all(Products)
        products_dict = {}
        for product in products:
            products_dict[product.id] = product.product_name
        result = []
        for order in orders:
            info = {
                'id': order.id,
                'product': products_dict[order.product],
                'date': order.date,
                'quantity': order.quantity,
                'full_cost': order.full_cost,
                'client': order.client,
            }
            result.append(info)
        return result