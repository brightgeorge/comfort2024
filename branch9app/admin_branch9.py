# admin_branch9
import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

from branch9app.models import *
import datetime


# ***branch1 rooms start here

def branch1_room_create9(request):
    if 'username' in request.session:

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            'brname': 'BRANCH 9 Room Creation Form',
            'brname': 'BRANCH 9'
        }
        return render(request, 'branches/branch9/rooms/create_room.html', context)
    return render(request, 'index.html')


def branch1_room_create_regi9(request):
    if 'username' in request.session:
        if request.method == 'POST':
            chk_room_no = request.POST.get('roonno')
            chk_room = room_pg1.objects.all().filter(roon_no=chk_room_no).exists()
            if chk_room == True:

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': 'BRANCH 9 Room Creation Form',
                    'br': room_pg1.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 9'
                }
                messages.info(request, 'BRANCH9 roon no already exists')
                return render(request, 'branches/branch9/rooms/view_all_rooms.html', context)
            else:
                room_no = request.POST.get('roonno')
                room_name = request.POST.get('roomname')
                share_type = request.POST.get('sharetype')
                ic = room_pg1()
                ic.roon_no = room_no
                ic.room_name = room_name
                ic.share_type = share_type
                ic.created_by = request.session['username']
                ic.save()

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': 'BRANCH 9 Room Creation Form',
                    'br': room_pg1.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 9'
                }
                messages.info(request, 'BRANCH9 room created sucessfully')
                return render(request, 'branches/branch9/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')








def multiple_branch1_room_create_regi9(request):
    if 'username' in request.session:
        if request.method == 'POST':
            chk_room_no = request.POST.get('roonno')
            chk_room = room_pg1.objects.all().filter(roon_no=chk_room_no).exists()
            if chk_room == True:

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': 'BRANCH 9 Room Creation Form',
                    'br': room_pg1.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 9'
                }
                messages.info(request, 'BRANCH9 roon no already exists')
                return render(request, 'branches/branch9/rooms/view_all_rooms.html', context)
            else:
                rnum = [
                    '2',
                    '101',
                    '102',
                    '103',
                    '104',
                    '105',
                    '106',
                    '107',
                    '108',
                    '109',
                    '110',
                    '111',
                    '112',
                    '201',
                    '202',
                    '203',
                    '204',
                    '205',
                    '206',
                    '207',
                    '208',
                    '209',
                    '210',
                    '211',
                    '212',
                    '301',
                    '302',
                    '303',
                    '304',
                    '305',
                    '306',
                    '307',
                    '308',
                    '309',
                    '310',
                    '311',
                    '312',
                    '401',
                    '402',
                    '403',
                    '404',
                    '405',
                    '406',
                    '407',
                    '408',
                    '409',
                    '410',
                    '411',
                    '412',
                    '501',
                    '502',
                    '503',
                    '504',
                    '505',
                    '506',
                    '507',
                    '508',
                    '509',
                    '510',
                    '511',
                    '512',

                ]

                rnam = [
                    'G2',
                    '101',
                    '102',
                    '103',
                    '104',
                    '105',
                    '106',
                    '107',
                    '108',
                    '109',
                    '110',
                    '111',
                    '112',
                    '201',
                    '202',
                    '203',
                    '204',
                    '205',
                    '206',
                    '207',
                    '208',
                    '209',
                    '210',
                    '211',
                    '212',
                    '301',
                    '302',
                    '303',
                    '304',
                    '305',
                    '306',
                    '307',
                    '308',
                    '309',
                    '310',
                    '311',
                    '312',
                    '401',
                    '402',
                    '403',
                    '404',
                    '405',
                    '406',
                    '407',
                    '408',
                    '409',
                    '410',
                    '411',
                    '412',
                    '501',
                    '502',
                    '503',
                    '504',
                    '505',
                    '506',
                    '507',
                    '508',
                    '509',
                    '510',
                    '511',
                    '512',

                ]

                styp = [
                    '4',
                    '1',
                    '4',
                    '2',
                    '1',
                    '4',
                    '2',
                    '3',
                    '3',
                    '4',
                    '2',
                    '3',
                    '4',
                    '1',
                    '4',
                    '2',
                    '1',
                    '4',
                    '2',
                    '2',
                    '2',
                    '4',
                    '2',
                    '2',
                    '5',
                    '1',
                    '4',
                    '2',
                    '1',
                    '4',
                    '2',
                    '3',
                    '3',
                    '4',
                    '3',
                    '3',
                    '4',
                    '1',
                    '4',
                    '2',
                    '1',
                    '4',
                    '2',
                    '2',
                    '3',
                    '4',
                    '2',
                    '2',
                    '5',
                    '1',
                    '5',
                    '2',
                    '1',
                    '4',
                    '2',
                    '2',
                    '2',
                    '4',
                    '2',
                    '2',
                    '4',

                ]

                print(len(rnum))
                print(len(rnam))
                print(len(styp))

                #room_no = request.POST.get('roonno')
                #room_name = request.POST.get('roomname')
                #share_type = request.POST.get('sharetype')

                for i in range(len(rnum)):
                    ic = room_pg1()
                    ic.roon_no = rnum[i]
                    ic.room_name = rnam[i]
                    ic.share_type = styp[i]
                    ic.created_by = request.session['username']
                    ic.save()

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': 'BRANCH 9 Room Creation Form',
                    'br': room_pg1.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 9'
                }
                messages.info(request, 'BRANCH9 room created sucessfully')
                return render(request, 'branches/branch9/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')








