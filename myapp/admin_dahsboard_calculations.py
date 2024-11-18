#admin_dahsboard_calculations
#admin_dashboard_reports
#total_vaccant_share_choose_branches
from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
import branch2app
import branch3app
import branch4app
import branch5app
import branch6app
import branch7app
import branch8app
import branch9app
import branch10app
import branch11app
import branch12app
import branch13app
import branch14app
import branch15app
import branch16app

def total_guest():
    tg=[]
    total_guest_br1 = pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br1))
    total_guest_br2= branch2app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br5))

    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br7))
    total_guest_br8 = branch8app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br8))
    total_guest_br9 = branch9app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br9))

    total_guest_br10 = branch10app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br10))
    total_guest_br11 = branch11app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br11))
    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br14))

    total_guest_br15 = branch15app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br15))
    total_guest_br16 = branch16app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br16))

    return sum(tg)

def branchwise_total_guest(request):
    tg=[]
    total_guest_br1 = pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br1))
    total_guest_br2= branch2app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br5))

    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br7))
    total_guest_br8 = branch8app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br8))
    total_guest_br9 = branch9app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br9))

    total_guest_br10 = branch10app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br10))
    total_guest_br11 = branch11app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br11))
    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br14))

    total_guest_br15 = branch15app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br15))
    total_guest_br16 = branch16app.models.pg1_new_beds.objects.all().filter(flag=2)
    tg.append(len(total_guest_br16))

    context={
        'tg' : tg,
    }
    return render(request,'admindashboard/admin_dashboard_reports/branchwise_total_guest_choose_branches.html', context)


def total_vaccant_share1():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br5))

    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br7))
    total_guest_br8 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br8))
    total_guest_br9 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br9))

    total_guest_br10 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br10))
    total_guest_br11 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br11))
    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    total_guest_br15 = branch15app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br15))
    total_guest_br16 = branch16app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br16))

    return sum(tsv)

def total_vaccant_share2():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br5))

    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br7))
    total_guest_br8 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br8))
    total_guest_br9 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br9))

    total_guest_br10 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br10))
    total_guest_br11 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br11))
    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    total_guest_br15 = branch15app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br15))
    total_guest_br16 = branch16app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br16))

    return sum(tsv)

def total_vaccant_share3():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br5))

    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br7))
    total_guest_br8 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br8))
    total_guest_br9 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br9))

    total_guest_br10 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br10))
    total_guest_br11 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br11))
    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    total_guest_br15 = branch15app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br15))
    total_guest_br16 = branch16app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br16))

    return sum(tsv)

def total_vaccant_share4():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br5))

    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br7))
    total_guest_br8 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br8))
    total_guest_br9 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br9))

    total_guest_br10 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br10))
    total_guest_br11 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br11))
    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    total_guest_br15 = branch15app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br15))
    total_guest_br16 = branch16app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br16))

    return sum(tsv)

def total_vaccant_share5():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))

    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br7))
    total_guest_br8 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br8))
    total_guest_br9 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br9))

    total_guest_br10 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br10))
    total_guest_br11 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br11))
    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    total_guest_br15 = branch15app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br15))
    total_guest_br16 = branch16app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br16))

    return sum(tsv)

def total_vaccant_share6():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))

    total_guest_br6 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br6))
    total_guest_br7 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br7))
    total_guest_br8 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br8))
    total_guest_br9 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br9))

    total_guest_br10 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br10))
    total_guest_br11 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br11))
    total_guest_br12 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br12))
    total_guest_br13 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br13))
    total_guest_br14 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br14))

    total_guest_br15 = branch15app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br15))
    total_guest_br16 = branch16app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br16))

    return sum(tsv)

def total_vaccant_room():
    tsv = []
    total_vaccant_room_br1 = total_vaccant_share1()
    tsv.append(total_vaccant_room_br1)
    total_vaccant_room_br2 = total_vaccant_share2()
    tsv.append(total_vaccant_room_br2)
    total_vaccant_room_br3 = total_vaccant_share3()
    tsv.append(total_vaccant_room_br3)
    total_vaccant_room_br4 = total_vaccant_share4()
    tsv.append(total_vaccant_room_br4)
    total_vaccant_room_br5 = total_vaccant_share5()
    tsv.append(total_vaccant_room_br5)
    total_vaccant_room_br6 = total_vaccant_share6()
    tsv.append(total_vaccant_room_br6)

    return sum(tsv)


