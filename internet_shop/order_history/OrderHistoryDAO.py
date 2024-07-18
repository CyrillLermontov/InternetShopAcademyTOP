from sqlalchemy import select
from sqlalchemy.orm import aliased

from base.BaseDAO import BaseDAO
from .models import OrderHistory
from products.models import Products
from database import session_maker


class OrderHistoryDAO(BaseDAO):
    @classmethod
    def find_all_orders(cls) -> list:
        with session_maker() as session:
            products_alias = aliased(Products)
            query = (
            select(
                OrderHistory.id,
                OrderHistory.date,
                OrderHistory.quantity,
                OrderHistory.full_cost,
                OrderHistory.client,
                products_alias.product_name,
            )
            .select_from(OrderHistory)
            .join(products_alias, OrderHistory.product == products_alias.id)
            )
            result = []
            for row in session.execute(query):
                info = {
                    'id': row.id,
                    'product': row.product_name,
                    'date': row.date,
                    'quantity': row.quantity,
                    'full_cost': row.full_cost,
                    'client': row.client,
                }
                result.append(info)
        return result
    
    @classmethod
    def find_order_by_id(cls, id: int) -> list:
        with session_maker() as session:
            products_alias = aliased(Products)
            query = (
            select(
                OrderHistory.id,
                OrderHistory.date,
                OrderHistory.quantity,
                OrderHistory.full_cost,
                OrderHistory.client,
                products_alias.product_name,
            )
            .select_from(OrderHistory)
            .join(products_alias, OrderHistory.product == products_alias.id)
            .where(OrderHistory.id == id)
            )
            result = []
            for row in session.execute(query):
                info = {
                    'id': row.id,
                    'product': row.product_name,
                    'date': row.date,
                    'quantity': row.quantity,
                    'full_cost': row.full_cost,
                    'client': row.client,
                }
                result.append(info)
        return result