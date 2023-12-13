from django.urls import path, include

from . import admin_branch12
from . import admin_branch12
from . import branch12
from . import reports12
from . import payment12
from . import admin_dashboard_calculations_br12
from . import accounts12

urlpatterns = [

    path('branch1_dashboard_ob_ch12/', branch12.branch1_dashboard_ob_ch12, name='branch1_dashboard_ob_ch12'),
    path('background_ob_ch12',branch12.background_ob_ch12,name='background_ob_ch12'),
    path('background_regi_ob_ch12',branch12.background_regi_ob_ch12,name='background_regi_ob_ch12'),
    path('custom_background_regi_ob_ch12',branch12.custom_background_regi_ob_ch12,name='custom_background_regi_ob_ch12'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch12/',admin_branch12.branch1_room_create_regi_ob_ch12,name='branch1_room_create_regi_ob_ch12'),
    path('view_all_room_ob_ch12/',admin_branch12.view_all_room_ob_ch12,name='view_all_room_ob_ch12'),
    path('delete_room_ob_ch12/<id>',admin_branch12.delete_room_ob_ch12,name='delete_room_ob_ch12'),

    path('branch1_room_create_ob_ch12/',admin_branch12.branch1_room_create_ob_ch12,name='branch1_room_create_ob_ch12'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch12/', admin_branch12.pg1_bed_create_regi_ob_ch12, name='pg1_bed_create_regi_ob_ch12'),
    path('pg1_view_all_beds_ob_ch12/', admin_branch12.pg1_view_all_beds_ob_ch12, name='pg1_view_all_beds_ob_ch12'),
    path('delete_bed_ob_ch12/<id>', admin_branch12.delete_bed_ob_ch12, name='delete_bed_ob_ch12'),

    path('pg1_bed_create_ob_ch12/', admin_branch12.pg1_bed_create_ob_ch12, name='pg1_bed_create_ob_ch12'),

    path('single_pg1_bed_create_regi_ob_ch12/',admin_branch12.single_pg1_bed_create_regi_ob_ch12,name='single_pg1_bed_create_regi_ob_ch12'),
    path('update_bed_basic_details_ob_ch12/<id>',admin_branch12.update_bed_basic_details_ob_ch12, name='update_bed_basic_details_ob_ch12'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch12/<id>',branch12.br1_admit_guest_ob_ch12,name='br1_admit_guest_ob_ch12'),
    path('view_all_new_guest_ob_ch12/',branch12.view_all_new_guest_ob_ch12,name='view_all_new_guest_ob_ch12'),
    path('update_br1_admit_guest_ob_ch12/<id>',branch12.update_br1_admit_guest_ob_ch12,name='update_br1_admit_guest_ob_ch12'),
    path('vacate_br1_guest_ob_ch12/<id>',branch12.vacate_br1_guest_ob_ch12,name='vacate_br1_guest_ob_ch12'),

    path('active_guest_details_ob_ch12/<guest_code>',branch12.active_guest_details_ob_ch12,name='active_guest_details_ob_ch12'),
    path('view_all_guest_ob_ch12/',branch12.view_all_guest_ob_ch12,name='view_all_guest_ob_ch12'),
    path('shift_guest_ob_ch12/<id>',branch12.shift_guest_ob_ch12,name='shift_guest_ob_ch12'),
    path('shift_guest_regi_ob_ch12/',branch12.shift_guest_regi_ob_ch12,name='shift_guest_regi_ob_ch12'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),

#guest end here


##################################
#_ADVANCE_ob_ch12 START HERE
################################


    path('choose_months_advance_ob_ch12/',branch12.choose_months_advance_ob_ch12,name='choose_months_advance_ob_ch12'),

    path('jan_advance_ob_ch12/', branch12.jan_advance_ob_ch12, name='jan_advance_ob_ch12'),
    path('jan_make_payments_advance_ob_ch12/<id>', branch12.jan_make_payments_advance_ob_ch12,name='jan_make_payments_advance_ob_ch12'),
    path('feb_advance_ob_ch12/', branch12.feb_advance_ob_ch12, name='feb_advance_ob_ch12'),
    path('feb_make_payments_advance_ob_ch12/<id>', branch12.feb_make_payments_advance_ob_ch12,name='feb_make_payments_advance_ob_ch12'),
    path('march_advance_ob_ch12/', branch12.march_advance_ob_ch12, name='march_advance_ob_ch12'),
    path('march_make_payments_advance_ob_ch12/<id>', branch12.march_make_payments_advance_ob_ch12,name='march_make_payments_advance_ob_ch12'),
    path('april_advance_ob_ch12/', branch12.april_advance_ob_ch12, name='april_advance_ob_ch12'),
    path('april_make_payments_advance_ob_ch12/<id>', branch12.april_make_payments_advance_ob_ch12, name='april_make_payments_advance_ob_ch12'),

    path('may_advance_ob_ch12/',branch12.may_advance_ob_ch12,name='may_advance_ob_ch12'),
    path('may_make_payments_advance_ob_ch12/<id>', branch12.may_make_payments_advance_ob_ch12, name='may_make_payments_advance_ob_ch12'),
    path('june_advance_ob_ch12/',branch12.june_advance_ob_ch12,name='june_advance_ob_ch12'),
    path('june_make_payments_advance_ob_ch12/<id>', branch12.june_make_payments_advance_ob_ch12, name='june_make_payments_advance_ob_ch12'),
    path('july_advance_ob_ch12/',branch12.july_advance_ob_ch12,name='july_advance_ob_ch12'),
    path('july_make_payments_advance_ob_ch12/<id>', branch12.july_make_payments_advance_ob_ch12, name='july_make_payments_advance_ob_ch12'),
    path('auguest_advance_ob_ch12/', branch12.auguest_advance_ob_ch12, name='auguest_advance_ob_ch12'),
    path('auguest_make_payments_advance_ob_ch12/<id>', branch12.auguest_make_payments_advance_ob_ch12, name='auguest_make_payments_advance_ob_ch12'),

    path('sept_advance_ob_ch12/', branch12.sept_advance_ob_ch12, name='sept_advance_ob_ch12'),
    path('sept_make_payments_advance_ob_ch12/<id>', branch12.sept_make_payments_advance_ob_ch12,name='sept_make_payments_advance_ob_ch12'),
    path('october_advance_ob_ch12/', branch12.october_advance_ob_ch12, name='october_advance_ob_ch12'),
    path('october_make_payments_advance_ob_ch12/<id>', branch12.october_make_payments_advance_ob_ch12, name='october_make_payments_advance_ob_ch12'),
    path('nov_advance_ob_ch12/', branch12.nov_advance_ob_ch12, name='nov_advance_ob_ch12'),
    path('nov_make_payments_advance_ob_ch12/<id>', branch12.nov_make_payments_advance_ob_ch12,name='nov_make_payments_advance_ob_ch12'),
    path('dec_advance_ob_ch12/', branch12.dec_advance_ob_ch12, name='dec_advance_ob_ch12'),
    path('dec_make_payments_advance_ob_ch12/<id>', branch12.dec_make_payments_advance_ob_ch12, name='dec_make_payments_advance_ob_ch12'),



##################################
#_ADVANCE_ob_ch12 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch12/',branch12.choose_months_ob_ch12,name='choose_months_ob_ch12'),

    path('jan_ob_ch12/',branch12.jan_ob_ch12,name='jan_ob_ch12'),
    path('jan_manke_payments_ob_ch12/<id>',branch12.jan_manke_payments_ob_ch12,name='jan_manke_payments_ob_ch12'),

    path('feb_ob_ch12/',branch12.feb_ob_ch12,name='feb_ob_ch12'),
    path('feb_manke_payments_ob_ch12/<id>',branch12.feb_manke_payments_ob_ch12,name='feb_manke_payments_ob_ch12'),

    path('march_ob_ch12/',branch12.march_ob_ch12,name='march_ob_ch12'),
    path('march_manke_payments_ob_ch12/<id>',branch12.march_manke_payments_ob_ch12,name='march_manke_payments_ob_ch12'),

    path('april_ob_ch12/',branch12.april_ob_ch12,name='april_ob_ch12'),
    path('april_make_payments_ob_ch12/<id>',branch12.april_make_payments_ob_ch12,name='april_make_payments_ob_ch12'),

    path('may_ob_ch12/',branch12.may_ob_ch12,name='may_ob_ch12'),
    path('may_make_payments_ob_ch12/<id>',branch12.may_make_payments_ob_ch12,name='may_make_payments_ob_ch12'),

    path('june_ob_ch12/',branch12.june_ob_ch12,name='june_ob_ch12'),
    path('june_make_payments_ob_ch12/<id>',branch12.june_make_payments_ob_ch12,name='june_make_payments_ob_ch12'),

    path('july_ob_ch12/',branch12.july_ob_ch12,name='july_ob_ch12'),
    path('july_make_payments_ob_ch12/<id>',branch12.july_make_payments_ob_ch12,name='july_make_payments_ob_ch12'),

    path('aug_ob_ch12/',branch12.aug_ob_ch12,name='aug_ob_ch12'),
    path('aug_make_payments_ob_ch12/<id>',branch12.aug_make_payments_ob_ch12,name='aug_make_payments_ob_ch12'),

    path('sept_ob_ch12/',branch12.sept_ob_ch12,name='sept_ob_ch12'),
    path('sept_make_payments_ob_ch12/<id>',branch12.sept_make_payments_ob_ch12,name='sept_make_payments_ob_ch12'),

    path('oct_ob_ch12/',branch12.oct_ob_ch12,name='oct_ob_ch12'),
    path('oct_make_payments_ob_ch12/<id>',branch12.oct_make_payments_ob_ch12,name='oct_make_payments_ob_ch12'),

    path('nov_ob_ch12/',branch12.nov_ob_ch12,name='nov_ob_ch12'),
    path('nov_make_payments_ob_ch12/<id>',branch12.nov_make_payments_ob_ch12,name='nov_make_payments_ob_ch12'),

    path('dec_ob_ch12/',branch12.dec_ob_ch12,name='dec_ob_ch12'),
    path('dec_make_payments_ob_ch12/<id>',branch12.dec_make_payments_ob_ch12,name='dec_make_payments_ob_ch12'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch12/', payment12.choose_user_ob_ch12, name='choose_user_ob_ch12'),
    path('payment_user_details_ob_ch12/<id>', payment12.payment_user_details_ob_ch12, name='payment_user_details_ob_ch12'),
    path('close_choose_user_ob_ch12/<id>',payment12.close_choose_user_ob_ch12,name='close_choose_user_ob_ch12'),

    path('monthly_jan_make_payments_ob_ch12/<id>', payment12.monthly_jan_make_payments_ob_ch12, name='monthly_jan_make_payments_ob_ch12'),
    path('monthly_feb_make_payments_ob_ch12/<id>', payment12.monthly_feb_make_payments_ob_ch12, name='monthly_feb_make_payments_ob_ch12'),
    path('monthly_march_make_payments_ob_ch12/<id>', payment12.monthly_march_make_payments_ob_ch12, name='monthly_march_make_payments_ob_ch12'),
    path('monthly_april_make_payments_ob_ch12/<id>', payment12.monthly_april_make_payments_ob_ch12, name='monthly_april_make_payments_ob_ch12'),
    path('monthly_may_make_payments_ob_ch12/<id>', payment12.monthly_may_make_payments_ob_ch12, name='monthly_may_make_payments_ob_ch12'),
    path('monthly_june_make_payments_ob_ch12/<id>', payment12.monthly_june_make_payments_ob_ch12, name='monthly_june_make_payments_ob_ch12'),

    path('monthly_july_make_payments_ob_ch12/<id>', payment12.monthly_july_make_payments_ob_ch12, name='monthly_july_make_payments_ob_ch12'),
    path('monthly_aug_make_payments_ob_ch12/<id>', payment12.monthly_aug_make_payments_ob_ch12, name='monthly_aug_make_payments_ob_ch12'),
    path('monthly_sept_make_payments_ob_ch12/<id>', payment12.monthly_sept_make_payments_ob_ch12, name='monthly_sept_make_payments_ob_ch12'),
    path('monthly_oct_make_payments_ob_ch12/<id>', payment12.monthly_oct_make_payments_ob_ch12, name='monthly_oct_make_payments_ob_ch12'),
    path('monthly_nov_make_payments_ob_ch12/<id>', payment12.monthly_nov_make_payments_ob_ch12, name='monthly_nov_make_payments_ob_ch12'),
    path('monthly_dec_make_payments_ob_ch12/<id>', payment12.monthly_dec_make_payments_ob_ch12, name='monthly_dec_make_payments_ob_ch12'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch12/',branch12.unpaid_rent_choose_months_ob_ch12,name='unpaid_rent_choose_months_ob_ch12'),

    path('jan_unpaid_rent_ob_ch12/', branch12.jan_unpaid_rent_ob_ch12, name='jan_unpaid_rent_ob_ch12'),
    path('table_jan_unpaid_rent_ob_ch12/', branch12.table_jan_unpaid_rent_ob_ch12, name='table_jan_unpaid_rent_ob_ch12'),
    path('feb_unpaid_rent_ob_ch12/', branch12.feb_unpaid_rent_ob_ch12, name='feb_unpaid_rent_ob_ch12'),
    path('table_feb_unpaid_rent_ob_ch12/', branch12.table_feb_unpaid_rent_ob_ch12, name='table_feb_unpaid_rent_ob_ch12'),
    path('mar_unpaid_rent_ob_ch12/', branch12.mar_unpaid_rent_ob_ch12, name='mar_unpaid_rent_ob_ch12'),
    path('table_mar_unpaid_rent_ob_ch12/', branch12.table_mar_unpaid_rent_ob_ch12, name='table_mar_unpaid_rent_ob_ch12'),
    path('april_unpaid_rent_ob_ch12/', branch12.april_unpaid_rent_ob_ch12, name='april_unpaid_rent_ob_ch12'),
    path('table_april_unpaid_rent_ob_ch12/', branch12.table_april_unpaid_rent_ob_ch12, name='table_april_unpaid_rent_ob_ch12'),

    path('may_unpaid_rent_ob_ch12/', branch12.may_unpaid_rent_ob_ch12, name='may_unpaid_rent_ob_ch12'),
    path('table_may_unpaid_rent_ob_ch12/', branch12.table_may_unpaid_rent_ob_ch12, name='table_may_unpaid_rent_ob_ch12'),
    path('june_unpaid_rent_ob_ch12/', branch12.june_unpaid_rent_ob_ch12, name='june_unpaid_rent_ob_ch12'),
    path('table_june_unpaid_rent_ob_ch12/', branch12.table_june_unpaid_rent_ob_ch12, name='table_june_unpaid_rent_ob_ch12'),
    path('july_unpaid_rent_ob_ch12/', branch12.july_unpaid_rent_ob_ch12, name='july_unpaid_rent_ob_ch12'),
    path('table_july_unpaid_rent_ob_ch12',branch12.table_july_unpaid_rent_ob_ch12,name='table_july_unpaid_rent_ob_ch12'),
    path('aug_unpaid_rent_ob_ch12/', branch12.aug_unpaid_rent_ob_ch12, name='aug_unpaid_rent_ob_ch12'),
    path('table_aug_unpaid_rent_ob_ch12/',branch12.table_aug_unpaid_rent_ob_ch12,name='table_aug_unpaid_rent_ob_ch12'),

    path('sept_unpaid_rent_ob_ch12/', branch12.sept_unpaid_rent_ob_ch12, name='sept_unpaid_rent_ob_ch12'),
    path('table_sept_unpaid_rent_ob_ch12/', branch12.table_sept_unpaid_rent_ob_ch12, name='table_sept_unpaid_rent_ob_ch12'),
    path('oct_unpaid_rent_ob_ch12/', branch12.oct_unpaid_rent_ob_ch12, name='oct_unpaid_rent_ob_ch12'),
    path('table_oct_unpaid_rent_ob_ch12/', branch12.table_oct_unpaid_rent_ob_ch12, name='table_oct_unpaid_rent_ob_ch12'),
    path('nov_unpaid_rent_ob_ch12/', branch12.nov_unpaid_rent_ob_ch12, name='nov_unpaid_rent_ob_ch12'),
    path('table_nov_unpaid_rent_ob_ch12/', branch12.table_nov_unpaid_rent_ob_ch12, name='table_nov_unpaid_rent_ob_ch12'),
    path('dec_unpaid_rent_ob_ch12/', branch12.dec_unpaid_rent_ob_ch12, name='dec_unpaid_rent_ob_ch12'),
    path('table_dec_unpaid_rent_ob_ch12/', branch12.table_dec_unpaid_rent_ob_ch12, name='table_dec_unpaid_rent_ob_ch12'),

    path('details_of_unpaid_guests_ob_ch12/<id>',branch12.details_of_unpaid_guests_ob_ch12,name='details_of_unpaid_guests_ob_ch12'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch12/',branch12.paid_rent_choose_months_ob_ch12,name='paid_rent_choose_months_ob_ch12'),
    path('partially_paid_guest_choose_months_ob_ch12/',reports12.partially_paid_guest_choose_months_ob_ch12,name='partially_paid_guest_choose_months_ob_ch12'),

    path('jan_paid_rent_ob_ch12/', branch12.jan_paid_rent_ob_ch12, name='jan_paid_rent_ob_ch12'),
    path('table_jan_paid_rent_ob_ch12/', branch12.table_jan_paid_rent_ob_ch12, name='table_jan_paid_rent_ob_ch12'),
    path('jan_full_paid_guest_ob_ch12/', reports12.jan_full_paid_guest_ob_ch12, name='jan_full_paid_guest_ob_ch12'),
    path('jan_partially_paid_guest_ob_ch12/', reports12.jan_partially_paid_guest_ob_ch12, name='jan_partially_paid_guest_ob_ch12'),
    path('table_jan_partially_paid_guest_ob_ch12/', reports12.table_jan_partially_paid_guest_ob_ch12,name='table_jan_partially_paid_guest_ob_ch12'),

    path('feb_paid_rent_ob_ch12/', branch12.feb_paid_rent_ob_ch12, name='feb_paid_rent_ob_ch12'),
    path('table_feb_paid_rent_ob_ch12/', branch12.table_feb_paid_rent_ob_ch12, name='table_feb_paid_rent_ob_ch12'),
    path('feb_full_paid_guest_ob_ch12/', reports12.feb_full_paid_guest_ob_ch12, name='feb_full_paid_guest_ob_ch12'),
    path('feb_partially_paid_guest_ob_ch12/', reports12.feb_partially_paid_guest_ob_ch12, name='feb_partially_paid_guest_ob_ch12'),
    path('table_feb_partially_paid_guest_ob_ch12/', reports12.table_feb_partially_paid_guest_ob_ch12,name='table_feb_partially_paid_guest_ob_ch12'),

    path('mar_paid_rent_ob_ch12/', branch12.mar_paid_rent_ob_ch12, name='mar_paid_rent_ob_ch12'),
    path('table_mar_paid_rent_ob_ch12/', branch12.table_mar_paid_rent_ob_ch12, name='table_mar_paid_rent_ob_ch12'),
    path('march_full_paid_guest_ob_ch12/', reports12.march_full_paid_guest_ob_ch12, name='march_full_paid_guest_ob_ch12'),
    path('march_partially_paid_guest_ob_ch12/', reports12.march_partially_paid_guest_ob_ch12, name='march_partially_paid_guest_ob_ch12'),
    path('table_march_partially_paid_guest_ob_ch12/', reports12.table_march_partially_paid_guest_ob_ch12,name='table_march_partially_paid_guest_ob_ch12'),

    path('april_paid_rent_ob_ch12/', branch12.april_paid_rent_ob_ch12, name='april_paid_rent_ob_ch12'),
    path('table_april_paid_rent_ob_ch12/', branch12.table_april_paid_rent_ob_ch12, name='table_april_paid_rent_ob_ch12'),
    path('april_full_paid_guest_ob_ch12/', reports12.april_full_paid_guest_ob_ch12, name='april_full_paid_guest_ob_ch12'),
    path('april_partially_paid_guest_ob_ch12/', reports12.april_partially_paid_guest_ob_ch12, name='april_partially_paid_guest_ob_ch12'),
    path('table_april_partially_paid_guest_ob_ch12/', reports12.table_april_partially_paid_guest_ob_ch12,name='table_april_partially_paid_guest_ob_ch12'),

    path('may_paid_rent_ob_ch12/', branch12.may_paid_rent_ob_ch12, name='may_paid_rent_ob_ch12'),
    path('table_may_paid_rent_ob_ch12/', branch12.table_may_paid_rent_ob_ch12, name='table_may_paid_rent_ob_ch12'),
    path('may_full_paid_guest_ob_ch12/', reports12.may_full_paid_guest_ob_ch12, name='may_full_paid_guest_ob_ch12'),
    path('may_partially_paid_guest_ob_ch12/', reports12.may_partially_paid_guest_ob_ch12, name='may_partially_paid_guest_ob_ch12'),
    path('table_may_partially_paid_guest_ob_ch12/', reports12.table_may_partially_paid_guest_ob_ch12, name='table_may_partially_paid_guest_ob_ch12'),

    path('june_paid_rent_ob_ch12/', branch12.june_paid_rent_ob_ch12, name='june_paid_rent_ob_ch12'),
    path('table_june_paid_rent_ob_ch12/', branch12.table_june_paid_rent_ob_ch12, name='table_june_paid_rent_ob_ch12'),
    path('june_full_paid_guest_ob_ch12/', reports12.june_full_paid_guest_ob_ch12, name='june_full_paid_guest_ob_ch12'),
    path('june_partially_paid_guest_ob_ch12/', reports12.june_partially_paid_guest_ob_ch12, name='june_partially_paid_guest_ob_ch12'),
    path('table_june_partially_paid_guest_ob_ch12/', reports12.table_june_partially_paid_guest_ob_ch12, name='table_june_partially_paid_guest_ob_ch12'),

    path('july_paid_rent_ob_ch12/', branch12.july_paid_rent_ob_ch12, name='july_paid_rent_ob_ch12'),
    path('table_july_paid_rent_ob_ch12/', branch12.table_july_paid_rent_ob_ch12, name='table_july_paid_rent_ob_ch12'),
    path('july_full_paid_guest_ob_ch12/', reports12.july_full_paid_guest_ob_ch12, name='july_full_paid_guest_ob_ch12'),
    path('july_partially_paid_guest_ob_ch12/', reports12.july_partially_paid_guest_ob_ch12, name='july_partially_paid_guest_ob_ch12'),
    path('table_july_partially_paid_guest_ob_ch12/', reports12.table_july_partially_paid_guest_ob_ch12, name='table_july_partially_paid_guest_ob_ch12'),

    path('aug_paid_rent_ob_ch12/', branch12.aug_paid_rent_ob_ch12, name='aug_paid_rent_ob_ch12'),
    path('table_aug_paid_rent_ob_ch12/', branch12.table_aug_paid_rent_ob_ch12, name='table_aug_paid_rent_ob_ch12'),
    path('auguest_full_paid_guest_ob_ch12/', reports12.auguest_full_paid_guest_ob_ch12, name='auguest_full_paid_guest_ob_ch12'),
    path('auguest_partially_paid_guest_ob_ch12/', reports12.auguest_partially_paid_guest_ob_ch12,name='auguest_partially_paid_guest_ob_ch12'),
    path('table_auguest_partially_paid_guest_ob_ch12/', reports12.table_auguest_partially_paid_guest_ob_ch12,name='table_auguest_partially_paid_guest_ob_ch12'),

    path('sept_paid_rent_ob_ch12/', branch12.sept_paid_rent_ob_ch12, name='sept_paid_rent_ob_ch12'),
    path('table_sept_paid_rent_ob_ch12/', branch12.table_sept_paid_rent_ob_ch12, name='table_sept_paid_rent_ob_ch12'),
    path('sept_full_paid_guest_ob_ch12/', reports12.sept_full_paid_guest_ob_ch12, name='sept_full_paid_guest_ob_ch12'),
    path('sept_partially_paid_guest_ob_ch12/', reports12.sept_partially_paid_guest_ob_ch12, name='sept_partially_paid_guest_ob_ch12'),
    path('table_sept_partially_paid_guest_ob_ch12/', reports12.table_sept_partially_paid_guest_ob_ch12,name='table_sept_partially_paid_guest_ob_ch12'),

    path('oct_paid_rent_ob_ch12/', branch12.oct_paid_rent_ob_ch12, name='oct_paid_rent_ob_ch12'),
    path('table_oct_paid_rent_ob_ch12/', branch12.table_oct_paid_rent_ob_ch12, name='table_oct_paid_rent_ob_ch12'),
    path('october_full_paid_guest_ob_ch12/', reports12.october_full_paid_guest_ob_ch12, name='october_full_paid_guest_ob_ch12'),
    path('october_partially_paid_guest_ob_ch12/', reports12.october_partially_paid_guest_ob_ch12,name='october_partially_paid_guest_ob_ch12'),
    path('table_october_partially_paid_guest_ob_ch12/', reports12.table_october_partially_paid_guest_ob_ch12,name='table_october_partially_paid_guest_ob_ch12'),

    path('nov_paid_rent_ob_ch12/', branch12.nov_paid_rent_ob_ch12, name='nov_paid_rent_ob_ch12'),
    path('table_nov_paid_rent_ob_ch12/', branch12.table_nov_paid_rent_ob_ch12, name='table_nov_paid_rent_ob_ch12'),
    path('nov_full_paid_guest_ob_ch12/', reports12.nov_full_paid_guest_ob_ch12, name='nov_full_paid_guest_ob_ch12'),
    path('nov_partially_paid_guest_ob_ch12/', reports12.nov_partially_paid_guest_ob_ch12, name='nov_partially_paid_guest_ob_ch12'),
    path('table_nov_partially_paid_guest_ob_ch12/', reports12.table_nov_partially_paid_guest_ob_ch12,name='table_nov_partially_paid_guest_ob_ch12'),

    path('dec_paid_rent_ob_ch12/', branch12.dec_paid_rent_ob_ch12, name='dec_paid_rent_ob_ch12'),
    path('table_dec_paid_rent_ob_ch12/', branch12.table_dec_paid_rent_ob_ch12, name='table_dec_paid_rent_ob_ch12'),
    path('dec_full_paid_guest_ob_ch12/', reports12.dec_full_paid_guest_ob_ch12, name='dec_full_paid_guest_ob_ch12'),
    path('dec_partially_paid_guest_ob_ch12/', reports12.dec_partially_paid_guest_ob_ch12, name='dec_partially_paid_guest_ob_ch12'),
    path('table_dec_partially_paid_guest_ob_ch12/', reports12.table_dec_partially_paid_guest_ob_ch12,name='table_dec_partially_paid_guest_ob_ch12'),

    path('details_of_paid_guests_ob_ch12/<id>',branch12.details_of_paid_guests_ob_ch12,name='details_of_paid_guests_ob_ch12'),
    path('full_paid_guest_ob_ch12/',reports12.full_paid_guest_ob_ch12,name='full_paid_guest_ob_ch12'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch12/',branch12.viewall_vacate_guest_ob_ch12,name='viewall_vacate_guest_ob_ch12'),
    path('details_of_vacate_guest_ob_ch12/<id>',branch12.details_of_vacate_guest_ob_ch12,name='details_of_vacate_guest_ob_ch12'),
    path('full_vacated_guest_details_ob_ch12',branch12.full_vacated_guest_details_ob_ch12,name='full_vacated_guest_details_ob_ch12'),
    path('full_vacated_guest_table_ob_ch12',branch12.full_vacated_guest_table_ob_ch12,name='full_vacated_guest_table_ob_ch12'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch12/<id>', branch12.jan_manke_payments_vacate_ob_ch12, name='jan_manke_payments_vacate_ob_ch12'),
    path('feb_manke_payments_vacate_ob_ch12/<id>', branch12.feb_manke_payments_vacate_ob_ch12, name='feb_manke_payments_vacate_ob_ch12'),
    path('march_manke_payments_vacate_ob_ch12/<id>', branch12.march_manke_payments_vacate_ob_ch12, name='march_manke_payments_vacate_ob_ch12'),
    path('april_make_payments_vacate_ob_ch12/<id>', branch12.april_make_payments_vacate_ob_ch12, name='april_make_payments_vacate_ob_ch12'),

    path('may_make_payments_vacate_ob_ch12/<id>', branch12.may_make_payments_vacate_ob_ch12, name='may_make_payments_vacate_ob_ch12'),
    path('june_make_payments_vacate_ob_ch12/<id>', branch12.june_make_payments_vacate_ob_ch12, name='june_make_payments_vacate_ob_ch12'),
    path('july_make_payments_vacate_ob_ch12/<id>', branch12.july_make_payments_vacate_ob_ch12, name='july_make_payments_vacate_ob_ch12'),
    path('aug_make_payments_vacate_ob_ch12/<id>', branch12.aug_make_payments_vacate_ob_ch12, name='aug_make_payments_vacate_ob_ch12'),

    path('sept_make_payments_vacate_ob_ch12/<id>', branch12.sept_make_payments_vacate_ob_ch12, name='sept_make_payments_vacate_ob_ch12'),
    path('oct_make_payments_vacate_ob_ch12/<id>', branch12.oct_make_payments_vacate_ob_ch12, name='oct_make_payments_vacate_ob_ch12'),
    path('nov_make_payments_vacate_ob_ch12/<id>', branch12.nov_make_payments_vacate_ob_ch12, name='nov_make_payments_vacate_ob_ch12'),
    path('dec_make_payments_vacate_ob_ch12/<id>', branch12.dec_make_payments_vacate_ob_ch12, name='dec_make_payments_vacate_ob_ch12'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch12/',branch12.detail_guest_general_ob_ch12,name='detail_guest_general_ob_ch12'),

    path('jan_print_ob_ch12/',branch12.jan_print_ob_ch12,name='jan_print_ob_ch12'),
    path('feb_print_ob_ch12/',branch12.feb_print_ob_ch12,name='feb_print_ob_ch12'),
    path('march_print_ob_ch12/',branch12.march_print_ob_ch12,name='march_print_ob_ch12'),
    path('april_print_ob_ch12/',branch12.april_print_ob_ch12,name='april_print_ob_ch12'),

    path('may_print_ob_ch12/',branch12.may_print_ob_ch12,name='may_print_ob_ch12'),
    path('june_print_ob_ch12/',branch12.june_print_ob_ch12,name='june_print_ob_ch12'),
    path('july_print_ob_ch12/', branch12.july_print_ob_ch12, name='july_print_ob_ch12'),
    path('aug_print_ob_ch12/', branch12.aug_print_ob_ch12, name='aug_print_ob_ch12'),

    path('sept_print_ob_ch12/', branch12.sept_print_ob_ch12, name='sept_print_ob_ch12'),
    path('oct_print_ob_ch12/', branch12.oct_print_ob_ch12, name='oct_print_ob_ch12'),
    path('nov_print_ob_ch12/', branch12.nov_print_ob_ch12, name='nov_print_ob_ch12'),
    path('dec_print_ob_ch12/', branch12.dec_print_ob_ch12, name='dec_print_ob_ch12'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch12/', branch12.jan_close_ob_ch12, name='jan_close_ob_ch12'),
    path('jan_close_decision_page_ob_ch12/', branch12.jan_close_decision_page_ob_ch12, name='jan_close_decision_page_ob_ch12'),
    path('feb_close/', branch12.feb_close_ob_ch12, name='feb_close_ob_ch12'),
    path('feb_close_decision_page_ob_ch12/', branch12.feb_close_decision_page_ob_ch12, name='feb_close_decision_page_ob_ch12'),
    path('mar_close_ob_ch12/', branch12.mar_close_ob_ch12, name='mar_close_ob_ch12'),
    path('mar_close_decision_page/', branch12.mar_close_decision_page_ob_ch12, name='mar_close_decision_page_ob_ch12'),
    path('apr_close_ob_ch12/', branch12.apr_close_ob_ch12, name='apr_close_ob_ch12'),
    path('apr_close_decision_page_ob_ch12/', branch12.apr_close_decision_page_ob_ch12, name='apr_close_decision_page_ob_ch12'),

    path('may_close_ob_ch12/', branch12.may_close_ob_ch12, name='may_close_ob_ch12'),
    path('may_close_decision_page_ob_ch12/', branch12.may_close_decision_page_ob_ch12, name='may_close_decision_page_ob_ch12'),
    path('jun_close_ob_ch12/', branch12.jun_close_ob_ch12, name='jun_close_ob_ch12'),
    path('jun_close_decision_page_ob_ch12/', branch12.jun_close_decision_page_ob_ch12, name='jun_close_decision_page_ob_ch12'),
    path('jul_close_ob_ch12/', branch12.jul_close_ob_ch12, name='jul_close_ob_ch12'),
    path('jul_close_decision_page_ob_ch12/', branch12.jul_close_decision_page_ob_ch12, name='jul_close_decision_page_ob_ch12'),
    path('aug_close_ob_ch12/', branch12.aug_close_ob_ch12, name='aug_close_ob_ch12'),
    path('aug_close_decision_page_ob_ch12/', branch12.aug_close_decision_page_ob_ch12, name='aug_close_decision_page_ob_ch12'),

    path('sep_close_ob_ch12/', branch12.sep_close_ob_ch12, name='sep_close_ob_ch12'),
    path('sep_close_decision_page_ob_ch12/', branch12.sep_close_decision_page_ob_ch12, name='sep_close_decision_page_ob_ch12'),
    path('oct_close_ob_ch12/', branch12.oct_close_ob_ch12, name='oct_close_ob_ch12'),
    path('oct_close_decision_page_ob_ch12/', branch12.oct_close_decision_page_ob_ch12, name='oct_close_decision_page_ob_ch12'),
    path('nov_close_ob_ch12/', branch12.nov_close_ob_ch12, name='nov_close_ob_ch12'),
    path('nov_close_decision_page_ob_ch12/', branch12.nov_close_decision_page_ob_ch12, name='nov_close_decision_page_ob_ch12'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch12/',reports12.detailed_report_choose_months_ob_ch12,name='detailed_report_choose_months_ob_ch12'),

    path('jan_details_live_ob_ch12/', reports12.jan_details_live_ob_ch12, name='jan_details_live_ob_ch12'),
    path('jan_print_live_ob_ch12/', reports12.jan_print_live_ob_ch12, name='jan_print_live_ob_ch12'),
    path('feb_details_live_ob_ch12/', reports12.feb_details_live_ob_ch12, name='feb_details_live_ob_ch12'),
    path('feb_print_live_ob_ch12/', reports12.feb_print_live_ob_ch12, name='feb_print_live_ob_ch12'),
    path('march_details_live_ob_ch12/', reports12.march_details_live_ob_ch12, name='march_details_live_ob_ch12'),
    path('march_print_live_ob_ch12/', reports12.march_print_live_ob_ch12, name='march_print_live_ob_ch12'),

    path('april_details_live_ob_ch12/', reports12.april_details_live_ob_ch12, name='april_details_live_ob_ch12'),
    path('april_print_live_ob_ch12/', reports12.april_print_live_ob_ch12, name='april_print_live_ob_ch12'),
    path('may_details_live_ob_ch12/', reports12.may_details_live_ob_ch12, name='may_details_live_ob_ch12'),
    path('may_print_live_ob_ch12/', reports12.may_print_live_ob_ch12, name='may_print_live_ob_ch12'),
    path('june_details_live_ob_ch12/',reports12.june_details_live_ob_ch12,name='june_details_live_ob_ch12'),
    path('june_print_live_ob_ch12/', reports12.june_print_live_ob_ch12, name='june_print_live_ob_ch12'),

    path('july_details_live_ob_ch12/', reports12.july_details_live_ob_ch12, name='july_details_live_ob_ch12'),
    path('july_print_live_ob_ch12/', reports12.july_print_live_ob_ch12, name='july_print_live_ob_ch12'),
    path('auguest_details_live_ob_ch12/', reports12.auguest_details_live_ob_ch12, name='auguest_details_live_ob_ch12'),
    path('auguest_print_live_ob_ch12/', reports12.auguest_print_live_ob_ch12, name='auguest_print_live_ob_ch12'),
    path('sept_details_live_ob_ch12/', reports12.sept_details_live_ob_ch12, name='sept_details_live_ob_ch12'),
    path('sept_print_live_ob_ch12/', reports12.sept_print_live_ob_ch12, name='sept_print_live_ob_ch12'),

    path('october_details_live_ob_ch12/', reports12.october_details_live_ob_ch12, name='october_details_live_ob_ch12'),
    path('october_print_live_ob_ch12/', reports12.october_print_live_ob_ch12, name='october_print_live_ob_ch12'),
    path('nov_details_live_ob_ch12/', reports12.nov_details_live_ob_ch12, name='nov_details_live_ob_ch12'),
    path('nov_print_live_ob_ch12/', reports12.nov_print_live_ob_ch12, name='nov_print_live_ob_ch12'),
    path('dec_details_live_ob_ch12/', reports12.dec_details_live_ob_ch12, name='dec_details_live_ob_ch12'),
    path('dec_print_live_ob_ch12/', reports12.dec_print_live_ob_ch12, name='dec_print_live_ob_ch12'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch12/', reports12.viewall_vaccant_room_ob_ch12, name='viewall_vaccant_room_ob_ch12'),

    path('d_ob_ch12/', branch12.dynamic, name='dynamic'),

    path('manage_bed_ob_ch12/', branch12.manage_bed_ob_ch12, name='manage_bed_ob_ch12'),
    path('manage_new_guest_ob_ch12/', branch12.manage_new_guest_ob_ch12, name='manage_new_guest_ob_ch12'),
    path('manage_update_new_guest_ob_ch12/<id>', branch12.manage_update_new_guest_ob_ch12, name='manage_update_new_guest_ob_ch12'),
    path('manage_update_beds_ob_ch12/<id>', branch12.manage_update_beds_ob_ch12, name='manage_update_beds_ob_ch12'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch12/', branch12.view_all_due_amt_ob_ch12, name='view_all_due_amt_ob_ch12'),
    path('due_amt_mgt_choose_months_ob_ch12/', branch12.due_amt_mgt_choose_months_ob_ch12, name='due_amt_mgt_choose_months_ob_ch12'),

    path('view_jan_account_details_ob_ch12/', branch12.view_jan_account_details_ob_ch12, name='view_jan_account_details_ob_ch12'),
    path('jan_account_mgt_ob_ch12/<id>',branch12.jan_account_mgt_ob_ch12,name='jan_account_mgt_ob_ch12'),
    path('view_feb_account_details_ob_ch12/', branch12.view_feb_account_details_ob_ch12, name='view_feb_account_details_ob_ch12'),
    path('feb_account_mgt_ob_ch12/<id>',branch12.feb_account_mgt_ob_ch12,name='feb_account_mgt_ob_ch12'),
    path('view_march_account_details_ob_ch12/', branch12.view_march_account_details_ob_ch12, name='view_march_account_details_ob_ch12'),
    path('march_account_mgt_ob_ch12/<id>',branch12.march_account_mgt_ob_ch12,name='march_account_mgt_ob_ch12'),
    path('view_april_account_details_ob_ch12/', branch12.view_april_account_details_ob_ch12, name='view_april_account_details_ob_ch12'),
    path('april_account_mgt_ob_ch12/<id>',branch12.april_account_mgt_ob_ch12,name='april_account_mgt_ob_ch12'),

    path('view_may_account_details_ob_ch12/',branch12.view_may_account_details_ob_ch12,name='view_may_account_details_ob_ch12'),
    path('may_account_mgt_ob_ch12/<id>', branch12.may_account_mgt_ob_ch12, name='may_account_mgt_ob_ch12'),
    path('view_june_account_details_ob_ch12/', branch12.view_june_account_details_ob_ch12, name='view_june_account_details_ob_ch12'),
    path('june_account_mgt_ob_ch12/<id>',branch12.june_account_mgt_ob_ch12,name='june_account_mgt_ob_ch12'),
    path('view_july_account_details_ob_ch12/', branch12.view_july_account_details_ob_ch12, name='view_july_account_details_ob_ch12'),
    path('july_account_mgt_ob_ch12/<id>',branch12.july_account_mgt_ob_ch12,name='july_account_mgt_ob_ch12'),
    path('view_auguest_account_details_ob_ch12/', branch12.view_auguest_account_details_ob_ch12, name='view_auguest_account_details_ob_ch12'),
    path('auguest_account_mgt_ob_ch12/<id>',branch12.auguest_account_mgt_ob_ch12,name='auguest_account_mgt_ob_ch12'),

    path('view_sept_account_details_ob_ch12/', branch12.view_sept_account_details_ob_ch12, name='view_sept_account_details_ob_ch12'),
    path('sept_account_mgt_ob_ch12/<id>',branch12.sept_account_mgt_ob_ch12,name='sept_account_mgt_ob_ch12'),
    path('view_october_account_details_ob_ch12/', branch12.view_october_account_details_ob_ch12, name='view_october_account_details_ob_ch12'),
    path('october_account_mgt_ob_ch12/<id>',branch12.october_account_mgt_ob_ch12,name='october_account_mgt_ob_ch12'),
    path('view_nov_account_details_ob_ch12/', branch12.view_nov_account_details_ob_ch12, name='view_nov_account_details_ob_ch12'),
    path('nov_account_mgt_ob_ch12/<id>',branch12.nov_account_mgt_ob_ch12,name='nov_account_mgt_ob_ch12'),
    path('view_dec_account_details_ob_ch12/', branch12.view_dec_account_details_ob_ch12, name='view_dec_account_details_ob_ch12'),
    path('dec_account_mgt_ob_ch12/<id>',branch12.dec_account_mgt_ob_ch12,name='dec_account_mgt_ob_ch12'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch12', admin_dashboard_calculations_br12.monthly_details_due_ob_ch12, name='monthly_details_due_ob_ch12'),
    path('monthly_collection_details_ob_ch12/', admin_dashboard_calculations_br12.monthly_collection_details_ob_ch12, name='monthly_collection_details_ob_ch12'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch12/',branch12.guest_all_ob_ch12,name='guest_all_ob_ch12'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category12/', accounts12.view_all_category12, name='view_all_category12'),
    path('create_new_category12/', accounts12.create_new_category12, name='create_new_category12'),
    path('regi_new_category12/', accounts12.regi_new_category12, name='regi_new_category12'),
    path('update_category12/<id>',accounts12.update_category12,name='update_category12'),

    path('delete_category12/<id>', accounts12.delete_category12, name='delete_category12'),
    path('view_all_category_delete12/', accounts12.view_all_category_delete12, name='view_all_category_delete12'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items12/', accounts12.view_all_items12, name='view_all_items12'),
    path('create_new_item12/', accounts12.create_new_item12, name='create_new_item12'),
    path('regi_new_item12/', accounts12.regi_new_item12, name='regi_new_item12'),
    path('delete_item12/<id>',accounts12.delete_item12,name='delete_item12'),
    path('update_item12/<id>', accounts12.update_item12, name='update_item12'),
    path('view_all_items_delete12/',accounts12.view_all_items_delete12,name='view_all_items_delete12'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger12/', accounts12.view_all_ledger12, name='view_all_ledger12'),
    path('create_new_ledger12/', accounts12.create_new_ledger12, name='create_new_ledger12'),
    path('regi_new_ledger12/', accounts12.regi_new_ledger12, name='regi_new_ledger12'),
    path('delete_ledger12/<id>',accounts12.delete_ledger12,name='delete_ledger12'),
    path('update_ledger12/<id>',accounts12.update_ledger12,name='update_ledger12'),
    path('view_all_ledger_delete12/',accounts12.view_all_ledger_delete12,name='view_all_ledger_delete12'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book12/', accounts12.view_all_accounts_book12, name='view_all_accounts_book12'),
    path('create_new_accounts_book12/', accounts12.create_new_accounts_book12, name='create_new_accounts_book12'),
    path('regi_new_accounts_book12/', accounts12.regi_new_accounts_book12, name='regi_new_accounts_book12'),
    path('update_accounts_book12/<id>',accounts12.update_accounts_book12,name='update_accounts_book12'),
    path('delete_accounts_book12/<id>',accounts12.delete_accounts_book12,name='delete_accounts_book12'),
    path('view_all_accounts_book_delete12/',accounts12.view_all_accounts_book_delete12,name='view_all_accounts_book_delete12'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries12/', accounts12.get_countries12, name='get_countries12'),

    path('in_exp_items_entry12/', accounts12.in_exp_items_entry12, name='in_exp_items_entry12'),
    path('reg_in_exp_items_entry12/', accounts12.reg_in_exp_items_entry12, name='reg_in_exp_items_entry12'),
    path('delete_journal12/<id>',accounts12.delete_journal12,name='delete_journal12'),
    path('update_in_exp_items_entry12/<id>',accounts12.update_in_exp_items_entry12,name='update_in_exp_items_entry12'),
    path('detailed_journal_report12/',accounts12.detailed_journal_report12,name='detailed_journal_report12'),
    path('journal_report_deleted12/',accounts12.journal_report_deleted12,name='journal_report_deleted12'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise12/', accounts12.daily_category_wise12, name='daily_category_wise12'),
    path('monthly_category_based_reports12/',accounts12.monthly_category_based_reports12,name='monthly_category_based_reports12'),
    path('yearly_category_based_reports12/', accounts12.yearly_category_based_reports12,name='yearly_category_based_reports12'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed12/', accounts12.daily_detailed12, name='daily_detailed12'),
    path('monthly_detailed12/',accounts12.monthly_detailed12,name='monthly_detailed12'),
    path('yearly_detailed12/',accounts12.yearly_detailed12,name='yearly_detailed12'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports12/', accounts12.item_based_reports12, name='item_based_reports12'),
    path('daily_item_based_reports12/',accounts12.daily_item_based_reports12,name='daily_item_based_reports12'),
    path('monthly_item_based_reports12/',accounts12.monthly_item_based_reports12,name='monthly_item_based_reports12'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports12/', accounts12.ledger_based_reports12, name='ledger_based_reports12'),
    path('monthly_ledger_based_reports12/', accounts12.monthly_ledger_based_reports12, name='monthly_ledger_based_reports12'),
    path('daily_ledger_based_reports12/',accounts12.daily_ledger_based_reports12,name='daily_ledger_based_reports12'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports12/', accounts12.accounts_book_based_reports12, name='accounts_book_based_reports12'),
    path('daily_accounts_book_based_reports12/',accounts12.daily_accounts_book_based_reports12,name='daily_accounts_book_based_reports12'),
    path('monthly_accounts_book_based_reports12/',accounts12.monthly_accounts_book_based_reports12,name='monthly_accounts_book_based_reports12'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months12/', accounts12.monthly_reports_choose_months12, name='monthly_reports_choose_months12'),
    path('monthly_detailed_daily_in_exp_items_report12/<mo>',accounts12.monthly_detailed_daily_in_exp_items_report12,name='monthly_detailed_daily_in_exp_items_report12'),

    path('single_monthly_reports_choose_months12/', accounts12.single_monthly_reports_choose_months12,name='single_monthly_reports_choose_months12'),
    path('single_monthly_daily_in_exp_items_report12/<mo>',accounts12.single_monthly_daily_in_exp_items_report12,name='single_monthly_daily_in_exp_items_report12'),

    path('accounts_dash_board_ob_ch12/',accounts12.accounts_dash_board_ob_ch12,name='accounts_dash_board_ob_ch12'),

    path('profit_sharing_choose_months12', accounts12.profit_sharing_choose_months12,name='profit_sharing_choose_months12'),
    path('profit_sharing12/<mo>', accounts12.profit_sharing12, name='profit_sharing12'),
    path('view_share_holders12', accounts12.view_share_holders12, name='view_share_holders12'),
    path('create_share_holders12', accounts12.create_share_holders12, name='create_share_holders12'),
    path('regi_share_holders12', accounts12.regi_share_holders12, name='regi_share_holders12'),
    path('update_share_holders12/<id>', accounts12.update_share_holders12, name='update_share_holders12'),
    path('delete_share_holders12/<id>', accounts12.delete_share_holders12, name='delete_share_holders12'),
    path('view_deleted_share_holders12', accounts12.view_deleted_share_holders12, name='view_deleted_share_holders12'),

]