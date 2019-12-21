from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from datetime import datetime, timedelta

from .models import Product, Material

# Create your views here.
class InventoryList(TemplateView):
    template_name = 'modules/inventory/inventory.html'

    def get_context_data(self, **kwargs):
        context = super(InventoryList, self).get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        context['material_list'] = Material.objects.all()
        return context


# class ProductDetail(DetailView):
#     model = Product
#     template_name = 'modules/inventory/product_detail.html'
#     context_object_name = 'product'


class ProductUpdate(UpdateView):
    model = Product
    fields = ['inventory', 'safety_stock']
    template_name = 'modules/inventory/product_update.html'

    def get_success_url(self):
        return reverse('inventory:list')

class MaterialUpdate(UpdateView):
    model = Material
    fields = ['inventory']
    template_name = 'modules/inventory/material_update.html'

    def get_success_url(self):
        return reverse('inventory:list')


class ScheduleForm(View):
    def get(self, request):
        return render(request, 'modules/inventory/schedule_form.html')

    def post(self, request):
        try:
            get_um = self.request.POST.get('umbrella')
            num = int(self.request.POST.get('num_of_umbrella'))
            date = self.request.POST.get('date')
        except ValueError:
            err_message = "資料不完全，請輸入完整資料。"
            return render(request, 'modules/inventory/schedule_form.html', locals())
        date_1 = datetime.strptime(date, "%Y-%m-%d").date()
        umbrella = ""
        if get_um == "雞汁小雞麵":
            umbrella = Product.objects.get(number="1")
        elif get_um == "辣味小雞麵":
            umbrella = Product.objects.get(number="2")
        elif get_um == "海苔小雞麵":
            umbrella = Product.objects.get(number="3")
        elif get_um == "起司小雞麵":
            umbrella = Product.objects.get(number="4")
        elif get_um == "BBQ小雞麵":
            umbrella = Product.objects.get(number="5")

        lack = num - umbrella.inventory
        product_tree_list = []
        material_tree_list = []
        plastic = 0
        frp = 0
        fabric = 0
        plastic_date_lst = []
        frp_date_lst = []
        fabric_date = None

        product = umbrella.name
        product_wanted = num
        product_inventory= umbrella.inventory
        product_diff = product_wanted - umbrella.inventory
        product_lead_time = umbrella.lead_time
        produce_date = date_1 - timedelta(days=umbrella.lead_time)
        produce_date_str = str(date_1 - timedelta(days=umbrella.lead_time))
        produce_epq = umbrella.epq
        product_tree_list.append([product, product_wanted, product_inventory, product_diff, product_lead_time, produce_date_str, produce_epq])

        for material in umbrella.materials_required.all():
            material_wanted = lack
            material_diff = material_wanted - material.inventory
            produce_date = date_1 - timedelta(days=material.material_detail.lead_time)
            produce_date_str = str(date_1 - timedelta(days=material.material_detail.lead_time)-timedelta(days=umbrella.lead_time))
            material_tree_list.append([material, material_wanted, material_diff, produce_date_str])
        return render(request, 'modules/inventory/schedule_form.html', locals())