def total_vaccant_share_branch1():
    tsv = []
    total_guest_br1 = pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch2():
    tsv = []
    total_guest_br1 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch2app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch3():
    tsv = []
    total_guest_br1 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch3app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch4():
    tsv = []
    total_guest_br1 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch4app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch5():
    tsv = []
    total_guest_br1 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch5app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch6():
    tsv = []
    total_guest_br1 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch6app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch7():
    tsv = []
    total_guest_br1 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch7app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch8():
    tsv = []
    total_guest_br1 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch8app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch9():
    tsv = []
    total_guest_br1 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch9app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch10():
    tsv = []
    total_guest_br1 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch10app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch11():
    tsv = []
    total_guest_br1 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch11app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch12():
    tsv = []
    total_guest_br1 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch12app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch13():
    tsv = []
    total_guest_br1 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch13app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch14():
    tsv = []
    total_guest_br1 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch15():
    tsv = []
    total_guest_br1 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv

def total_vaccant_share_branch16():
    tsv = []
    total_guest_br1 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='1').exclude(flag=2)
    tsv.append(len(total_guest_br1))
    total_guest_br2 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='2').exclude(flag=2)
    tsv.append(len(total_guest_br2))
    total_guest_br3 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='3').exclude(flag=2)
    tsv.append(len(total_guest_br3))
    total_guest_br4 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='4').exclude(flag=2)
    tsv.append(len(total_guest_br4))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='5').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    total_guest_br5 = branch14app.models.pg1_new_beds.objects.all().filter(share_type='6').exclude(flag=2)
    tsv.append(len(total_guest_br5))
    return tsv



