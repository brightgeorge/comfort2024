#admin_branch_ob_ch1616
import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

from branch16app.models import *
import datetime

#***branch1 rooms start here

def branch1_room_create_ob_ch1616(request):
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

        }
        return render(request,'branches/branch16/rooms/create_room.html',context)
    return render(request, 'index.html')

def branch1_room_create_regi_ob_ch1616(request):
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

                    'br': room_pg1.objects.all().order_by('roon_no'),

                }
                messages.info(request, 'BRANCH no already exists')
                return render(request, 'branches/branch16/rooms/view_all_rooms.html', context)
            else:
                room_no = request.POST.get('roonno')
                room_name = request.POST.get('roomname')
                share_type = request.POST.get('sharetype')
                ic=room_pg1()
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

                    'br' : room_pg1.objects.all().order_by('roon_no'),
                }
                messages.info(request, 'BRANCH room created sucessfully')
                return render(request,'branches/branch16/rooms/view_all_rooms.html',context)
    return render(request, 'index.html')












def multiple_branch1_room_create_regi16(request):
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

                    'brname': 'BRANCH 16 Room Creation Form',
                    'br': room_pg1.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 16'
                }
                messages.info(request, 'BRANCH9 roon no already exists')
                return render(request, 'branches/branch16/rooms/view_all_rooms.html', context)
            else:
                rnum = [

                    '161',
                    '162',
                    '163',
                    '164',
                    '165',
                    '166',
                    '167',
                    '168',
                    '169',
                    '116',
                    '111',
                    '112',
                    '113',
                    '201',
                    '202',
                    '203',
                    '204',
                    '205',
                    '206',
                    '207',
                    '208',
                    '209',
                    '216',
                    '211',
                    '212',
                    '213',
                    '301',
                    '302',
                    '303',
                    '304',
                    '305',
                    '306',
                    '307',
                    '308',
                    '309',
                    '316',
                    '311',
                    '312',
                    '313',
                    '401',
                    '402',
                    '403',
                    '404',
                    '405',
                    '406',
                    '407',
                    '408',
                    '409',
                    '416',
                    '411',
                    '412',
                    '413',
                    '501',
                    '502',
                    '503',
                    '504',
                    '505',
                    '506',
                    '507',
                    '508',
                    '509',
                    '516',
                    '511',
                    '512',
                    '513',
                    '601',
                    '602',
                    '603',
                    '604',
                    '605',
                    '606',
                    '607',
                    '608',
                    '609',
                    '616',

                ]

                rnam = [

                    '161',
                    '162',
                    '163',
                    '164',
                    '165',
                    '166',
                    '167',
                    '168',
                    '169',
                    '116',
                    '111',
                    '112',
                    '113',
                    '201',
                    '202',
                    '203',
                    '204',
                    '205',
                    '206',
                    '207',
                    '208',
                    '209',
                    '216',
                    '211',
                    '212',
                    '213',
                    '301',
                    '302',
                    '303',
                    '304',
                    '305',
                    '306',
                    '307',
                    '308',
                    '309',
                    '316',
                    '311',
                    '312',
                    '313',
                    '401',
                    '402',
                    '403',
                    '404',
                    '405',
                    '406',
                    '407',
                    '408',
                    '409',
                    '416',
                    '411',
                    '412',
                    '413',
                    '501',
                    '502',
                    '503',
                    '504',
                    '505',
                    '506',
                    '507',
                    '508',
                    '509',
                    '516',
                    '511',
                    '512',
                    '513',
                    '601',
                    '602',
                    '603',
                    '604',
                    '605',
                    '606',
                    '607',
                    '608',
                    '609',
                    '616',

                ]

                styp = [

                    '4',
                    '3',
                    '4',
                    '3',
                    '4',
                    '4',
                    '1',
                    '2',
                    '1',
                    '3',
                    '2',
                    '2',
                    '2',
                    '4',
                    '3',
                    '4',
                    '3',
                    '4',
                    '4',
                    '2',
                    '2',
                    '1',
                    '3',
                    '2',
                    '2',
                    '2',
                    '4',
                    '3',
                    '4',
                    '3',
                    '4',
                    '4',
                    '1',
                    '2',
                    '1',
                    '3',
                    '2',
                    '2',
                    '2',
                    '4',
                    '3',
                    '4',
                    '4',
                    '4',
                    '5',
                    '1',
                    '2',
                    '1',
                    '3',
                    '2',
                    '2',
                    '2',
                    '4',
                    '4',
                    '4',
                    '3',
                    '4',
                    '4',
                    '1',
                    '2',
                    '1',
                    '3',
                    '2',
                    '2',
                    '2',
                    '3',
                    '4',
                    '3',
                    '4',
                    '4',
                    '1',
                    '2',
                    '3',
                    '2',
                    '2',

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

                    'brname': 'BRANCH 16 Room Creation Form',
                    'br': room_pg1.objects.all().order_by('roon_no'),
                    'brname': 'BRANCH 16'
                }
                messages.info(request, 'BRANCH16 room created sucessfully')
                return render(request, 'branches/branch16/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')













