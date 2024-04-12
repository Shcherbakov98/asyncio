"""Очередь в супермаркете"""
import asyncio
from asyncio import Queue
from random import randrange
from typing import List


class Product:
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time


class Customer:
    def __init__(self, customer_id: int, products: List[Product]):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    while not queue.empty():  # выбираем покупателя, если в очереди кто-то есть
        customer: Customer = queue.get_nowait()
        print(f'Кассир {cashier_number} обслуживает покупателя {customer.customer_id}')
        for product in customer.products:  # обрабатываем каждый товар, купленный покупателем
            print(f'Кассир {cashier_number} обслуживает покупателя {customer.customer_id}: {product.name}')
            await asyncio.sleep(product.checkout_time)
        print(f'Кассир {cashier_number} закончил обслуживать покупателя {customer.customer_id}')
        queue.task_done()


async def main():
    customer_queue = Queue()

    all_products = [
        Product('Пиво', 2),
        Product('Бананы', 5),
        Product('Колбаса', 0.2),
        Product('Подгузники', 0.2),
    ]
    # создать 10 покупателей, со случайным набором товаров
    for i in range(10):
        products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]
        customer_queue.put_nowait(Customer(i, products))
    # создать трех кассиров, т.е задач, исполнителей, обслуживающих покупателей
    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(3)]
    await asyncio.gather(customer_queue.join(), *cashiers)


asyncio.run(main())