def total_vaccant_share_choose_branches(request):
    context = {
        'br1' : total_vaccant_share_branch1(),
        'br2': total_vaccant_share_branch2(),
        'br3': total_vaccant_share_branch3(),
        'br4': total_vaccant_share_branch4(),
        'br5': total_vaccant_share_branch5(),

        'br6': total_vaccant_share_branch6(),
        'br7': total_vaccant_share_branch7(),
        'br8': total_vaccant_share_branch8(),
        'br9': total_vaccant_share_branch9(),

        'br10': total_vaccant_share_branch10(),
        'br11': total_vaccant_share_branch11(),
        'br12': total_vaccant_share_branch12(),
        'br13': total_vaccant_share_branch13(),
        'br14': total_vaccant_share_branch14(),

        'br15': total_vaccant_share_branch15(),
        'br16': total_vaccant_share_branch16(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/total_vaccant_share_choose_branches.html',context)

######TOTAL COLLECTION START HERE

def total_gtc():
    a1 = admin_dashboard_calculations_br1.grand_total_collection()
    a2 = branch2app.admin_dashboard_calculations_br2.grand_total_collection()
    a3 = branch3app.admin_dashboard_calculations_br3.grand_total_collection()
    a4 = branch4app.admin_dashboard_calculations_br4.grand_total_collection()
    a5 = branch5app.admin_dashboard_calculations_br5.grand_total_collection()
    a6 = branch6app.admin_dashboard_calculations_br6.grand_total_collection()
    a7 = branch7app.admin_dashboard_calculations_br7.grand_total_collection()
    a8 = branch8app.admin_dashboard_calculations_br8.grand_total_collection()
    a9 = branch9app.admin_dashboard_calculations_br9.grand_total_collection()

    a10 = branch10app.admin_dashboard_calculations_br10.grand_total_collection()
    a11 = branch11app.admin_dashboard_calculations_br11.grand_total_collection()
    a12 = branch12app.admin_dashboard_calculations_br12.grand_total_collection()
    a13 = branch13app.admin_dashboard_calculations_br13.grand_total_collection()
    a14 = branch14app.admin_dashboard_calculations_br14.grand_total_collection()

    a15 = branch15app.admin_dashboard_calculations_br15.grand_total_collection()
    a16 = branch16app.admin_dashboard_calculations_br16.grand_total_collection()

    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    l=[]
    l.append(a1[cm])
    l.append(a2[cm])
    l.append(a3[cm])
    l.append(a4[cm])
    l.append(a5[cm])
    l.append(a6[cm])
    l.append(a7[cm])
    l.append(a8[cm])
    l.append(a9[cm])

    l.append(a10[cm])
    l.append(a11[cm])
    l.append(a12[cm])
    l.append(a13[cm])
    l.append(a14[cm])

    l.append(a15[cm])
    l.append(a16[cm])

    gtc=sum(l)
    print('this is total branch gtc sum',gtc)
    return gtc

def total_advance():
    a1 = admin_dashboard_calculations_br1.total_collection_advance()
    a2 = branch2app.admin_dashboard_calculations_br2.total_collection_advance()
    a3 = branch3app.admin_dashboard_calculations_br3.total_collection_advance()
    a4 = branch4app.admin_dashboard_calculations_br4.total_collection_advance()
    a5 = branch5app.admin_dashboard_calculations_br5.total_collection_advance()
    a6 = branch6app.admin_dashboard_calculations_br6.total_collection_advance()
    a7 = branch7app.admin_dashboard_calculations_br7.total_collection_advance()
    a8 = branch8app.admin_dashboard_calculations_br8.total_collection_advance()
    a9 = branch9app.admin_dashboard_calculations_br9.total_collection_advance()

    a10 = branch10app.admin_dashboard_calculations_br10.total_collection_advance()
    a11 = branch11app.admin_dashboard_calculations_br11.total_collection_advance()
    a12 = branch12app.admin_dashboard_calculations_br12.total_collection_advance()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collection_advance()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collection_advance()

    a15 = branch15app.admin_dashboard_calculations_br15.total_collection_advance()
    a16 = branch16app.admin_dashboard_calculations_br16.total_collection_advance()

    l = []
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)

    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)

    l.append(a15)
    l.append(a16)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def total_discount():
    a1 = admin_dashboard_calculations_br1.total_discount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_discount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_discount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_discount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_discount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_discount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_discount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_discount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_discount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_discount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_discount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_discount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_discount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_discount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_discount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_discount()

    l = []
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)

    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)

    l.append(a15)
    l.append(a16)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def all_total_collatable_amount():
    a1 = admin_dashboard_calculations_br1.total_colatable_amount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_colatable_amount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_colatable_amount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_colatable_amount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_colatable_amount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_colatable_amount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_colatable_amount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_colatable_amount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_colatable_amount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_colatable_amount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_colatable_amount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_colatable_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_colatable_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_colatable_amount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_colatable_amount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_colatable_amount()

    l = []
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)

    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)

    l.append(a15)
    l.append(a16)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def all_total_collected_amount():
    a1 = admin_dashboard_calculations_br1.total_collected_amount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_collected_amount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_collected_amount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_collected_amount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_collected_amount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_collected_amount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_collected_amount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_collected_amount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_collected_amount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_collected_amount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_collected_amount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_collected_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collected_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collected_amount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_collected_amount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_collected_amount()

    l = []
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)

    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)

    l.append(a15)
    l.append(a16)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

def all_total_due():
    a1 = admin_dashboard_calculations_br1.total_due()
    a2 = branch2app.admin_dashboard_calculations_br2.total_due()
    a3 = branch3app.admin_dashboard_calculations_br3.total_due()
    a4 = branch4app.admin_dashboard_calculations_br4.total_due()
    a5 = branch5app.admin_dashboard_calculations_br5.total_due()
    a6 = branch6app.admin_dashboard_calculations_br6.total_due()
    a7 = branch7app.admin_dashboard_calculations_br7.total_due()
    a8 = branch8app.admin_dashboard_calculations_br8.total_due()
    a9 = branch9app.admin_dashboard_calculations_br9.total_due()

    a10 = branch10app.admin_dashboard_calculations_br10.total_due()
    a11 = branch11app.admin_dashboard_calculations_br11.total_due()
    a12 = branch12app.admin_dashboard_calculations_br12.total_due()
    a13 = branch13app.admin_dashboard_calculations_br13.total_due()
    a14 = branch14app.admin_dashboard_calculations_br14.total_due()

    a15 = branch15app.admin_dashboard_calculations_br15.total_due()
    a16 = branch16app.admin_dashboard_calculations_br16.total_due()

    l = []
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)
    l.append(a7)
    l.append(a8)
    l.append(a9)

    l.append(a10)
    l.append(a11)
    l.append(a12)
    l.append(a13)
    l.append(a14)

    l.append(a15)
    l.append(a16)

    gtc = sum(l)
    print('this is total branch gtc sum', gtc)
    return gtc