def view_all_room_ob_ch1616(request):
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

            'br': room_pg1.objects.all().order_by('roon_no').values(),
        }
        return render(request,'branches/branch16/rooms/view_all_rooms.html',context)
    return render(request,'index.html')

def delete_room_ob_ch1616(request,id):
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

            'br': room_pg1.objects.all().order_by('roon_no')
        }
        messages.info(request, 'BRANCH Room Updated sucessfully')
        return render(request, 'branches/branch16/rooms/view_all_rooms.html', context)
    return render(request, 'index.html')

#***branch1 rooms end here
#bed creation start here


def pg1_bed_create_ob_ch1616(request):
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

            'roomno' : room_pg1.objects.all(),
            'roomtype': set(room_pg1.objects.values_list('share_type')),
        }
        return render(request,'branches/branch16/beds/create_beds.html',context)
    return render(request, 'index.html')

def pg1_bed_create_regi_ob_ch1616(request):
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

                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                }
                messages.info(request, ' Bed no Already Exists')
                return render(request, 'branches/branch16/beds/view_all_beds.html', context)
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

                    'brname': ' Room Creation Form',
                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                }
                messages.info(request, ' Room Created Sucessfully')
                return render(request, 'branches/branch16/beds/view_all_beds.html', context)
    return render(request, 'index.html')




def single_pg1_bed_create_regi_ob_ch1616(request):
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

                    'brname': ' Room Creation Form',
                    'br': pg1_new_beds.objects.all().order_by('roon_no'),
                }
                messages.info(request, ' Bed no Already Exists')
                return render(request, 'branches/branch16/beds/view_all_beds.html', context)
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

                'brname': ' Room Creation Form',
                'br': pg1_new_beds.objects.all().order_by('roon_no'),
            }
            messages.info(request, ' Room Created Sucessfully')
            return render(request, 'branches/branch16/beds/view_all_beds.html', context)
    return render(request, 'index.html')