def view_all_room9(request):
    if 'username' in request.session:

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            'brname': 'BRANCH 9 Room Creation Form',
            'br': room_pg1.objects.all().order_by('roon_no').values(),
        }
        return render(request, 'branches/branch9/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')


def delete_room9(request, id):
    if 'username' in request.session:
        dr = room_pg1.objects.get(id=id)
        dr.delete()

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            'brname': 'BRANCH 9 Room Creation Form',
            'br': room_pg1.objects.all().order_by('roon_no')
        }
        return render(request, 'branches/branch9/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')


# ***branch1 rooms end here
# bed creation start here


def pg1_bed_create9(request):
    if 'username' in request.session:

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            'brname': 'BRANCH 9 Room Creation Form',
            'brname': 'BRANCH 9',
            'roomno': room_pg1.objects.all().order_by('roon_no'),
            'roomtype': set(room_pg1.objects.values_list('share_type')),
        }
        return render(request, 'branches/branch9/beds/create_beds.html', context)
    return render(request, 'index.html')


def pg1_bed_create_regi9(request):
    if 'username' in request.session:
        if request.method == 'POST':

            chk_bed_no = request.POST.get('bedno')
            print('chk_bed_no', chk_bed_no)
            chk_room_no = request.POST.get('roomno')
            print('chk_room_no', chk_room_no)

            bd_code = chk_bed_no + chk_room_no
            int_bd_code = int(bd_code)
            chk_bd_code = pg1_new_beds.objects.all().filter(bed_code=int_bd_code).exists()

            if chk_bd_code == True:

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': 'BRANCH THREE Room Creation Form',
                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 9'
                }
                messages.info(request, 'BRANCH9 bed no already exists')
                return render(request, 'branches/branch9/beds/view_all_beds.html', context)
            else:
                room_no = request.POST.get('roomno')
                room_name = request.POST.get('roomname')
                bed_no = request.POST.get('bedno')
                room_type = request.POST.get('roomtype')

                c = 0
                for i in range(int(room_type)):
                    ic = pg1_new_beds()
                    ic.roon_no = room_no
                    ic.room_name = room_name
                    c = c + 1
                    ic.bed_no = c

                    ic.created_by = request.session['username']
                    ic.bed_code = int_bd_code
                    ic.share_type = room_type

                    ic.guest_code = 0

                    ic.jan_rent = 0
                    ic.jan_advance = 0
                    ic.jan_due_amt = 0
                    ic.jan_dis_amt = 0
                    ic.jan_rent_flag = 33

                    ic.feb_rent = 0
                    ic.feb_advance = 0
                    ic.feb_due_amt = 0
                    ic.feb_dis_amt = 0
                    ic.feb_rent_flag = 33

                    ic.march_rent = 0
                    ic.march_advance = 0
                    ic.march_due_amt = 0
                    ic.march_dis_amt = 0
                    ic.march_rent_flag = 33

                    ic.april_rent = 0
                    ic.april_advance = 0
                    ic.april_due_amt = 0
                    ic.april_dis_amt = 0
                    ic.april_rent_flag = 33

                    ic.may_rent = 0
                    ic.may_advance = 0
                    ic.may_due_amt = 0
                    ic.may_dis_amt = 0
                    ic.may_rent_flag = 33

                    ic.june_rent = 0
                    ic.june_advance = 0
                    ic.june_due_amt = 0
                    ic.june_dis_amt = 0
                    ic.june_rent_flag = 33

                    ic.july_rent = 0
                    ic.july_advance = 0
                    ic.july_due_amt = 0
                    ic.july_dis_amt = 0
                    ic.july_rent_flag = 33

                    ic.auguest_rent = 0
                    ic.auguest_advance = 0
                    ic.auguest_due_amt = 0
                    ic.auguest_dis_amt = 0
                    ic.auguest_rent_flag = 33

                    ic.sept_rent = 0
                    ic.sept_advance = 0
                    ic.sept_due_amt = 0
                    ic.sept_dis_amt = 0
                    ic.sept_rent_flag = 33

                    ic.october_rent = 0
                    ic.october_advance = 0
                    ic.october_due_amt = 0
                    ic.october_dis_amt = 0
                    ic.october_rent_flag = 33

                    ic.nov_rent = 0
                    ic.nov_advance = 0
                    ic.nov_due_amt = 0
                    ic.nov_dis_amt = 0
                    ic.nov_rent_flag = 33

                    ic.dec_rent = 0
                    ic.dec_advance = 0
                    ic.dec_due_amt = 0
                    ic.dec_dis_amt = 0
                    ic.dec_rent_flag = 33

                    ic.flag = 1

                    ic.save()

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': 'BRANCH 9 Room Creation Form',
                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 9'
                }
                messages.info(request, 'BRANCH9 room created sucessfully')
                return render(request, 'branches/branch9/beds/view_all_beds.html', context)
    return render(request, 'index.html')