#*************************************
#####LIST OF TOTAL COLLECTION
#*************************************

def branchwise_total_collection(request):
    a1 = admin_dashboard_calculations_br1.grand_total_collection()
    a2 = branch2app.admin_dashboard_calculations_br2.grand_total_collection()
    a3 = branch3app.admin_dashboard_calculations_br3.grand_total_collection()
    a4 = branch4app.admin_dashboard_calculations_br4.grand_total_collection()
    a5 = branch5app.admin_dashboard_calculations_br5.grand_total_collection()
    a6 = branch6app.admin_dashboard_calculations_br6.grand_total_collection()
    a7 = branch7app.admin_dashboard_calculations_br7.grand_total_collection()
    a8 = branch8app.admin_dashboard_calculations_br8.grand_total_collection()
    a9 = branch9app.admin_dashboard_calculations_br9.grand_total_collection()

    a10 = branch10app.admin_dashboard_calculations_br10.grand_total_collection()
    a11 = branch11app.admin_dashboard_calculations_br11.grand_total_collection()
    a12 = branch12app.admin_dashboard_calculations_br12.grand_total_collection()
    a13 = branch13app.admin_dashboard_calculations_br13.grand_total_collection()
    a14 = branch14app.admin_dashboard_calculations_br14.grand_total_collection()

    a15 = branch15app.admin_dashboard_calculations_br15.grand_total_collection()
    a16 = branch16app.admin_dashboard_calculations_br16.grand_total_collection()

    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    list_total_gtc = []
    list_total_gtc.append(a1[cm])
    list_total_gtc.append(a2[cm])
    list_total_gtc.append(a3[cm])
    list_total_gtc.append(a4[cm])
    list_total_gtc.append(a5[cm])
    list_total_gtc.append(a6[cm])
    list_total_gtc.append(a7[cm])
    list_total_gtc.append(a8[cm])
    list_total_gtc.append(a9[cm])

    list_total_gtc.append(a10[cm])
    list_total_gtc.append(a11[cm])
    list_total_gtc.append(a12[cm])
    list_total_gtc.append(a13[cm])
    list_total_gtc.append(a14[cm])

    list_total_gtc.append(a15[cm])
    list_total_gtc.append(a16[cm])

#******list_total_advance

    a1 = admin_dashboard_calculations_br1.total_collection_advance()
    a2 = branch2app.admin_dashboard_calculations_br2.total_collection_advance()
    a3 = branch3app.admin_dashboard_calculations_br3.total_collection_advance()
    a4 = branch4app.admin_dashboard_calculations_br4.total_collection_advance()
    a5 = branch5app.admin_dashboard_calculations_br5.total_collection_advance()
    a6 = branch6app.admin_dashboard_calculations_br6.total_collection_advance()
    a7 = branch7app.admin_dashboard_calculations_br7.total_collection_advance()
    a8 = branch8app.admin_dashboard_calculations_br8.total_collection_advance()
    a9 = branch9app.admin_dashboard_calculations_br9.total_collection_advance()

    a10 = branch10app.admin_dashboard_calculations_br10.total_collection_advance()
    a11 = branch11app.admin_dashboard_calculations_br11.total_collection_advance()
    a12 = branch12app.admin_dashboard_calculations_br12.total_collection_advance()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collection_advance()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collection_advance()

    a15 = branch15app.admin_dashboard_calculations_br15.total_collection_advance()
    a16 = branch16app.admin_dashboard_calculations_br16.total_collection_advance()

    list_total_advance = []
    list_total_advance.append(a1)
    list_total_advance.append(a2)
    list_total_advance.append(a3)
    list_total_advance.append(a4)
    list_total_advance.append(a5)
    list_total_advance.append(a6)
    list_total_advance.append(a7)
    list_total_advance.append(a8)
    list_total_advance.append(a9)

    list_total_advance.append(a10)
    list_total_advance.append(a11)
    list_total_advance.append(a12)
    list_total_advance.append(a13)
    list_total_advance.append(a14)

    list_total_advance.append(a15)
    list_total_advance.append(a16)