def multiple_single_pg1_bed_create_regi16(request):
    if 'username' in request.session:
        if request.method == 'POST':

            a = [

                '161',
                '161',
                '161',
                '161',
                '162',
                '162',
                '162',
                '163',
                '163',
                '163',
                '163',
                '164',
                '164',
                '164',
                '165',
                '165',
                '165',
                '165',
                '166',
                '166',
                '166',
                '166',
                '167',
                '168',
                '168',
                '169',
                '116',
                '116',
                '116',
                '111',
                '111',
                '112',
                '112',
                '113',
                '113',
                '201',
                '201',
                '201',
                '201',
                '202',
                '202',
                '202',
                '203',
                '203',
                '203',
                '203',
                '204',
                '204',
                '204',
                '205',
                '205',
                '205',
                '205',
                '206',
                '206',
                '206',
                '206',
                '207',
                '207',
                '208',
                '208',
                '209',
                '216',
                '216',
                '216',
                '211',
                '211',
                '212',
                '212',
                '213',
                '213',
                '301',
                '301',
                '301',
                '301',
                '302',
                '302',
                '302',
                '303',
                '303',
                '303',
                '303',
                '304',
                '304',
                '304',
                '305',
                '305',
                '305',
                '305',
                '306',
                '306',
                '306',
                '306',
                '307',
                '308',
                '308',
                '309',
                '316',
                '316',
                '316',
                '311',
                '311',
                '312',
                '312',
                '313',
                '313',
                '401',
                '401',
                '401',
                '401',
                '402',
                '402',
                '402',
                '403',
                '403',
                '403',
                '403',
                '404',
                '404',
                '404',
                '404',
                '405',
                '405',
                '405',
                '405',
                '406',
                '406',
                '406',
                '406',
                '406',
                '407',
                '408',
                '408',
                '409',
                '416',
                '416',
                '416',
                '411',
                '411',
                '412',
                '412',
                '413',
                '413',
                '501',
                '501',
                '501',
                '501',
                '502',
                '502',
                '502',
                '502',
                '503',
                '503',
                '503',
                '503',
                '504',
                '504',
                '504',
                '505',
                '505',
                '505',
                '505',
                '506',
                '506',
                '506',
                '506',
                '507',
                '508',
                '508',
                '509',
                '516',
                '516',
                '516',
                '511',
                '511',
                '512',
                '512',
                '513',
                '513',
                '601',
                '601',
                '601',
                '602',
                '602',
                '602',
                '602',
                '603',
                '603',
                '603',
                '604',
                '604',
                '604',
                '604',
                '605',
                '605',
                '605',
                '605',
                '606',
                '607',
                '607',
                '608',
                '608',
                '608',
                '609',
                '609',
                '616',
                '616',

            ]

            b = [

                '161',
                '161',
                '161',
                '161',
                '162',
                '162',
                '162',
                '163',
                '163',
                '163',
                '163',
                '164',
                '164',
                '164',
                '165',
                '165',
                '165',
                '165',
                '166',
                '166',
                '166',
                '166',
                '167',
                '168',
                '168',
                '169',
                '116',
                '116',
                '116',
                '111',
                '111',
                '112',
                '112',
                '113',
                '113',
                '201',
                '201',
                '201',
                '201',
                '202',
                '202',
                '202',
                '203',
                '203',
                '203',
                '203',
                '204',
                '204',
                '204',
                '205',
                '205',
                '205',
                '205',
                '206',
                '206',
                '206',
                '206',
                '207',
                '207',
                '208',
                '208',
                '209',
                '216',
                '216',
                '216',
                '211',
                '211',
                '212',
                '212',
                '213',
                '213',
                '301',
                '301',
                '301',
                '301',
                '302',
                '302',
                '302',
                '303',
                '303',
                '303',
                '303',
                '304',
                '304',
                '304',
                '305',
                '305',
                '305',
                '305',
                '306',
                '306',
                '306',
                '306',
                '307',
                '308',
                '308',
                '309',
                '316',
                '316',
                '316',
                '311',
                '311',
                '312',
                '312',
                '313',
                '313',
                '401',
                '401',
                '401',
                '401',
                '402',
                '402',
                '402',
                '403',
                '403',
                '403',
                '403',
                '404',
                '404',
                '404',
                '404',
                '405',
                '405',
                '405',
                '405',
                '406',
                '406',
                '406',
                '406',
                '406',
                '407',
                '408',
                '408',
                '409',
                '416',
                '416',
                '416',
                '411',
                '411',
                '412',
                '412',
                '413',
                '413',
                '501',
                '501',
                '501',
                '501',
                '502',
                '502',
                '502',
                '502',
                '503',
                '503',
                '503',
                '503',
                '504',
                '504',
                '504',
                '505',
                '505',
                '505',
                '505',
                '506',
                '506',
                '506',
                '506',
                '507',
                '508',
                '508',
                '509',
                '516',
                '516',
                '516',
                '511',
                '511',
                '512',
                '512',
                '513',
                '513',
                '601',
                '601',
                '601',
                '602',
                '602',
                '602',
                '602',
                '603',
                '603',
                '603',
                '604',
                '604',
                '604',
                '604',
                '605',
                '605',
                '605',
                '605',
                '606',
                '607',
                '607',
                '608',
                '608',
                '608',
                '609',
                '609',
                '616',
                '616',

            ]

            c = [

                '4',
                '4',
                '4',
                '4',
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
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '1',
                '2',
                '2',
                '1',
                '3',
                '3',
                '3',
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
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '2',
                '2',
                '2',
                '2',
                '1',
                '3',
                '3',
                '3',
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
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '1',
                '2',
                '2',
                '1',
                '3',
                '3',
                '3',
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
                '4',
                '4',
                '4',
                '4',
                '4',
                '5',
                '5',
                '5',
                '5',
                '5',
                '1',
                '2',
                '2',
                '1',
                '3',
                '3',
                '3',
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
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '3',
                '3',
                '3',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '1',
                '2',
                '2',
                '1',
                '3',
                '3',
                '3',
                '2',
                '2',
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
                '3',
                '3',
                '3',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '4',
                '1',
                '2',
                '2',
                '3',
                '3',
                '3',
                '2',
                '2',
                '2',
                '2',

            ]

            d = [

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
                '4',
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
                '4',
                '1',
                '1',
                '2',
                '1',
                '1',
                '2',
                '3',
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
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '1',
                '2',
                '1',
                '1',
                '2',
                '3',
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
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '1',
                '2',
                '1',
                '1',
                '2',
                '3',
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
                '3',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '5',
                '1',
                '1',
                '2',
                '1',
                '1',
                '2',
                '3',
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
                '3',
                '4',
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
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '1',
                '2',
                '1',
                '1',
                '2',
                '3',
                '1',
                '2',
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
                '3',
                '1',
                '2',
                '3',
                '4',
                '1',
                '2',
                '3',
                '4',
                '1',
                '1',
                '2',
                '1',
                '2',
                '3',
                '1',
                '2',
                '1',
                '2',

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
                        'brname': 'BRANCH 16'
                    }
                    messages.info(request, 'BRANCH16 bed no already exists')
                    return render(request, 'branches/branch16/beds/view_all_beds.html', context)
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

                'brname': 'BRANCH 16 Room Creation Form',
                'br': pg1_new_beds.objects.all().order_by('roon_no'),
                'brname': 'BRANCH 16'
            }
            messages.info(request, 'BRANCH16 room created sucessfully')
            return render(request, 'branches/branch16/beds/view_all_beds.html', context)
    return render(request, 'index.html')
















