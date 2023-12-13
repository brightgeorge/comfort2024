from django.contrib import admin
from django.urls import path, include

from django.urls import path
from . import views
from . import admin_branch2

#from . import branch1
from . import branch2
from . import reports2
from . import payment2
from . import admin_dashboard_calculations_br2
from . import accounts2


d='test'

import myapp.userurls
import branch2app.b2userurls
name='_branch2'
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('pysql/', branch1.pysql, name='pysql' + d),

    #path('viewall_vacate_guest/',branch1.viewall_vacate_guest,name='viewall_vacate_guest'+name),
    #path('view_all_users/', views.view_all_users, name='view_all_users'),
    #path('view_all_room/', admin_branch2.view_all_room, name='view_all_room'),
    path('branch1_dashboard2/', branch2.branch1_dashboard2, name='branch1_dashboard2'),

    path('background2', branch2.background2, name='background2'),
    path('background_regi2', branch2.background_regi2, name='background_regi2'),
    path('custom_background_regi2', branch2.custom_background_regi2, name='custom_background_regi2'),


#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi2/',admin_branch2.branch1_room_create_regi2,name='branch1_room_create_regi2'),
    path('view_all_room2/',admin_branch2.view_all_room2,name='view_all_room2'),
    path('delete_room2/<id>',admin_branch2.delete_room2,name='delete_room2'),

    path('branch1_room_create2/',admin_branch2.branch1_room_create2,name='branch1_room_create2'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi2/', admin_branch2.pg1_bed_create_regi2, name='pg1_bed_create_regi2'),
    path('pg1_view_all_beds2/', admin_branch2.pg1_view_all_beds2, name='pg1_view_all_beds2'),
    path('delete_bed2/<id>', admin_branch2.delete_bed2, name='delete_bed2'),

    path('pg1_bed_create2/', admin_branch2.pg1_bed_create2, name='pg1_bed_create2'),

    path('single_pg1_bed_create_regi2/', admin_branch2.single_pg1_bed_create_regi2, name='single_pg1_bed_create_regi2'),
    path('update_bed_basic_details2/<id>', admin_branch2.update_bed_basic_details2, name='update_bed_basic_details2'),

    #bed creation end here

#guest
    path('br1_admit_guest2/<id>',branch2.br1_admit_guest2,name='br1_admit_guest2'),
    path('view_all_new_guest2/',branch2.view_all_new_guest2,name='view_all_new_guest2'),
    path('update_br1_admit_guest2/<id>',branch2.update_br1_admit_guest2,name='update_br1_admit_guest2'),
    path('vacate_br1_guest2/<id>',branch2.vacate_br1_guest2,name='vacate_br1_guest2'),

    path('active_guest_details2/<guest_code>',branch2.active_guest_details2,name='active_guest_details2'),
    path('view_all_guest2/',branch2.view_all_guest2,name='view_all_guest2'),
    path('shift_guest2/<id>',branch2.shift_guest2,name='shift_guest2'),
    path('shift_guest_regi2/',branch2.shift_guest_regi2,name='shift_guest_regi2'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
#guest end here



##################################
#PAYMENTS START HERE
################################

    path('choose_months2/',branch2.choose_months2,name='choose_months2'),

    path('jan2/',branch2.jan2,name='jan2'),
    path('jan_manke_payments2/<id>',branch2.jan_manke_payments2,name='jan_manke_payments2'),

    path('feb2/',branch2.feb2,name='feb2'),
    path('feb_manke_payments2/<id>',branch2.feb_manke_payments2,name='feb_manke_payments2'),

    path('march2/',branch2.march2,name='march2'),
    path('march_manke_payments2/<id>',branch2.march_manke_payments2,name='march_manke_payments2'),

    path('april2/',branch2.april2,name='april2'),
    path('april_make_payments2/<id>',branch2.april_make_payments2,name='april_make_payments2'),

    path('may2/',branch2.may2,name='may2'),
    path('may_make_payments2/<id>',branch2.may_make_payments2,name='may_make_payments2'),

    path('june2/',branch2.june2,name='june2'),
    path('june_make_payments2/<id>',branch2.june_make_payments2,name='june_make_payments2'),

    path('july2/',branch2.july2,name='july2'),
    path('july_make_payments2/<id>',branch2.july_make_payments2,name='july_make_payments2'),

    path('aug2/',branch2.aug2,name='aug2'),
    path('aug_make_payments2/<id>',branch2.aug_make_payments2,name='aug_make_payments2'),

    path('sept2/',branch2.sept2,name='sept2'),
    path('sept_make_payments2/<id>',branch2.sept_make_payments2,name='sept_make_payments2'),

    path('oct2/',branch2.oct2,name='oct2'),
    path('oct_make_payments2/<id>',branch2.oct_make_payments2,name='oct_make_payments2'),

    path('nov2/',branch2.nov2,name='nov2'),
    path('nov_make_payments2/<id>',branch2.nov_make_payments2,name='nov_make_payments2'),

    path('dec2/',branch2.dec2,name='dec2'),
    path('dec_make_payments2/<id>',branch2.dec_make_payments2,name='dec_make_payments2'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user2/', payment2.choose_user2, name='choose_user2'),
    path('payment_user_details2/<id>', payment2.payment_user_details2, name='payment_user_details2'),
    path('close_choose_user2/<id>', payment2.close_choose_user2, name='close_choose_user2'),

    path('monthly_jan_make_payments2/<id>', payment2.monthly_jan_make_payments2, name='monthly_jan_make_payments2'),
    path('monthly_feb_make_payments2/<id>', payment2.monthly_feb_make_payments2, name='monthly_feb_make_payments2'),
    path('monthly_march_make_payments2/<id>', payment2.monthly_march_make_payments2, name='monthly_march_make_payments2'),
    path('monthly_april_make_payments2/<id>', payment2.monthly_april_make_payments2, name='monthly_april_make_payments2'),
    path('monthly_may_make_payments2/<id>', payment2.monthly_may_make_payments2, name='monthly_may_make_payments2'),
    path('monthly_june_make_payments2/<id>', payment2.monthly_june_make_payments2, name='monthly_june_make_payments2'),

    path('monthly_july_make_payments2/<id>', payment2.monthly_july_make_payments2, name='monthly_july_make_payments2'),
    path('monthly_aug_make_payments2/<id>', payment2.monthly_aug_make_payments2, name='monthly_aug_make_payments2'),
    path('monthly_sept_make_payments2/<id>', payment2.monthly_sept_make_payments2, name='monthly_sept_make_payments2'),
    path('monthly_oct_make_payments2/<id>', payment2.monthly_oct_make_payments2, name='monthly_oct_make_payments2'),
    path('monthly_nov_make_payments2/<id>', payment2.monthly_nov_make_payments2, name='monthly_nov_make_payments2'),
    path('monthly_dec_make_payments2/<id>', payment2.monthly_dec_make_payments2, name='monthly_dec_make_payments2'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################

##################################
# _ADVANCE2 START HERE
################################

    path('choose_months_advance2/', branch2.choose_months_advance2, name='choose_months_advance2'),

    path('jan_advance2/', branch2.jan_advance2, name='jan_advance2'),
    path('jan_make_payments_advance2/<id>', branch2.jan_make_payments_advance2, name='jan_make_payments_advance2'),
    path('feb_advance2/', branch2.feb_advance2, name='feb_advance2'),
    path('feb_make_payments_advance2/<id>', branch2.feb_make_payments_advance2, name='feb_make_payments_advance2'),
    path('march_advance2/', branch2.march_advance2, name='march_advance2'),
    path('march_make_payments_advance2/<id>', branch2.march_make_payments_advance2,
         name='march_make_payments_advance2'),
    path('april_advance2/', branch2.april_advance2, name='april_advance2'),
    path('april_make_payments_advance2/<id>', branch2.april_make_payments_advance2,
         name='april_make_payments_advance2'),

    path('may_advance2/', branch2.may_advance2, name='may_advance2'),
    path('may_make_payments_advance2/<id>', branch2.may_make_payments_advance2, name='may_make_payments_advance2'),
    path('june_advance2/', branch2.june_advance2, name='june_advance2'),
    path('june_make_payments_advance2/<id>', branch2.june_make_payments_advance2, name='june_make_payments_advance2'),
    path('july_advance2/', branch2.july_advance2, name='july_advance2'),
    path('july_make_payments_advance2/<id>', branch2.july_make_payments_advance2, name='july_make_payments_advance2'),
    path('auguest_advance2/', branch2.auguest_advance2, name='auguest_advance2'),
    path('auguest_make_payments_advance2/<id>', branch2.auguest_make_payments_advance2,
         name='auguest_make_payments_advance2'),

    path('sept_advance2/', branch2.sept_advance2, name='sept_advance2'),
    path('sept_make_payments_advance2/<id>', branch2.sept_make_payments_advance2, name='sept_make_payments_advance2'),
    path('october_advance2/', branch2.october_advance2, name='october_advance2'),
    path('october_make_payments_advance2/<id>', branch2.october_make_payments_advance2,
         name='october_make_payments_advance2'),
    path('nov_advance2/', branch2.nov_advance2, name='nov_advance2'),
    path('nov_make_payments_advance2/<id>', branch2.nov_make_payments_advance2, name='nov_make_payments_advance2'),
    path('dec_advance2/', branch2.dec_advance2, name='dec_advance2'),
    path('dec_make_payments_advance2/<id>', branch2.dec_make_payments_advance2, name='dec_make_payments_advance2'),

##################################
# _ADVANCE2 END HERE
################################

#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months2/',branch2.unpaid_rent_choose_months2,name='unpaid_rent_choose_months2'),

    path('jan_unpaid_rent2/', branch2.jan_unpaid_rent2, name='jan_unpaid_rent2'),
    path('table_jan_unpaid_rent2/', branch2.table_jan_unpaid_rent2, name='table_jan_unpaid_rent2'),
    path('feb_unpaid_rent2/', branch2.feb_unpaid_rent2, name='feb_unpaid_rent2'),
    path('table_feb_unpaid_rent2/', branch2.table_feb_unpaid_rent2, name='table_feb_unpaid_rent2'),
    path('mar_unpaid_rent2/', branch2.mar_unpaid_rent2, name='mar_unpaid_rent2'),
    path('table_mar_unpaid_rent2/', branch2.table_mar_unpaid_rent2, name='table_mar_unpaid_rent2'),
    path('april_unpaid_rent2/', branch2.april_unpaid_rent2, name='april_unpaid_rent2'),
    path('table_april_unpaid_rent2/', branch2.table_april_unpaid_rent2, name='table_april_unpaid_rent2'),

    path('may_unpaid_rent2/', branch2.may_unpaid_rent2, name='may_unpaid_rent2'),
    path('table_may_unpaid_rent2/', branch2.table_may_unpaid_rent2, name='table_may_unpaid_rent2'),
    path('june_unpaid_rent2/', branch2.june_unpaid_rent2, name='june_unpaid_rent2'),
    path('table_june_unpaid_rent2/', branch2.table_june_unpaid_rent2, name='table_june_unpaid_rent2'),
    path('july_unpaid_rent2/', branch2.july_unpaid_rent2, name='july_unpaid_rent2'),
    path('table_july_unpaid_rent2',branch2.table_july_unpaid_rent2,name='table_july_unpaid_rent2'),
    path('aug_unpaid_rent2/', branch2.aug_unpaid_rent2, name='aug_unpaid_rent2'),
    path('table_aug_unpaid_rent2/',branch2.table_aug_unpaid_rent2,name='table_aug_unpaid_rent2'),

    path('sept_unpaid_rent2/', branch2.sept_unpaid_rent2, name='sept_unpaid_rent2'),
    path('table_sept_unpaid_rent2/', branch2.table_sept_unpaid_rent2, name='table_sept_unpaid_rent2'),
    path('oct_unpaid_rent2/', branch2.oct_unpaid_rent2, name='oct_unpaid_rent2'),
    path('table_oct_unpaid_rent2/', branch2.table_oct_unpaid_rent2, name='table_oct_unpaid_rent2'),
    path('nov_unpaid_rent2/', branch2.nov_unpaid_rent2, name='nov_unpaid_rent2'),
    path('table_nov_unpaid_rent2/', branch2.table_nov_unpaid_rent2, name='table_nov_unpaid_rent2'),
    path('dec_unpaid_rent2/', branch2.dec_unpaid_rent2, name='dec_unpaid_rent2'),
    path('table_dec_unpaid_rent2/', branch2.table_dec_unpaid_rent2, name='table_dec_unpaid_rent2'),

    path('details_of_unpaid_guests2/<id>',branch2.details_of_unpaid_guests2,name='details_of_unpaid_guests2'),

#unpaid rent end here



#paid rent start here

path('paid_rent_choose_months2/',branch2.paid_rent_choose_months2,name='paid_rent_choose_months2'),
path('partially_paid_guest_choose_months2/',reports2.partially_paid_guest_choose_months2,name='partially_paid_guest_choose_months2'),

path('jan_paid_rent2/', branch2.jan_paid_rent2, name='jan_paid_rent2'),
path('table_jan_paid_rent2/', branch2.table_jan_paid_rent2, name='table_jan_paid_rent2'),
path('jan_full_paid_guest2/', reports2.jan_full_paid_guest2, name='jan_full_paid_guest2'),
path('jan_partially_paid_guest2/', reports2.jan_partially_paid_guest2, name='jan_partially_paid_guest2'),
path('table_jan_partially_paid_guest2/', reports2.table_jan_partially_paid_guest2,name='table_jan_partially_paid_guest2'),

path('feb_paid_rent2/', branch2.feb_paid_rent2, name='feb_paid_rent2'),
path('table_feb_paid_rent2/', branch2.table_feb_paid_rent2, name='table_feb_paid_rent2'),
path('feb_full_paid_guest2/', reports2.feb_full_paid_guest2, name='feb_full_paid_guest2'),
path('feb_partially_paid_guest2/', reports2.feb_partially_paid_guest2, name='feb_partially_paid_guest2'),
path('table_feb_partially_paid_guest2/', reports2.table_feb_partially_paid_guest2,name='table_feb_partially_paid_guest2'),

path('mar_paid_rent2/', branch2.mar_paid_rent2, name='mar_paid_rent2'),
path('table_mar_paid_rent2/', branch2.table_mar_paid_rent2, name='table_mar_paid_rent2'),
path('march_full_paid_guest2/', reports2.march_full_paid_guest2, name='march_full_paid_guest2'),
path('march_partially_paid_guest2/', reports2.march_partially_paid_guest2, name='march_partially_paid_guest2'),
path('table_march_partially_paid_guest2/', reports2.table_march_partially_paid_guest2,name='table_march_partially_paid_guest2'),

path('april_paid_rent2/', branch2.april_paid_rent2, name='april_paid_rent2'),
path('table_april_paid_rent2/', branch2.table_april_paid_rent2, name='table_april_paid_rent2'),
path('april_full_paid_guest2/', reports2.april_full_paid_guest2, name='april_full_paid_guest2'),
path('april_partially_paid_guest2/', reports2.april_partially_paid_guest2, name='april_partially_paid_guest2'),
path('table_april_partially_paid_guest2/', reports2.table_april_partially_paid_guest2,name='table_april_partially_paid_guest2'),

path('may_paid_rent2/', branch2.may_paid_rent2, name='may_paid_rent2'),
path('table_may_paid_rent2/', branch2.table_may_paid_rent2, name='table_may_paid_rent2'),
path('may_full_paid_guest2/', reports2.may_full_paid_guest2, name='may_full_paid_guest2'),
path('may_partially_paid_guest2/', reports2.may_partially_paid_guest2, name='may_partially_paid_guest2'),
path('table_may_partially_paid_guest2/', reports2.table_may_partially_paid_guest2, name='table_may_partially_paid_guest2'),

path('june_paid_rent2/', branch2.june_paid_rent2, name='june_paid_rent2'),
path('table_june_paid_rent2/', branch2.table_june_paid_rent2, name='table_june_paid_rent2'),
path('june_full_paid_guest2/', reports2.june_full_paid_guest2, name='june_full_paid_guest2'),
path('june_partially_paid_guest2/', reports2.june_partially_paid_guest2, name='june_partially_paid_guest2'),
path('table_june_partially_paid_guest2/', reports2.table_june_partially_paid_guest2, name='table_june_partially_paid_guest2'),

path('july_paid_rent2/', branch2.july_paid_rent2, name='july_paid_rent2'),
path('table_july_paid_rent2/', branch2.table_july_paid_rent2, name='table_july_paid_rent2'),
path('july_full_paid_guest2/', reports2.july_full_paid_guest2, name='july_full_paid_guest2'),
path('july_partially_paid_guest2/', reports2.july_partially_paid_guest2, name='july_partially_paid_guest2'),
path('table_july_partially_paid_guest2/', reports2.table_july_partially_paid_guest2, name='table_july_partially_paid_guest2'),

path('aug_paid_rent2/', branch2.aug_paid_rent2, name='aug_paid_rent2'),
path('table_aug_paid_rent2/', branch2.table_aug_paid_rent2, name='table_aug_paid_rent2'),
path('auguest_full_paid_guest2/', reports2.auguest_full_paid_guest2, name='auguest_full_paid_guest2'),
path('auguest_partially_paid_guest2/', reports2.auguest_partially_paid_guest2,name='auguest_partially_paid_guest2'),
path('table_auguest_partially_paid_guest2/', reports2.table_auguest_partially_paid_guest2,name='table_auguest_partially_paid_guest2'),

path('sept_paid_rent2/', branch2.sept_paid_rent2, name='sept_paid_rent2'),
path('table_sept_paid_rent2/', branch2.table_sept_paid_rent2, name='table_sept_paid_rent2'),
path('sept_full_paid_guest2/', reports2.sept_full_paid_guest2, name='sept_full_paid_guest2'),
path('sept_partially_paid_guest2/', reports2.sept_partially_paid_guest2, name='sept_partially_paid_guest2'),
path('table_sept_partially_paid_guest2/', reports2.table_sept_partially_paid_guest2,name='table_sept_partially_paid_guest2'),

path('oct_paid_rent2/', branch2.oct_paid_rent2, name='oct_paid_rent2'),
path('table_oct_paid_rent2/', branch2.table_oct_paid_rent2, name='table_oct_paid_rent2'),
path('october_full_paid_guest2/', reports2.october_full_paid_guest2, name='october_full_paid_guest2'),
path('october_partially_paid_guest2/', reports2.october_partially_paid_guest2,name='october_partially_paid_guest2'),
path('table_october_partially_paid_guest2/', reports2.table_october_partially_paid_guest2,name='table_october_partially_paid_guest2'),

path('nov_paid_rent2/', branch2.nov_paid_rent2, name='nov_paid_rent2'),
path('table_nov_paid_rent2/', branch2.table_nov_paid_rent2, name='table_nov_paid_rent2'),
path('nov_full_paid_guest2/', reports2.nov_full_paid_guest2, name='nov_full_paid_guest2'),
path('nov_partially_paid_guest2/', reports2.nov_partially_paid_guest2, name='nov_partially_paid_guest2'),
path('table_nov_partially_paid_guest2/', reports2.table_nov_partially_paid_guest2,name='table_nov_partially_paid_guest2'),

path('dec_paid_rent2/', branch2.dec_paid_rent2, name='dec_paid_rent2'),
path('table_dec_paid_rent2/', branch2.table_dec_paid_rent2, name='table_dec_paid_rent2'),
path('dec_full_paid_guest2/', reports2.dec_full_paid_guest2, name='dec_full_paid_guest2'),
path('dec_partially_paid_guest2/', reports2.dec_partially_paid_guest2, name='dec_partially_paid_guest2'),
path('table_dec_partially_paid_guest2/', reports2.table_dec_partially_paid_guest2,name='table_dec_partially_paid_guest2'),

path('details_of_paid_guests2/<id>',branch2.details_of_paid_guests2,name='details_of_paid_guests2'),
path('full_paid_guest2/',reports2.full_paid_guest2,name='full_paid_guest2'),


#paid rent end here



#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest2/',branch2.viewall_vacate_guest2,name='viewall_vacate_guest2'),
    path('details_of_vacate_guest2/<id>',branch2.details_of_vacate_guest2,name='details_of_vacate_guest2'),
    path('full_vacated_guest_details2',branch2.full_vacated_guest_details2,name='full_vacated_guest_details2'),
    path('full_vacated_guest_table2',branch2.full_vacated_guest_table2,name='full_vacated_guest_table2'),

    path('guest_details2/<guest_code>', branch2.guest_details2, name='guest_details2'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate2/<id>', branch2.jan_manke_payments_vacate2, name='jan_manke_payments_vacate2'),
    path('feb_manke_payments_vacate2/<id>', branch2.feb_manke_payments_vacate2, name='feb_manke_payments_vacate2'),
    path('march_manke_payments_vacate2/<id>', branch2.march_manke_payments_vacate2, name='march_manke_payments_vacate2'),
    path('april_make_payments_vacate2/<id>', branch2.april_make_payments_vacate2, name='april_make_payments_vacate2'),

    path('may_make_payments_vacate2/<id>', branch2.may_make_payments_vacate2, name='may_make_payments_vacate2'),
    path('june_make_payments_vacate2/<id>', branch2.june_make_payments_vacate2, name='june_make_payments_vacate2'),
    path('july_make_payments_vacate2/<id>', branch2.july_make_payments_vacate2, name='july_make_payments_vacate2'),
    path('aug_make_payments_vacate2/<id>', branch2.aug_make_payments_vacate2, name='aug_make_payments_vacate2'),

    path('sept_make_payments_vacate2/<id>', branch2.sept_make_payments_vacate2, name='sept_make_payments_vacate2'),
    path('oct_make_payments_vacate2/<id>', branch2.oct_make_payments_vacate2, name='oct_make_payments_vacate2'),
    path('nov_make_payments_vacate2/<id>', branch2.nov_make_payments_vacate2, name='nov_make_payments_vacate2'),
    path('dec_make_payments_vacate2/<id>', branch2.dec_make_payments_vacate2, name='dec_make_payments_vacate2'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################



##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general2/',branch2.detail_guest_general2,name='detail_guest_general2'),

    path('jan_print2/',branch2.jan_print2,name='jan_print2'),
    path('feb_print2/',branch2.feb_print2,name='feb_print2'),
    path('march_print2/',branch2.march_print2,name='march_print2'),
    path('april_print2/',branch2.april_print2,name='april_print2'),

    path('may_print2/',branch2.may_print2,name='may_print2'),
    path('june_print2/',branch2.june_print2,name='june_print2'),
    path('july_print2/', branch2.july_print2, name='july_print2'),
    path('aug_print2/', branch2.aug_print2, name='aug_print2'),

    path('sept_print2/', branch2.sept_print2, name='sept_print2'),
    path('oct_print2/', branch2.oct_print2, name='oct_print2'),
    path('nov_print2/', branch2.nov_print2, name='nov_print2'),
    path('dec_print2/', branch2.dec_print2, name='dec_print2'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close2/', branch2.jan_close2, name='jan_close2'),
    path('jan_close_decision_page2/', branch2.jan_close_decision_page2, name='jan_close_decision_page2'),
    path('feb_close/', branch2.feb_close2, name='feb_close2'),
    path('feb_close_decision_page2/', branch2.feb_close_decision_page2, name='feb_close_decision_page2'),
    path('mar_close2/', branch2.mar_close2, name='mar_close2'),
    path('mar_close_decision_page/', branch2.mar_close_decision_page2, name='mar_close_decision_page2'),
    path('apr_close2/', branch2.apr_close2, name='apr_close2'),
    path('apr_close_decision_page2/', branch2.apr_close_decision_page2, name='apr_close_decision_page2'),

    path('may_close2/', branch2.may_close2, name='may_close2'),
    path('may_close_decision_page2/', branch2.may_close_decision_page2, name='may_close_decision_page2'),
    path('jun_close2/', branch2.jun_close2, name='jun_close2'),
    path('jun_close_decision_page2/', branch2.jun_close_decision_page2, name='jun_close_decision_page2'),
    path('jul_close2/', branch2.jul_close2, name='jul_close2'),
    path('jul_close_decision_page2/', branch2.jul_close_decision_page2, name='jul_close_decision_page2'),
    path('aug_close2/', branch2.aug_close2, name='aug_close2'),
    path('aug_close_decision_page2/', branch2.aug_close_decision_page2, name='aug_close_decision_page2'),

    path('sep_close2/', branch2.sep_close2, name='sep_close2'),
    path('sep_close_decision_page2/', branch2.sep_close_decision_page2, name='sep_close_decision_page2'),
    path('oct_close2/', branch2.oct_close2, name='oct_close2'),
    path('oct_close_decision_page2/', branch2.oct_close_decision_page2, name='oct_close_decision_page2'),
    path('nov_close2/', branch2.nov_close2, name='nov_close2'),
    path('nov_close_decision_page2/', branch2.nov_close_decision_page2, name='nov_close_decision_page2'),

########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months2/', reports2.detailed_report_choose_months2,name='detailed_report_choose_months2'),

    path('jan_details_live2/', reports2.jan_details_live2, name='jan_details_live2'),
    path('jan_print_live2/', reports2.jan_print_live2, name='jan_print_live2'),
    path('feb_details_live2/', reports2.feb_details_live2, name='feb_details_live2'),
    path('feb_print_live2/', reports2.feb_print_live2, name='feb_print_live2'),
    path('march_details_live2/', reports2.march_details_live2, name='march_details_live2'),
    path('march_print_live2/', reports2.march_print_live2, name='march_print_live2'),

    path('april_details_live2/', reports2.april_details_live2, name='april_details_live2'),
    path('april_print_live2/', reports2.april_print_live2, name='april_print_live2'),
    path('may_details_live2/', reports2.may_details_live2, name='may_details_live2'),
    path('may_print_live2/', reports2.may_print_live2, name='may_print_live2'),
    path('june_details_live2/', reports2.june_details_live2, name='june_details_live2'),
    path('june_print_live2/', reports2.june_print_live2, name='june_print_live2'),

    path('july_details_live2/', reports2.july_details_live2, name='july_details_live2'),
    path('july_print_live2/', reports2.july_print_live2, name='july_print_live2'),
    path('auguest_details_live2/', reports2.auguest_details_live2, name='auguest_details_live2'),
    path('auguest_print_live2/', reports2.auguest_print_live2, name='auguest_print_live2'),
    path('sept_details_live2/', reports2.sept_details_live2, name='sept_details_live2'),
    path('sept_print_live2/', reports2.sept_print_live2, name='sept_print_live2'),

    path('october_details_live2/', reports2.october_details_live2, name='october_details_live2'),
    path('october_print_live2/', reports2.october_print_live2, name='october_print_live2'),
    path('nov_details_live2/', reports2.nov_details_live2, name='nov_details_live2'),
    path('nov_print_live2/', reports2.nov_print_live2, name='nov_print_live2'),
    path('dec_details_live2/', reports2.dec_details_live2, name='dec_details_live2'),
    path('dec_print_live2/', reports2.dec_print_live2, name='dec_print_live2'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room2/', reports2.viewall_vaccant_room2, name='viewall_vaccant_room2'),



########################################
# DUE AMT MANAGEMENT START HERE
###########################

path('view_all_due_amt2/', branch2.view_all_due_amt2, name='view_all_due_amt2'),
path('due_amt_mgt_choose_months2/', branch2.due_amt_mgt_choose_months2, name='due_amt_mgt_choose_months2'),

path('view_jan_account_details2/', branch2.view_jan_account_details2, name='view_jan_account_details2'),
path('jan_account_mgt2/<id>',branch2.jan_account_mgt2,name='jan_account_mgt2'),
path('view_feb_account_details2/', branch2.view_feb_account_details2, name='view_feb_account_details2'),
path('feb_account_mgt2/<id>',branch2.feb_account_mgt2,name='feb_account_mgt2'),
path('view_march_account_details2/', branch2.view_march_account_details2, name='view_march_account_details2'),
path('march_account_mgt2/<id>',branch2.march_account_mgt2,name='march_account_mgt2'),
path('view_april_account_details2/', branch2.view_april_account_details2, name='view_april_account_details2'),
path('april_account_mgt2/<id>',branch2.april_account_mgt2,name='april_account_mgt2'),

path('view_may_account_details2/',branch2.view_may_account_details2,name='view_may_account_details2'),
path('may_account_mgt2/<id>', branch2.may_account_mgt2, name='may_account_mgt2'),
path('view_june_account_details2/', branch2.view_june_account_details2, name='view_june_account_details2'),
path('june_account_mgt2/<id>',branch2.june_account_mgt2,name='june_account_mgt2'),
path('view_july_account_details2/', branch2.view_july_account_details2, name='view_july_account_details2'),
path('july_account_mgt2/<id>',branch2.july_account_mgt2,name='july_account_mgt2'),
path('view_auguest_account_details2/', branch2.view_auguest_account_details2, name='view_auguest_account_details2'),
path('auguest_account_mgt2/<id>',branch2.auguest_account_mgt2,name='auguest_account_mgt2'),

path('view_sept_account_details2/', branch2.view_sept_account_details2, name='view_sept_account_details2'),
path('sept_account_mgt2/<id>',branch2.sept_account_mgt2,name='sept_account_mgt2'),
path('view_october_account_details2/', branch2.view_october_account_details2, name='view_october_account_details2'),
path('october_account_mgt2/<id>',branch2.october_account_mgt2,name='october_account_mgt2'),
path('view_nov_account_details2/', branch2.view_nov_account_details2, name='view_nov_account_details2'),
path('nov_account_mgt2/<id>',branch2.nov_account_mgt2,name='nov_account_mgt2'),
path('view_dec_account_details2/', branch2.view_dec_account_details2, name='view_dec_account_details2'),
path('dec_account_mgt2/<id>',branch2.dec_account_mgt2,name='dec_account_mgt2'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due2', admin_dashboard_calculations_br2.monthly_details_due2, name='monthly_details_due2'),
    path('monthly_collection_details2/', admin_dashboard_calculations_br2.monthly_collection_details2, name='monthly_collection_details2'),

########################################
# DASHBOARD REPORTS END HERE
###########################






#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category2/', accounts2.view_all_category2, name='view_all_category2'),
    path('create_new_category2/', accounts2.create_new_category2, name='create_new_category2'),
    path('regi_new_category2/', accounts2.regi_new_category2, name='regi_new_category2'),
    path('update_category2/<id>',accounts2.update_category2,name='update_category2'),

    path('delete_category2/<id>', accounts2.delete_category2, name='delete_category2'),
    path('view_all_category_delete2/', accounts2.view_all_category_delete2, name='view_all_category_delete2'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items2/', accounts2.view_all_items2, name='view_all_items2'),
    path('create_new_item2/', accounts2.create_new_item2, name='create_new_item2'),
    path('regi_new_item2/', accounts2.regi_new_item2, name='regi_new_item2'),
    path('delete_item2/<id>',accounts2.delete_item2,name='delete_item2'),
    path('update_item2/<id>', accounts2.update_item2, name='update_item2'),
    path('view_all_items_delete2/',accounts2.view_all_items_delete2,name='view_all_items_delete2'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger2/', accounts2.view_all_ledger2, name='view_all_ledger2'),
    path('create_new_ledger2/', accounts2.create_new_ledger2, name='create_new_ledger2'),
    path('regi_new_ledger2/', accounts2.regi_new_ledger2, name='regi_new_ledger2'),
    path('delete_ledger2/<id>',accounts2.delete_ledger2,name='delete_ledger2'),
    path('update_ledger2/<id>',accounts2.update_ledger2,name='update_ledger2'),
    path('view_all_ledger_delete2/',accounts2.view_all_ledger_delete2,name='view_all_ledger_delete2'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book2/', accounts2.view_all_accounts_book2, name='view_all_accounts_book2'),
    path('create_new_accounts_book2/', accounts2.create_new_accounts_book2, name='create_new_accounts_book2'),
    path('regi_new_accounts_book2/', accounts2.regi_new_accounts_book2, name='regi_new_accounts_book2'),
    path('update_accounts_book2/<id>',accounts2.update_accounts_book2,name='update_accounts_book2'),
    path('delete_accounts_book2/<id>',accounts2.delete_accounts_book2,name='delete_accounts_book2'),
    path('view_all_accounts_book_delete2/',accounts2.view_all_accounts_book_delete2,name='view_all_accounts_book_delete2'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries2/', accounts2.get_countries2, name='get_countries2'),

    path('in_exp_items_entry2/', accounts2.in_exp_items_entry2, name='in_exp_items_entry2'),
    path('reg_in_exp_items_entry2/', accounts2.reg_in_exp_items_entry2, name='reg_in_exp_items_entry2'),
    path('delete_journal2/<id>',accounts2.delete_journal2,name='delete_journal2'),
    path('update_in_exp_items_entry2/<id>',accounts2.update_in_exp_items_entry2,name='update_in_exp_items_entry2'),
    path('detailed_journal_report2/',accounts2.detailed_journal_report2,name='detailed_journal_report2'),
    path('journal_report_deleted2/',accounts2.journal_report_deleted2,name='journal_report_deleted2'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise2/', accounts2.daily_category_wise2, name='daily_category_wise2'),
    path('monthly_category_based_reports2/',accounts2.monthly_category_based_reports2,name='monthly_category_based_reports2'),
    path('yearly_category_based_reports2/', accounts2.yearly_category_based_reports2,name='yearly_category_based_reports2'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed2/', accounts2.daily_detailed2, name='daily_detailed2'),
    path('monthly_detailed2/',accounts2.monthly_detailed2,name='monthly_detailed2'),
    path('yearly_detailed2/',accounts2.yearly_detailed2,name='yearly_detailed2'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports2/', accounts2.item_based_reports2, name='item_based_reports2'),
    path('daily_item_based_reports2/',accounts2.daily_item_based_reports2,name='daily_item_based_reports2'),
    path('monthly_item_based_reports2/',accounts2.monthly_item_based_reports2,name='monthly_item_based_reports2'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports2/', accounts2.ledger_based_reports2, name='ledger_based_reports2'),
    path('monthly_ledger_based_reports2/', accounts2.monthly_ledger_based_reports2, name='monthly_ledger_based_reports2'),
    path('daily_ledger_based_reports2/',accounts2.daily_ledger_based_reports2,name='daily_ledger_based_reports2'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports2/', accounts2.accounts_book_based_reports2, name='accounts_book_based_reports2'),
    path('daily_accounts_book_based_reports2/',accounts2.daily_accounts_book_based_reports2,name='daily_accounts_book_based_reports2'),
    path('monthly_accounts_book_based_reports2/',accounts2.monthly_accounts_book_based_reports2,name='monthly_accounts_book_based_reports2'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months2/', accounts2.monthly_reports_choose_months2, name='monthly_reports_choose_months2'),
    path('monthly_detailed_daily_in_exp_items_report2/<mo>',accounts2.monthly_detailed_daily_in_exp_items_report2,name='monthly_detailed_daily_in_exp_items_report2'),

    path('single_monthly_reports_choose_months2/', accounts2.single_monthly_reports_choose_months2,name='single_monthly_reports_choose_months2'),
    path('single_monthly_daily_in_exp_items_report2/<mo>',accounts2.single_monthly_daily_in_exp_items_report2,name='single_monthly_daily_in_exp_items_report2'),

    path('accounts_dash_board2/',accounts2.accounts_dash_board2,name='accounts_dash_board2'),



    path('profit_sharing_choose_months2', accounts2.profit_sharing_choose_months2, name='profit_sharing_choose_months2'),
    path('profit_sharing2/<mo>',accounts2.profit_sharing2,name='profit_sharing2'),
    path('view_share_holders2',accounts2.view_share_holders2,name='view_share_holders2'),
    path('create_share_holders2',accounts2.create_share_holders2,name='create_share_holders2'),
    path('regi_share_holders2', accounts2.regi_share_holders2, name='regi_share_holders2'),
    path('update_share_holders2/<id>',accounts2.update_share_holders2,name='update_share_holders2'),
    path('delete_share_holders2/<id>', accounts2.delete_share_holders2, name='delete_share_holders2'),
    path('view_deleted_share_holders2', accounts2.view_deleted_share_holders2, name='view_deleted_share_holders2'),




]