#***********list_total_discount

    a1 = admin_dashboard_calculations_br1.total_discount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_discount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_discount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_discount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_discount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_discount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_discount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_discount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_discount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_discount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_discount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_discount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_discount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_discount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_discount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_discount()

    total_discount = []
    total_discount.append(a1)
    total_discount.append(a2)
    total_discount.append(a3)
    total_discount.append(a4)
    total_discount.append(a5)
    total_discount.append(a6)
    total_discount.append(a7)
    total_discount.append(a8)
    total_discount.append(a9)

    total_discount.append(a10)
    total_discount.append(a11)
    total_discount.append(a12)
    total_discount.append(a13)
    total_discount.append(a14)

    total_discount.append(a15)
    total_discount.append(a16)


#******list_all_total_collatable_amount

    a1 = admin_dashboard_calculations_br1.total_colatable_amount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_colatable_amount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_colatable_amount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_colatable_amount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_colatable_amount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_colatable_amount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_colatable_amount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_colatable_amount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_colatable_amount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_colatable_amount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_colatable_amount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_colatable_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_colatable_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_colatable_amount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_colatable_amount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_colatable_amount()

    total_colatable_amount = []
    total_colatable_amount.append(a1)
    total_colatable_amount.append(a2)
    total_colatable_amount.append(a3)
    total_colatable_amount.append(a4)
    total_colatable_amount.append(a5)
    total_colatable_amount.append(a6)
    total_colatable_amount.append(a7)
    total_colatable_amount.append(a8)
    total_colatable_amount.append(a9)

    total_colatable_amount.append(a10)
    total_colatable_amount.append(a11)
    total_colatable_amount.append(a12)
    total_colatable_amount.append(a13)
    total_colatable_amount.append(a14)

    total_colatable_amount.append(a15)
    total_colatable_amount.append(a16)

#*******list_all_total_collected_amount

    a1 = admin_dashboard_calculations_br1.total_collected_amount()
    a2 = branch2app.admin_dashboard_calculations_br2.total_collected_amount()
    a3 = branch3app.admin_dashboard_calculations_br3.total_collected_amount()
    a4 = branch4app.admin_dashboard_calculations_br4.total_collected_amount()
    a5 = branch5app.admin_dashboard_calculations_br5.total_collected_amount()
    a6 = branch6app.admin_dashboard_calculations_br6.total_collected_amount()
    a7 = branch7app.admin_dashboard_calculations_br7.total_collected_amount()
    a8 = branch8app.admin_dashboard_calculations_br8.total_collected_amount()
    a9 = branch9app.admin_dashboard_calculations_br9.total_collected_amount()

    a10 = branch10app.admin_dashboard_calculations_br10.total_collected_amount()
    a11 = branch11app.admin_dashboard_calculations_br11.total_collected_amount()
    a12 = branch12app.admin_dashboard_calculations_br12.total_collected_amount()
    a13 = branch13app.admin_dashboard_calculations_br13.total_collected_amount()
    a14 = branch14app.admin_dashboard_calculations_br14.total_collected_amount()

    a15 = branch15app.admin_dashboard_calculations_br15.total_collected_amount()
    a16 = branch16app.admin_dashboard_calculations_br16.total_collected_amount()

    total_collected_amount = []
    total_collected_amount.append(a1)
    total_collected_amount.append(a2)
    total_collected_amount.append(a3)
    total_collected_amount.append(a4)
    total_collected_amount.append(a5)
    total_collected_amount.append(a6)
    total_collected_amount.append(a7)
    total_collected_amount.append(a8)
    total_collected_amount.append(a9)

    total_collected_amount.append(a10)
    total_collected_amount.append(a11)
    total_collected_amount.append(a12)
    total_collected_amount.append(a13)
    total_collected_amount.append(a14)

    total_collected_amount.append(a15)
    total_collected_amount.append(a16)