def pg1_view_all_beds_ob_ch1616(request):
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

            'br': pg1_new_beds.objects.all().order_by('roon_no')
        }
        return render(request,'branches/branch16/beds/view_all_beds.html',context)
    return render(request,'index.html')

def delete_bed_ob_ch1616(request,id):
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

            'br': pg1_new_beds.objects.all().order_by('roon_no')
        }
        return render(request, 'branches/branch16/beds/view_all_beds.html', context)
    return render(request, 'index.html')

def update_bed_basic_details_ob_ch1616(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            room_type = request.POST.get('roomtype')
            ic = pg1_new_beds.objects.get(id=id)
            ic.created_by = request.session['username']
            ic.share_type = room_type
            ic.save()

            nuph=pg1_new_beds.objects.all().filter(id=id)
            np=[]
            for i in nuph:
                np.append(i.self_mob)

            nc=pg1_new_guest.objects.get(self_mob=np[0])
            nc.created_by = request.session['username']
            nc.share_type = room_type
            nc.save()

            return pg1_view_all_beds_ob_ch1616(request)

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

            'br': pg1_new_beds.objects.all().order_by('roon_no'),
            'sd': pg1_new_beds.objects.get(id=id),
            'roomno': room_pg1.objects.all().values('share_type').distinct(),
        }
        messages.info(request, ' Room Created Sucessfully')
        return render(request, 'branches/branch16/beds/update_bed.html', context)
    return render(request,'index.html')


#bed creation end here
import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *
from branch16app.models import *
import datetime

database_name = 'cpg'
database_password = '#123.com#'
database_user = 'root'
database_host = 'localhost'

import pymysql as py

