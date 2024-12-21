from django.urls import path

from . import admin_branch3
from . import branch3
from . import reports3
from . import payment3
from . import admin_dashboard_calculations_br3
from . import accounts3


urlpatterns = [

    path('branch1_dashboard3/', branch3.branch1_dashboard3, name='branch1_dashboard3'),
    path('user_dashboard_calculations_ob_ch3/',branch3.user_dashboard_calculations_ob_ch3,name='user_dashboard_calculations_ob_ch3'),

    path('background3', branch3.background3, name='background3'),
    path('background_regi3', branch3.background_regi3, name='background_regi3'),
    path('custom_background_regi3', branch3.custom_background_regi3, name='custom_background_regi3'),


#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi3/',admin_branch3.branch1_room_create_regi3,name='branch1_room_create_regi3'),
    path('view_all_room3/',admin_branch3.view_all_room3,name='view_all_room3'),
    path('delete_room3/<id>',admin_branch3.delete_room3,name='delete_room3'),

    path('branch1_room_create3/',admin_branch3.branch1_room_create3,name='branch1_room_create3'),

    path('multiple_branch1_room_create_regi3/',admin_branch3.multiple_branch1_room_create_regi3,name='multiple_branch1_room_create_regi3'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi3/', admin_branch3.pg1_bed_create_regi3, name='pg1_bed_create_regi3'),
    path('pg1_view_all_beds3/', admin_branch3.pg1_view_all_beds3, name='pg1_view_all_beds3'),
    path('delete_bed3/<id>', admin_branch3.delete_bed3, name='delete_bed3'),

    path('pg1_bed_create3/', admin_branch3.pg1_bed_create3, name='pg1_bed_create3'),

    path('single_pg1_bed_create_regi3/', admin_branch3.single_pg1_bed_create_regi3, name='single_pg1_bed_create_regi3'),
    path('update_bed_basic_details3/<id>', admin_branch3.update_bed_basic_details3, name='update_bed_basic_details3'),

    path('multiple_single_pg1_bed_create_regi3/',admin_branch3.multiple_single_pg1_bed_create_regi3,name='multiple_single_pg1_bed_create_regi3'),

    #bed creation end here

#guest
    path('br1_admit_guest3/<id>',branch3.br1_admit_guest3,name='br1_admit_guest3'),
    path('view_all_new_guest3/',branch3.view_all_new_guest3,name='view_all_new_guest3'),
    path('update_br1_admit_guest3/<id>',branch3.update_br1_admit_guest3,name='update_br1_admit_guest3'),
    path('vacate_br1_guest3/<id>',branch3.vacate_br1_guest3,name='vacate_br1_guest3'),

    path('active_guest_details3/<guest_code>',branch3.active_guest_details3,name='active_guest_details3'),
    path('view_all_guest3/',branch3.view_all_guest3,name='view_all_guest3'),
    path('change_duplicate_guest_status3/<id>',branch3.change_duplicate_guest_status3,name='change_duplicate_guest_status3'),
    path('shift_guest3/<id>',branch3.shift_guest3,name='shift_guest3'),
    path('shift_guest_regi3/',branch3.shift_guest_regi3,name='shift_guest_regi3'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),

    path('multiple_br1_admit_guest3/<id>',branch3.multiple_br1_admit_guest3,name='multiple_br1_admit_guest3'),
#guest end here



##################################
#_ADVANCE3 START HERE
################################


path('choose_months_advance3/',branch3.choose_months_advance3,name='choose_months_advance3'),

path('jan_advance3/', branch3.jan_advance3, name='jan_advance3'),
path('jan_make_payments_advance3/<id>', branch3.jan_make_payments_advance3,name='jan_make_payments_advance3'),
path('feb_advance3/', branch3.feb_advance3, name='feb_advance3'),
path('feb_make_payments_advance3/<id>', branch3.feb_make_payments_advance3,name='feb_make_payments_advance3'),
path('march_advance3/', branch3.march_advance3, name='march_advance3'),
path('march_make_payments_advance3/<id>', branch3.march_make_payments_advance3,name='march_make_payments_advance3'),
path('april_advance3/', branch3.april_advance3, name='april_advance3'),
path('april_make_payments_advance3/<id>', branch3.april_make_payments_advance3, name='april_make_payments_advance3'),

path('may_advance3/',branch3.may_advance3,name='may_advance3'),
path('may_make_payments_advance3/<id>', branch3.may_make_payments_advance3, name='may_make_payments_advance3'),
path('june_advance3/',branch3.june_advance3,name='june_advance3'),
path('june_make_payments_advance3/<id>', branch3.june_make_payments_advance3, name='june_make_payments_advance3'),
path('july_advance3/',branch3.july_advance3,name='july_advance3'),
path('july_make_payments_advance3/<id>', branch3.july_make_payments_advance3, name='july_make_payments_advance3'),
path('auguest_advance3/', branch3.auguest_advance3, name='auguest_advance3'),
path('auguest_make_payments_advance3/<id>', branch3.auguest_make_payments_advance3, name='auguest_make_payments_advance3'),

path('sept_advance3/', branch3.sept_advance3, name='sept_advance3'),
path('sept_make_payments_advance3/<id>', branch3.sept_make_payments_advance3,name='sept_make_payments_advance3'),
path('october_advance3/', branch3.october_advance3, name='october_advance3'),
path('october_make_payments_advance3/<id>', branch3.october_make_payments_advance3, name='october_make_payments_advance3'),
path('nov_advance3/', branch3.nov_advance3, name='nov_advance3'),
path('nov_make_payments_advance3/<id>', branch3.nov_make_payments_advance3,name='nov_make_payments_advance3'),
path('dec_advance3/', branch3.dec_advance3, name='dec_advance3'),
path('dec_make_payments_advance3/<id>', branch3.dec_make_payments_advance3, name='dec_make_payments_advance3'),



    ##################################
#_ADVANCE3 END HERE
################################




##################################
#PAYMENTS START HERE
################################

    path('choose_months3/',branch3.choose_months3,name='choose_months3'),

    path('jan3/',branch3.jan3,name='jan3'),
    path('jan_manke_payments3/<id>',branch3.jan_manke_payments3,name='jan_manke_payments3'),

    path('feb3/',branch3.feb3,name='feb3'),
    path('feb_manke_payments3/<id>',branch3.feb_manke_payments3,name='feb_manke_payments3'),

    path('march3/',branch3.march3,name='march3'),
    path('march_manke_payments3/<id>',branch3.march_manke_payments3,name='march_manke_payments3'),

    path('april3/',branch3.april3,name='april3'),
    path('april_make_payments3/<id>',branch3.april_make_payments3,name='april_make_payments3'),

    path('may3/',branch3.may3,name='may3'),
    path('may_make_payments3/<id>',branch3.may_make_payments3,name='may_make_payments3'),

    path('june3/',branch3.june3,name='june3'),
    path('june_make_payments3/<id>',branch3.june_make_payments3,name='june_make_payments3'),

    path('july3/',branch3.july3,name='july3'),
    path('july_make_payments3/<id>',branch3.july_make_payments3,name='july_make_payments3'),

    path('aug3/',branch3.aug3,name='aug3'),
    path('aug_make_payments3/<id>',branch3.aug_make_payments3,name='aug_make_payments3'),

    path('sept3/',branch3.sept3,name='sept3'),
    path('sept_make_payments3/<id>',branch3.sept_make_payments3,name='sept_make_payments3'),

    path('oct3/',branch3.oct3,name='oct3'),
    path('oct_make_payments3/<id>',branch3.oct_make_payments3,name='oct_make_payments3'),

    path('nov3/',branch3.nov3,name='nov3'),
    path('nov_make_payments3/<id>',branch3.nov_make_payments3,name='nov_make_payments3'),

    path('dec3/',branch3.dec3,name='dec3'),
    path('dec_make_payments3/<id>',branch3.dec_make_payments3,name='dec_make_payments3'),

##################################
#PAYMENTS END HERE
################################



##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user3/', payment3.choose_user3, name='choose_user3'),
    path('payment_user_details3/<id>', payment3.payment_user_details3, name='payment_user_details3'),
    path('close_choose_user3/<id>', payment3.close_choose_user3, name='close_choose_user3'),

    path('monthly_jan_make_payments3/<id>', payment3.monthly_jan_make_payments3, name='monthly_jan_make_payments3'),
    path('monthly_feb_make_payments3/<id>', payment3.monthly_feb_make_payments3, name='monthly_feb_make_payments3'),
    path('monthly_march_make_payments3/<id>', payment3.monthly_march_make_payments3, name='monthly_march_make_payments3'),
    path('monthly_april_make_payments3/<id>', payment3.monthly_april_make_payments3, name='monthly_april_make_payments3'),
    path('monthly_may_make_payments3/<id>', payment3.monthly_may_make_payments3, name='monthly_may_make_payments3'),
    path('monthly_june_make_payments3/<id>', payment3.monthly_june_make_payments3, name='monthly_june_make_payments3'),

    path('monthly_july_make_payments3/<id>', payment3.monthly_july_make_payments3, name='monthly_july_make_payments3'),
    path('monthly_aug_make_payments3/<id>', payment3.monthly_aug_make_payments3, name='monthly_aug_make_payments3'),
    path('monthly_sept_make_payments3/<id>', payment3.monthly_sept_make_payments3, name='monthly_sept_make_payments3'),
    path('monthly_oct_make_payments3/<id>', payment3.monthly_oct_make_payments3, name='monthly_oct_make_payments3'),
    path('monthly_nov_make_payments3/<id>', payment3.monthly_nov_make_payments3, name='monthly_nov_make_payments3'),
    path('monthly_dec_make_payments3/<id>', payment3.monthly_dec_make_payments3, name='monthly_dec_make_payments3'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################





#*********reports start here



#unpaid rent start here
    path('unpaid_rent_choose_months3/',branch3.unpaid_rent_choose_months3,name='unpaid_rent_choose_months3'),

    path('jan_unpaid_rent3/', branch3.jan_unpaid_rent3, name='jan_unpaid_rent3'),
    path('table_jan_unpaid_rent3/', branch3.table_jan_unpaid_rent3, name='table_jan_unpaid_rent3'),
    path('feb_unpaid_rent3/', branch3.feb_unpaid_rent3, name='feb_unpaid_rent3'),
    path('table_feb_unpaid_rent3/', branch3.table_feb_unpaid_rent3, name='table_feb_unpaid_rent3'),
    path('mar_unpaid_rent3/', branch3.mar_unpaid_rent3, name='mar_unpaid_rent3'),
    path('table_mar_unpaid_rent3/', branch3.table_mar_unpaid_rent3, name='table_mar_unpaid_rent3'),
    path('april_unpaid_rent3/', branch3.april_unpaid_rent3, name='april_unpaid_rent3'),
    path('table_april_unpaid_rent3/', branch3.table_april_unpaid_rent3, name='table_april_unpaid_rent3'),

    path('may_unpaid_rent3/', branch3.may_unpaid_rent3, name='may_unpaid_rent3'),
    path('table_may_unpaid_rent3/', branch3.table_may_unpaid_rent3, name='table_may_unpaid_rent3'),
    path('june_unpaid_rent3/', branch3.june_unpaid_rent3, name='june_unpaid_rent3'),
    path('table_june_unpaid_rent3/', branch3.table_june_unpaid_rent3, name='table_june_unpaid_rent3'),
    path('july_unpaid_rent3/', branch3.july_unpaid_rent3, name='july_unpaid_rent3'),
    path('table_july_unpaid_rent3',branch3.table_july_unpaid_rent3,name='table_july_unpaid_rent3'),
    path('aug_unpaid_rent3/', branch3.aug_unpaid_rent3, name='aug_unpaid_rent3'),
    path('table_aug_unpaid_rent3/',branch3.table_aug_unpaid_rent3,name='table_aug_unpaid_rent3'),

    path('sept_unpaid_rent3/', branch3.sept_unpaid_rent3, name='sept_unpaid_rent3'),
    path('table_sept_unpaid_rent3/', branch3.table_sept_unpaid_rent3, name='table_sept_unpaid_rent3'),
    path('oct_unpaid_rent3/', branch3.oct_unpaid_rent3, name='oct_unpaid_rent3'),
    path('table_oct_unpaid_rent3/', branch3.table_oct_unpaid_rent3, name='table_oct_unpaid_rent3'),
    path('nov_unpaid_rent3/', branch3.nov_unpaid_rent3, name='nov_unpaid_rent3'),
    path('table_nov_unpaid_rent3/', branch3.table_nov_unpaid_rent3, name='table_nov_unpaid_rent3'),
    path('dec_unpaid_rent3/', branch3.dec_unpaid_rent3, name='dec_unpaid_rent3'),
    path('table_dec_unpaid_rent3/', branch3.table_dec_unpaid_rent3, name='table_dec_unpaid_rent3'),

    path('details_of_unpaid_guests3/<id>',branch3.details_of_unpaid_guests3,name='details_of_unpaid_guests3'),

#unpaid rent end here

#paid rent start here

path('paid_rent_choose_months3/',branch3.paid_rent_choose_months3,name='paid_rent_choose_months3'),
path('partially_paid_guest_choose_months3/',reports3.partially_paid_guest_choose_months3,name='partially_paid_guest_choose_months3'),

path('jan_paid_rent3/', branch3.jan_paid_rent3, name='jan_paid_rent3'),
path('table_jan_paid_rent3/', branch3.table_jan_paid_rent3, name='table_jan_paid_rent3'),
path('jan_full_paid_guest3/', reports3.jan_full_paid_guest3, name='jan_full_paid_guest3'),
path('jan_partially_paid_guest3/', reports3.jan_partially_paid_guest3, name='jan_partially_paid_guest3'),
path('table_jan_partially_paid_guest3/', reports3.table_jan_partially_paid_guest3,name='table_jan_partially_paid_guest3'),

path('feb_paid_rent3/', branch3.feb_paid_rent3, name='feb_paid_rent3'),
path('table_feb_paid_rent3/', branch3.table_feb_paid_rent3, name='table_feb_paid_rent3'),
path('feb_full_paid_guest3/', reports3.feb_full_paid_guest3, name='feb_full_paid_guest3'),
path('feb_partially_paid_guest3/', reports3.feb_partially_paid_guest3, name='feb_partially_paid_guest3'),
path('table_feb_partially_paid_guest3/', reports3.table_feb_partially_paid_guest3,name='table_feb_partially_paid_guest3'),

path('mar_paid_rent3/', branch3.mar_paid_rent3, name='mar_paid_rent3'),
path('table_mar_paid_rent3/', branch3.table_mar_paid_rent3, name='table_mar_paid_rent3'),
path('march_full_paid_guest3/', reports3.march_full_paid_guest3, name='march_full_paid_guest3'),
path('march_partially_paid_guest3/', reports3.march_partially_paid_guest3, name='march_partially_paid_guest3'),
path('table_march_partially_paid_guest3/', reports3.table_march_partially_paid_guest3,name='table_march_partially_paid_guest3'),

path('april_paid_rent3/', branch3.april_paid_rent3, name='april_paid_rent3'),
path('table_april_paid_rent3/', branch3.table_april_paid_rent3, name='table_april_paid_rent3'),
path('april_full_paid_guest3/', reports3.april_full_paid_guest3, name='april_full_paid_guest3'),
path('april_partially_paid_guest3/', reports3.april_partially_paid_guest3, name='april_partially_paid_guest3'),
path('table_april_partially_paid_guest3/', reports3.table_april_partially_paid_guest3,name='table_april_partially_paid_guest3'),

path('may_paid_rent3/', branch3.may_paid_rent3, name='may_paid_rent3'),
path('table_may_paid_rent3/', branch3.table_may_paid_rent3, name='table_may_paid_rent3'),
path('may_full_paid_guest3/', reports3.may_full_paid_guest3, name='may_full_paid_guest3'),
path('may_partially_paid_guest3/', reports3.may_partially_paid_guest3, name='may_partially_paid_guest3'),
path('table_may_partially_paid_guest3/', reports3.table_may_partially_paid_guest3, name='table_may_partially_paid_guest3'),

path('june_paid_rent3/', branch3.june_paid_rent3, name='june_paid_rent3'),
path('table_june_paid_rent3/', branch3.table_june_paid_rent3, name='table_june_paid_rent3'),
path('june_full_paid_guest3/', reports3.june_full_paid_guest3, name='june_full_paid_guest3'),
path('june_partially_paid_guest3/', reports3.june_partially_paid_guest3, name='june_partially_paid_guest3'),
path('table_june_partially_paid_guest3/', reports3.table_june_partially_paid_guest3, name='table_june_partially_paid_guest3'),

path('july_paid_rent3/', branch3.july_paid_rent3, name='july_paid_rent3'),
path('table_july_paid_rent3/', branch3.table_july_paid_rent3, name='table_july_paid_rent3'),
path('july_full_paid_guest3/', reports3.july_full_paid_guest3, name='july_full_paid_guest3'),
path('july_partially_paid_guest3/', reports3.july_partially_paid_guest3, name='july_partially_paid_guest3'),
path('table_july_partially_paid_guest3/', reports3.table_july_partially_paid_guest3, name='table_july_partially_paid_guest3'),

path('aug_paid_rent3/', branch3.aug_paid_rent3, name='aug_paid_rent3'),
path('table_aug_paid_rent3/', branch3.table_aug_paid_rent3, name='table_aug_paid_rent3'),
path('auguest_full_paid_guest3/', reports3.auguest_full_paid_guest3, name='auguest_full_paid_guest3'),
path('auguest_partially_paid_guest3/', reports3.auguest_partially_paid_guest3,name='auguest_partially_paid_guest3'),
path('table_auguest_partially_paid_guest3/', reports3.table_auguest_partially_paid_guest3,name='table_auguest_partially_paid_guest3'),

path('sept_paid_rent3/', branch3.sept_paid_rent3, name='sept_paid_rent3'),
path('table_sept_paid_rent3/', branch3.table_sept_paid_rent3, name='table_sept_paid_rent3'),
path('sept_full_paid_guest3/', reports3.sept_full_paid_guest3, name='sept_full_paid_guest3'),
path('sept_partially_paid_guest3/', reports3.sept_partially_paid_guest3, name='sept_partially_paid_guest3'),
path('table_sept_partially_paid_guest3/', reports3.table_sept_partially_paid_guest3,name='table_sept_partially_paid_guest3'),

path('oct_paid_rent3/', branch3.oct_paid_rent3, name='oct_paid_rent3'),
path('table_oct_paid_rent3/', branch3.table_oct_paid_rent3, name='table_oct_paid_rent3'),
path('october_full_paid_guest3/', reports3.october_full_paid_guest3, name='october_full_paid_guest3'),
path('october_partially_paid_guest3/', reports3.october_partially_paid_guest3,name='october_partially_paid_guest3'),
path('table_october_partially_paid_guest3/', reports3.table_october_partially_paid_guest3,name='table_october_partially_paid_guest3'),

path('nov_paid_rent3/', branch3.nov_paid_rent3, name='nov_paid_rent3'),
path('table_nov_paid_rent3/', branch3.table_nov_paid_rent3, name='table_nov_paid_rent3'),
path('nov_full_paid_guest3/', reports3.nov_full_paid_guest3, name='nov_full_paid_guest3'),
path('nov_partially_paid_guest3/', reports3.nov_partially_paid_guest3, name='nov_partially_paid_guest3'),
path('table_nov_partially_paid_guest3/', reports3.table_nov_partially_paid_guest3,name='table_nov_partially_paid_guest3'),

path('dec_paid_rent3/', branch3.dec_paid_rent3, name='dec_paid_rent3'),
path('table_dec_paid_rent3/', branch3.table_dec_paid_rent3, name='table_dec_paid_rent3'),
path('dec_full_paid_guest3/', reports3.dec_full_paid_guest3, name='dec_full_paid_guest3'),
path('dec_partially_paid_guest3/', reports3.dec_partially_paid_guest3, name='dec_partially_paid_guest3'),
path('table_dec_partially_paid_guest3/', reports3.table_dec_partially_paid_guest3,name='table_dec_partially_paid_guest3'),

path('details_of_paid_guests3/<id>',branch3.details_of_paid_guests3,name='details_of_paid_guests3'),
path('full_paid_guest3/',reports3.full_paid_guest3,name='full_paid_guest3'),


#paid rent end here



#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest3/',branch3.viewall_vacate_guest3,name='viewall_vacate_guest3'),
    path('details_of_vacate_guest3/<id>',branch3.details_of_vacate_guest3,name='details_of_vacate_guest3'),
    path('full_vacated_guest_details3',branch3.full_vacated_guest_details3,name='full_vacated_guest_details3'),
    path('full_vacated_guest_table3',branch3.full_vacated_guest_table3,name='full_vacated_guest_table3'),

    path('guest_details3/<guest_code>', branch3.guest_details3, name='guest_details3'),


#********vacate guest payments start here**********

    path('jan_manke_payments_vacate3/<id>', branch3.jan_manke_payments_vacate3, name='jan_manke_payments_vacate3'),
    path('feb_manke_payments_vacate3/<id>', branch3.feb_manke_payments_vacate3, name='feb_manke_payments_vacate3'),
    path('march_manke_payments_vacate3/<id>', branch3.march_manke_payments_vacate3, name='march_manke_payments_vacate3'),
    path('april_make_payments_vacate3/<id>', branch3.april_make_payments_vacate3, name='april_make_payments_vacate3'),

    path('may_make_payments_vacate3/<id>', branch3.may_make_payments_vacate3, name='may_make_payments_vacate3'),
    path('june_make_payments_vacate3/<id>', branch3.june_make_payments_vacate3, name='june_make_payments_vacate3'),
    path('july_make_payments_vacate3/<id>', branch3.july_make_payments_vacate3, name='july_make_payments_vacate3'),
    path('aug_make_payments_vacate3/<id>', branch3.aug_make_payments_vacate3, name='aug_make_payments_vacate3'),

    path('sept_make_payments_vacate3/<id>', branch3.sept_make_payments_vacate3, name='sept_make_payments_vacate3'),
    path('oct_make_payments_vacate3/<id>', branch3.oct_make_payments_vacate3, name='oct_make_payments_vacate3'),
    path('nov_make_payments_vacate3/<id>', branch3.nov_make_payments_vacate3, name='nov_make_payments_vacate3'),
    path('dec_make_payments_vacate3/<id>', branch3.dec_make_payments_vacate3, name='dec_make_payments_vacate3'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################



##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general3/',branch3.detail_guest_general3,name='detail_guest_general3'),

    path('jan_print3/',branch3.jan_print3,name='jan_print3'),
    path('feb_print3/',branch3.feb_print3,name='feb_print3'),
    path('march_print3/',branch3.march_print3,name='march_print3'),
    path('april_print3/',branch3.april_print3,name='april_print3'),

    path('may_print3/',branch3.may_print3,name='may_print3'),
    path('june_print3/',branch3.june_print3,name='june_print3'),
    path('july_print3/', branch3.july_print3, name='july_print3'),
    path('aug_print3/', branch3.aug_print3, name='aug_print3'),

    path('sept_print3/', branch3.sept_print3, name='sept_print3'),
    path('oct_print3/', branch3.oct_print3, name='oct_print3'),
    path('nov_print3/', branch3.nov_print3, name='nov_print3'),
    path('dec_print3/', branch3.dec_print3, name='dec_print3'),

    path('new_year_jan_print3/', branch3.new_year_jan_print3, name='new_year_jan_print3'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close3/', branch3.jan_close3, name='jan_close3'),
    path('jan_close_decision_page3/', branch3.jan_close_decision_page3, name='jan_close_decision_page3'),
    path('feb_close/', branch3.feb_close3, name='feb_close3'),
    path('feb_close_decision_page3/', branch3.feb_close_decision_page3, name='feb_close_decision_page3'),
    path('mar_close3/', branch3.mar_close3, name='mar_close3'),
    path('mar_close_decision_page/', branch3.mar_close_decision_page3, name='mar_close_decision_page3'),
    path('apr_close3/', branch3.apr_close3, name='apr_close3'),
    path('apr_close_decision_page3/', branch3.apr_close_decision_page3, name='apr_close_decision_page3'),

    path('may_close3/', branch3.may_close3, name='may_close3'),
    path('may_close_decision_page3/', branch3.may_close_decision_page3, name='may_close_decision_page3'),
    path('jun_close3/', branch3.jun_close3, name='jun_close3'),
    path('jun_close_decision_page3/', branch3.jun_close_decision_page3, name='jun_close_decision_page3'),
    path('jul_close3/', branch3.jul_close3, name='jul_close3'),
    path('jul_close_decision_page3/', branch3.jul_close_decision_page3, name='jul_close_decision_page3'),
    path('aug_close3/', branch3.aug_close3, name='aug_close3'),
    path('aug_close_decision_page3/', branch3.aug_close_decision_page3, name='aug_close_decision_page3'),

    path('sep_close3/', branch3.sep_close3, name='sep_close3'),
    path('sep_close_decision_page3/', branch3.sep_close_decision_page3, name='sep_close_decision_page3'),
    path('oct_close3/', branch3.oct_close3, name='oct_close3'),
    path('oct_close_decision_page3/', branch3.oct_close_decision_page3, name='oct_close_decision_page3'),
    path('nov_close3/', branch3.nov_close3, name='nov_close3'),
    path('nov_close_decision_page3/', branch3.nov_close_decision_page3, name='nov_close_decision_page3'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months3/',reports3.detailed_report_choose_months3,name='detailed_report_choose_months3'),

    path('jan_details_live3/', reports3.jan_details_live3, name='jan_details_live3'),
    path('jan_print_live3/', reports3.jan_print_live3, name='jan_print_live3'),
    path('feb_details_live3/', reports3.feb_details_live3, name='feb_details_live3'),
    path('feb_print_live3/', reports3.feb_print_live3, name='feb_print_live3'),
    path('march_details_live3/', reports3.march_details_live3, name='march_details_live3'),
    path('march_print_live3/', reports3.march_print_live3, name='march_print_live3'),

    path('april_details_live3/', reports3.april_details_live3, name='april_details_live3'),
    path('april_print_live3/', reports3.april_print_live3, name='april_print_live3'),
    path('may_details_live3/', reports3.may_details_live3, name='may_details_live3'),
    path('may_print_live3/', reports3.may_print_live3, name='may_print_live3'),
    path('june_details_live3/',reports3.june_details_live3,name='june_details_live3'),
    path('june_print_live3/', reports3.june_print_live3, name='june_print_live3'),

    path('july_details_live3/', reports3.july_details_live3, name='july_details_live3'),
    path('july_print_live3/', reports3.july_print_live3, name='july_print_live3'),
    path('auguest_details_live3/', reports3.auguest_details_live3, name='auguest_details_live3'),
    path('auguest_print_live3/', reports3.auguest_print_live3, name='auguest_print_live3'),
    path('sept_details_live3/', reports3.sept_details_live3, name='sept_details_live3'),
    path('sept_print_live3/', reports3.sept_print_live3, name='sept_print_live3'),

    path('october_details_live3/', reports3.october_details_live3, name='october_details_live3'),
    path('october_print_live3/', reports3.october_print_live3, name='october_print_live3'),
    path('nov_details_live3/', reports3.nov_details_live3, name='nov_details_live3'),
    path('nov_print_live3/', reports3.nov_print_live3, name='nov_print_live3'),
    path('dec_details_live3/', reports3.dec_details_live3, name='dec_details_live3'),
    path('dec_print_live3/', reports3.dec_print_live3, name='dec_print_live3'),

########################################
#  DETAILED REPORT END HERE
###########################



    path('viewall_vaccant_room3/', reports3.viewall_vaccant_room3, name='viewall_vaccant_room3'),

    ########################################
# DUE AMT MANAGEMENT START HERE
###########################

path('view_all_due_amt3/', branch3.view_all_due_amt3, name='view_all_due_amt3'),
path('due_amt_mgt_choose_months3/', branch3.due_amt_mgt_choose_months3, name='due_amt_mgt_choose_months3'),

path('view_jan_account_details3/', branch3.view_jan_account_details3, name='view_jan_account_details3'),
path('jan_account_mgt3/<id>',branch3.jan_account_mgt3,name='jan_account_mgt3'),
path('view_feb_account_details3/', branch3.view_feb_account_details3, name='view_feb_account_details3'),
path('feb_account_mgt3/<id>',branch3.feb_account_mgt3,name='feb_account_mgt3'),
path('view_march_account_details3/', branch3.view_march_account_details3, name='view_march_account_details3'),
path('march_account_mgt3/<id>',branch3.march_account_mgt3,name='march_account_mgt3'),
path('view_april_account_details3/', branch3.view_april_account_details3, name='view_april_account_details3'),
path('april_account_mgt3/<id>',branch3.april_account_mgt3,name='april_account_mgt3'),

path('view_may_account_details3/',branch3.view_may_account_details3,name='view_may_account_details3'),
path('may_account_mgt3/<id>', branch3.may_account_mgt3, name='may_account_mgt3'),
path('view_june_account_details3/', branch3.view_june_account_details3, name='view_june_account_details3'),
path('june_account_mgt3/<id>',branch3.june_account_mgt3,name='june_account_mgt3'),
path('view_july_account_details3/', branch3.view_july_account_details3, name='view_july_account_details3'),
path('july_account_mgt3/<id>',branch3.july_account_mgt3,name='july_account_mgt3'),
path('view_auguest_account_details3/', branch3.view_auguest_account_details3, name='view_auguest_account_details3'),
path('auguest_account_mgt3/<id>',branch3.auguest_account_mgt3,name='auguest_account_mgt3'),

path('view_sept_account_details3/', branch3.view_sept_account_details3, name='view_sept_account_details3'),
path('sept_account_mgt3/<id>',branch3.sept_account_mgt3,name='sept_account_mgt3'),
path('view_october_account_details3/', branch3.view_october_account_details3, name='view_october_account_details3'),
path('october_account_mgt3/<id>',branch3.october_account_mgt3,name='october_account_mgt3'),
path('view_nov_account_details3/', branch3.view_nov_account_details3, name='view_nov_account_details3'),
path('nov_account_mgt3/<id>',branch3.nov_account_mgt3,name='nov_account_mgt3'),
path('view_dec_account_details3/', branch3.view_dec_account_details3, name='view_dec_account_details3'),
path('dec_account_mgt3/<id>',branch3.dec_account_mgt3,name='dec_account_mgt3'),


########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due3', admin_dashboard_calculations_br3.monthly_details_due3, name='monthly_details_due3'),
    path('monthly_collection_details3/', admin_dashboard_calculations_br3.monthly_collection_details3, name='monthly_collection_details3'),

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

    path('view_all_category3/', accounts3.view_all_category3, name='view_all_category3'),
    path('create_new_category3/', accounts3.create_new_category3, name='create_new_category3'),
    path('regi_new_category3/', accounts3.regi_new_category3, name='regi_new_category3'),
    path('update_category3/<id>',accounts3.update_category3,name='update_category3'),

    path('delete_category3/<id>', accounts3.delete_category3, name='delete_category3'),
    path('view_all_category_delete3/', accounts3.view_all_category_delete3, name='view_all_category_delete3'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items3/', accounts3.view_all_items3, name='view_all_items3'),
    path('create_new_item3/', accounts3.create_new_item3, name='create_new_item3'),
    path('regi_new_item3/', accounts3.regi_new_item3, name='regi_new_item3'),
    path('delete_item3/<id>',accounts3.delete_item3,name='delete_item3'),
    path('update_item3/<id>', accounts3.update_item3, name='update_item3'),
    path('view_all_items_delete3/',accounts3.view_all_items_delete3,name='view_all_items_delete3'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger3/', accounts3.view_all_ledger3, name='view_all_ledger3'),
    path('create_new_ledger3/', accounts3.create_new_ledger3, name='create_new_ledger3'),
    path('regi_new_ledger3/', accounts3.regi_new_ledger3, name='regi_new_ledger3'),
    path('delete_ledger3/<id>',accounts3.delete_ledger3,name='delete_ledger3'),
    path('update_ledger3/<id>',accounts3.update_ledger3,name='update_ledger3'),
    path('view_all_ledger_delete3/',accounts3.view_all_ledger_delete3,name='view_all_ledger_delete3'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book3/', accounts3.view_all_accounts_book3, name='view_all_accounts_book3'),
    path('create_new_accounts_book3/', accounts3.create_new_accounts_book3, name='create_new_accounts_book3'),
    path('regi_new_accounts_book3/', accounts3.regi_new_accounts_book3, name='regi_new_accounts_book3'),
    path('update_accounts_book3/<id>',accounts3.update_accounts_book3,name='update_accounts_book3'),
    path('delete_accounts_book3/<id>',accounts3.delete_accounts_book3,name='delete_accounts_book3'),
    path('view_all_accounts_book_delete3/',accounts3.view_all_accounts_book_delete3,name='view_all_accounts_book_delete3'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries3/', accounts3.get_countries3, name='get_countries3'),

    path('in_exp_items_entry3/', accounts3.in_exp_items_entry3, name='in_exp_items_entry3'),
    path('reg_in_exp_items_entry3/', accounts3.reg_in_exp_items_entry3, name='reg_in_exp_items_entry3'),
    path('delete_journal3/<id>',accounts3.delete_journal3,name='delete_journal3'),
    path('update_in_exp_items_entry3/<id>',accounts3.update_in_exp_items_entry3,name='update_in_exp_items_entry3'),
    path('detailed_journal_report3/',accounts3.detailed_journal_report3,name='detailed_journal_report3'),
    path('journal_report_deleted3/',accounts3.journal_report_deleted3,name='journal_report_deleted3'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise3/', accounts3.daily_category_wise3, name='daily_category_wise3'),
    path('monthly_category_based_reports3/',accounts3.monthly_category_based_reports3,name='monthly_category_based_reports3'),
    path('yearly_category_based_reports3/', accounts3.yearly_category_based_reports3,name='yearly_category_based_reports3'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed3/', accounts3.daily_detailed3, name='daily_detailed3'),
    path('monthly_detailed3/',accounts3.monthly_detailed3,name='monthly_detailed3'),
    path('yearly_detailed3/',accounts3.yearly_detailed3,name='yearly_detailed3'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports3/', accounts3.item_based_reports3, name='item_based_reports3'),
    path('daily_item_based_reports3/',accounts3.daily_item_based_reports3,name='daily_item_based_reports3'),
    path('monthly_item_based_reports3/',accounts3.monthly_item_based_reports3,name='monthly_item_based_reports3'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports3/', accounts3.ledger_based_reports3, name='ledger_based_reports3'),
    path('monthly_ledger_based_reports3/', accounts3.monthly_ledger_based_reports3, name='monthly_ledger_based_reports3'),
    path('daily_ledger_based_reports3/',accounts3.daily_ledger_based_reports3,name='daily_ledger_based_reports3'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports3/', accounts3.accounts_book_based_reports3, name='accounts_book_based_reports3'),
    path('daily_accounts_book_based_reports3/',accounts3.daily_accounts_book_based_reports3,name='daily_accounts_book_based_reports3'),
    path('monthly_accounts_book_based_reports3/',accounts3.monthly_accounts_book_based_reports3,name='monthly_accounts_book_based_reports3'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months3/', accounts3.monthly_reports_choose_months3, name='monthly_reports_choose_months3'),
    path('monthly_detailed_daily_in_exp_items_report3/<mo>',accounts3.monthly_detailed_daily_in_exp_items_report3,name='monthly_detailed_daily_in_exp_items_report3'),

    path('single_monthly_reports_choose_months3/', accounts3.single_monthly_reports_choose_months3,name='single_monthly_reports_choose_months3'),
    path('single_monthly_daily_in_exp_items_report3/<mo>',accounts3.single_monthly_daily_in_exp_items_report3,name='single_monthly_daily_in_exp_items_report3'),

    path('accounts_dash_board3/',accounts3.accounts_dash_board3,name='accounts_dash_board3'),



    path('profit_sharing_choose_months3', accounts3.profit_sharing_choose_months3, name='profit_sharing_choose_months3'),
    path('profit_sharing3/<mo>',accounts3.profit_sharing3,name='profit_sharing3'),
    path('view_share_holders3',accounts3.view_share_holders3,name='view_share_holders3'),
    path('create_share_holders3',accounts3.create_share_holders3,name='create_share_holders3'),
    path('regi_share_holders3', accounts3.regi_share_holders3, name='regi_share_holders3'),
    path('update_share_holders3/<id>',accounts3.update_share_holders3,name='update_share_holders3'),
    path('delete_share_holders3/<id>', accounts3.delete_share_holders3, name='delete_share_holders3'),
    path('view_deleted_share_holders3', accounts3.view_deleted_share_holders3, name='view_deleted_share_holders3'),





]