#*****list_all_total_due

    a1 = admin_dashboard_calculations_br1.total_due()
    a2 = branch2app.admin_dashboard_calculations_br2.total_due()
    a3 = branch3app.admin_dashboard_calculations_br3.total_due()
    a4 = branch4app.admin_dashboard_calculations_br4.total_due()
    a5 = branch5app.admin_dashboard_calculations_br5.total_due()
    a6 = branch6app.admin_dashboard_calculations_br6.total_due()
    a7 = branch7app.admin_dashboard_calculations_br7.total_due()
    a8 = branch8app.admin_dashboard_calculations_br8.total_due()
    a9 = branch9app.admin_dashboard_calculations_br9.total_due()

    a10 = branch10app.admin_dashboard_calculations_br10.total_due()
    a11 = branch11app.admin_dashboard_calculations_br11.total_due()
    a12 = branch12app.admin_dashboard_calculations_br12.total_due()
    a13 = branch13app.admin_dashboard_calculations_br13.total_due()
    a14 = branch14app.admin_dashboard_calculations_br14.total_due()

    a15 = branch15app.admin_dashboard_calculations_br15.total_due()
    a16 = branch16app.admin_dashboard_calculations_br16.total_due()

    total_due = []
    total_due.append(a1)
    total_due.append(a2)
    total_due.append(a3)
    total_due.append(a4)
    total_due.append(a5)
    total_due.append(a6)
    total_due.append(a7)
    total_due.append(a8)
    total_due.append(a9)

    total_due.append(a10)
    total_due.append(a11)
    total_due.append(a12)
    total_due.append(a13)
    total_due.append(a14)

    total_due.append(a15)
    total_due.append(a16)


    context={
        'grand_total_collection':list_total_gtc,
        'total_collection_advance': list_total_advance,
        'total_discount': total_discount,

        'total_colatable_amount': total_colatable_amount,
        'total_collected_amount': total_collected_amount,
        'total_due': total_due
    }
    return render(request,'admindashboard/admin_dashboard_reports/branchwise_total_collection.html', context)





######TOTAL COLLECTION END HERE
from . import admin_dashboard_calculations_br1
def details_branch1(request):
    a = admin_dashboard_calculations_br1.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]
    context = {
        'tc': pg1_new_beds.objects.all().filter(flag=2),
        'vr': pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': admin_dashboard_calculations_br1.total_collection_advance(),
        'total_discount': admin_dashboard_calculations_br1.total_discount(),

        'total_colatable_amount': admin_dashboard_calculations_br1.total_colatable_amount(),
        'total_collected_amount': admin_dashboard_calculations_br1.total_collected_amount(),
        'total_due': admin_dashboard_calculations_br1.total_due(),
        'l': admin_dashboard_calculations_br1.grand_total(),
    }
    return render(request, 'admindashboard/admin_dashboard_reports/branch_details/details_branch.html', context)



def details_branch2(request):
    a = branch2app.admin_dashboard_calculations_br2.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]
    context = {
        'tc' : branch2app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch2app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch2app.admin_dashboard_calculations_br2.total_collection_advance(),
        'total_discount': branch2app.admin_dashboard_calculations_br2.total_discount(),

        'total_colatable_amount': branch2app.admin_dashboard_calculations_br2.total_colatable_amount(),
        'total_collected_amount': branch2app.admin_dashboard_calculations_br2.total_collected_amount(),
        'total_due': branch2app.admin_dashboard_calculations_br2.total_due(),
        'l': branch2app.admin_dashboard_calculations_br2.grand_total(),
    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch3(request):
    a = branch3app.admin_dashboard_calculations_br3.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch3app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch3app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch3app.admin_dashboard_calculations_br3.total_collection_advance(),
        'total_discount': branch3app.admin_dashboard_calculations_br3.total_discount(),

        'total_colatable_amount': branch3app.admin_dashboard_calculations_br3.total_colatable_amount(),
        'total_collected_amount': branch3app.admin_dashboard_calculations_br3.total_collected_amount(),
        'total_due': branch3app.admin_dashboard_calculations_br3.total_due(),
        'l': branch3app.admin_dashboard_calculations_br3.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch4(request):
    a = branch4app.admin_dashboard_calculations_br4.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch4app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch4app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch4app.admin_dashboard_calculations_br4.total_collection_advance(),
        'total_discount': branch4app.admin_dashboard_calculations_br4.total_discount(),

        'total_colatable_amount': branch4app.admin_dashboard_calculations_br4.total_colatable_amount(),
        'total_collected_amount': branch4app.admin_dashboard_calculations_br4.total_collected_amount(),
        'total_due': branch4app.admin_dashboard_calculations_br4.total_due(),
        'l': branch4app.admin_dashboard_calculations_br4.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch5(request):
    a = branch5app.admin_dashboard_calculations_br5.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch5app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch5app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch5app.admin_dashboard_calculations_br5.total_collection_advance(),
        'total_discount': branch5app.admin_dashboard_calculations_br5.total_discount(),

        'total_colatable_amount': branch5app.admin_dashboard_calculations_br5.total_colatable_amount(),
        'total_collected_amount': branch5app.admin_dashboard_calculations_br5.total_collected_amount(),
        'total_due': branch5app.admin_dashboard_calculations_br5.total_due(),
        'l': branch5app.admin_dashboard_calculations_br5.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)