def choose_user_ob_ch16(request):
    if 'username' in request.session:
        from datetime import datetime

        currentMonth = datetime.now().month
        a = currentMonth - 1
        l = ['jan_rent_flag', 'feb_rent_flag', 'march_rent_flag', 'april_rent_flag', 'may_rent_flag', 'june_rent_flag',
             'july_rent_flag',
             'auguest_rent_flag', 'sept_rent_flag', 'october_rent_flag', 'nov_rent_flag', 'dec_rent_flag']
        ll = ['jan_due_amt', 'feb_due_amt', 'march_due_amt', 'april_due_amt', 'may_due_amt', 'june_due_amt',
              'july_due_amt',
              'auguest_due_amt', 'sept_due_amt', 'october_due_amt', 'nov_due_amt', 'dec_due_amt']

        d={'1':'get_total_due_feb','2':'get_total_due_march',
           '3':'get_total_due_april','4':'get_total_due_may',
           '_ob_ch16':'get_total_due_june','6':'get_total_due_july',
           '7':'get_total_due_auguest'
           }

        color=d['7']
        print('color',color)

        res = []
        res.append(l[a])
        #res.append(ll[a])

        print(res)

        from datetime import datetime
        cmm = datetime.now().month
        cm = cmm - 1
        #gtc = a[cm]

        rn = request.POST.get('rno')

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

            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2),
            'roomno':rn,
            'room': room_pg1.objects.all().order_by('roon_no').values(),
            'res' : res,
            'a' : 1,
            '{% if i.get_total_due_auguest >0 %}' : '{% if i.get_total_due_auguest >0 %}',
        }
        return render(request, 'branches/branch16/payments/choose_user.html',context)
def payment_user_details_ob_ch16(request, id):
    if 'username' in request.session:

        r=pg1_new_guest.objects.all().filter(id=id,flag=2)
        rl=[]
        for i in r:
            rl.append(i.roon_no)
            break

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

            'pd': pg1_new_guest.objects.all().filter(id=id,flag=2),
            'rll' : rl,
        }
        return render(request, 'branches/branch16/payments/payment_user_details.html', context)



def close_choose_user_ob_ch16(request,id):
    if 'username' in request.session:
        from datetime import datetime

        currentMonth = datetime.now().month
        a = currentMonth - 1
        l = ['jan_rent_flag', 'feb_rent_flag', 'march_rent_flag', 'april_rent_flag', 'may_rent_flag', 'june_rent_flag',
             'july_rent_flag',
             'auguest_rent_flag', 'sept_rent_flag', 'october_rent_flag', 'nov_rent_flag', 'dec_rent_flag']
        ll = ['jan_due_amt', 'feb_due_amt', 'march_due_amt', 'april_due_amt', 'may_due_amt', 'june_due_amt',
              'july_due_amt',
              'auguest_due_amt', 'sept_due_amt', 'october_due_amt', 'nov_due_amt', 'dec_due_amt']

        d={'1':'get_total_due_feb','2':'get_total_due_march',
           '3':'get_total_due_april','4':'get_total_due_may',
           '_ob_ch16':'get_total_due_june','6':'get_total_due_july',
           '7':'get_total_due_auguest'
           }

        color=d['7']
        print('color',color)

        res = []
        res.append(l[a])
        #res.append(ll[a])

        print(res)

        from datetime import datetime
        cmm = datetime.now().month
        cm = cmm - 1
        #gtc = a[cm]

        #rn = request.POST.get('rno')
        rn=id

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

            'pd':pg1_new_guest.objects.all().filter(roon_no=rn,flag=2),
            'roomno':rn,
            'room': room_pg1.objects.all().order_by('roon_no').values(),
            'res' : res,
            'a' : 1,
            '{% if i.get_total_due_auguest >0 %}' : '{% if i.get_total_due_auguest >0 %}',
        }
        return render(request, 'branches/branch16/payments/choose_user.html',context)




#jan make payments start here

def monthly_jan_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt = request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.jan_rent = amt
            jp.remark = remark
            jp.jan_due_amt = due_amt
            jp.jan_dis_amt = dis_amt
            jp.jan_rent_rec_date = date
            jp.jan_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.jan_rent = amt
            jp.remark = remark
            jp.jan_due_amt = due_amt
            jp.jan_dis_amt = dis_amt
            jp.jan_rent_rec_date = date
            jp.jan_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            ll = []
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s = ''.join(l)
            gc = ''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2, jan_rent_flag__gt=99, guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll': rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html', context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.jan_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch16/payments/payment_details_of_months/jan/monthly_jan_make_payments.html',context)


#jan make payments start here

#feb make payments start here

def monthly_feb_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.feb_rent = amt
            jp.remark = remark
            jp.feb_due_amt = due_amt
            jp.feb_dis_amt = dis_amt
            jp.feb_rent_rec_date = date
            jp.feb_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.feb_rent = amt
            jp.remark = remark
            jp.feb_due_amt = due_amt
            jp.feb_dis_amt = dis_amt
            jp.feb_rent_rec_date = date
            jp.feb_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,feb_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.feb_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch16/payments/payment_details_of_months/feb/monthly_feb_make_payments.html', context)