def single_pg1_bed_create_regi9(request):
    if 'username' in request.session:
        if request.method == 'POST':

            chk_bed_no = request.POST.get('bedno')
            print('chk_bed_no', chk_bed_no)
            chk_room_no = request.POST.get('roomno')
            print('chk_room_no', chk_room_no)

            bd_code = chk_bed_no + chk_room_no
            int_bd_code = int(bd_code)
            chk_bd_code = pg1_new_beds.objects.all().filter(bed_code=int_bd_code).exists()

            if chk_bd_code == True:

                us = request.session['username']
                bgs = background_color.objects.all().filter(username=us)
                bg = background_color.objects.all().filter(username=us).exists()
                a = []
                if bg == True:
                    a.append(us)
                else:
                    a.append('f')

                context = {
                    'bg': bgs,
                    'us': us,
                    'th_us': a[0],
                    'name': us,

                    'brname': 'BRANCH THREE Room Creation Form',
                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 9'
                }
                messages.info(request, 'BRANCH9 bed no already exists')
                return render(request, 'branches/branch9/beds/view_all_beds.html', context)
            else:
                room_no = request.POST.get('roomno')
                room_name = request.POST.get('roomname')
                bed_no = request.POST.get('bedno')
                room_type = request.POST.get('roomtype')

                ic = pg1_new_beds()
                ic.roon_no = room_no
                ic.room_name = room_name

                ic.bed_no = bed_no

                ic.created_by = request.session['username']
                ic.bed_code = int_bd_code
                ic.share_type = room_type

                ic.guest_code = 0
                ic.jan_rent = 0
                ic.jan_advance = 0
                ic.jan_due_amt = 0
                ic.jan_rent_flag = 33

                ic.feb_rent = 0
                ic.feb_advance = 0
                ic.feb_due_amt = 0
                ic.feb_rent_flag = 33

                ic.march_rent = 0
                ic.march_advance = 0
                ic.march_due_amt = 0
                ic.march_rent_flag = 33

                ic.april_rent = 0
                ic.april_advance = 0
                ic.april_due_amt = 0
                ic.april_rent_flag = 33

                ic.may_rent = 0
                ic.may_advance = 0
                ic.may_due_amt = 0
                ic.may_rent_flag = 33

                ic.june_rent = 0
                ic.june_advance = 0
                ic.june_due_amt = 0
                ic.june_rent_flag = 33

                ic.july_rent = 0
                ic.july_advance = 0
                ic.july_due_amt = 0
                ic.july_rent_flag = 33

                ic.auguest_rent = 0
                ic.auguest_advance = 0
                ic.auguest_due_amt = 0
                ic.auguest_rent_flag = 33

                ic.sept_rent = 0
                ic.sept_advance = 0
                ic.sept_due_amt = 0
                ic.sept_rent_flag = 33

                ic.october_rent = 0
                ic.october_advance = 0
                ic.october_due_amt = 0
                ic.october_rent_flag = 33

                ic.nov_rent = 0
                ic.nov_advance = 0
                ic.nov_due_amt = 0
                ic.nov_rent_flag = 33

                ic.dec_rent = 0
                ic.dec_advance = 0
                ic.dec_due_amt = 0
                ic.dec_rent_flag = 33

                ic.flag = 1

                ic.save()

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
            a = []
            if bg == True:
                a.append(us)
            else:
                a.append('f')

            context = {
                'bg': bgs,
                'us': us,
                'th_us': a[0],
                'name': us,

                'brname': 'BRANCH 9 Room Creation Form',
                'br': pg1_new_beds.objects.all().order_by('roon_no'),
                'brname': 'BRANCH 9'
            }
            messages.info(request, 'BRANCH9 room created sucessfully')
            return render(request, 'branches/branch9/beds/view_all_beds.html', context)
    return render(request, 'index.html')














