import json
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, View
from django.db.models import Q

from datetime import datetime, timedelta

from mysite.views import ListView
from .models import Transaction, Transaction_product
from apps.inventory.models import Product

# Create your views here.
class TransactionYear(View):
    def get(self, request):
        product_dict = {
            '雞汁小雞麵': [0, 0, 0], '辣味小雞麵': [0, 0, 0], '海苔小雞麵': [0, 0, 0], '起司小雞麵': [0, 0, 0],
            'BBQ小雞麵': [0, 0, 0],
        }
        products_2016 = Transaction_product.objects.filter(transaction__date__year=2016)
        products_2017 = Transaction_product.objects.filter(transaction__date__year=2017)
        products_2018 = Transaction_product.objects.filter(transaction__date__year=2018)
        for trans_data in products_2016:
            product_dict[trans_data.product.name][0] += trans_data.quantity
        for trans_data in products_2017:
            product_dict[trans_data.product.name][1] += trans_data.quantity
        for trans_data in products_2018:
            product_dict[trans_data.product.name][2] += trans_data.quantity
        return render(request, 'modules/transaction/transaction_year.html', locals())


class TransactionSeason(View):
    def get(self, request):
        return render(request, 'modules/transaction/transaction_season.html')
    def post(self, request):
        req_season = self.request.POST.get('season')
        month_start = 0
        month_end = 0
        if req_season == "春季":
            month_start = 3
            month_end = 5
        elif req_season == "夏季":
            month_start = 6
            month_end = 8
        elif req_season == "秋季":
            month_start = 9
            month_end = 11
        elif req_season == "冬季":
            month_start = 12
            month_end = 2
        product_dict = {
            '雞汁小雞麵': [0, 0, 0], '辣味小雞麵': [0, 0, 0], '海苔小雞麵': [0, 0, 0], '起司小雞麵': [0, 0, 0],
            'BBQ小雞麵': [0, 0, 0],
        }
        if req_season != "冬季":
            products_2016 = Transaction_product.objects.filter(transaction__date__year=2016, transaction__date__month__gte=month_start, transaction__date__month__lte=month_end)
            products_2017 = Transaction_product.objects.filter(transaction__date__year=2017, transaction__date__month__gte=month_start, transaction__date__month__lte=month_end)
            products_2018 = Transaction_product.objects.filter(transaction__date__year=2018, transaction__date__month__gte=month_start, transaction__date__month__lte=month_end)
            for trans_data in products_2016:
                product_dict[trans_data.product.name][0] += trans_data.quantity
            for trans_data in products_2017:
                product_dict[trans_data.product.name][1] += trans_data.quantity
            for trans_data in products_2018:
                product_dict[trans_data.product.name][2] += trans_data.quantity
        elif req_season == "冬季":
            products_2016 = Transaction_product.objects.filter(Q(transaction__date__year=2016) & (Q(transaction__date__month=12) |
            Q(transaction__date__month=1) | Q(transaction__date__month=2)))
            products_2017 = Transaction_product.objects.filter(Q(transaction__date__year=2017) & (Q(transaction__date__month=12) |
            Q(transaction__date__month=1) | Q(transaction__date__month=2)))
            products_2018 = Transaction_product.objects.filter(Q(transaction__date__year=2018) & (Q(transaction__date__month=12) |
            Q(transaction__date__month=1) | Q(transaction__date__month=2)))
            for trans_data in products_2016:
                product_dict[trans_data.product.name][0] += trans_data.quantity
            for trans_data in products_2017:
                product_dict[trans_data.product.name][1] += trans_data.quantity
            for trans_data in products_2018:
                product_dict[trans_data.product.name][2] += trans_data.quantity
        return render(request, 'modules/transaction/transaction_season.html', locals())


class TransactionMonth(View):
    def get(self, request):
        return render(request, 'modules/transaction/transaction_month.html')
    def post(self, request):
        req_month = self.request.POST.get('month')
        product_dict = {
            '雞汁小雞麵': [0, 0, 0], '辣味小雞麵': [0, 0, 0], '海苔小雞麵': [0, 0, 0], '起司小雞麵': [0, 0, 0],
            'BBQ小雞麵': [0, 0, 0],
        }
        products_2016 = Transaction_product.objects.filter(transaction__date__year=2016, transaction__date__month=req_month)
        products_2017 = Transaction_product.objects.filter(transaction__date__year=2017, transaction__date__month=req_month)
        products_2018 = Transaction_product.objects.filter(transaction__date__year=2018, transaction__date__month=req_month)
        for trans_data in products_2016:
            product_dict[trans_data.product.name][0] += trans_data.quantity
        for trans_data in products_2017:
            product_dict[trans_data.product.name][1] += trans_data.quantity
        for trans_data in products_2018:
            product_dict[trans_data.product.name][2] += trans_data.quantity
        return render(request, 'modules/transaction/transaction_month.html', locals())


class TransactionChart(View):
    def get(self, request):
        return render(request, 'modules/transaction/transaction_chart.html')

    def post(self, request):
        year = int(self.request.POST.get('year'))
        month = int(self.request.POST.get('month'))
        uv_s_sold = 0
        uv_auto_sold = 0
        uv_manual_sold = 0
        wind_s_sold = 0
        wind_auto_sold = 0
        wind_manual_sold = 0
        l_s_sold = 0
        l_auto_sold = 0
        l_manual_sold = 0
        for trans_data in Transaction_product.objects.filter(Q(transaction__date__year=year) &
        Q(transaction__date__month=month)):
            if trans_data.product.name == "雞汁小雞麵":
                uv_s_sold += trans_data.quantity
            elif trans_data.product.name == "辣味小雞麵":
                uv_auto_sold += trans_data.quantity
            elif trans_data.product.name == "海苔小雞麵":
                uv_manual_sold += trans_data.quantity
            elif trans_data.product.name == "起司小雞麵":
                wind_s_sold += trans_data.quantity
            elif trans_data.product.name == "BBQ小雞麵":
                wind_auto_sold += trans_data.quantity

        chart = {
            'chart': {'type': 'column', 'colors': 'Array.<Highcharts.ColorString>', 'backgroundColor': 'rgba(0, 0, 0, 0)'},
            'title': {
                'text': str(year) + '年 ' + str(month) + '月雨傘銷售分布',
                'style': {
                    'fontFamily': 'Microsoft JhengHei'
                }
            },
            'xAxis': {'categories': ['雞汁小雞麵', '辣味小雞麵', '海苔小雞麵', '起司小雞麵', 'BBQ小雞麵']},
            'series': [{
                'name': '銷售量',
                'data': [
                    {'y': uv_s_sold, 'color': '#058DC7'},
                    {'y': uv_auto_sold, 'color': '#50B432'},
                    {'y': uv_manual_sold, 'color': '#ED561B'},
                    {'y': wind_s_sold, 'color': '#DDDF00'},
                    {'y': wind_auto_sold, 'color': '#24CBE5'},
                    {'y': wind_manual_sold, 'color': '#64E572'},
                    {'y': l_s_sold, 'color': '#FF9655'},
                    {'y': l_auto_sold, 'color': '#FFF263'},
                    {'y': l_manual_sold, 'color': '#6AF9C4'},
                ],
            'backgroundColor': '#f4f7f6'
            }],

            'plotOptions': {
                'series': {
                    # 'grouping': False,
                }
            }
        }

        dump = json.dumps(chart)

        return render(request, 'modules/transaction/transaction_chart.html', {'chart': dump})