#PRESTIGE START HERE
#################################
def details_branch6(request):
    a = branch6app.admin_dashboard_calculations_br6.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch6app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch6app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch6app.admin_dashboard_calculations_br6.total_collection_advance(),
        'total_discount': branch6app.admin_dashboard_calculations_br6.total_discount(),

        'total_colatable_amount': branch6app.admin_dashboard_calculations_br6.total_colatable_amount(),
        'total_collected_amount': branch6app.admin_dashboard_calculations_br6.total_collected_amount(),
        'total_due': branch6app.admin_dashboard_calculations_br6.total_due(),
        'l': branch6app.admin_dashboard_calculations_br6.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch7(request):
    a = branch7app.admin_dashboard_calculations_br7.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch7app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch7app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch7app.admin_dashboard_calculations_br7.total_collection_advance(),
        'total_discount': branch7app.admin_dashboard_calculations_br7.total_discount(),

        'total_colatable_amount': branch7app.admin_dashboard_calculations_br7.total_colatable_amount(),
        'total_collected_amount': branch7app.admin_dashboard_calculations_br7.total_collected_amount(),
        'total_due': branch7app.admin_dashboard_calculations_br7.total_due(),
        'l': branch7app.admin_dashboard_calculations_br7.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch8(request):
    a = branch8app.admin_dashboard_calculations_br8.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch8app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch8app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch8app.admin_dashboard_calculations_br8.total_collection_advance(),
        'total_discount': branch8app.admin_dashboard_calculations_br8.total_discount(),

        'total_colatable_amount': branch8app.admin_dashboard_calculations_br8.total_colatable_amount(),
        'total_collected_amount': branch8app.admin_dashboard_calculations_br8.total_collected_amount(),
        'total_due': branch8app.admin_dashboard_calculations_br8.total_due(),
        'l': branch8app.admin_dashboard_calculations_br8.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch9(request):
    a = branch9app.admin_dashboard_calculations_br9.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch9app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch9app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch9app.admin_dashboard_calculations_br9.total_collection_advance(),
        'total_discount': branch9app.admin_dashboard_calculations_br9.total_discount(),

        'total_colatable_amount': branch9app.admin_dashboard_calculations_br9.total_colatable_amount(),
        'total_collected_amount': branch9app.admin_dashboard_calculations_br9.total_collected_amount(),
        'total_due': branch9app.admin_dashboard_calculations_br9.total_due(),
        'l': branch9app.admin_dashboard_calculations_br9.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)



def details_branch10(request):
    a = branch10app.admin_dashboard_calculations_br10.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch10app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch10app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch10app.admin_dashboard_calculations_br10.total_collection_advance(),
        'total_discount': branch10app.admin_dashboard_calculations_br10.total_discount(),

        'total_colatable_amount': branch10app.admin_dashboard_calculations_br10.total_colatable_amount(),
        'total_collected_amount': branch10app.admin_dashboard_calculations_br10.total_collected_amount(),
        'total_due': branch10app.admin_dashboard_calculations_br10.total_due(),
        'l': branch10app.admin_dashboard_calculations_br10.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)