def multiple_single_pg1_bed_create_regi9(request):
    if 'username' in request.session:
        if request.method == 'POST':

            a = [
                '2',
                '2',
                '2',
                '2',
                '101',
                '102',
                '102',
                '102',
                '102',
                '103',
                '103',
                '104',
                '105',
                '105',
                '105',
                '105',
                '106',
                '106',
                '107',
                '107',
                '107',
                '108',
                '108',
                '108',
                '109',
                '109',
                '109',
                '109',
                '110',
                '110',
                '111',
                '111',
                '111',
                '112',
                '112',
                '112',
                '112',
                '201',
                '202',
                '202',
                '202',
                '202',
                '203',
                '203',
                '204',
                '205',
                '205',
                '205',
                '205',
                '206',
                '206',
                '207',
                '207',
                '208',
                '208',
                '209',
                '209',
                '209',
                '209',
                '210',
                '210',
                '211',
                '211',
                '212',
                '212',
                '212',
                '212',
                '212',
                '301',
                '302',
                '302',
                '302',
                '302',
                '303',
                '303',
                '304',
                '305',
                '305',
                '305',
                '305',
                '306',
                '306',
                '307',
                '307',
                '307',
                '308',
                '308',
                '308',
                '309',
                '309',
                '309',
                '309',
                '310',
                '310',
                '310',
                '311',
                '311',
                '311',
                '312',
                '312',
                '312',
                '312',
                '401',
                '402',
                '402',
                '402',
                '402',
                '403',
                '403',
                '404',
                '405',
                '405',
                '405',
                '405',
                '406',
                '406',
                '407',
                '407',
                '408',
                '408',
                '408',
                '409',
                '409',
                '409',
                '409',
                '410',
                '410',
                '411',
                '411',
                '412',
                '412',
                '412',
                '412',
                '412',
                '501',
                '502',
                '502',
                '502',
                '502',
                '502',
                '503',
                '503',
                '504',
                '505',
                '505',
                '505',
                '505',
                '506',
                '506',
                '507',
                '507',
                '508',
                '508',
                '509',
                '509',
                '509',
                '509',
                '510',
                '510',
                '511',
                '511',
                '512',
                '512',
                '512',
                '512',
            ]

            b = [

                'G2',
                'G2',
                'G2',
                'G2',
                '101',
                '102',
                '102',
                '102',
                '102',
                '103',
                '103',
                '104',
                '105',
                '105',
                '105',
                '105',
                '106',
                '106',
                '107',
                '107',
                '107',
                '108',
                '108',
                '108',
                '109',
                '109',
                '109',
                '109',
                '110',
                '110',
                '111',
                '111',
                '111',
                '112',
                '112',
                '112',
                '112',
                '201',
                '202',
                '202',
                '202',
                '202',
                '203',
                '203',
                '204',
                '205',
                '205',
                '205',
                '205',
                '206',
                '206',
                '207',
                '207',
                '208',
                '208',
                '209',
                '209',
                '209',
                '209',
                '210',
                '210',
                '211',
                '211',
                '212',
                '212',
                '212',
                '212',
                '212',
                '301',
                '302',
                '302',
                '302',
                '302',
                '303',
                '303',
                '304',
                '305',
                '305',
                '305',
                '305',
                '306',
                '306',
                '307',
                '307',
                '307',
                '308',
                '308',
                '308',
                '309',
                '309',
                '309',
                '309',
                '310',
                '310',
                '310',
                '311',
                '311',
                '311',
                '312',
                '312',
                '312',
                '312',
                '401',
                '402',
                '402',
                '402',
                '402',
                '403',
                '403',
                '404',
                '405',
                '405',
                '405',
                '405',
                '406',
                '406',
                '407',
                '407',
                '408',
                '408',
                '408',
                '409',
                '409',
                '409',
                '409',
                '410',
                '410',
                '411',
                '411',
                '412',
                '412',
                '412',
                '412',
                '412',
                '501',
                '502',
                '502',
                '502',
                '502',
                '502',
                '503',
                '503',
                '504',
                '505',
                '505',
                '505',
                '505',
                '506',
                '506',
                '507',
                '507',
                '508',
                '508',
                '509',
                '509',
                '509',
                '509',
                '510',
                '510',
                '511',
                '511',
                '512',
                '512',
                '512',
                '512',

            ]

            c = [

                '4',
                '4',
                '4',
                '4',
                '1',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '1',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '3',
                '3',
                '3',
                '3',
                '3',
                '3',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '3',
                '3',
                '3',
                '4',
                '4',
                '4',
                '4',
                '1',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '1',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '2',
                '2',
                '2',
                '2',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '3',
                '3',
                '5',
                '5',
                '5',
                '5',
                '5',
                '1',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '1',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '3',
                '3',
                '3',
                '3',
                '3',
                '3',
                '4',
                '4',
                '4',
                '4',
                '3',
                '3',
                '3',
                '3',
                '3',
                '3',
                '4',
                '4',
                '4',
                '4',
                '1',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '1',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '2',
                '2',
                '3',
                '3',
                '3',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '2',
                '2',
                '4',
                '4',
                '4',
                '4',
                '5',
                '1',
                '4',
                '4',
                '4',
                '4',
                '5',
                '2',
                '2',
                '1',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '2',
                '2',
                '2',
                '2',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '2',
                '2',
                '4',
                '4',
                '4',
                '4',

            ]

            d = [

                '1',
                '2',
                '3',
                '4',
                '1',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '2',
                '3',
                '1',
                '2',
                '3',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '2',
                '3',
                '1',
                '2',
                '3',
                '4',
                '1',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '2',
                '1',
                '2',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '3',
                '1',
                '2',
                '3',
                '4',
                '5',
                '1',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '2',
                '3',
                '1',
                '2',
                '3',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '1',
                '2',
                '3',
                '1',
                '2',
                '3',
                '4',
                '1',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '2',
                '1',
                '2',
                '3',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '2',
                '1',
                '2',
                '3',
                '4',
                '5',
                '1',
                '1',
                '2',
                '3',
                '4',
                '5',
                '1',
                '2',
                '1',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '2',
                '1',
                '2',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '2',
                '1',
                '2',
                '3',
                '4',

            ]

            print(len(a))
            print(len(b))
            print(len(c))
            print(len(d))

            for i in range(len(a)):

                #chk_bed_no = request.POST.get('bedno')
                chk_bed_no = d[i]
                print('chk_bed_no', chk_bed_no)
                #chk_room_no = request.POST.get('roomno')
                chk_room_no = a[i]
                print('chk_room_no', chk_room_no)

                bd_code = chk_bed_no + chk_room_no
                int_bd_code = int(bd_code)
                chk_bd_code = pg1_new_beds.objects.all().filter(bed_code=int_bd_code).exists()

                if chk_bd_code == True:

                    us = request.session['username']
                    bgs = background_color.objects.all().filter(username=us)
                    bg = background_color.objects.all().filter(username=us).exists()
                    a = []
                    if bg == True:
                        a.append(us)
                    else:
                        a.append('f')

                    context = {
                        'bg': bgs,
                        'us': us,
                        'th_us': a[0],
                        'name': us,

                        'brname': 'BRANCH THREE Room Creation Form',
                        'br': pg1_new_beds.objects.all().order_by('roon_no'),
                        'brname': 'BRANCH 9'
                    }
                    messages.info(request, 'BRANCH9 bed no already exists')
                    return render(request, 'branches/branch9/beds/view_all_beds.html', context)
                else:
                    room_no = a[i]
                    room_name = b[i]
                    bed_no = d[i]
                    room_type = c[i]

                    ic = pg1_new_beds()
                    ic.roon_no = room_no
                    ic.room_name = room_name

                    ic.bed_no = bed_no

                    ic.created_by = request.session['username']
                    ic.bed_code = int_bd_code
                    ic.share_type = room_type

                    ic.guest_code = 0
                    ic.jan_rent = 0
                    ic.jan_advance = 0
                    ic.jan_due_amt = 0
                    ic.jan_rent_flag = 33

                    ic.feb_rent = 0
                    ic.feb_advance = 0
                    ic.feb_due_amt = 0
                    ic.feb_rent_flag = 33

                    ic.march_rent = 0
                    ic.march_advance = 0
                    ic.march_due_amt = 0
                    ic.march_rent_flag = 33

                    ic.april_rent = 0
                    ic.april_advance = 0
                    ic.april_due_amt = 0
                    ic.april_rent_flag = 33

                    ic.may_rent = 0
                    ic.may_advance = 0
                    ic.may_due_amt = 0
                    ic.may_rent_flag = 33

                    ic.june_rent = 0
                    ic.june_advance = 0
                    ic.june_due_amt = 0
                    ic.june_rent_flag = 33

                    ic.july_rent = 0
                    ic.july_advance = 0
                    ic.july_due_amt = 0
                    ic.july_rent_flag = 33

                    ic.auguest_rent = 0
                    ic.auguest_advance = 0
                    ic.auguest_due_amt = 0
                    ic.auguest_rent_flag = 33

                    ic.sept_rent = 0
                    ic.sept_advance = 0
                    ic.sept_due_amt = 0
                    ic.sept_rent_flag = 33

                    ic.october_rent = 0
                    ic.october_advance = 0
                    ic.october_due_amt = 0
                    ic.october_rent_flag = 33

                    ic.nov_rent = 0
                    ic.nov_advance = 0
                    ic.nov_due_amt = 0
                    ic.nov_rent_flag = 33

                    ic.dec_rent = 0
                    ic.dec_advance = 0
                    ic.dec_due_amt = 0
                    ic.dec_rent_flag = 33

                    ic.flag = 1

                    ic.save()

            us = request.session['username']
            bgs = background_color.objects.all().filter(username=us)
            bg = background_color.objects.all().filter(username=us).exists()
            a = []
            if bg == True:
                a.append(us)
            else:
                a.append('f')

            context = {
                'bg': bgs,
                'us': us,
                'th_us': a[0],
                'name': us,

                'brname': 'BRANCH 9 Room Creation Form',
                'br': pg1_new_beds.objects.all().order_by('roon_no'),
                'brname': 'BRANCH 9'
            }
            messages.info(request, 'BRANCH9 room created sucessfully')
            return render(request, 'branches/branch9/beds/view_all_beds.html', context)
    return render(request, 'index.html')












