import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *
from branch9app.models import *
import datetime

database_name = 'cpg'
database_password = '#123.com#'
database_user = 'root'
database_host = 'localhost'

import pymysql as py
import pymysql.cursors

def detailed_report_choose_months9(request):
    if 'username' in request.session:
        return render(request, 'branches/branch9/live_print_report/detailed_report_choose_months.html')
    return render(request, 'index.html')


def jan_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/jan/jan_details_live.html', context)
    return render(request, 'index.html')

def jan_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/jan/jan_print_live.html', context)
    return render(request, 'index.html')


def feb_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/feb/feb_details_live.html', context)
    return render(request, 'index.html')

def feb_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/feb/feb_print_live.html', context)
    return render(request, 'index.html')



def march_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/march/march_details_live.html', context)
    return render(request, 'index.html')

def march_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/march/march_print_live.html', context)
    return render(request, 'index.html')



def april_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/april/april_details_live.html', context)
    return render(request, 'index.html')

def april_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/april/april_print_live.html', context)
    return render(request, 'index.html')


def may_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/may/may_details_live.html', context)
    return render(request, 'index.html')

def may_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/may/may_print_live.html', context)
    return render(request, 'index.html')

def june_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/june/june_dtails_live.html', context)
    return render(request, 'index.html')

def june_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/june/june_print_live.html', context)
    return render(request, 'index.html')

def july_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/july/july_details_live.html', context)
    return render(request, 'index.html')

def july_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/july/july_print_live.html', context)
    return render(request, 'index.html')


def auguest_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/aug/aug_details_live.html', context)
    return render(request, 'index.html')

def auguest_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/aug/aug_print_live.html', context)
    return render(request, 'index.html')


def sept_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/sept/sept_details_live.html', context)
    return render(request, 'index.html')

def sept_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/sept/sept_print_live.html', context)
    return render(request, 'index.html')


def october_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/oct/oct_details_live.html', context)
    return render(request, 'index.html')

def october_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/oct/oct_print_live.html', context)
    return render(request, 'index.html')


def nov_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/nov/nov_details_live.html', context)
    return render(request, 'index.html')

def nov_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/nov/nov_print_live.html', context)
    return render(request, 'index.html')