def details_branch11(request):
    a = branch11app.admin_dashboard_calculations_br11.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch11app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch11app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch11app.admin_dashboard_calculations_br11.total_collection_advance(),
        'total_discount': branch11app.admin_dashboard_calculations_br11.total_discount(),

        'total_colatable_amount': branch11app.admin_dashboard_calculations_br11.total_colatable_amount(),
        'total_collected_amount': branch11app.admin_dashboard_calculations_br11.total_collected_amount(),
        'total_due': branch11app.admin_dashboard_calculations_br11.total_due(),
        'l': branch11app.admin_dashboard_calculations_br11.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)


def details_branch12(request):
    a = branch12app.admin_dashboard_calculations_br12.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch12app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch12app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch12app.admin_dashboard_calculations_br12.total_collection_advance(),
        'total_discount': branch12app.admin_dashboard_calculations_br12.total_discount(),

        'total_colatable_amount': branch12app.admin_dashboard_calculations_br12.total_colatable_amount(),
        'total_collected_amount': branch12app.admin_dashboard_calculations_br12.total_collected_amount(),
        'total_due': branch12app.admin_dashboard_calculations_br12.total_due(),
        'l': branch12app.admin_dashboard_calculations_br12.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)


def details_branch13(request):
    a = branch13app.admin_dashboard_calculations_br13.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch13app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch13app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch13app.admin_dashboard_calculations_br13.total_collection_advance(),
        'total_discount': branch13app.admin_dashboard_calculations_br13.total_discount(),

        'total_colatable_amount': branch13app.admin_dashboard_calculations_br13.total_colatable_amount(),
        'total_collected_amount': branch13app.admin_dashboard_calculations_br13.total_collected_amount(),
        'total_due': branch13app.admin_dashboard_calculations_br13.total_due(),
        'l': branch13app.admin_dashboard_calculations_br13.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)


def details_branch14(request):
    a = branch14app.admin_dashboard_calculations_br14.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch14app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch14app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch14app.admin_dashboard_calculations_br14.total_collection_advance(),
        'total_discount': branch14app.admin_dashboard_calculations_br14.total_discount(),

        'total_colatable_amount': branch14app.admin_dashboard_calculations_br14.total_colatable_amount(),
        'total_collected_amount': branch14app.admin_dashboard_calculations_br14.total_collected_amount(),
        'total_due': branch14app.admin_dashboard_calculations_br14.total_due(),
        'l': branch14app.admin_dashboard_calculations_br14.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch15(request):
    a = branch15app.admin_dashboard_calculations_br15.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch15app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch15app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch15app.admin_dashboard_calculations_br15.total_collection_advance(),
        'total_discount': branch15app.admin_dashboard_calculations_br15.total_discount(),

        'total_colatable_amount': branch15app.admin_dashboard_calculations_br15.total_colatable_amount(),
        'total_collected_amount': branch15app.admin_dashboard_calculations_br15.total_collected_amount(),
        'total_due': branch15app.admin_dashboard_calculations_br15.total_due(),
        'l': branch15app.admin_dashboard_calculations_br15.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)

def details_branch16(request):
    a = branch16app.admin_dashboard_calculations_br16.grand_total_collection()
    from datetime import datetime
    cmm = datetime.now().month
    cm = cmm - 1
    gtc = a[cm]

    context = {
        'tc': branch16app.models.pg1_new_beds.objects.all().filter(flag=2),
        'vr': branch16app.models.pg1_new_beds.objects.all().exclude(flag=2).order_by('roon_no'),

        'grand_total_collection': gtc,
        'total_collection_advance': branch16app.admin_dashboard_calculations_br16.total_collection_advance(),
        'total_discount': branch16app.admin_dashboard_calculations_br16.total_discount(),

        'total_colatable_amount': branch16app.admin_dashboard_calculations_br16.total_colatable_amount(),
        'total_collected_amount': branch16app.admin_dashboard_calculations_br16.total_collected_amount(),
        'total_due': branch16app.admin_dashboard_calculations_br16.total_due(),
        'l': branch16app.admin_dashboard_calculations_br16.grand_total(),

    }
    return render(request,'admindashboard/admin_dashboard_reports/branch_details/details_branch.html',context)
