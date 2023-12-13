import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *
from branch7app.models import *
import datetime

database_name = 'cpg'
database_password = '#123.com#'
database_user = 'root'
database_host = 'localhost'

import pymysql as py
import pymysql.cursors

def detailed_report_choose_months7(request):
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
        return render(request, 'branches/branch7/live_print_report/detailed_report_choose_months.html',context)
    return render(request, 'index.html')


def jan_details_live7(request):
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

            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/jan/jan_details_live.html', context)
    return render(request, 'index.html')

def jan_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/jan/jan_print_live.html', context)
    return render(request, 'index.html')


def feb_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/feb/feb_details_live.html', context)
    return render(request, 'index.html')

def feb_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/feb/feb_print_live.html', context)
    return render(request, 'index.html')



def march_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/march/march_details_live.html', context)
    return render(request, 'index.html')

def march_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/march/march_print_live.html', context)
    return render(request, 'index.html')



def april_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/april/april_details_live.html', context)
    return render(request, 'index.html')

def april_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/april/april_print_live.html', context)
    return render(request, 'index.html')


def may_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/may/may_details_live.html', context)
    return render(request, 'index.html')

def may_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/may/may_print_live.html', context)
    return render(request, 'index.html')

def june_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/june/june_dtails_live.html', context)
    return render(request, 'index.html')

def june_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/june/june_print_live.html', context)
    return render(request, 'index.html')

def july_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/july/july_details_live.html', context)
    return render(request, 'index.html')

def july_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/july/july_print_live.html', context)
    return render(request, 'index.html')


def auguest_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/aug/aug_details_live.html', context)
    return render(request, 'index.html')

def auguest_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/aug/aug_print_live.html', context)
    return render(request, 'index.html')


def sept_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/sept/sept_details_live.html', context)
    return render(request, 'index.html')

def sept_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/sept/sept_print_live.html', context)
    return render(request, 'index.html')


def october_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/oct/oct_details_live.html', context)
    return render(request, 'index.html')

def october_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/oct/oct_print_live.html', context)
    return render(request, 'index.html')


def nov_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/nov/nov_details_live.html', context)
    return render(request, 'index.html')

def nov_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/nov/nov_print_live.html', context)
    return render(request, 'index.html')