#feb make payments start here

#march make payments start here

def monthly_march_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.march_rent = amt
            jp.remark = remark
            jp.march_due_amt = due_amt
            jp.march_dis_amt = dis_amt
            jp.march_rent_rec_date = date
            jp.march_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.march_rent = amt
            jp.remark = remark
            jp.march_due_amt = due_amt
            jp.march_dis_amt = dis_amt
            jp.march_rent_rec_date = date
            jp.march_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,march_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.march_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch16/payments/payment_details_of_months/march/monthly_march_make_payments.html', context)

#march make payments start here


#april make payments start here

def monthly_april_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.april_rent = amt
            jp.remark = remark
            jp.april_due_amt = due_amt
            jp.april_dis_amt = dis_amt
            jp.april_rent_rec_date = date
            jp.april_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.april_rent = amt
            jp.remark = remark
            jp.april_due_amt = due_amt
            jp.april_dis_amt = dis_amt
            jp.april_rent_rec_date = date
            jp.april_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,april_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.april_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd': pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch16/payments/payment_details_of_months/april/monthly_april_make_payments.html', context)

#april make payments start here


#may make payments start here

def monthly_may_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.may_rent = amt
            jp.remark = remark
            jp.may_due_amt = due_amt
            jp.may_dis_amt = dis_amt
            jp.may_rent_rec_date = date
            jp.may_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll',l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.may_rent = amt
            jp.remark = remark
            jp.may_due_amt = due_amt
            jp.may_dis_amt = dis_amt
            jp.may_rent_rec_date = date
            jp.may_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,may_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.may_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch16/payments/payment_details_of_months/may/monthly_may_make_payments.html', context)

#may make payments start here

#june make payments start here

def monthly_june_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.june_rent = amt
            jp.remark = remark
            jp.june_due_amt = due_amt
            jp.june_dis_amt = dis_amt
            jp.june_rent_rec_date = date
            jp.june_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.june_rent = amt
            jp.remark = remark
            jp.june_due_amt = due_amt
            jp.june_dis_amt = dis_amt
            jp.june_rent_rec_date = date
            jp.june_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,june_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2,guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.june_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request, 'branches/branch16/payments/payment_details_of_months/june/monthly_june_make_payments.html', context)


#june make payments start here



#july make payments start here

def monthly_july_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.july_rent = amt
            jp.remark = remark
            jp.july_due_amt = due_amt
            jp.july_dis_amt = dis_amt
            jp.july_rent_rec_date = date
            jp.july_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.july_rent = amt
            jp.remark = remark
            jp.july_due_amt = due_amt
            jp.july_dis_amt = dis_amt
            jp.july_rent_rec_date = date
            jp.july_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,july_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html', context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.july_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch16/payments/payment_details_of_months/july/monthly_july_make_payments.html', context)

#july make payments end here

#agu make payments start here

def monthly_aug_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.auguest_rent = amt
            jp.remark = remark
            jp.auguest_due_amt = due_amt
            jp.auguest_dis_amt = dis_amt
            jp.auguest_rent_rec_date = date
            jp.auguest_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.auguest_rent = amt
            jp.remark = remark
            jp.auguest_due_amt = due_amt
            jp.auguest_dis_amt = dis_amt
            jp.auguest_rent_rec_date = date
            jp.auguest_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,auguest_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.auguest_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch16/payments/payment_details_of_months/aug/monthly_aug_make_payments.html', context)

#aug make payments start here

#sept make payments start here

def monthly_sept_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.sept_rent = amt
            jp.remark = remark
            jp.sept_due_amt = due_amt
            jp.sept_dis_amt = dis_amt
            jp.sept_rent_rec_date = date
            jp.sept_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.sept_rent = amt
            jp.remark = remark
            jp.sept_due_amt = due_amt
            jp.sept_dis_amt = dis_amt
            jp.sept_rent_rec_date = date
            jp.sept_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,sept_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.sept_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=1),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch16/payments/payment_details_of_months/sept/monthly_sept_make_payments.html', context)

#sept make payments start here

#oct make payments start here

