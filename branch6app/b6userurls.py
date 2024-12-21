from django.urls import path, include

#from . import admin_branch6
from . import admin_branch6
from . import branch6
from . import reports6
from . import admin_dashboard_calculations_br6
from . import payment6
from . import accounts6

urlpatterns = [
    path('branch1_dashboard6/', branch6.branch1_dashboard6, name='branch1_dashboard6'),
    path('user_dashboard_calculations_ob_ch6/',branch6.user_dashboard_calculations_ob_ch6,name='user_dashboard_calculations_ob_ch6'),

    path('background6',branch6.background6,name='background6'),
    path('background_regi6',branch6.background_regi6,name='background_regi6'),
    path('custom_background_regi6',branch6.custom_background_regi6,name='custom_background_regi6'),

#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi6/',admin_branch6.branch1_room_create_regi6,name='branch1_room_create_regi6'),
    path('view_all_room6/',admin_branch6.view_all_room6,name='view_all_room6'),
    path('delete_room6/<id>',admin_branch6.delete_room6,name='delete_room6'),

    path('branch1_room_create6/',admin_branch6.branch1_room_create6,name='branch1_room_create6'),

    path('multiple_branch1_room_create_regi6/',admin_branch6.multiple_branch1_room_create_regi6,name='multiple_branch1_room_create_regi6'),

#**room creation end here


#bed creation start here

    path('pg1_bed_create_regi6/', admin_branch6.pg1_bed_create_regi6, name='pg1_bed_create_regi6'),
    path('pg1_view_all_beds6/', admin_branch6.pg1_view_all_beds6, name='pg1_view_all_beds6'),
    path('delete_bed6/<id>', admin_branch6.delete_bed6, name='delete_bed6'),

    path('pg1_bed_create6/', admin_branch6.pg1_bed_create6, name='pg1_bed_create6'),

    path('single_pg1_bed_create_regi6/',admin_branch6.single_pg1_bed_create_regi6,name='single_pg1_bed_create_regi6'),
    path('update_bed_basic_details6/<id>',admin_branch6.update_bed_basic_details6, name='update_bed_basic_details6'),

    path('multiple_single_pg1_bed_create_regi6/',admin_branch6.multiple_single_pg1_bed_create_regi6,name='multiple_single_pg1_bed_create_regi6'),

#bed creation end here

#guest
    path('br1_admit_guest6/<id>',branch6.br1_admit_guest6,name='br1_admit_guest6'),
    path('view_all_new_guest6/',branch6.view_all_new_guest6,name='view_all_new_guest6'),
    path('update_br1_admit_guest6/<id>',branch6.update_br1_admit_guest6,name='update_br1_admit_guest6'),
    path('vacate_br1_guest6/<id>',branch6.vacate_br1_guest6,name='vacate_br1_guest6'),

    path('active_guest_details6/<guest_code>',branch6.active_guest_details6,name='active_guest_details6'),
    path('view_all_guest6/',branch6.view_all_guest6,name='view_all_guest6'),
    path('shift_guest6/<id>',branch6.shift_guest6,name='shift_guest6'),
    path('shift_guest_regi6/',branch6.shift_guest_regi6,name='shift_guest_regi6'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('multiple_br1_admit_guest6/<id>',branch6.multiple_br1_admit_guest6,name='multiple_br1_admit_guest6'),

#guest end here


#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months6/',branch6.unpaid_rent_choose_months6,name='unpaid_rent_choose_months6'),

    path('jan_unpaid_rent6/', branch6.jan_unpaid_rent6, name='jan_unpaid_rent6'),
    path('table_jan_unpaid_rent6/', branch6.table_jan_unpaid_rent6, name='table_jan_unpaid_rent6'),
    path('feb_unpaid_rent6/', branch6.feb_unpaid_rent6, name='feb_unpaid_rent6'),
    path('table_feb_unpaid_rent6/', branch6.table_feb_unpaid_rent6, name='table_feb_unpaid_rent6'),
    path('mar_unpaid_rent6/', branch6.mar_unpaid_rent6, name='mar_unpaid_rent6'),
    path('table_mar_unpaid_rent6/', branch6.table_mar_unpaid_rent6, name='table_mar_unpaid_rent6'),
    path('april_unpaid_rent6/', branch6.april_unpaid_rent6, name='april_unpaid_rent6'),
    path('table_april_unpaid_rent6/', branch6.table_april_unpaid_rent6, name='table_april_unpaid_rent6'),

    path('may_unpaid_rent6/', branch6.may_unpaid_rent6, name='may_unpaid_rent6'),
    path('table_may_unpaid_rent6/', branch6.table_may_unpaid_rent6, name='table_may_unpaid_rent6'),
    path('june_unpaid_rent6/', branch6.june_unpaid_rent6, name='june_unpaid_rent6'),
    path('table_june_unpaid_rent6/', branch6.table_june_unpaid_rent6, name='table_june_unpaid_rent6'),
    path('july_unpaid_rent6/', branch6.july_unpaid_rent6, name='july_unpaid_rent6'),
    path('table_july_unpaid_rent6',branch6.table_july_unpaid_rent6,name='table_july_unpaid_rent6'),
    path('aug_unpaid_rent6/', branch6.aug_unpaid_rent6, name='aug_unpaid_rent6'),
    path('table_aug_unpaid_rent6/',branch6.table_aug_unpaid_rent6,name='table_aug_unpaid_rent6'),

    path('sept_unpaid_rent6/', branch6.sept_unpaid_rent6, name='sept_unpaid_rent6'),
    path('table_sept_unpaid_rent6/', branch6.table_sept_unpaid_rent6, name='table_sept_unpaid_rent6'),
    path('oct_unpaid_rent6/', branch6.oct_unpaid_rent6, name='oct_unpaid_rent6'),
    path('table_oct_unpaid_rent6/', branch6.table_oct_unpaid_rent6, name='table_oct_unpaid_rent6'),
    path('nov_unpaid_rent6/', branch6.nov_unpaid_rent6, name='nov_unpaid_rent6'),
    path('table_nov_unpaid_rent6/', branch6.table_nov_unpaid_rent6, name='table_nov_unpaid_rent6'),
    path('dec_unpaid_rent6/', branch6.dec_unpaid_rent6, name='dec_unpaid_rent6'),
    path('table_dec_unpaid_rent6/', branch6.table_dec_unpaid_rent6, name='table_dec_unpaid_rent6'),

    path('details_of_unpaid_guests6/<id>',branch6.details_of_unpaid_guests6,name='details_of_unpaid_guests6'),

#unpaid rent end here

#paid rent start here


path('paid_rent_choose_months6/',branch6.paid_rent_choose_months6,name='paid_rent_choose_months6'),
path('partially_paid_guest_choose_months6/',reports6.partially_paid_guest_choose_months6,name='partially_paid_guest_choose_months6'),

path('jan_paid_rent6/', branch6.jan_paid_rent6, name='jan_paid_rent6'),
path('table_jan_paid_rent6/', branch6.table_jan_paid_rent6, name='table_jan_paid_rent6'),
path('jan_full_paid_guest6/', reports6.jan_full_paid_guest6, name='jan_full_paid_guest6'),
path('jan_partially_paid_guest6/', reports6.jan_partially_paid_guest6, name='jan_partially_paid_guest6'),
path('table_jan_partially_paid_guest6/', reports6.table_jan_partially_paid_guest6,name='table_jan_partially_paid_guest6'),

path('feb_paid_rent6/', branch6.feb_paid_rent6, name='feb_paid_rent6'),
path('table_feb_paid_rent6/', branch6.table_feb_paid_rent6, name='table_feb_paid_rent6'),
path('feb_full_paid_guest6/', reports6.feb_full_paid_guest6, name='feb_full_paid_guest6'),
path('feb_partially_paid_guest6/', reports6.feb_partially_paid_guest6, name='feb_partially_paid_guest6'),
path('table_feb_partially_paid_guest6/', reports6.table_feb_partially_paid_guest6,name='table_feb_partially_paid_guest6'),

path('mar_paid_rent6/', branch6.mar_paid_rent6, name='mar_paid_rent6'),
path('table_mar_paid_rent6/', branch6.table_mar_paid_rent6, name='table_mar_paid_rent6'),
path('march_full_paid_guest6/', reports6.march_full_paid_guest6, name='march_full_paid_guest6'),
path('march_partially_paid_guest6/', reports6.march_partially_paid_guest6, name='march_partially_paid_guest6'),
path('table_march_partially_paid_guest6/', reports6.table_march_partially_paid_guest6,name='table_march_partially_paid_guest6'),

path('april_paid_rent6/', branch6.april_paid_rent6, name='april_paid_rent6'),
path('table_april_paid_rent6/', branch6.table_april_paid_rent6, name='table_april_paid_rent6'),
path('april_full_paid_guest6/', reports6.april_full_paid_guest6, name='april_full_paid_guest6'),
path('april_partially_paid_guest6/', reports6.april_partially_paid_guest6, name='april_partially_paid_guest6'),
path('table_april_partially_paid_guest6/', reports6.table_april_partially_paid_guest6,name='table_april_partially_paid_guest6'),

path('may_paid_rent6/', branch6.may_paid_rent6, name='may_paid_rent6'),
path('table_may_paid_rent6/', branch6.table_may_paid_rent6, name='table_may_paid_rent6'),
path('may_full_paid_guest6/', reports6.may_full_paid_guest6, name='may_full_paid_guest6'),
path('may_partially_paid_guest6/', reports6.may_partially_paid_guest6, name='may_partially_paid_guest6'),
path('table_may_partially_paid_guest6/', reports6.table_may_partially_paid_guest6, name='table_may_partially_paid_guest6'),

path('june_paid_rent6/', branch6.june_paid_rent6, name='june_paid_rent6'),
path('table_june_paid_rent6/', branch6.table_june_paid_rent6, name='table_june_paid_rent6'),
path('june_full_paid_guest6/', reports6.june_full_paid_guest6, name='june_full_paid_guest6'),
path('june_partially_paid_guest6/', reports6.june_partially_paid_guest6, name='june_partially_paid_guest6'),
path('table_june_partially_paid_guest6/', reports6.table_june_partially_paid_guest6, name='table_june_partially_paid_guest6'),

path('july_paid_rent6/', branch6.july_paid_rent6, name='july_paid_rent6'),
path('table_july_paid_rent6/', branch6.table_july_paid_rent6, name='table_july_paid_rent6'),
path('july_full_paid_guest6/', reports6.july_full_paid_guest6, name='july_full_paid_guest6'),
path('july_partially_paid_guest6/', reports6.july_partially_paid_guest6, name='july_partially_paid_guest6'),
path('table_july_partially_paid_guest6/', reports6.table_july_partially_paid_guest6, name='table_july_partially_paid_guest6'),

path('aug_paid_rent6/', branch6.aug_paid_rent6, name='aug_paid_rent6'),
path('table_aug_paid_rent6/', branch6.table_aug_paid_rent6, name='table_aug_paid_rent6'),
path('auguest_full_paid_guest6/', reports6.auguest_full_paid_guest6, name='auguest_full_paid_guest6'),
path('auguest_partially_paid_guest6/', reports6.auguest_partially_paid_guest6,name='auguest_partially_paid_guest6'),
path('table_auguest_partially_paid_guest6/', reports6.table_auguest_partially_paid_guest6,name='table_auguest_partially_paid_guest6'),

path('sept_paid_rent6/', branch6.sept_paid_rent6, name='sept_paid_rent6'),
path('table_sept_paid_rent6/', branch6.table_sept_paid_rent6, name='table_sept_paid_rent6'),
path('sept_full_paid_guest6/', reports6.sept_full_paid_guest6, name='sept_full_paid_guest6'),
path('sept_partially_paid_guest6/', reports6.sept_partially_paid_guest6, name='sept_partially_paid_guest6'),
path('table_sept_partially_paid_guest6/', reports6.table_sept_partially_paid_guest6,name='table_sept_partially_paid_guest6'),

path('oct_paid_rent6/', branch6.oct_paid_rent6, name='oct_paid_rent6'),
path('table_oct_paid_rent6/', branch6.table_oct_paid_rent6, name='table_oct_paid_rent6'),
path('october_full_paid_guest6/', reports6.october_full_paid_guest6, name='october_full_paid_guest6'),
path('october_partially_paid_guest6/', reports6.october_partially_paid_guest6,name='october_partially_paid_guest6'),
path('table_october_partially_paid_guest6/', reports6.table_october_partially_paid_guest6,name='table_october_partially_paid_guest6'),

path('nov_paid_rent6/', branch6.nov_paid_rent6, name='nov_paid_rent6'),
path('table_nov_paid_rent6/', branch6.table_nov_paid_rent6, name='table_nov_paid_rent6'),
path('nov_full_paid_guest6/', reports6.nov_full_paid_guest6, name='nov_full_paid_guest6'),
path('nov_partially_paid_guest6/', reports6.nov_partially_paid_guest6, name='nov_partially_paid_guest6'),
path('table_nov_partially_paid_guest6/', reports6.table_nov_partially_paid_guest6,name='table_nov_partially_paid_guest6'),

path('dec_paid_rent6/', branch6.dec_paid_rent6, name='dec_paid_rent6'),
path('table_dec_paid_rent6/', branch6.table_dec_paid_rent6, name='table_dec_paid_rent6'),
path('dec_full_paid_guest6/', reports6.dec_full_paid_guest6, name='dec_full_paid_guest6'),
path('dec_partially_paid_guest6/', reports6.dec_partially_paid_guest6, name='dec_partially_paid_guest6'),
path('table_dec_partially_paid_guest6/', reports6.table_dec_partially_paid_guest6,name='table_dec_partially_paid_guest6'),

path('details_of_paid_guests6/<id>',branch6.details_of_paid_guests6,name='details_of_paid_guests6'),
path('full_paid_guest6/',reports6.full_paid_guest6,name='full_paid_guest6'),

path('paid_rent_choose_months6/',branch6.paid_rent_choose_months6,name='paid_rent_choose_months6'),
path('partially_paid_guest_choose_months6/',reports6.partially_paid_guest_choose_months6,name='partially_paid_guest_choose_months6'),

path('jan_paid_rent6/', branch6.jan_paid_rent6, name='jan_paid_rent6'),
path('table_jan_paid_rent6/', branch6.table_jan_paid_rent6, name='table_jan_paid_rent6'),
path('jan_full_paid_guest6/', reports6.jan_full_paid_guest6, name='jan_full_paid_guest6'),
path('jan_partially_paid_guest6/', reports6.jan_partially_paid_guest6, name='jan_partially_paid_guest6'),
path('table_jan_partially_paid_guest6/', reports6.table_jan_partially_paid_guest6,name='table_jan_partially_paid_guest6'),

path('feb_paid_rent6/', branch6.feb_paid_rent6, name='feb_paid_rent6'),
path('table_feb_paid_rent6/', branch6.table_feb_paid_rent6, name='table_feb_paid_rent6'),
path('feb_full_paid_guest6/', reports6.feb_full_paid_guest6, name='feb_full_paid_guest6'),
path('feb_partially_paid_guest6/', reports6.feb_partially_paid_guest6, name='feb_partially_paid_guest6'),
path('table_feb_partially_paid_guest6/', reports6.table_feb_partially_paid_guest6,name='table_feb_partially_paid_guest6'),

path('mar_paid_rent6/', branch6.mar_paid_rent6, name='mar_paid_rent6'),
path('table_mar_paid_rent6/', branch6.table_mar_paid_rent6, name='table_mar_paid_rent6'),
path('march_full_paid_guest6/', reports6.march_full_paid_guest6, name='march_full_paid_guest6'),
path('march_partially_paid_guest6/', reports6.march_partially_paid_guest6, name='march_partially_paid_guest6'),
path('table_march_partially_paid_guest6/', reports6.table_march_partially_paid_guest6,name='table_march_partially_paid_guest6'),

path('april_paid_rent6/', branch6.april_paid_rent6, name='april_paid_rent6'),
path('table_april_paid_rent6/', branch6.table_april_paid_rent6, name='table_april_paid_rent6'),
path('april_full_paid_guest6/', reports6.april_full_paid_guest6, name='april_full_paid_guest6'),
path('april_partially_paid_guest6/', reports6.april_partially_paid_guest6, name='april_partially_paid_guest6'),
path('table_april_partially_paid_guest6/', reports6.table_april_partially_paid_guest6,name='table_april_partially_paid_guest6'),

path('may_paid_rent6/', branch6.may_paid_rent6, name='may_paid_rent6'),
path('table_may_paid_rent6/', branch6.table_may_paid_rent6, name='table_may_paid_rent6'),
path('may_full_paid_guest6/', reports6.may_full_paid_guest6, name='may_full_paid_guest6'),
path('may_partially_paid_guest6/', reports6.may_partially_paid_guest6, name='may_partially_paid_guest6'),
path('table_may_partially_paid_guest6/', reports6.table_may_partially_paid_guest6, name='table_may_partially_paid_guest6'),

path('june_paid_rent6/', branch6.june_paid_rent6, name='june_paid_rent6'),
path('table_june_paid_rent6/', branch6.table_june_paid_rent6, name='table_june_paid_rent6'),
path('june_full_paid_guest6/', reports6.june_full_paid_guest6, name='june_full_paid_guest6'),
path('june_partially_paid_guest6/', reports6.june_partially_paid_guest6, name='june_partially_paid_guest6'),
path('table_june_partially_paid_guest6/', reports6.table_june_partially_paid_guest6, name='table_june_partially_paid_guest6'),

path('july_paid_rent6/', branch6.july_paid_rent6, name='july_paid_rent6'),
path('table_july_paid_rent6/', branch6.table_july_paid_rent6, name='table_july_paid_rent6'),
path('july_full_paid_guest6/', reports6.july_full_paid_guest6, name='july_full_paid_guest6'),
path('july_partially_paid_guest6/', reports6.july_partially_paid_guest6, name='july_partially_paid_guest6'),
path('table_july_partially_paid_guest6/', reports6.table_july_partially_paid_guest6, name='table_july_partially_paid_guest6'),

path('aug_paid_rent6/', branch6.aug_paid_rent6, name='aug_paid_rent6'),
path('table_aug_paid_rent6/', branch6.table_aug_paid_rent6, name='table_aug_paid_rent6'),
path('auguest_full_paid_guest6/', reports6.auguest_full_paid_guest6, name='auguest_full_paid_guest6'),
path('auguest_partially_paid_guest6/', reports6.auguest_partially_paid_guest6,name='auguest_partially_paid_guest6'),
path('table_auguest_partially_paid_guest6/', reports6.table_auguest_partially_paid_guest6,name='table_auguest_partially_paid_guest6'),

path('sept_paid_rent6/', branch6.sept_paid_rent6, name='sept_paid_rent6'),
path('table_sept_paid_rent6/', branch6.table_sept_paid_rent6, name='table_sept_paid_rent6'),
path('sept_full_paid_guest6/', reports6.sept_full_paid_guest6, name='sept_full_paid_guest6'),
path('sept_partially_paid_guest6/', reports6.sept_partially_paid_guest6, name='sept_partially_paid_guest6'),
path('table_sept_partially_paid_guest6/', reports6.table_sept_partially_paid_guest6,name='table_sept_partially_paid_guest6'),

path('oct_paid_rent6/', branch6.oct_paid_rent6, name='oct_paid_rent6'),
path('table_oct_paid_rent6/', branch6.table_oct_paid_rent6, name='table_oct_paid_rent6'),
path('october_full_paid_guest6/', reports6.october_full_paid_guest6, name='october_full_paid_guest6'),
path('october_partially_paid_guest6/', reports6.october_partially_paid_guest6,name='october_partially_paid_guest6'),
path('table_october_partially_paid_guest6/', reports6.table_october_partially_paid_guest6,name='table_october_partially_paid_guest6'),

path('nov_paid_rent6/', branch6.nov_paid_rent6, name='nov_paid_rent6'),
path('table_nov_paid_rent6/', branch6.table_nov_paid_rent6, name='table_nov_paid_rent6'),
path('nov_full_paid_guest6/', reports6.nov_full_paid_guest6, name='nov_full_paid_guest6'),
path('nov_partially_paid_guest6/', reports6.nov_partially_paid_guest6, name='nov_partially_paid_guest6'),
path('table_nov_partially_paid_guest6/', reports6.table_nov_partially_paid_guest6,name='table_nov_partially_paid_guest6'),

path('dec_paid_rent6/', branch6.dec_paid_rent6, name='dec_paid_rent6'),
path('table_dec_paid_rent6/', branch6.table_dec_paid_rent6, name='table_dec_paid_rent6'),
path('dec_full_paid_guest6/', reports6.dec_full_paid_guest6, name='dec_full_paid_guest6'),
path('dec_partially_paid_guest6/', reports6.dec_partially_paid_guest6, name='dec_partially_paid_guest6'),
path('table_dec_partially_paid_guest6/', reports6.table_dec_partially_paid_guest6,name='table_dec_partially_paid_guest6'),

path('details_of_paid_guests6/<id>',branch6.details_of_paid_guests6,name='details_of_paid_guests6'),
path('full_paid_guest6/',reports6.full_paid_guest6,name='full_paid_guest6'),



#paid rent end here

#*********reports end here


##################################
#_ADVANCE6 START HERE
################################


path('choose_months_advance6/',branch6.choose_months_advance6,name='choose_months_advance6'),

path('jan_advance6/', branch6.jan_advance6, name='jan_advance6'),
path('jan_make_payments_advance6/<id>', branch6.jan_make_payments_advance6,name='jan_make_payments_advance6'),
path('feb_advance6/', branch6.feb_advance6, name='feb_advance6'),
path('feb_make_payments_advance6/<id>', branch6.feb_make_payments_advance6,name='feb_make_payments_advance6'),
path('march_advance6/', branch6.march_advance6, name='march_advance6'),
path('march_make_payments_advance6/<id>', branch6.march_make_payments_advance6,name='march_make_payments_advance6'),
path('april_advance6/', branch6.april_advance6, name='april_advance6'),
path('april_make_payments_advance6/<id>', branch6.april_make_payments_advance6, name='april_make_payments_advance6'),

path('may_advance6/',branch6.may_advance6,name='may_advance6'),
path('may_make_payments_advance6/<id>', branch6.may_make_payments_advance6, name='may_make_payments_advance6'),
path('june_advance6/',branch6.june_advance6,name='june_advance6'),
path('june_make_payments_advance6/<id>', branch6.june_make_payments_advance6, name='june_make_payments_advance6'),
path('july_advance6/',branch6.july_advance6,name='july_advance6'),
path('july_make_payments_advance6/<id>', branch6.july_make_payments_advance6, name='july_make_payments_advance6'),
path('auguest_advance6/', branch6.auguest_advance6, name='auguest_advance6'),
path('auguest_make_payments_advance6/<id>', branch6.auguest_make_payments_advance6, name='auguest_make_payments_advance6'),

path('sept_advance6/', branch6.sept_advance6, name='sept_advance6'),
path('sept_make_payments_advance6/<id>', branch6.sept_make_payments_advance6,name='sept_make_payments_advance6'),
path('october_advance6/', branch6.october_advance6, name='october_advance6'),
path('october_make_payments_advance6/<id>', branch6.october_make_payments_advance6, name='october_make_payments_advance6'),
path('nov_advance6/', branch6.nov_advance6, name='nov_advance6'),
path('nov_make_payments_advance6/<id>', branch6.nov_make_payments_advance6,name='nov_make_payments_advance6'),
path('dec_advance6/', branch6.dec_advance6, name='dec_advance6'),
path('dec_make_payments_advance6/<id>', branch6.dec_make_payments_advance6, name='dec_make_payments_advance6'),



##################################
#_ADVANCE6 END HERE
################################


##################################
#PAYMENTS START HERE
################################

    path('choose_months6/',branch6.choose_months6,name='choose_months6'),

    path('jan6/',branch6.jan6,name='jan6'),
    path('jan_manke_payments6/<id>',branch6.jan_manke_payments6,name='jan_manke_payments6'),

    path('feb6/',branch6.feb6,name='feb6'),
    path('feb_manke_payments6/<id>',branch6.feb_manke_payments6,name='feb_manke_payments6'),

    path('march6/',branch6.march6,name='march6'),
    path('march_manke_payments6/<id>',branch6.march_manke_payments6,name='march_manke_payments6'),

    path('april6/',branch6.april6,name='april6'),
    path('april_make_payments6/<id>',branch6.april_make_payments6,name='april_make_payments6'),

    path('may6/',branch6.may6,name='may6'),
    path('may_make_payments6/<id>',branch6.may_make_payments6,name='may_make_payments6'),

    path('june6/',branch6.june6,name='june6'),
    path('june_make_payments6/<id>',branch6.june_make_payments6,name='june_make_payments6'),

    path('july6/',branch6.july6,name='july6'),
    path('july_make_payments6/<id>',branch6.july_make_payments6,name='july_make_payments6'),

    path('aug6/',branch6.aug6,name='aug6'),
    path('aug_make_payments6/<id>',branch6.aug_make_payments6,name='aug_make_payments6'),

    path('sept6/',branch6.sept6,name='sept6'),
    path('sept_make_payments6/<id>',branch6.sept_make_payments6,name='sept_make_payments6'),

    path('oct6/',branch6.oct6,name='oct6'),
    path('oct_make_payments6/<id>',branch6.oct_make_payments6,name='oct_make_payments6'),

    path('nov6/',branch6.nov6,name='nov6'),
    path('nov_make_payments6/<id>',branch6.nov_make_payments6,name='nov_make_payments6'),

    path('dec6/',branch6.dec6,name='dec6'),
    path('dec_make_payments6/<id>',branch6.dec_make_payments6,name='dec_make_payments6'),

##################################
#PAYMENTS END HERE
################################


##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user6/', payment6.choose_user6, name='choose_user6'),
    path('payment_user_details6/<id>', payment6.payment_user_details6, name='payment_user_details6'),
    path('close_choose_user6/<id>', payment6.close_choose_user6, name='close_choose_user6'),

    path('monthly_jan_make_payments6/<id>', payment6.monthly_jan_make_payments6, name='monthly_jan_make_payments6'),
    path('monthly_feb_make_payments6/<id>', payment6.monthly_feb_make_payments6, name='monthly_feb_make_payments6'),
    path('monthly_march_make_payments6/<id>', payment6.monthly_march_make_payments6, name='monthly_march_make_payments6'),
    path('monthly_april_make_payments6/<id>', payment6.monthly_april_make_payments6, name='monthly_april_make_payments6'),
    path('monthly_may_make_payments6/<id>', payment6.monthly_may_make_payments6, name='monthly_may_make_payments6'),
    path('monthly_june_make_payments6/<id>', payment6.monthly_june_make_payments6, name='monthly_june_make_payments6'),

    path('monthly_july_make_payments6/<id>', payment6.monthly_july_make_payments6, name='monthly_july_make_payments6'),
    path('monthly_aug_make_payments6/<id>', payment6.monthly_aug_make_payments6, name='monthly_aug_make_payments6'),
    path('monthly_sept_make_payments6/<id>', payment6.monthly_sept_make_payments6, name='monthly_sept_make_payments6'),
    path('monthly_oct_make_payments6/<id>', payment6.monthly_oct_make_payments6, name='monthly_oct_make_payments6'),
    path('monthly_nov_make_payments6/<id>', payment6.monthly_nov_make_payments6, name='monthly_nov_make_payments6'),
    path('monthly_dec_make_payments6/<id>', payment6.monthly_dec_make_payments6, name='monthly_dec_make_payments6'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################



##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general6/',branch6.detail_guest_general6,name='detail_guest_general6'),

    path('jan_print6/',branch6.jan_print6,name='jan_print6'),
    path('feb_print6/',branch6.feb_print6,name='feb_print6'),
    path('march_print6/',branch6.march_print6,name='march_print6'),
    path('april_print6/',branch6.april_print6,name='april_print6'),

    path('may_print6/',branch6.may_print6,name='may_print6'),
    path('june_print6/',branch6.june_print6,name='june_print6'),
    path('july_print6/', branch6.july_print6, name='july_print6'),
    path('aug_print6/', branch6.aug_print6, name='aug_print6'),

    path('sept_print6/', branch6.sept_print6, name='sept_print6'),
    path('oct_print6/', branch6.oct_print6, name='oct_print6'),
    path('nov_print6/', branch6.nov_print6, name='nov_print6'),
    path('dec_print6/', branch6.dec_print6, name='dec_print6'),

    path('new_year_jan_print6/', branch6.new_year_jan_print6, name='new_year_jan_print6'),

##################################
#PRINT OUTS END HERE
################################

########################################
# CLOSE MONTHS START HERE
###########################

    path('jan_close6/', branch6.jan_close6, name='jan_close6'),
    path('jan_close_decision_page6/', branch6.jan_close_decision_page6, name='jan_close_decision_page6'),
    path('feb_close/', branch6.feb_close6, name='feb_close6'),
    path('feb_close_decision_page6/', branch6.feb_close_decision_page6, name='feb_close_decision_page6'),
    path('mar_close6/', branch6.mar_close6, name='mar_close6'),
    path('mar_close_decision_page/', branch6.mar_close_decision_page6, name='mar_close_decision_page6'),
    path('apr_close6/', branch6.apr_close6, name='apr_close6'),
    path('apr_close_decision_page6/', branch6.apr_close_decision_page6, name='apr_close_decision_page6'),

    path('may_close6/', branch6.may_close6, name='may_close6'),
    path('may_close_decision_page6/', branch6.may_close_decision_page6, name='may_close_decision_page6'),
    path('jun_close6/', branch6.jun_close6, name='jun_close6'),
    path('jun_close_decision_page6/', branch6.jun_close_decision_page6, name='jun_close_decision_page6'),
    path('jul_close6/', branch6.jul_close6, name='jul_close6'),
    path('jul_close_decision_page6/', branch6.jul_close_decision_page6, name='jul_close_decision_page6'),
    path('aug_close6/', branch6.aug_close6, name='aug_close6'),
    path('aug_close_decision_page6/', branch6.aug_close_decision_page6, name='aug_close_decision_page6'),

    path('sep_close6/', branch6.sep_close6, name='sep_close6'),
    path('sep_close_decision_page6/', branch6.sep_close_decision_page6, name='sep_close_decision_page6'),
    path('oct_close6/', branch6.oct_close6, name='oct_close6'),
    path('oct_close_decision_page6/', branch6.oct_close_decision_page6, name='oct_close_decision_page6'),
    path('nov_close6/', branch6.nov_close6, name='nov_close6'),
    path('nov_close_decision_page6/', branch6.nov_close_decision_page6, name='nov_close_decision_page6'),

########################################
# CLOSE MONTHS END HERE
##########################


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months6/',reports6.detailed_report_choose_months6,name='detailed_report_choose_months6'),

    path('jan_details_live6/', reports6.jan_details_live6, name='jan_details_live6'),
    path('jan_print_live6/', reports6.jan_print_live6, name='jan_print_live6'),
    path('feb_details_live6/', reports6.feb_details_live6, name='feb_details_live6'),
    path('feb_print_live6/', reports6.feb_print_live6, name='feb_print_live6'),
    path('march_details_live6/', reports6.march_details_live6, name='march_details_live6'),
    path('march_print_live6/', reports6.march_print_live6, name='march_print_live6'),

    path('april_details_live6/', reports6.april_details_live6, name='april_details_live6'),
    path('april_print_live6/', reports6.april_print_live6, name='april_print_live6'),
    path('may_details_live6/', reports6.may_details_live6, name='may_details_live6'),
    path('may_print_live6/', reports6.may_print_live6, name='may_print_live6'),
    path('june_details_live6/',reports6.june_details_live6,name='june_details_live6'),
    path('june_print_live6/', reports6.june_print_live6, name='june_print_live6'),

    path('july_details_live6/', reports6.july_details_live6, name='july_details_live6'),
    path('july_print_live6/', reports6.july_print_live6, name='july_print_live6'),
    path('auguest_details_live6/', reports6.auguest_details_live6, name='auguest_details_live6'),
    path('auguest_print_live6/', reports6.auguest_print_live6, name='auguest_print_live6'),
    path('sept_details_live6/', reports6.sept_details_live6, name='sept_details_live6'),
    path('sept_print_live6/', reports6.sept_print_live6, name='sept_print_live6'),

    path('october_details_live6/', reports6.october_details_live6, name='october_details_live6'),
    path('october_print_live6/', reports6.october_print_live6, name='october_print_live6'),
    path('nov_details_live6/', reports6.nov_details_live6, name='nov_details_live6'),
    path('nov_print_live6/', reports6.nov_print_live6, name='nov_print_live6'),
    path('dec_details_live6/', reports6.dec_details_live6, name='dec_details_live6'),
    path('dec_print_live6/', reports6.dec_print_live6, name='dec_print_live6'),

########################################
#  DETAILED REPORT END HERE
###########################



    path('viewall_vaccant_room6/', reports6.viewall_vaccant_room6, name='viewall_vaccant_room6'),

    #path('d6/', branch6.dynamic, name='dynamic'),

    #path('manage_bed6/', branch6.manage_bed6, name='manage_bed6'),
    #path('manage_new_guest6/', branch6.manage_new_guest6, name='manage_new_guest6'),
    #path('manage_update_new_guest6/<id>', branch6.manage_update_new_guest6, name='manage_update_new_guest6'),
    #path('manage_update_beds6/<id>', branch6.manage_update_beds6, name='manage_update_beds6'),

#

########################################
# DUE AMT MANAGEMENT START HERE
###########################

path('view_all_due_amt6/', branch6.view_all_due_amt6, name='view_all_due_amt6'),
path('due_amt_mgt_choose_months6/', branch6.due_amt_mgt_choose_months6, name='due_amt_mgt_choose_months6'),

path('view_jan_account_details6/', branch6.view_jan_account_details6, name='view_jan_account_details6'),
path('jan_account_mgt6/<id>',branch6.jan_account_mgt6,name='jan_account_mgt6'),
path('view_feb_account_details6/', branch6.view_feb_account_details6, name='view_feb_account_details6'),
path('feb_account_mgt6/<id>',branch6.feb_account_mgt6,name='feb_account_mgt6'),
path('view_march_account_details6/', branch6.view_march_account_details6, name='view_march_account_details6'),
path('march_account_mgt6/<id>',branch6.march_account_mgt6,name='march_account_mgt6'),
path('view_april_account_details6/', branch6.view_april_account_details6, name='view_april_account_details6'),
path('april_account_mgt6/<id>',branch6.april_account_mgt6,name='april_account_mgt6'),

path('view_may_account_details6/',branch6.view_may_account_details6,name='view_may_account_details6'),
path('may_account_mgt6/<id>', branch6.may_account_mgt6, name='may_account_mgt6'),
path('view_june_account_details6/', branch6.view_june_account_details6, name='view_june_account_details6'),
path('june_account_mgt6/<id>',branch6.june_account_mgt6,name='june_account_mgt6'),
path('view_july_account_details6/', branch6.view_july_account_details6, name='view_july_account_details6'),
path('july_account_mgt6/<id>',branch6.july_account_mgt6,name='july_account_mgt6'),
path('view_auguest_account_details6/', branch6.view_auguest_account_details6, name='view_auguest_account_details6'),
path('auguest_account_mgt6/<id>',branch6.auguest_account_mgt6,name='auguest_account_mgt6'),

path('view_sept_account_details6/', branch6.view_sept_account_details6, name='view_sept_account_details6'),
path('sept_account_mgt6/<id>',branch6.sept_account_mgt6,name='sept_account_mgt6'),
path('view_october_account_details6/', branch6.view_october_account_details6, name='view_october_account_details6'),
path('october_account_mgt6/<id>',branch6.october_account_mgt6,name='october_account_mgt6'),
path('view_nov_account_details6/', branch6.view_nov_account_details6, name='view_nov_account_details6'),
path('nov_account_mgt6/<id>',branch6.nov_account_mgt6,name='nov_account_mgt6'),
path('view_dec_account_details6/', branch6.view_dec_account_details6, name='view_dec_account_details6'),
path('dec_account_mgt6/<id>',branch6.dec_account_mgt6,name='dec_account_mgt6'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest6/',branch6.viewall_vacate_guest6,name='viewall_vacate_guest6'),
    path('details_of_vacate_guest6/<id>',branch6.details_of_vacate_guest6,name='details_of_vacate_guest6'),
    path('full_vacated_guest_details6',branch6.full_vacated_guest_details6,name='full_vacated_guest_details6'),
    path('full_vacated_guest_table6',branch6.full_vacated_guest_table6,name='full_vacated_guest_table6'),

    path('guest_details6/<guest_code>', branch6.guest_details6, name='guest_details6'),



#********vacate guest payments start here**********

    path('jan_manke_payments_vacate6/<id>', branch6.jan_manke_payments_vacate6, name='jan_manke_payments_vacate6'),
    path('feb_manke_payments_vacate6/<id>', branch6.feb_manke_payments_vacate6, name='feb_manke_payments_vacate6'),
    path('march_manke_payments_vacate6/<id>', branch6.march_manke_payments_vacate6, name='march_manke_payments_vacate6'),
    path('april_make_payments_vacate6/<id>', branch6.april_make_payments_vacate6, name='april_make_payments_vacate6'),

    path('may_make_payments_vacate6/<id>', branch6.may_make_payments_vacate6, name='may_make_payments_vacate6'),
    path('june_make_payments_vacate6/<id>', branch6.june_make_payments_vacate6, name='june_make_payments_vacate6'),
    path('july_make_payments_vacate6/<id>', branch6.july_make_payments_vacate6, name='july_make_payments_vacate6'),
    path('aug_make_payments_vacate6/<id>', branch6.aug_make_payments_vacate6, name='aug_make_payments_vacate6'),

    path('sept_make_payments_vacate6/<id>', branch6.sept_make_payments_vacate6, name='sept_make_payments_vacate6'),
    path('oct_make_payments_vacate6/<id>', branch6.oct_make_payments_vacate6, name='oct_make_payments_vacate6'),
    path('nov_make_payments_vacate6/<id>', branch6.nov_make_payments_vacate6, name='nov_make_payments_vacate6'),
    path('dec_make_payments_vacate6/<id>', branch6.dec_make_payments_vacate6, name='dec_make_payments_vacate6'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due6', admin_dashboard_calculations_br6.monthly_details_due6, name='monthly_details_due6'),
    path('monthly_collection_details6/', admin_dashboard_calculations_br6.monthly_collection_details6, name='monthly_collection_details6'),

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

    path('view_all_category6/', accounts6.view_all_category6, name='view_all_category6'),
    path('create_new_category6/', accounts6.create_new_category6, name='create_new_category6'),
    path('regi_new_category6/', accounts6.regi_new_category6, name='regi_new_category6'),
    path('update_category6/<id>',accounts6.update_category6,name='update_category6'),

    path('delete_category6/<id>', accounts6.delete_category6, name='delete_category6'),
    path('view_all_category_delete6/', accounts6.view_all_category_delete6, name='view_all_category_delete6'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items6/', accounts6.view_all_items6, name='view_all_items6'),
    path('create_new_item6/', accounts6.create_new_item6, name='create_new_item6'),
    path('regi_new_item6/', accounts6.regi_new_item6, name='regi_new_item6'),
    path('delete_item6/<id>',accounts6.delete_item6,name='delete_item6'),
    path('update_item6/<id>', accounts6.update_item6, name='update_item6'),
    path('view_all_items_delete6/',accounts6.view_all_items_delete6,name='view_all_items_delete6'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger6/', accounts6.view_all_ledger6, name='view_all_ledger6'),
    path('create_new_ledger6/', accounts6.create_new_ledger6, name='create_new_ledger6'),
    path('regi_new_ledger6/', accounts6.regi_new_ledger6, name='regi_new_ledger6'),
    path('delete_ledger6/<id>',accounts6.delete_ledger6,name='delete_ledger6'),
    path('update_ledger6/<id>',accounts6.update_ledger6,name='update_ledger6'),
    path('view_all_ledger_delete6/',accounts6.view_all_ledger_delete6,name='view_all_ledger_delete6'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book6/', accounts6.view_all_accounts_book6, name='view_all_accounts_book6'),
    path('create_new_accounts_book6/', accounts6.create_new_accounts_book6, name='create_new_accounts_book6'),
    path('regi_new_accounts_book6/', accounts6.regi_new_accounts_book6, name='regi_new_accounts_book6'),
    path('update_accounts_book6/<id>',accounts6.update_accounts_book6,name='update_accounts_book6'),
    path('delete_accounts_book6/<id>',accounts6.delete_accounts_book6,name='delete_accounts_book6'),
    path('view_all_accounts_book_delete6/',accounts6.view_all_accounts_book_delete6,name='view_all_accounts_book_delete6'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries6/', accounts6.get_countries6, name='get_countries6'),

    path('in_exp_items_entry6/', accounts6.in_exp_items_entry6, name='in_exp_items_entry6'),
    path('reg_in_exp_items_entry6/', accounts6.reg_in_exp_items_entry6, name='reg_in_exp_items_entry6'),
    path('delete_journal6/<id>',accounts6.delete_journal6,name='delete_journal6'),
    path('update_in_exp_items_entry6/<id>',accounts6.update_in_exp_items_entry6,name='update_in_exp_items_entry6'),
    path('detailed_journal_report6/',accounts6.detailed_journal_report6,name='detailed_journal_report6'),
    path('journal_report_deleted6/',accounts6.journal_report_deleted6,name='journal_report_deleted6'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise6/', accounts6.daily_category_wise6, name='daily_category_wise6'),
    path('monthly_category_based_reports6/',accounts6.monthly_category_based_reports6,name='monthly_category_based_reports6'),
    path('yearly_category_based_reports6/', accounts6.yearly_category_based_reports6,name='yearly_category_based_reports6'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed6/', accounts6.daily_detailed6, name='daily_detailed6'),
    path('monthly_detailed6/',accounts6.monthly_detailed6,name='monthly_detailed6'),
    path('yearly_detailed6/',accounts6.yearly_detailed6,name='yearly_detailed6'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports6/', accounts6.item_based_reports6, name='item_based_reports6'),
    path('daily_item_based_reports6/',accounts6.daily_item_based_reports6,name='daily_item_based_reports6'),
    path('monthly_item_based_reports6/',accounts6.monthly_item_based_reports6,name='monthly_item_based_reports6'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports6/', accounts6.ledger_based_reports6, name='ledger_based_reports6'),
    path('monthly_ledger_based_reports6/', accounts6.monthly_ledger_based_reports6, name='monthly_ledger_based_reports6'),
    path('daily_ledger_based_reports6/',accounts6.daily_ledger_based_reports6,name='daily_ledger_based_reports6'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports6/', accounts6.accounts_book_based_reports6, name='accounts_book_based_reports6'),
    path('daily_accounts_book_based_reports6/',accounts6.daily_accounts_book_based_reports6,name='daily_accounts_book_based_reports6'),
    path('monthly_accounts_book_based_reports6/',accounts6.monthly_accounts_book_based_reports6,name='monthly_accounts_book_based_reports6'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months6/', accounts6.monthly_reports_choose_months6, name='monthly_reports_choose_months6'),
    path('monthly_detailed_daily_in_exp_items_report6/<mo>',accounts6.monthly_detailed_daily_in_exp_items_report6,name='monthly_detailed_daily_in_exp_items_report6'),

    path('single_monthly_reports_choose_months6/', accounts6.single_monthly_reports_choose_months6,name='single_monthly_reports_choose_months6'),
    path('single_monthly_daily_in_exp_items_report6/<mo>',accounts6.single_monthly_daily_in_exp_items_report6,name='single_monthly_daily_in_exp_items_report6'),

    path('accounts_dash_board6/',accounts6.accounts_dash_board6,name='accounts_dash_board6'),



    path('profit_sharing_choose_months6', accounts6.profit_sharing_choose_months6, name='profit_sharing_choose_months6'),
    path('profit_sharing6/<mo>',accounts6.profit_sharing6,name='profit_sharing6'),
    path('view_share_holders6',accounts6.view_share_holders6,name='view_share_holders6'),
    path('create_share_holders6',accounts6.create_share_holders6,name='create_share_holders6'),
    path('regi_share_holders6', accounts6.regi_share_holders6, name='regi_share_holders6'),
    path('update_share_holders6/<id>',accounts6.update_share_holders6,name='update_share_holders6'),
    path('delete_share_holders6/<id>', accounts6.delete_share_holders6, name='delete_share_holders6'),
    path('view_deleted_share_holders6', accounts6.view_deleted_share_holders6, name='view_deleted_share_holders6'),





]