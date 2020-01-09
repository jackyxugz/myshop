# -*- coding : utf-8 -*-
# coding: utf-8

from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    # Task to send an e-mail notification when an order is successfully created.
    order = Order.objects.get(id=order_id)
    subject = 'Your order No. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
               \n\nYour order id is {}.'.format(order.first_name, order.id)
    # mail_sent = send_mail(subject, message, 'admin@myshop.com', {order.email})
    send_mail(subject, message, 'laxgz@163.com', {order.email})
