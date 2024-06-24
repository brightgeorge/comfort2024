from django.contrib import admin
from django.urls import path, include

from . import admin_branch4
from . import branch4
from . import reports4
from . import payment4
from . import admin_dashboard_calculations_br4
from . import accounts4

urlpatterns = [

    path('branch1_dashboard4/', branch4.branch1_dashboard4, name='branch1_dashboard4'),
    path('user_dashboard_calculations_ob_ch4/',branch4.user_dashboard_calculations_ob_ch4,name='user_dashboard_calculations_ob_ch4'),
    path('monthly_details_due4', admin_dashboard_calculations_br4.monthly_details_due4, name='monthly_details_due4'),

    path('background4', branch4.background4, name='background4'),
    path('background_regi4', branch4.background_regi4, name='background_regi4'),
    path('custom_background_regi4', branch4.custom_background_regi4, name='custom_background_regi4'),

    #**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi4/',admin_branch4.branch1_room_create_regi4,name='branch1_room_create_regi4'),
    path('view_all_room4/',admin_branch4.view_all_room4,name='view_all_room4'),
    path('delete_room4/<id>',admin_branch4.delete_room4,name='delete_room4'),

    path('branch1_room_create4/',admin_branch4.branch1_room_create4,name='branch1_room_create4'),

    path('multiple_branch1_room_create_regi4/',admin_branch4.multiple_branch1_room_create_regi4,name='multiple_branch1_room_create_regi4'),

#**room creation end here


#bed creation start here

    path('pg1_bed_create_regi4/', admin_branch4.pg1_bed_create_regi4, name='pg1_bed_create_regi4'),
    path('pg1_view_all_beds4/', admin_branch4.pg1_view_all_beds4, name='pg1_view_all_beds4'),
    path('delete_bed4/<id>', admin_branch4.delete_bed4, name='delete_bed4'),

    path('pg1_bed_create4/', admin_branch4.pg1_bed_create4, name='pg1_bed_create4'),

    path('update_bed_basic_details4/<id>', admin_branch4.update_bed_basic_details4, name='update_bed_basic_details4'),
    path('single_pg1_bed_create_regi4', admin_branch4.single_pg1_bed_create_regi4, name='single_pg1_bed_create_regi4'),

    path('multiple_single_pg1_bed_create_regi4/',admin_branch4.multiple_single_pg1_bed_create_regi4,name='multiple_single_pg1_bed_create_regi4'),

#bed creation end here

#guest
    path('br1_admit_guest4/<id>',branch4.br1_admit_guest4,name='br1_admit_guest4'),
    path('view_all_new_guest4/',branch4.view_all_new_guest4,name='view_all_new_guest4'),
    path('update_br1_admit_guest4/<id>',branch4.update_br1_admit_guest4,name='update_br1_admit_guest4'),
    path('vacate_br1_guest4/<id>',branch4.vacate_br1_guest4,name='vacate_br1_guest4'),

    path('active_guest_details4/<guest_code>',branch4.active_guest_details4,name='active_guest_details4'),
    path('view_all_guest4/',branch4.view_all_guest4,name='view_all_guest4'),
    path('shift_guest4/<id>',branch4.shift_guest4,name='shift_guest4'),
    path('shift_guest_regi4/',branch4.shift_guest_regi4,name='shift_guest_regi4'),
    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('multiple_br1_admit_guest4/<id>',branch4.multiple_br1_admit_guest4,name='multiple_br1_admit_guest4'),

#guest end here


##################################
#_ADVANCE4 START HERE
################################


path('choose_months_advance4/',branch4.choose_months_advance4,name='choose_months_advance4'),

path('jan_advance4/', branch4.jan_advance4, name='jan_advance4'),
path('jan_make_payments_advance4/<id>', branch4.jan_make_payments_advance4,name='jan_make_payments_advance4'),
path('feb_advance4/', branch4.feb_advance4, name='feb_advance4'),
path('feb_make_payments_advance4/<id>', branch4.feb_make_payments_advance4,name='feb_make_payments_advance4'),
path('march_advance4/', branch4.march_advance4, name='march_advance4'),
path('march_make_payments_advance4/<id>', branch4.march_make_payments_advance4,name='march_make_payments_advance4'),
path('april_advance4/', branch4.april_advance4, name='april_advance4'),
path('april_make_payments_advance4/<id>', branch4.april_make_payments_advance4, name='april_make_payments_advance4'),

path('may_advance4/',branch4.may_advance4,name='may_advance4'),
path('may_make_payments_advance4/<id>', branch4.may_make_payments_advance4, name='may_make_payments_advance4'),
path('june_advance4/',branch4.june_advance4,name='june_advance4'),
path('june_make_payments_advance4/<id>', branch4.june_make_payments_advance4, name='june_make_payments_advance4'),
path('july_advance4/',branch4.july_advance4,name='july_advance4'),
path('july_make_payments_advance4/<id>', branch4.july_make_payments_advance4, name='july_make_payments_advance4'),
path('auguest_advance4/', branch4.auguest_advance4, name='auguest_advance4'),
path('auguest_make_payments_advance4/<id>', branch4.auguest_make_payments_advance4, name='auguest_make_payments_advance4'),

path('sept_advance4/', branch4.sept_advance4, name='sept_advance4'),
path('sept_make_payments_advance4/<id>', branch4.sept_make_payments_advance4,name='sept_make_payments_advance4'),
path('october_advance4/', branch4.october_advance4, name='october_advance4'),
path('october_make_payments_advance4/<id>', branch4.october_make_payments_advance4, name='october_make_payments_advance4'),
path('nov_advance4/', branch4.nov_advance4, name='nov_advance4'),
path('nov_make_payments_advance4/<id>', branch4.nov_make_payments_advance4,name='nov_make_payments_advance4'),
path('dec_advance4/', branch4.dec_advance4, name='dec_advance4'),
path('dec_make_payments_advance4/<id>', branch4.dec_make_payments_advance4, name='dec_make_payments_advance4'),



##################################
#_ADVANCE4 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months4/',branch4.choose_months4,name='choose_months4'),

    path('jan4/',branch4.jan4,name='jan4'),
    path('jan_manke_payments4/<id>',branch4.jan_manke_payments4,name='jan_manke_payments4'),

    path('feb4/',branch4.feb4,name='feb4'),
    path('feb_manke_payments4/<id>',branch4.feb_manke_payments4,name='feb_manke_payments4'),

    path('march4/',branch4.march4,name='march4'),
    path('march_manke_payments4/<id>',branch4.march_manke_payments4,name='march_manke_payments4'),

    path('april4/',branch4.april4,name='april4'),
    path('april_make_payments4/<id>',branch4.april_make_payments4,name='april_make_payments4'),

    path('may4/',branch4.may4,name='may4'),
    path('may_make_payments4/<id>',branch4.may_make_payments4,name='may_make_payments4'),

    path('june4/',branch4.june4,name='june4'),
    path('june_make_payments4/<id>',branch4.june_make_payments4,name='june_make_payments4'),

    path('july4/',branch4.july4,name='july4'),
    path('july_make_payments4/<id>',branch4.july_make_payments4,name='july_make_payments4'),

    path('aug4/',branch4.aug4,name='aug4'),
    path('aug_make_payments4/<id>',branch4.aug_make_payments4,name='aug_make_payments4'),

    path('sept4/',branch4.sept4,name='sept4'),
    path('sept_make_payments4/<id>',branch4.sept_make_payments4,name='sept_make_payments4'),

    path('oct4/',branch4.oct4,name='oct4'),
    path('oct_make_payments4/<id>',branch4.oct_make_payments4,name='oct_make_payments4'),

    path('nov4/',branch4.nov4,name='nov4'),
    path('nov_make_payments4/<id>',branch4.nov_make_payments4,name='nov_make_payments4'),

    path('dec4/',branch4.dec4,name='dec4'),
    path('dec_make_payments4/<id>',branch4.dec_make_payments4,name='dec_make_payments4'),

##################################
#PAYMENTS END HERE
################################


##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user4/', payment4.choose_user4, name='choose_user4'),
    path('payment_user_details4/<id>', payment4.payment_user_details4, name='payment_user_details4'),
    path('close_choose_user4/<id>', payment4.close_choose_user4, name='close_choose_user4'),

    path('monthly_jan_make_payments4/<id>', payment4.monthly_jan_make_payments4, name='monthly_jan_make_payments4'),
    path('monthly_feb_make_payments4/<id>', payment4.monthly_feb_make_payments4, name='monthly_feb_make_payments4'),
    path('monthly_march_make_payments4/<id>', payment4.monthly_march_make_payments4, name='monthly_march_make_payments4'),
    path('monthly_april_make_payments4/<id>', payment4.monthly_april_make_payments4, name='monthly_april_make_payments4'),
    path('monthly_may_make_payments4/<id>', payment4.monthly_may_make_payments4, name='monthly_may_make_payments4'),
    path('monthly_june_make_payments4/<id>', payment4.monthly_june_make_payments4, name='monthly_june_make_payments4'),

    path('monthly_july_make_payments4/<id>', payment4.monthly_july_make_payments4, name='monthly_july_make_payments4'),
    path('monthly_aug_make_payments4/<id>', payment4.monthly_aug_make_payments4, name='monthly_aug_make_payments4'),
    path('monthly_sept_make_payments4/<id>', payment4.monthly_sept_make_payments4, name='monthly_sept_make_payments4'),
    path('monthly_oct_make_payments4/<id>', payment4.monthly_oct_make_payments4, name='monthly_oct_make_payments4'),
    path('monthly_nov_make_payments4/<id>', payment4.monthly_nov_make_payments4, name='monthly_nov_make_payments4'),
    path('monthly_dec_make_payments4/<id>', payment4.monthly_dec_make_payments4, name='monthly_dec_make_payments4'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################




#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months4/',branch4.unpaid_rent_choose_months4,name='unpaid_rent_choose_months4'),

    path('jan_unpaid_rent4/', branch4.jan_unpaid_rent4, name='jan_unpaid_rent4'),
    path('table_jan_unpaid_rent4/', branch4.table_jan_unpaid_rent4, name='table_jan_unpaid_rent4'),
    path('feb_unpaid_rent4/', branch4.feb_unpaid_rent4, name='feb_unpaid_rent4'),
    path('table_feb_unpaid_rent4/', branch4.table_feb_unpaid_rent4, name='table_feb_unpaid_rent4'),
    path('mar_unpaid_rent4/', branch4.mar_unpaid_rent4, name='mar_unpaid_rent4'),
    path('table_mar_unpaid_rent4/', branch4.table_mar_unpaid_rent4, name='table_mar_unpaid_rent4'),
    path('april_unpaid_rent4/', branch4.april_unpaid_rent4, name='april_unpaid_rent4'),
    path('table_april_unpaid_rent4/', branch4.table_april_unpaid_rent4, name='table_april_unpaid_rent4'),

    path('may_unpaid_rent4/', branch4.may_unpaid_rent4, name='may_unpaid_rent4'),
    path('table_may_unpaid_rent4/', branch4.table_may_unpaid_rent4, name='table_may_unpaid_rent4'),
    path('june_unpaid_rent4/', branch4.june_unpaid_rent4, name='june_unpaid_rent4'),
    path('table_june_unpaid_rent4/', branch4.table_june_unpaid_rent4, name='table_june_unpaid_rent4'),
    path('july_unpaid_rent4/', branch4.july_unpaid_rent4, name='july_unpaid_rent4'),
    path('table_july_unpaid_rent4',branch4.table_july_unpaid_rent4,name='table_july_unpaid_rent4'),
    path('aug_unpaid_rent4/', branch4.aug_unpaid_rent4, name='aug_unpaid_rent4'),
    path('table_aug_unpaid_rent4/',branch4.table_aug_unpaid_rent4,name='table_aug_unpaid_rent4'),

    path('sept_unpaid_rent4/', branch4.sept_unpaid_rent4, name='sept_unpaid_rent4'),
    path('table_sept_unpaid_rent4/', branch4.table_sept_unpaid_rent4, name='table_sept_unpaid_rent4'),
    path('oct_unpaid_rent4/', branch4.oct_unpaid_rent4, name='oct_unpaid_rent4'),
    path('table_oct_unpaid_rent4/', branch4.table_oct_unpaid_rent4, name='table_oct_unpaid_rent4'),
    path('nov_unpaid_rent4/', branch4.nov_unpaid_rent4, name='nov_unpaid_rent4'),
    path('table_nov_unpaid_rent4/', branch4.table_nov_unpaid_rent4, name='table_nov_unpaid_rent4'),
    path('dec_unpaid_rent4/', branch4.dec_unpaid_rent4, name='dec_unpaid_rent4'),
    path('table_dec_unpaid_rent4/', branch4.table_dec_unpaid_rent4, name='table_dec_unpaid_rent4'),



    path('details_of_unpaid_guests4/<id>',branch4.details_of_unpaid_guests4,name='details_of_unpaid_guests4'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months4/',branch4.paid_rent_choose_months4,name='paid_rent_choose_months4'),
    path('partially_paid_guest_choose_months4/',reports4.partially_paid_guest_choose_months4,name='partially_paid_guest_choose_months4'),

    path('jan_paid_rent4/', branch4.jan_paid_rent4, name='jan_paid_rent4'),
    path('table_jan_paid_rent4/', branch4.table_jan_paid_rent4, name='table_jan_paid_rent4'),
    path('jan_full_paid_guest4/', reports4.jan_full_paid_guest4, name='jan_full_paid_guest4'),
    path('jan_partially_paid_guest4/', reports4.jan_partially_paid_guest4, name='jan_partially_paid_guest4'),
    path('table_jan_partially_paid_guest4/', reports4.table_jan_partially_paid_guest4,name='table_jan_partially_paid_guest4'),

    path('feb_paid_rent4/', branch4.feb_paid_rent4, name='feb_paid_rent4'),
    path('table_feb_paid_rent4/', branch4.table_feb_paid_rent4, name='table_feb_paid_rent4'),
    path('feb_full_paid_guest4/', reports4.feb_full_paid_guest4, name='feb_full_paid_guest4'),
    path('feb_partially_paid_guest4/', reports4.feb_partially_paid_guest4, name='feb_partially_paid_guest4'),
    path('table_feb_partially_paid_guest4/', reports4.table_feb_partially_paid_guest4,name='table_feb_partially_paid_guest4'),

    path('mar_paid_rent4/', branch4.mar_paid_rent4, name='mar_paid_rent4'),
    path('table_mar_paid_rent4/', branch4.table_mar_paid_rent4, name='table_mar_paid_rent4'),
    path('march_full_paid_guest4/', reports4.march_full_paid_guest4, name='march_full_paid_guest4'),
    path('march_partially_paid_guest4/', reports4.march_partially_paid_guest4, name='march_partially_paid_guest4'),
    path('table_march_partially_paid_guest4/', reports4.table_march_partially_paid_guest4,name='table_march_partially_paid_guest4'),

    path('april_paid_rent4/', branch4.april_paid_rent4, name='april_paid_rent4'),
    path('table_april_paid_rent4/', branch4.table_april_paid_rent4, name='table_april_paid_rent4'),
    path('april_full_paid_guest4/', reports4.april_full_paid_guest4, name='april_full_paid_guest4'),
    path('april_partially_paid_guest4/', reports4.april_partially_paid_guest4, name='april_partially_paid_guest4'),
    path('table_april_partially_paid_guest4/', reports4.table_april_partially_paid_guest4,name='table_april_partially_paid_guest4'),

    path('may_paid_rent4/', branch4.may_paid_rent4, name='may_paid_rent4'),
    path('table_may_paid_rent4/', branch4.table_may_paid_rent4, name='table_may_paid_rent4'),
    path('may_full_paid_guest4/', reports4.may_full_paid_guest4, name='may_full_paid_guest4'),
    path('may_partially_paid_guest4/', reports4.may_partially_paid_guest4, name='may_partially_paid_guest4'),
    path('table_may_partially_paid_guest4/', reports4.table_may_partially_paid_guest4, name='table_may_partially_paid_guest4'),

    path('june_paid_rent4/', branch4.june_paid_rent4, name='june_paid_rent4'),
    path('table_june_paid_rent4/', branch4.table_june_paid_rent4, name='table_june_paid_rent4'),
    path('june_full_paid_guest4/', reports4.june_full_paid_guest4, name='june_full_paid_guest4'),
    path('june_partially_paid_guest4/', reports4.june_partially_paid_guest4, name='june_partially_paid_guest4'),
    path('table_june_partially_paid_guest4/', reports4.table_june_partially_paid_guest4, name='table_june_partially_paid_guest4'),

    path('july_paid_rent4/', branch4.july_paid_rent4, name='july_paid_rent4'),
    path('table_july_paid_rent4/', branch4.table_july_paid_rent4, name='table_july_paid_rent4'),
    path('july_full_paid_guest4/', reports4.july_full_paid_guest4, name='july_full_paid_guest4'),
    path('july_partially_paid_guest4/', reports4.july_partially_paid_guest4, name='july_partially_paid_guest4'),
    path('table_july_partially_paid_guest4/', reports4.table_july_partially_paid_guest4, name='table_july_partially_paid_guest4'),

    path('aug_paid_rent4/', branch4.aug_paid_rent4, name='aug_paid_rent4'),
    path('table_aug_paid_rent4/', branch4.table_aug_paid_rent4, name='table_aug_paid_rent4'),
    path('auguest_full_paid_guest4/', reports4.auguest_full_paid_guest4, name='auguest_full_paid_guest4'),
    path('auguest_partially_paid_guest4/', reports4.auguest_partially_paid_guest4,name='auguest_partially_paid_guest4'),
    path('table_auguest_partially_paid_guest4/', reports4.table_auguest_partially_paid_guest4,name='table_auguest_partially_paid_guest4'),

    path('sept_paid_rent4/', branch4.sept_paid_rent4, name='sept_paid_rent4'),
    path('table_sept_paid_rent4/', branch4.table_sept_paid_rent4, name='table_sept_paid_rent4'),
    path('sept_full_paid_guest4/', reports4.sept_full_paid_guest4, name='sept_full_paid_guest4'),
    path('sept_partially_paid_guest4/', reports4.sept_partially_paid_guest4, name='sept_partially_paid_guest4'),
    path('table_sept_partially_paid_guest4/', reports4.table_sept_partially_paid_guest4,name='table_sept_partially_paid_guest4'),

    path('oct_paid_rent4/', branch4.oct_paid_rent4, name='oct_paid_rent4'),
    path('table_oct_paid_rent4/', branch4.table_oct_paid_rent4, name='table_oct_paid_rent4'),
    path('october_full_paid_guest4/', reports4.october_full_paid_guest4, name='october_full_paid_guest4'),
    path('october_partially_paid_guest4/', reports4.october_partially_paid_guest4,name='october_partially_paid_guest4'),
    path('table_october_partially_paid_guest4/', reports4.table_october_partially_paid_guest4,name='table_october_partially_paid_guest4'),

    path('nov_paid_rent4/', branch4.nov_paid_rent4, name='nov_paid_rent4'),
    path('table_nov_paid_rent4/', branch4.table_nov_paid_rent4, name='table_nov_paid_rent4'),
    path('nov_full_paid_guest4/', reports4.nov_full_paid_guest4, name='nov_full_paid_guest4'),
    path('nov_partially_paid_guest4/', reports4.nov_partially_paid_guest4, name='nov_partially_paid_guest4'),
    path('table_nov_partially_paid_guest4/', reports4.table_nov_partially_paid_guest4,name='table_nov_partially_paid_guest4'),

    path('dec_paid_rent4/', branch4.dec_paid_rent4, name='dec_paid_rent4'),
    path('table_dec_paid_rent4/', branch4.table_dec_paid_rent4, name='table_dec_paid_rent4'),
    path('dec_full_paid_guest4/', reports4.dec_full_paid_guest4, name='dec_full_paid_guest4'),
    path('dec_partially_paid_guest4/', reports4.dec_partially_paid_guest4, name='dec_partially_paid_guest4'),
    path('table_dec_partially_paid_guest4/', reports4.table_dec_partially_paid_guest4,name='table_dec_partially_paid_guest4'),

    path('details_of_paid_guests4/<id>',branch4.details_of_paid_guests4,name='details_of_paid_guests4'),
    path('full_paid_guest4/',reports4.full_paid_guest4,name='full_paid_guest4'),

#paid rent end here

#*********reports end here

##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest4/',branch4.viewall_vacate_guest4,name='viewall_vacate_guest4'),
    path('details_of_vacate_guest4/<id>',branch4.details_of_vacate_guest4,name='details_of_vacate_guest4'),
    path('full_vacated_guest_details4',branch4.full_vacated_guest_details4,name='full_vacated_guest_details4'),
    path('full_vacated_guest_table4',branch4.full_vacated_guest_table4,name='full_vacated_guest_table4'),

    path('guest_details4/<guest_code>', branch4.guest_details4, name='guest_details4'),


#********vacate guest payments start here**********

    path('jan_manke_payments_vacate4/<id>', branch4.jan_manke_payments_vacate4, name='jan_manke_payments_vacate4'),
    path('feb_manke_payments_vacate4/<id>', branch4.feb_manke_payments_vacate4, name='feb_manke_payments_vacate4'),
    path('march_manke_payments_vacate4/<id>', branch4.march_manke_payments_vacate4, name='march_manke_payments_vacate4'),
    path('april_make_payments_vacate4/<id>', branch4.april_make_payments_vacate4, name='april_make_payments_vacate4'),

    path('may_make_payments_vacate4/<id>', branch4.may_make_payments_vacate4, name='may_make_payments_vacate4'),
    path('june_make_payments_vacate4/<id>', branch4.june_make_payments_vacate4, name='june_make_payments_vacate4'),
    path('july_make_payments_vacate4/<id>', branch4.july_make_payments_vacate4, name='july_make_payments_vacate4'),
    path('aug_make_payments_vacate4/<id>', branch4.aug_make_payments_vacate4, name='aug_make_payments_vacate4'),

    path('sept_make_payments_vacate4/<id>', branch4.sept_make_payments_vacate4, name='sept_make_payments_vacate4'),
    path('oct_make_payments_vacate4/<id>', branch4.oct_make_payments_vacate4, name='oct_make_payments_vacate4'),
    path('nov_make_payments_vacate4/<id>', branch4.nov_make_payments_vacate4, name='nov_make_payments_vacate4'),
    path('dec_make_payments_vacate4/<id>', branch4.dec_make_payments_vacate4, name='dec_make_payments_vacate4'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################



##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general4/',branch4.detail_guest_general4,name='detail_guest_general4'),

    path('jan_print4/',branch4.jan_print4,name='jan_print4'),
    path('feb_print4/',branch4.feb_print4,name='feb_print4'),
    path('march_print4/',branch4.march_print4,name='march_print4'),
    path('april_print4/',branch4.april_print4,name='april_print4'),

    path('may_print4/',branch4.may_print4,name='may_print4'),
    path('june_print4/',branch4.june_print4,name='june_print4'),
    path('july_print4/', branch4.july_print4, name='july_print4'),
    path('aug_print4/', branch4.aug_print4, name='aug_print4'),

    path('sept_print4/', branch4.sept_print4, name='sept_print4'),
    path('oct_print4/', branch4.oct_print4, name='oct_print4'),
    path('nov_print4/', branch4.nov_print4, name='nov_print4'),
    path('dec_print4/', branch4.dec_print4, name='dec_print4'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close4/', branch4.jan_close4, name='jan_close4'),
    path('jan_close_decision_page4/', branch4.jan_close_decision_page4, name='jan_close_decision_page4'),
    path('feb_close/', branch4.feb_close4, name='feb_close4'),
    path('feb_close_decision_page4/', branch4.feb_close_decision_page4, name='feb_close_decision_page4'),
    path('mar_close4/', branch4.mar_close4, name='mar_close4'),
    path('mar_close_decision_page/', branch4.mar_close_decision_page4, name='mar_close_decision_page4'),
    path('apr_close4/', branch4.apr_close4, name='apr_close4'),
    path('apr_close_decision_page4/', branch4.apr_close_decision_page4, name='apr_close_decision_page4'),

    path('may_close4/', branch4.may_close4, name='may_close4'),
    path('may_close_decision_page4/', branch4.may_close_decision_page4, name='may_close_decision_page4'),
    path('jun_close4/', branch4.jun_close4, name='jun_close4'),
    path('jun_close_decision_page4/', branch4.jun_close_decision_page4, name='jun_close_decision_page4'),
    path('jul_close4/', branch4.jul_close4, name='jul_close4'),
    path('jul_close_decision_page4/', branch4.jul_close_decision_page4, name='jul_close_decision_page4'),
    path('aug_close4/', branch4.aug_close4, name='aug_close4'),
    path('aug_close_decision_page4/', branch4.aug_close_decision_page4, name='aug_close_decision_page4'),

    path('sep_close4/', branch4.sep_close4, name='sep_close4'),
    path('sep_close_decision_page4/', branch4.sep_close_decision_page4, name='sep_close_decision_page4'),
    path('oct_close4/', branch4.oct_close4, name='oct_close4'),
    path('oct_close_decision_page4/', branch4.oct_close_decision_page4, name='oct_close_decision_page4'),
    path('nov_close4/', branch4.nov_close4, name='nov_close4'),
    path('nov_close_decision_page4/', branch4.nov_close_decision_page4, name='nov_close_decision_page4'),


    path('test/',branch4.pysql,name='pysql'),
    path('d4/', branch4.dynamic, name='dynamic'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months4/',reports4.detailed_report_choose_months4,name='detailed_report_choose_months4'),

    path('jan_details_live4/', reports4.jan_details_live4, name='jan_details_live4'),
    path('jan_print_live4/', reports4.jan_print_live4, name='jan_print_live4'),
    path('feb_details_live4/', reports4.feb_details_live4, name='feb_details_live4'),
    path('feb_print_live4/', reports4.feb_print_live4, name='feb_print_live4'),
    path('march_details_live4/', reports4.march_details_live4, name='march_details_live4'),
    path('march_print_live4/', reports4.march_print_live4, name='march_print_live4'),

    path('april_details_live4/', reports4.april_details_live4, name='april_details_live4'),
    path('april_print_live4/', reports4.april_print_live4, name='april_print_live4'),
    path('may_details_live4/', reports4.may_details_live4, name='may_details_live4'),
    path('may_print_live4/', reports4.may_print_live4, name='may_print_live4'),
    path('june_details_live4/',reports4.june_details_live4,name='june_details_live4'),
    path('june_print_live4/', reports4.june_print_live4, name='june_print_live4'),

    path('july_details_live4/', reports4.july_details_live4, name='july_details_live4'),
    path('july_print_live4/', reports4.july_print_live4, name='july_print_live4'),
    path('auguest_details_live4/', reports4.auguest_details_live4, name='auguest_details_live4'),
    path('auguest_print_live4/', reports4.auguest_print_live4, name='auguest_print_live4'),
    path('sept_details_live4/', reports4.sept_details_live4, name='sept_details_live4'),
    path('sept_print_live4/', reports4.sept_print_live4, name='sept_print_live4'),

    path('october_details_live4/', reports4.october_details_live4, name='october_details_live4'),
    path('october_print_live4/', reports4.october_print_live4, name='october_print_live4'),
    path('nov_details_live4/', reports4.nov_details_live4, name='nov_details_live4'),
    path('nov_print_live4/', reports4.nov_print_live4, name='nov_print_live4'),
    path('dec_details_live4/', reports4.dec_details_live4, name='dec_details_live4'),
    path('dec_print_live4/', reports4.dec_print_live4, name='dec_print_live4'),

########################################
#  DETAILED REPORT END HERE
###########################



    path('viewall_vaccant_room4/',reports4.viewall_vaccant_room4,name='viewall_vaccant_room4'),

########################################
# DUE AMT MANAGEMENT START HERE
###########################

path('view_all_due_amt4/', branch4.view_all_due_amt4, name='view_all_due_amt4'),
path('due_amt_mgt_choose_months4/', branch4.due_amt_mgt_choose_months4, name='due_amt_mgt_choose_months4'),

path('view_jan_account_details4/', branch4.view_jan_account_details4, name='view_jan_account_details4'),
path('jan_account_mgt4/<id>',branch4.jan_account_mgt4,name='jan_account_mgt4'),
path('view_feb_account_details4/', branch4.view_feb_account_details4, name='view_feb_account_details4'),
path('feb_account_mgt4/<id>',branch4.feb_account_mgt4,name='feb_account_mgt4'),
path('view_march_account_details4/', branch4.view_march_account_details4, name='view_march_account_details4'),
path('march_account_mgt4/<id>',branch4.march_account_mgt4,name='march_account_mgt4'),
path('view_april_account_details4/', branch4.view_april_account_details4, name='view_april_account_details4'),
path('april_account_mgt4/<id>',branch4.april_account_mgt4,name='april_account_mgt4'),

path('view_may_account_details4/',branch4.view_may_account_details4,name='view_may_account_details4'),
path('may_account_mgt4/<id>', branch4.may_account_mgt4, name='may_account_mgt4'),
path('view_june_account_details4/', branch4.view_june_account_details4, name='view_june_account_details4'),
path('june_account_mgt4/<id>',branch4.june_account_mgt4,name='june_account_mgt4'),
path('view_july_account_details4/', branch4.view_july_account_details4, name='view_july_account_details4'),
path('july_account_mgt4/<id>',branch4.july_account_mgt4,name='july_account_mgt4'),
path('view_auguest_account_details4/', branch4.view_auguest_account_details4, name='view_auguest_account_details4'),
path('auguest_account_mgt4/<id>',branch4.auguest_account_mgt4,name='auguest_account_mgt4'),

path('view_sept_account_details4/', branch4.view_sept_account_details4, name='view_sept_account_details4'),
path('sept_account_mgt4/<id>',branch4.sept_account_mgt4,name='sept_account_mgt4'),
path('view_october_account_details4/', branch4.view_october_account_details4, name='view_october_account_details4'),
path('october_account_mgt4/<id>',branch4.october_account_mgt4,name='october_account_mgt4'),
path('view_nov_account_details4/', branch4.view_nov_account_details4, name='view_nov_account_details4'),
path('nov_account_mgt4/<id>',branch4.nov_account_mgt4,name='nov_account_mgt4'),
path('view_dec_account_details4/', branch4.view_dec_account_details4, name='view_dec_account_details4'),
path('dec_account_mgt4/<id>',branch4.dec_account_mgt4,name='dec_account_mgt4'),


########################################
# DUE AMT MANAGEMENT END HERE
###########################

    path('manage_bed4/', branch4.manage_bed4, name='manage_bed4'),
    path('manage_new_guest4/', branch4.manage_new_guest4, name='manage_new_guest4'),
    path('manage_update_new_guest4/<id>', branch4.manage_update_new_guest4, name='manage_update_new_guest4'),
    path('manage_update_beds4/<id>', branch4.manage_update_beds4, name='manage_update_beds4'),


########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_collection_details4/', admin_dashboard_calculations_br4.monthly_collection_details4, name='monthly_collection_details4'),

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

    path('view_all_category4/', accounts4.view_all_category4, name='view_all_category4'),
    path('create_new_category4/', accounts4.create_new_category4, name='create_new_category4'),
    path('regi_new_category4/', accounts4.regi_new_category4, name='regi_new_category4'),
    path('update_category4/<id>',accounts4.update_category4,name='update_category4'),

    path('delete_category4/<id>', accounts4.delete_category4, name='delete_category4'),
    path('view_all_category_delete4/', accounts4.view_all_category_delete4, name='view_all_category_delete4'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items4/', accounts4.view_all_items4, name='view_all_items4'),
    path('create_new_item4/', accounts4.create_new_item4, name='create_new_item4'),
    path('regi_new_item4/', accounts4.regi_new_item4, name='regi_new_item4'),
    path('delete_item4/<id>',accounts4.delete_item4,name='delete_item4'),
    path('update_item4/<id>', accounts4.update_item4, name='update_item4'),
    path('view_all_items_delete4/',accounts4.view_all_items_delete4,name='view_all_items_delete4'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger4/', accounts4.view_all_ledger4, name='view_all_ledger4'),
    path('create_new_ledger4/', accounts4.create_new_ledger4, name='create_new_ledger4'),
    path('regi_new_ledger4/', accounts4.regi_new_ledger4, name='regi_new_ledger4'),
    path('delete_ledger4/<id>',accounts4.delete_ledger4,name='delete_ledger4'),
    path('update_ledger4/<id>',accounts4.update_ledger4,name='update_ledger4'),
    path('view_all_ledger_delete4/',accounts4.view_all_ledger_delete4,name='view_all_ledger_delete4'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book4/', accounts4.view_all_accounts_book4, name='view_all_accounts_book4'),
    path('create_new_accounts_book4/', accounts4.create_new_accounts_book4, name='create_new_accounts_book4'),
    path('regi_new_accounts_book4/', accounts4.regi_new_accounts_book4, name='regi_new_accounts_book4'),
    path('update_accounts_book4/<id>',accounts4.update_accounts_book4,name='update_accounts_book4'),
    path('delete_accounts_book4/<id>',accounts4.delete_accounts_book4,name='delete_accounts_book4'),
    path('view_all_accounts_book_delete4/',accounts4.view_all_accounts_book_delete4,name='view_all_accounts_book_delete4'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries4/', accounts4.get_countries4, name='get_countries4'),

    path('in_exp_items_entry4/', accounts4.in_exp_items_entry4, name='in_exp_items_entry4'),
    path('reg_in_exp_items_entry4/', accounts4.reg_in_exp_items_entry4, name='reg_in_exp_items_entry4'),
    path('delete_journal4/<id>',accounts4.delete_journal4,name='delete_journal4'),
    path('update_in_exp_items_entry4/<id>',accounts4.update_in_exp_items_entry4,name='update_in_exp_items_entry4'),
    path('detailed_journal_report4/',accounts4.detailed_journal_report4,name='detailed_journal_report4'),
    path('journal_report_deleted4/',accounts4.journal_report_deleted4,name='journal_report_deleted4'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise4/', accounts4.daily_category_wise4, name='daily_category_wise4'),
    path('monthly_category_based_reports4/',accounts4.monthly_category_based_reports4,name='monthly_category_based_reports4'),
    path('yearly_category_based_reports4/', accounts4.yearly_category_based_reports4,name='yearly_category_based_reports4'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed4/', accounts4.daily_detailed4, name='daily_detailed4'),
    path('monthly_detailed4/',accounts4.monthly_detailed4,name='monthly_detailed4'),
    path('yearly_detailed4/',accounts4.yearly_detailed4,name='yearly_detailed4'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports4/', accounts4.item_based_reports4, name='item_based_reports4'),
    path('daily_item_based_reports4/',accounts4.daily_item_based_reports4,name='daily_item_based_reports4'),
    path('monthly_item_based_reports4/',accounts4.monthly_item_based_reports4,name='monthly_item_based_reports4'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports4/', accounts4.ledger_based_reports4, name='ledger_based_reports4'),
    path('monthly_ledger_based_reports4/', accounts4.monthly_ledger_based_reports4, name='monthly_ledger_based_reports4'),
    path('daily_ledger_based_reports4/',accounts4.daily_ledger_based_reports4,name='daily_ledger_based_reports4'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports4/', accounts4.accounts_book_based_reports4, name='accounts_book_based_reports4'),
    path('daily_accounts_book_based_reports4/',accounts4.daily_accounts_book_based_reports4,name='daily_accounts_book_based_reports4'),
    path('monthly_accounts_book_based_reports4/',accounts4.monthly_accounts_book_based_reports4,name='monthly_accounts_book_based_reports4'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months4/', accounts4.monthly_reports_choose_months4, name='monthly_reports_choose_months4'),
    path('monthly_detailed_daily_in_exp_items_report4/<mo>',accounts4.monthly_detailed_daily_in_exp_items_report4,name='monthly_detailed_daily_in_exp_items_report4'),

    path('single_monthly_reports_choose_months4/', accounts4.single_monthly_reports_choose_months4,name='single_monthly_reports_choose_months4'),
    path('single_monthly_daily_in_exp_items_report4/<mo>',accounts4.single_monthly_daily_in_exp_items_report4,name='single_monthly_daily_in_exp_items_report4'),

    path('accounts_dash_board4/',accounts4.accounts_dash_board4,name='accounts_dash_board4'),




    path('profit_sharing_choose_months4', accounts4.profit_sharing_choose_months4, name='profit_sharing_choose_months4'),
    path('profit_sharing4/<mo>',accounts4.profit_sharing4,name='profit_sharing4'),
    path('view_share_holders4',accounts4.view_share_holders4,name='view_share_holders4'),
    path('create_share_holders4',accounts4.create_share_holders4,name='create_share_holders4'),
    path('regi_share_holders4', accounts4.regi_share_holders4, name='regi_share_holders4'),
    path('update_share_holders4/<id>',accounts4.update_share_holders4,name='update_share_holders4'),
    path('delete_share_holders4/<id>', accounts4.delete_share_holders4, name='delete_share_holders4'),
    path('view_deleted_share_holders4', accounts4.view_deleted_share_holders4, name='view_deleted_share_holders4'),




]