# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render

from django.views import View
# Create your views here.
class OrderView(View):
    def get(self,request):

        import jsonpickle
        # 判断当前用户是否登录
        if not request.session.get('user'):

            return HttpResponseRedirect('/user/login/?redirect=order&cartitems=' + request.GET.get('cartitems'))
        else:

            # 将购物项反序列化成[{k:v}{k:v}]形式列表对象

            # [{'goodsid':'','sizeid':'','colorid':''},{},{}]
            raw_cartitems = jsonpickle.loads('[' + request.GET.get('cartitems') + ']')
            # 目前还没有创建订单
            # 将购物项存放至session对象中
            # print 'hello1'
            # print raw_cartitems
            request.session['raw_cartitems'] = raw_cartitems
            return HttpResponseRedirect('/order/order.html')
            # return render(request,'order.html')

from cart.cartmanager import *

class OrderListView(View):
    def get(self,request):

        #获取当前用户下的购物项
        cart_manager = getCartManger(request)

        cartitems = [cart_manager.get_cartitems(**item) for item in request.session.get('raw_cartitems',[])]


        #获取当前用户下的默认收货地址
        address = request.session.get('user').address_set.get(isdefault=True)


        #计算结算总金额
        totalprice = 0
        for cartitem in cartitems:
            totalprice+=cartitem.total_price()

        return render(request,'order.html',{'cartitems':cartitems,'address':address,'totalprice':totalprice})

#Order  订单做的事情
# 将购物项转换成订单项(待支付)
# 将购物项从购物车删除
# 修改库存
# 根据支付方式跳转到支付界面
# 支付成功
# 验签
# 修改订单状态--->待发货
from User.models import *
from django.db.transaction import atomic
from models import *
from goods.models import *
from utils.alipay import AliPay

#创建Alipay对象初始化参数
alipay = AliPay(appid='2016091200491710', app_notify_url='http://127.0.0.1:8000/order/checkorder', app_private_key_path='my_private_key',
                 alipay_public_key_path='alipay_public_key', return_url='http://127.0.0.1:8000/order/checkorder', debug=True)

#获取支付宝付款页面
class ToOrderView(View):

    @atomic
    def get(self, request):
        import json, uuid, datetime

        #[{'goodsid':'','sizeid':'','colorid':'','count':''}]
        cartitems = json.loads(request.GET.get('cartitems'))


        raw_order = {
            'address': Address.objects.get(id=request.GET.get('address')),
            'payway': request.GET.get('payway', 'alipay'),
            'out_trade_num': uuid.uuid4().get_hex(),
            'order_num': datetime.datetime.today().strftime('%Y%m%d%H%M%S'),
            'user': request.session.get('user'),
        }
        order = Order.objects.create(**raw_order)
        total_amount = 0
        for item in cartitems:

            #创建订单项
            orderitem = OrderItem.objects.create(order=order, **item)
            #计算总金额
            total_amount += orderitem.total_price()
            #删除购物车中的购物项
            CartItem.objects.filter(**item).delete()
            #修改商品库存

            Inventory.objects.filter(goods_id=item['goodsid'], color_id=item['colorid'], size_id=item['sizeid']).update(
                count=F('count') - int(item['count']))
            #删除session中的结算购物项
            if 'raw_cartitems' in request.session:
                del request.session['raw_cartitems']


        params = alipay.direct_pay(subject='九块九电商支付', total_amount=str(total_amount),
                                   out_trade_no=order.out_trade_num)

        url = 'https://openapi.alipaydev.com/gateway.do?' + params

        return HttpResponseRedirect(url)

# 验证是否支付成功
class CheckOrderView(View):
    def get(self,request):
        # 获取所有请求参数
        d = request.GET.dict()

        # 从请求参数中移除sign
        sign = d.pop('sign')
        # 验证签名
        if alipay.verify(d, sign):
            out_trade_no = d.get('out_trade_no')
            # 根据订单支付编号获取当前订单
            order = Order.objects.get(out_trade_num=out_trade_no)
            # 修改订单状态
            if order.status == '待付款':
                order.status = '待发货'
                order.trade_no = d.get('trade_no')
                order.save()
            return HttpResponse('付款成功！')
        else:
            return HttpResponse('付款失败！')