def pg1_view_all_beds9(request):
    if 'username' in request.session:

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            'brname': 'BRANCH 9 Room',
            'br': pg1_new_beds.objects.all().order_by('roon_no')
        }
        return render(request, 'branches/branch9/beds/view_all_beds.html', context)
    return render(request, 'index.html')


def delete_bed9(request, id):
    if 'username' in request.session:
        dr = pg1_new_beds.objects.get(id=id)
        dr.delete()

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            'brname': 'BRANCH 9 Room',
            'br': pg1_new_beds.objects.all().order_by('roon_no')
        }
        return render(request, 'branches/branch9/beds/view_all_beds.html', context)
    return render(request, 'index.html')


def update_bed_basic_details9(request, id):
    if 'username' in request.session:
        if request.method == 'POST':
            room_type = request.POST.get('roomtype')
            ic = pg1_new_beds.objects.get(id=id)
            ic.created_by = request.session['username']
            ic.share_type = room_type
            ic.save()

            nuph = pg1_new_beds.objects.all().filter(id=id)
            np = []
            for i in nuph:
                np.append(i.self_mob)

            nc = pg1_new_guest.objects.get(self_mob=np[0])
            nc.created_by = request.session['username']
            nc.share_type = room_type
            nc.save()

            return pg1_view_all_beds9(request)

        us = request.session['username']
        bgs = background_color.objects.all().filter(username=us)
        bg = background_color.objects.all().filter(username=us).exists()
        a = []
        if bg == True:
            a.append(us)
        else:
            a.append('f')

        context = {
            'bg': bgs,
            'us': us,
            'th_us': a[0],
            'name': us,


            'brname': 'BRANCH 9 Room Creation Form',
            'br': pg1_new_beds.objects.all().order_by('roon_no'),
            'brname': 'BRANCH 9',
            'sd': pg1_new_beds.objects.get(id=id),
            'roomno': room_pg1.objects.all().values('share_type').distinct(),
        }
        messages.info(request, 'BRANCH9 room created sucessfully')
        return render(request, 'branches/branch9/beds/update_bed.html', context)
    return render(request, 'index.html')

# bed creation end here