def monthly_oct_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            print('amt',amt)
            print('remark',remark)

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.october_rent = amt
            jp.remark = remark
            jp.october_due_amt = due_amt
            jp.october_dis_amt = dis_amt
            jp.october_rent_rec_date = date
            jp.october_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.october_rent = amt
            jp.remark = remark
            jp.october_due_amt = due_amt
            jp.october_dis_amt = dis_amt
            jp.october_rent_rec_date = date
            jp.october_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,october_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.october_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch16/payments/payment_details_of_months/oct/monthly_oct_make_payments.html', context)

#oct make payments start here

#nov make payments start here

def monthly_nov_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.nov_rent = amt
            jp.remark = remark
            jp.nov_due_amt = due_amt
            jp.nov_dis_amt = dis_amt
            jp.nov_rent_rec_date = date
            jp.nov_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.nov_rent = amt
            jp.remark = remark
            jp.nov_due_amt = due_amt
            jp.nov_dis_amt = dis_amt
            jp.nov_rent_rec_date = date
            jp.nov_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,nov_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.nov_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch16/payments/payment_details_of_months/nov/monthly_nov_make_payments.html', context)

#nov make payments start here

#dec make payments start here

def monthly_dec_make_payments_ob_ch16(request,id):
    if 'username' in request.session:
        if request.method == 'POST':
            amt=request.POST.get('janamt')
            remark = request.POST.get('janremark')
            date = request.POST.get('pdate')
            due_amt = request.POST.get('dueamt')
            dis_amt = request.POST.get('disamt')

            import branch16app
            jp = branch16app.models.pg1_new_guest.objects.get(id=id)
            jp.dec_rent = amt
            jp.remark = remark
            jp.dec_due_amt = due_amt
            jp.dec_dis_amt = dis_amt
            jp.dec_rent_rec_date = date
            jp.dec_rent_flag = 200
            jp.save()

            rno = pg1_new_guest.objects.all().filter(id=id)
            l = []
            for i in rno:
                l.append(str(i.guest_code))
            gc = ''.join(l)
            print('lll', l)

            #jp = pg1_new_beds.objects.get(guest_code=l[0])
            import branch16app
            jp = branch16app.models.pg1_new_beds.objects.get(guest_code=l[0])
            jp.dec_rent = amt
            jp.remark = remark
            jp.dec_due_amt = due_amt
            jp.dec_dis_amt = dis_amt
            jp.dec_rent_rec_date = date
            jp.dec_rent_flag = 200
            jp.save()

            rno= pg1_new_guest.objects.all().filter(id=id)
            l=[]
            ll=[]
            for i in rno:
                l.append(str(i.roon_no))
                ll.append(str(i.guest_code))
            s=''.join(l)
            gc=''.join(ll)

            r = pg1_new_guest.objects.all().filter(id=id, flag=2)
            rl = []
            for i in r:
                rl.append(i.roon_no)
                break

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

                'pd': pg1_new_guest.objects.all().filter(roon_no=s, flag=2,dec_rent_flag__gt=99,guest_code=gc),
                'user_details': pg1_new_guest.objects.all().filter(id=id),
                'room': room_pg1.objects.all().order_by('roon_no'),
                'rll' : rl,
            }
            return render(request, 'branches/branch16/payments/payment_user_details.html',context)
        rn = request.POST.get('rno')

        rno = pg1_new_guest.objects.all().filter(id=id)
        l = []
        for i in rno:
            l.append(str(i.guest_code))
        gc = ''.join(l)
        print('lll', l)

        import branch16app
        total_discout_amt = []
        pg1_new_beds = branch16app.models.pg1_new_guest.objects.all().filter(flag=2, guest_code=l[0])
        for i in pg1_new_beds:
            total_discout_amt.append(int(i.dec_dis_amt))

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

            'pd': pg1_new_guest.objects.all().filter(roon_no=rn, flag=2),
            'roomno': rn,
            'sd' : pg1_new_guest.objects.get(id=id),
            'room': room_pg1.objects.all().order_by('roon_no'),
            'user_details': pg1_new_guest.objects.all().filter(id=id),
            'discount_amt': total_discout_amt[0],
        }
        return render(request,'branches/branch16/payments/payment_details_of_months/dec/monthly_dec_make_payments.html', context)

#dec make payments start here