def dec_details_live7(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/dec/dec_details_live.html', context)
    return render(request, 'index.html')

def dec_print_live7(request):
    if 'username' in request.session:
        l = []
        data = pg1_new_beds.objects.all()
        for i in data:
            l.append(i.share_type)

        ll = []
        # rsdata = room_pg1.objects.all().order_by('roon_no')1,
        # a
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        g1_data = pg1_new_beds.objects.all().filter(roon_no=1),
        print('room share type of branch22', ll)
        print('room share type of branchl0', ll[0])
        print('room share type of branchl1', ll[1])

        context = {
            'brname': 'BRANCH 7 Room Creation Form',
            # 'br': pg1_new_beds.objects.all().filter(roon_no=101).order_by('roon_no'),
            'rn1': l[0],
            'table_height': '70px',

            'g1': ll[0],
            'g1_data': pg1_new_beds.objects.all().filter(roon_no=1),
            # 'g1_data':g1_data,
            'g2': ll[1],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),
            'g3': ll[2],
            'g3_data': pg1_new_beds.objects.all().filter(roon_no=3),
            'g4': ll[3],
            'g4_data': pg1_new_beds.objects.all().filter(roon_no=4),
            'g5': ll[4],
            'g5_data': pg1_new_beds.objects.all().filter(roon_no=5),

            'rs101': ll[5],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[6],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[7],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            # 'rs104': ll[9],
            # '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[8],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[9],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),

            'rs201': ll[10],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[11],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[12],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[13],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[14],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[15],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            ##############################################

            'rs301': ll[16],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[17],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[18],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[19],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[20],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[21],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            ########################

            'rs401': ll[22],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[23],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[24],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[25],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[26],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[27],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs601': ll[28],
            '601_data': pg1_new_beds.objects.all().filter(roon_no=601),
            'rs602': ll[29],
            '602_data': pg1_new_beds.objects.all().filter(roon_no=602),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch7/live_print_report/live_monthly_details/dec/dec_print_live.html', context)
    return render(request, 'index.html')



def viewall_vaccant_room7(request):
    context = {
        'vr': pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/vaccant_room/viewall_vaccant_room.html', context)

#########FULL PAID GUEST START HERE ############


def full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt='0',june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/full_paid_guest.html', context)


def jan_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,jan_due_amt='0',jan_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/jan/jan_full_paid_guest.html', context)


def feb_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,feb_due_amt='0',feb_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/feb/feb_full_paid_guest.html', context)


def march_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,march_due_amt='0',march_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/mar/march_full_paid_guest.html', context)


def april_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,april_due_amt='0',april_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/apr/april_full_paid_guest.html', context)


def may_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,may_due_amt='0',may_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/may/may_full_paid_guest.html', context)

def june_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,june_due_amt='0',june_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/jun/june_full_paid_guest.html', context)

def july_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,july_due_amt='0',july_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/jul/july_full_paid_guest.html', context)

def auguest_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,auguest_due_amt='0',auguest_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/aug/aug_full_paid_guest.html', context)


def sept_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,sept_due_amt='0',sept_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/sep/sept_full_paid_guest.html', context)


def october_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,october_due_amt='0',october_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/oct/october_full_paid_guest.html', context)


def nov_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,nov_due_amt='0',nov_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/nov/nov_full_paid_guest.html', context)


def dec_full_paid_guest7(request):
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

        'fpr': pg1_new_guest.objects.all().filter(flag=2,dec_due_amt='0',dec_rent_flag=200).order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/dec/dec_full_paid_guest.html', context)



#########FULL PAID GUEST END HERE ############

#########PARTIALLY PAID GUEST START HERE ############


def partially_paid_guest_choose_months7(request):
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

        return render(request, 'branches/branch7/reports/paid_rent/partially_paid_guest_choose_months.html',context)


def jan_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,jan_rent_flag=200).exclude(jan_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/jan/jan_partially_paid_guest.html', context)
def table_jan_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,jan_rent_flag=200).exclude(jan_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/jan/table_jan_partially_paid_guest.html', context)


def feb_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,feb_rent_flag=200).exclude(feb_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/feb/feb_partially_paid_guest.html', context)
def table_feb_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,feb_rent_flag=200).exclude(feb_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/feb/table_feb_partially_paid_guest.html', context)


def march_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,march_rent_flag=200).exclude(march_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/mar/march_partially_paid_guest.html', context)
def table_march_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,march_rent_flag=200).exclude(march_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/mar/table_march_partially_paid_guest.html', context)


def april_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,april_rent_flag=200).exclude(april_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/apr/april_partially_paid_guest.html', context)
def table_april_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,april_rent_flag=200).exclude(april_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/apr/table_april_partially_paid_guest.html', context)


def may_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag=200).exclude(may_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/may/may_partially_paid_guest.html', context)
def table_may_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,may_rent_flag=200).exclude(may_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/may/table_may_partially_paid_guest.html', context)

def june_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag=200).exclude(june_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/jun/june_partially_paid_guest.html', context)
def table_june_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,june_rent_flag=200).exclude(june_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/jun/table_june_partially_paid_guest.html', context)

def july_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag=200).exclude(july_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/jul/july_partially_paid_guest.html', context)
def table_july_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,july_rent_flag=200).exclude(july_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/jul/table_july_partially_paid_guest.html', context)


def auguest_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,auguest_rent_flag=200).exclude(auguest_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/aug/auguest_partially_paid_guest.html', context)
def table_auguest_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,auguest_rent_flag=200).exclude(auguest_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/aug/table_auguest_partially_paid_guest.html', context)


def sept_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,sept_rent_flag=200).exclude(sept_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/sep/sept_partially_paid_guest.html', context)
def table_sept_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,sept_rent_flag=200).exclude(sept_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/sep/table_sept_partially_paid_guest.html', context)


def october_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,october_rent_flag=200).exclude(october_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/oct/october_partially_paid_guest.html', context)
def table_october_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,october_rent_flag=200).exclude(october_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/oct/table_october_partially_paid_guest.html', context)


def nov_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,nov_rent_flag=200).exclude(nov_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/nov/nov_partially_paid_guest.html', context)
def table_nov_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,nov_rent_flag=200).exclude(nov_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/nov/table_nov_partially_paid_guest.html', context)


def dec_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,dec_rent_flag=200).exclude(dec_due_amt='0').order_by('roon_no')
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/dec/dec_partially_paid_guest.html', context)
def table_dec_partially_paid_guest7(request):
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

        'ppr': pg1_new_guest.objects.all().filter(flag=2,dec_rent_flag=200).exclude(dec_due_amt='0').order_by('roon_no'),
    }
    return render(request, 'branches/branch7/reports/paid_rent/paid_monthly_reports/dec/table_dec_partially_paid_guest.html', context)



#########PARTIALLY PAID GUEST START HERE ############