def dec_details_live9(request):
    if 'username' in request.session:
        context = {
            'details' : pg1_new_beds.objects.all(),
        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/dec/dec_details_live.html', context)
    return render(request, 'index.html')

def dec_print_live9(request):
    if 'username' in request.session:
        ll = []
        rsdata = room_pg1.objects.all().order_by('roon_no')
        for i in rsdata:
            ll.append(i.share_type)

        context = {
            'brname': 'BRANCH 9 Room Creation Form',
            'table_height': '50px',

            'g2': ll[0],
            'g2_data': pg1_new_beds.objects.all().filter(roon_no=2),

            'rs101': ll[1],
            '101_data': pg1_new_beds.objects.all().filter(roon_no=101),
            'rs102': ll[2],
            '102_data': pg1_new_beds.objects.all().filter(roon_no=102),
            'rs103': ll[3],
            '103_data': pg1_new_beds.objects.all().filter(roon_no=103),
            'rs104': ll[4],
            '104_data': pg1_new_beds.objects.all().filter(roon_no=104),
            'rs105': ll[5],
            '105_data': pg1_new_beds.objects.all().filter(roon_no=105),
            'rs106': ll[6],
            '106_data': pg1_new_beds.objects.all().filter(roon_no=106),
            'rs107': ll[7],
            '107_data': pg1_new_beds.objects.all().filter(roon_no=107),
            'rs108': ll[8],
            '108_data': pg1_new_beds.objects.all().filter(roon_no=108),
            'rs109': ll[9],
            '109_data': pg1_new_beds.objects.all().filter(roon_no=109),
            'rs110': ll[10],
            '110_data': pg1_new_beds.objects.all().filter(roon_no=110),
            'rs111': ll[11],
            '111_data': pg1_new_beds.objects.all().filter(roon_no=111),
            'rs112': ll[12],
            '112_data': pg1_new_beds.objects.all().filter(roon_no=112),

            'rs201': ll[13],
            '201_data': pg1_new_beds.objects.all().filter(roon_no=201),
            'rs202': ll[14],
            '202_data': pg1_new_beds.objects.all().filter(roon_no=202),
            'rs203': ll[15],
            '203_data': pg1_new_beds.objects.all().filter(roon_no=203),
            'rs204': ll[16],
            '204_data': pg1_new_beds.objects.all().filter(roon_no=204),
            'rs205': ll[17],
            '205_data': pg1_new_beds.objects.all().filter(roon_no=205),
            'rs206': ll[18],
            '206_data': pg1_new_beds.objects.all().filter(roon_no=206),

            'rs207': ll[19],
            '207_data': pg1_new_beds.objects.all().filter(roon_no=207),
            'rs208': ll[20],
            '208_data': pg1_new_beds.objects.all().filter(roon_no=208),
            'rs209': ll[21],
            '209_data': pg1_new_beds.objects.all().filter(roon_no=209),
            'rs210': ll[22],
            '210_data': pg1_new_beds.objects.all().filter(roon_no=210),
            'rs211': ll[23],
            '211_data': pg1_new_beds.objects.all().filter(roon_no=211),
            'rs212': ll[24],
            '212_data': pg1_new_beds.objects.all().filter(roon_no=212),

            ##############################################

            'rs301': ll[25],
            '301_data': pg1_new_beds.objects.all().filter(roon_no=301),
            'rs302': ll[26],
            '302_data': pg1_new_beds.objects.all().filter(roon_no=302),
            'rs303': ll[27],
            '303_data': pg1_new_beds.objects.all().filter(roon_no=303),
            'rs304': ll[28],
            '304_data': pg1_new_beds.objects.all().filter(roon_no=304),
            'rs305': ll[29],
            '305_data': pg1_new_beds.objects.all().filter(roon_no=305),
            'rs306': ll[30],
            '306_data': pg1_new_beds.objects.all().filter(roon_no=306),

            'rs307': ll[31],
            '307_data': pg1_new_beds.objects.all().filter(roon_no=307),
            'rs308': ll[32],
            '308_data': pg1_new_beds.objects.all().filter(roon_no=308),
            'rs309': ll[33],
            '309_data': pg1_new_beds.objects.all().filter(roon_no=309),
            'rs310': ll[34],
            '310_data': pg1_new_beds.objects.all().filter(roon_no=310),
            'rs311': ll[35],
            '311_data': pg1_new_beds.objects.all().filter(roon_no=311),
            'rs312': ll[36],
            '312_data': pg1_new_beds.objects.all().filter(roon_no=312),

            ########################

            'rs401': ll[37],
            '401_data': pg1_new_beds.objects.all().filter(roon_no=401),
            'rs402': ll[38],
            '402_data': pg1_new_beds.objects.all().filter(roon_no=402),
            'rs403': ll[39],
            '403_data': pg1_new_beds.objects.all().filter(roon_no=403),
            'rs404': ll[40],
            '404_data': pg1_new_beds.objects.all().filter(roon_no=404),
            'rs405': ll[41],
            '405_data': pg1_new_beds.objects.all().filter(roon_no=405),
            'rs406': ll[42],
            '406_data': pg1_new_beds.objects.all().filter(roon_no=406),

            'rs407': ll[43],
            '407_data': pg1_new_beds.objects.all().filter(roon_no=407),
            'rs408': ll[44],
            '408_data': pg1_new_beds.objects.all().filter(roon_no=408),
            'rs409': ll[45],
            '409_data': pg1_new_beds.objects.all().filter(roon_no=409),
            'rs410': ll[46],
            '410_data': pg1_new_beds.objects.all().filter(roon_no=410),
            'rs411': ll[47],
            '411_data': pg1_new_beds.objects.all().filter(roon_no=411),
            'rs412': ll[48],
            '412_data': pg1_new_beds.objects.all().filter(roon_no=412),

            ######################################

            'rs501': ll[49],
            '501_data': pg1_new_beds.objects.all().filter(roon_no=501),
            'rs502': ll[50],
            '502_data': pg1_new_beds.objects.all().filter(roon_no=502),
            'rs503': ll[51],
            '503_data': pg1_new_beds.objects.all().filter(roon_no=503),
            'rs504': ll[52],
            '504_data': pg1_new_beds.objects.all().filter(roon_no=504),
            'rs505': ll[53],
            '505_data': pg1_new_beds.objects.all().filter(roon_no=505),
            'rs506': ll[54],
            '506_data': pg1_new_beds.objects.all().filter(roon_no=506),

            'rs507': ll[55],
            '507_data': pg1_new_beds.objects.all().filter(roon_no=507),
            'rs508': ll[56],
            '508_data': pg1_new_beds.objects.all().filter(roon_no=508),
            'rs509': ll[57],
            '509_data': pg1_new_beds.objects.all().filter(roon_no=509),
            'rs510': ll[58],
            '510_data': pg1_new_beds.objects.all().filter(roon_no=510),
            'rs511': ll[59],
            '511_data': pg1_new_beds.objects.all().filter(roon_no=511),
            'rs512': ll[60],
            '512_data': pg1_new_beds.objects.all().filter(roon_no=512),

            ###########################
            'myl': ll,

        }
        return render(request, 'branches/branch9/live_print_report/live_monthly_details/dec/dec_print_live.html', context)
    return render(request, 'index.html')



def viewall_vaccant_room9(request):
    context = {
        'vr': pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no')
    }
    return render(request, 'branches/branch9/reports/vaccant_room/viewall_vaccant_room.html', context)

#########FULL PAID GUEST START HERE ############


def full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/full_paid_guest.html', context)


def jan_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/jan/jan_full_paid_guest.html', context)


def feb_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/feb/feb_full_paid_guest.html', context)


def march_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/mar/march_full_paid_guest.html', context)


def april_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/apr/april_full_paid_guest.html', context)


def may_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/may/may_full_paid_guest.html', context)

def june_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/jun/june_full_paid_guest.html', context)

def july_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/jul/july_full_paid_guest.html', context)

def auguest_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/aug/aug_full_paid_guest.html', context)


def sept_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/sep/sept_full_paid_guest.html', context)


def october_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/oct/october_full_paid_guest.html', context)


def nov_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/nov/nov_full_paid_guest.html', context)


def dec_full_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/dec/dec_full_paid_guest.html', context)



#########FULL PAID GUEST END HERE ############

#########PARTIALLY PAID GUEST START HERE ############


def partially_paid_guest_choose_months9(request):
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

        return render(request, 'branches/branch9/reports/paid_rent/partially_paid_guest_choose_months.html',context)


def jan_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/jan/jan_partially_paid_guest.html', context)
def table_jan_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/jan/table_jan_partially_paid_guest.html', context)


def feb_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/feb/feb_partially_paid_guest.html', context)
def table_feb_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/feb/table_feb_partially_paid_guest.html', context)


def march_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/mar/march_partially_paid_guest.html', context)
def table_march_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/mar/table_march_partially_paid_guest.html', context)


def april_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/apr/april_partially_paid_guest.html', context)
def table_april_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/apr/table_april_partially_paid_guest.html', context)


def may_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/may/may_partially_paid_guest.html', context)
def table_may_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/may/table_may_partially_paid_guest.html', context)

def june_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/jun/june_partially_paid_guest.html', context)
def table_june_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/jun/table_june_partially_paid_guest.html', context)

def july_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/jul/july_partially_paid_guest.html', context)
def table_july_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/jul/table_july_partially_paid_guest.html', context)


def auguest_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/aug/auguest_partially_paid_guest.html', context)
def table_auguest_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/aug/table_auguest_partially_paid_guest.html', context)


def sept_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/sep/sept_partially_paid_guest.html', context)
def table_sept_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/sep/table_sept_partially_paid_guest.html', context)


def october_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/oct/october_partially_paid_guest.html', context)
def table_october_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/oct/table_october_partially_paid_guest.html', context)


def nov_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/nov/nov_partially_paid_guest.html', context)
def table_nov_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/nov/table_nov_partially_paid_guest.html', context)


def dec_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/dec/dec_partially_paid_guest.html', context)
def table_dec_partially_paid_guest9(request):
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
    return render(request, 'branches/branch9/reports/paid_rent/paid_monthly_reports/dec/table_dec_partially_paid_guest.html', context)



#########PARTIALLY PAID GUEST START HERE ############

