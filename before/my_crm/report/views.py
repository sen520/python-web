from django.shortcuts import render
from customer.models import *
from django.db.models import Sum, Count
from django.views.decorators.http import require_POST, require_GET
from django.core.paginator import Paginator
from django.http.response import JsonResponse
from serve.models import *


# Create your views here.


# 客户贡献报表
def customer_contribute_index(request):
    return render(request, 'report_customer_contribution.html')


# 分页查询客户贡献值
@require_GET
def customer_contribute(request):
    queryset = Customer.objects.values('id', 'name') \
        .annotate(sum=Sum('customerorders__ordersdetail__sum')).order_by('-sum')
    # 过滤条件
    customer_name = request.GET.get('customerName')
    if customer_name:
        queryset = queryset.filter(name__icontains=customer_name)

    page_size = request.GET.get('rows', 10)
    page = request.GET.get('page', 1)
    # 构建分页对象
    p = Paginator(queryset, page_size)
    # 获取数据
    data = p.page(page).object_list
    total = p.count

    return JsonResponse({'rows': list(data), 'total': total})


# 客户构成分析
def customer_component_index(request):
    return render(request, 'report_customer_component.html')


# 获取客户构成数据
def customer_component(request):
    data = Customer.objects.values('level').annotate(amount=Count('level'))
    return JsonResponse(list(data), safe=False)


# 客户服务分析
def customer_serve_index(request):
    return render(request, 'report_customer_serve.html')


# 获取客户构成数据
def customer_serve(request):
    data = CustomerServe.objects.values('serveType').annotate(amount=Count('serveType'))
    return JsonResponse(list(data), safe=False)


# 客户流失分析
def customer_loss_index(request):
    return render(request, 'report_customer_loss.html')
