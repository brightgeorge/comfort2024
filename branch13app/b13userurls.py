from django.urls import path, include

from . import admin_branch13
from . import admin_branch13
from . import branch13
from . import reports13
from . import payment13
from . import admin_dashboard_calculations_br13
from . import accounts13

urlpatterns = [

    path('branch1_dashboard_ob_ch13/', branch13.branch1_dashboard_ob_ch13, name='branch1_dashboard_ob_ch13'),
    path('background_ob_ch13',branch13.background_ob_ch13,name='background_ob_ch13'),
    path('background_regi_ob_ch13',branch13.background_regi_ob_ch13,name='background_regi_ob_ch13'),
    path('custom_background_regi_ob_ch13',branch13.custom_background_regi_ob_ch13,name='custom_background_regi_ob_ch13'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch13/',admin_branch13.branch1_room_create_regi_ob_ch13,name='branch1_room_create_regi_ob_ch13'),
    path('view_all_room_ob_ch13/',admin_branch13.view_all_room_ob_ch13,name='view_all_room_ob_ch13'),
    path('delete_room_ob_ch13/<id>',admin_branch13.delete_room_ob_ch13,name='delete_room_ob_ch13'),

    path('branch1_room_create_ob_ch13/',admin_branch13.branch1_room_create_ob_ch13,name='branch1_room_create_ob_ch13'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch13/', admin_branch13.pg1_bed_create_regi_ob_ch13, name='pg1_bed_create_regi_ob_ch13'),
    path('pg1_view_all_beds_ob_ch13/', admin_branch13.pg1_view_all_beds_ob_ch13, name='pg1_view_all_beds_ob_ch13'),
    path('delete_bed_ob_ch13/<id>', admin_branch13.delete_bed_ob_ch13, name='delete_bed_ob_ch13'),

    path('pg1_bed_create_ob_ch13/', admin_branch13.pg1_bed_create_ob_ch13, name='pg1_bed_create_ob_ch13'),

    path('single_pg1_bed_create_regi_ob_ch13/',admin_branch13.single_pg1_bed_create_regi_ob_ch13,name='single_pg1_bed_create_regi_ob_ch13'),
    path('update_bed_basic_details_ob_ch13/<id>',admin_branch13.update_bed_basic_details_ob_ch13, name='update_bed_basic_details_ob_ch13'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch13/<id>',branch13.br1_admit_guest_ob_ch13,name='br1_admit_guest_ob_ch13'),
    path('view_all_new_guest_ob_ch13/',branch13.view_all_new_guest_ob_ch13,name='view_all_new_guest_ob_ch13'),
    path('update_br1_admit_guest_ob_ch13/<id>',branch13.update_br1_admit_guest_ob_ch13,name='update_br1_admit_guest_ob_ch13'),
    path('vacate_br1_guest_ob_ch13/<id>',branch13.vacate_br1_guest_ob_ch13,name='vacate_br1_guest_ob_ch13'),

    path('active_guest_details_ob_ch13/<guest_code>',branch13.active_guest_details_ob_ch13,name='active_guest_details_ob_ch13'),
    path('view_all_guest_ob_ch13/',branch13.view_all_guest_ob_ch13,name='view_all_guest_ob_ch13'),
    path('change_duplicate_guest_status_ob_ch13/<id>', branch13.change_duplicate_guest_status_ob_ch13,name='change_duplicate_guest_status_ob_ch13'),
    path('shift_guest_ob_ch13/<id>',branch13.shift_guest_ob_ch13,name='shift_guest_ob_ch13'),
    path('shift_guest_regi_ob_ch13/',branch13.shift_guest_regi_ob_ch13,name='shift_guest_regi_ob_ch13'),

    path('view_all_duplicate_entry_ob_ch13/',branch13.view_all_duplicate_entry_ob_ch13,name='view_all_duplicate_entry_ob_ch13'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),

#guest end here


##################################
#_ADVANCE_ob_ch13 START HERE
################################


    path('choose_months_advance_ob_ch13/',branch13.choose_months_advance_ob_ch13,name='choose_months_advance_ob_ch13'),

    path('jan_advance_ob_ch13/', branch13.jan_advance_ob_ch13, name='jan_advance_ob_ch13'),
    path('jan_make_payments_advance_ob_ch13/<id>', branch13.jan_make_payments_advance_ob_ch13,name='jan_make_payments_advance_ob_ch13'),
    path('feb_advance_ob_ch13/', branch13.feb_advance_ob_ch13, name='feb_advance_ob_ch13'),
    path('feb_make_payments_advance_ob_ch13/<id>', branch13.feb_make_payments_advance_ob_ch13,name='feb_make_payments_advance_ob_ch13'),
    path('march_advance_ob_ch13/', branch13.march_advance_ob_ch13, name='march_advance_ob_ch13'),
    path('march_make_payments_advance_ob_ch13/<id>', branch13.march_make_payments_advance_ob_ch13,name='march_make_payments_advance_ob_ch13'),
    path('april_advance_ob_ch13/', branch13.april_advance_ob_ch13, name='april_advance_ob_ch13'),
    path('april_make_payments_advance_ob_ch13/<id>', branch13.april_make_payments_advance_ob_ch13, name='april_make_payments_advance_ob_ch13'),

    path('may_advance_ob_ch13/',branch13.may_advance_ob_ch13,name='may_advance_ob_ch13'),
    path('may_make_payments_advance_ob_ch13/<id>', branch13.may_make_payments_advance_ob_ch13, name='may_make_payments_advance_ob_ch13'),
    path('june_advance_ob_ch13/',branch13.june_advance_ob_ch13,name='june_advance_ob_ch13'),
    path('june_make_payments_advance_ob_ch13/<id>', branch13.june_make_payments_advance_ob_ch13, name='june_make_payments_advance_ob_ch13'),
    path('july_advance_ob_ch13/',branch13.july_advance_ob_ch13,name='july_advance_ob_ch13'),
    path('july_make_payments_advance_ob_ch13/<id>', branch13.july_make_payments_advance_ob_ch13, name='july_make_payments_advance_ob_ch13'),
    path('auguest_advance_ob_ch13/', branch13.auguest_advance_ob_ch13, name='auguest_advance_ob_ch13'),
    path('auguest_make_payments_advance_ob_ch13/<id>', branch13.auguest_make_payments_advance_ob_ch13, name='auguest_make_payments_advance_ob_ch13'),

    path('sept_advance_ob_ch13/', branch13.sept_advance_ob_ch13, name='sept_advance_ob_ch13'),
    path('sept_make_payments_advance_ob_ch13/<id>', branch13.sept_make_payments_advance_ob_ch13,name='sept_make_payments_advance_ob_ch13'),
    path('october_advance_ob_ch13/', branch13.october_advance_ob_ch13, name='october_advance_ob_ch13'),
    path('october_make_payments_advance_ob_ch13/<id>', branch13.october_make_payments_advance_ob_ch13, name='october_make_payments_advance_ob_ch13'),
    path('nov_advance_ob_ch13/', branch13.nov_advance_ob_ch13, name='nov_advance_ob_ch13'),
    path('nov_make_payments_advance_ob_ch13/<id>', branch13.nov_make_payments_advance_ob_ch13,name='nov_make_payments_advance_ob_ch13'),
    path('dec_advance_ob_ch13/', branch13.dec_advance_ob_ch13, name='dec_advance_ob_ch13'),
    path('dec_make_payments_advance_ob_ch13/<id>', branch13.dec_make_payments_advance_ob_ch13, name='dec_make_payments_advance_ob_ch13'),



##################################
#_ADVANCE_ob_ch13 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch13/',branch13.choose_months_ob_ch13,name='choose_months_ob_ch13'),

    path('jan_ob_ch13/',branch13.jan_ob_ch13,name='jan_ob_ch13'),
    path('jan_manke_payments_ob_ch13/<id>',branch13.jan_manke_payments_ob_ch13,name='jan_manke_payments_ob_ch13'),

    path('feb_ob_ch13/',branch13.feb_ob_ch13,name='feb_ob_ch13'),
    path('feb_manke_payments_ob_ch13/<id>',branch13.feb_manke_payments_ob_ch13,name='feb_manke_payments_ob_ch13'),

    path('march_ob_ch13/',branch13.march_ob_ch13,name='march_ob_ch13'),
    path('march_manke_payments_ob_ch13/<id>',branch13.march_manke_payments_ob_ch13,name='march_manke_payments_ob_ch13'),

    path('april_ob_ch13/',branch13.april_ob_ch13,name='april_ob_ch13'),
    path('april_make_payments_ob_ch13/<id>',branch13.april_make_payments_ob_ch13,name='april_make_payments_ob_ch13'),

    path('may_ob_ch13/',branch13.may_ob_ch13,name='may_ob_ch13'),
    path('may_make_payments_ob_ch13/<id>',branch13.may_make_payments_ob_ch13,name='may_make_payments_ob_ch13'),

    path('june_ob_ch13/',branch13.june_ob_ch13,name='june_ob_ch13'),
    path('june_make_payments_ob_ch13/<id>',branch13.june_make_payments_ob_ch13,name='june_make_payments_ob_ch13'),

    path('july_ob_ch13/',branch13.july_ob_ch13,name='july_ob_ch13'),
    path('july_make_payments_ob_ch13/<id>',branch13.july_make_payments_ob_ch13,name='july_make_payments_ob_ch13'),

    path('aug_ob_ch13/',branch13.aug_ob_ch13,name='aug_ob_ch13'),
    path('aug_make_payments_ob_ch13/<id>',branch13.aug_make_payments_ob_ch13,name='aug_make_payments_ob_ch13'),

    path('sept_ob_ch13/',branch13.sept_ob_ch13,name='sept_ob_ch13'),
    path('sept_make_payments_ob_ch13/<id>',branch13.sept_make_payments_ob_ch13,name='sept_make_payments_ob_ch13'),

    path('oct_ob_ch13/',branch13.oct_ob_ch13,name='oct_ob_ch13'),
    path('oct_make_payments_ob_ch13/<id>',branch13.oct_make_payments_ob_ch13,name='oct_make_payments_ob_ch13'),

    path('nov_ob_ch13/',branch13.nov_ob_ch13,name='nov_ob_ch13'),
    path('nov_make_payments_ob_ch13/<id>',branch13.nov_make_payments_ob_ch13,name='nov_make_payments_ob_ch13'),

    path('dec_ob_ch13/',branch13.dec_ob_ch13,name='dec_ob_ch13'),
    path('dec_make_payments_ob_ch13/<id>',branch13.dec_make_payments_ob_ch13,name='dec_make_payments_ob_ch13'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch13/', payment13.choose_user_ob_ch13, name='choose_user_ob_ch13'),
    path('payment_user_details_ob_ch13/<id>', payment13.payment_user_details_ob_ch13, name='payment_user_details_ob_ch13'),
    path('close_choose_user_ob_ch13/<id>',payment13.close_choose_user_ob_ch13,name='close_choose_user_ob_ch13'),

    path('monthly_jan_make_payments_ob_ch13/<id>', payment13.monthly_jan_make_payments_ob_ch13, name='monthly_jan_make_payments_ob_ch13'),
    path('monthly_feb_make_payments_ob_ch13/<id>', payment13.monthly_feb_make_payments_ob_ch13, name='monthly_feb_make_payments_ob_ch13'),
    path('monthly_march_make_payments_ob_ch13/<id>', payment13.monthly_march_make_payments_ob_ch13, name='monthly_march_make_payments_ob_ch13'),
    path('monthly_april_make_payments_ob_ch13/<id>', payment13.monthly_april_make_payments_ob_ch13, name='monthly_april_make_payments_ob_ch13'),
    path('monthly_may_make_payments_ob_ch13/<id>', payment13.monthly_may_make_payments_ob_ch13, name='monthly_may_make_payments_ob_ch13'),
    path('monthly_june_make_payments_ob_ch13/<id>', payment13.monthly_june_make_payments_ob_ch13, name='monthly_june_make_payments_ob_ch13'),

    path('monthly_july_make_payments_ob_ch13/<id>', payment13.monthly_july_make_payments_ob_ch13, name='monthly_july_make_payments_ob_ch13'),
    path('monthly_aug_make_payments_ob_ch13/<id>', payment13.monthly_aug_make_payments_ob_ch13, name='monthly_aug_make_payments_ob_ch13'),
    path('monthly_sept_make_payments_ob_ch13/<id>', payment13.monthly_sept_make_payments_ob_ch13, name='monthly_sept_make_payments_ob_ch13'),
    path('monthly_oct_make_payments_ob_ch13/<id>', payment13.monthly_oct_make_payments_ob_ch13, name='monthly_oct_make_payments_ob_ch13'),
    path('monthly_nov_make_payments_ob_ch13/<id>', payment13.monthly_nov_make_payments_ob_ch13, name='monthly_nov_make_payments_ob_ch13'),
    path('monthly_dec_make_payments_ob_ch13/<id>', payment13.monthly_dec_make_payments_ob_ch13, name='monthly_dec_make_payments_ob_ch13'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch13/',branch13.unpaid_rent_choose_months_ob_ch13,name='unpaid_rent_choose_months_ob_ch13'),

    path('jan_unpaid_rent_ob_ch13/', branch13.jan_unpaid_rent_ob_ch13, name='jan_unpaid_rent_ob_ch13'),
    path('table_jan_unpaid_rent_ob_ch13/', branch13.table_jan_unpaid_rent_ob_ch13, name='table_jan_unpaid_rent_ob_ch13'),
    path('feb_unpaid_rent_ob_ch13/', branch13.feb_unpaid_rent_ob_ch13, name='feb_unpaid_rent_ob_ch13'),
    path('table_feb_unpaid_rent_ob_ch13/', branch13.table_feb_unpaid_rent_ob_ch13, name='table_feb_unpaid_rent_ob_ch13'),
    path('mar_unpaid_rent_ob_ch13/', branch13.mar_unpaid_rent_ob_ch13, name='mar_unpaid_rent_ob_ch13'),
    path('table_mar_unpaid_rent_ob_ch13/', branch13.table_mar_unpaid_rent_ob_ch13, name='table_mar_unpaid_rent_ob_ch13'),
    path('april_unpaid_rent_ob_ch13/', branch13.april_unpaid_rent_ob_ch13, name='april_unpaid_rent_ob_ch13'),
    path('table_april_unpaid_rent_ob_ch13/', branch13.table_april_unpaid_rent_ob_ch13, name='table_april_unpaid_rent_ob_ch13'),

    path('may_unpaid_rent_ob_ch13/', branch13.may_unpaid_rent_ob_ch13, name='may_unpaid_rent_ob_ch13'),
    path('table_may_unpaid_rent_ob_ch13/', branch13.table_may_unpaid_rent_ob_ch13, name='table_may_unpaid_rent_ob_ch13'),
    path('june_unpaid_rent_ob_ch13/', branch13.june_unpaid_rent_ob_ch13, name='june_unpaid_rent_ob_ch13'),
    path('table_june_unpaid_rent_ob_ch13/', branch13.table_june_unpaid_rent_ob_ch13, name='table_june_unpaid_rent_ob_ch13'),
    path('july_unpaid_rent_ob_ch13/', branch13.july_unpaid_rent_ob_ch13, name='july_unpaid_rent_ob_ch13'),
    path('table_july_unpaid_rent_ob_ch13',branch13.table_july_unpaid_rent_ob_ch13,name='table_july_unpaid_rent_ob_ch13'),
    path('aug_unpaid_rent_ob_ch13/', branch13.aug_unpaid_rent_ob_ch13, name='aug_unpaid_rent_ob_ch13'),
    path('table_aug_unpaid_rent_ob_ch13/',branch13.table_aug_unpaid_rent_ob_ch13,name='table_aug_unpaid_rent_ob_ch13'),

    path('sept_unpaid_rent_ob_ch13/', branch13.sept_unpaid_rent_ob_ch13, name='sept_unpaid_rent_ob_ch13'),
    path('table_sept_unpaid_rent_ob_ch13/', branch13.table_sept_unpaid_rent_ob_ch13, name='table_sept_unpaid_rent_ob_ch13'),
    path('oct_unpaid_rent_ob_ch13/', branch13.oct_unpaid_rent_ob_ch13, name='oct_unpaid_rent_ob_ch13'),
    path('table_oct_unpaid_rent_ob_ch13/', branch13.table_oct_unpaid_rent_ob_ch13, name='table_oct_unpaid_rent_ob_ch13'),
    path('nov_unpaid_rent_ob_ch13/', branch13.nov_unpaid_rent_ob_ch13, name='nov_unpaid_rent_ob_ch13'),
    path('table_nov_unpaid_rent_ob_ch13/', branch13.table_nov_unpaid_rent_ob_ch13, name='table_nov_unpaid_rent_ob_ch13'),
    path('dec_unpaid_rent_ob_ch13/', branch13.dec_unpaid_rent_ob_ch13, name='dec_unpaid_rent_ob_ch13'),
    path('table_dec_unpaid_rent_ob_ch13/', branch13.table_dec_unpaid_rent_ob_ch13, name='table_dec_unpaid_rent_ob_ch13'),

    path('details_of_unpaid_guests_ob_ch13/<id>',branch13.details_of_unpaid_guests_ob_ch13,name='details_of_unpaid_guests_ob_ch13'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch13/',branch13.paid_rent_choose_months_ob_ch13,name='paid_rent_choose_months_ob_ch13'),
    path('partially_paid_guest_choose_months_ob_ch13/',reports13.partially_paid_guest_choose_months_ob_ch13,name='partially_paid_guest_choose_months_ob_ch13'),

    path('jan_paid_rent_ob_ch13/', branch13.jan_paid_rent_ob_ch13, name='jan_paid_rent_ob_ch13'),
    path('table_jan_paid_rent_ob_ch13/', branch13.table_jan_paid_rent_ob_ch13, name='table_jan_paid_rent_ob_ch13'),
    path('jan_full_paid_guest_ob_ch13/', reports13.jan_full_paid_guest_ob_ch13, name='jan_full_paid_guest_ob_ch13'),
    path('jan_partially_paid_guest_ob_ch13/', reports13.jan_partially_paid_guest_ob_ch13, name='jan_partially_paid_guest_ob_ch13'),
    path('table_jan_partially_paid_guest_ob_ch13/', reports13.table_jan_partially_paid_guest_ob_ch13,name='table_jan_partially_paid_guest_ob_ch13'),

    path('feb_paid_rent_ob_ch13/', branch13.feb_paid_rent_ob_ch13, name='feb_paid_rent_ob_ch13'),
    path('table_feb_paid_rent_ob_ch13/', branch13.table_feb_paid_rent_ob_ch13, name='table_feb_paid_rent_ob_ch13'),
    path('feb_full_paid_guest_ob_ch13/', reports13.feb_full_paid_guest_ob_ch13, name='feb_full_paid_guest_ob_ch13'),
    path('feb_partially_paid_guest_ob_ch13/', reports13.feb_partially_paid_guest_ob_ch13, name='feb_partially_paid_guest_ob_ch13'),
    path('table_feb_partially_paid_guest_ob_ch13/', reports13.table_feb_partially_paid_guest_ob_ch13,name='table_feb_partially_paid_guest_ob_ch13'),

    path('mar_paid_rent_ob_ch13/', branch13.mar_paid_rent_ob_ch13, name='mar_paid_rent_ob_ch13'),
    path('table_mar_paid_rent_ob_ch13/', branch13.table_mar_paid_rent_ob_ch13, name='table_mar_paid_rent_ob_ch13'),
    path('march_full_paid_guest_ob_ch13/', reports13.march_full_paid_guest_ob_ch13, name='march_full_paid_guest_ob_ch13'),
    path('march_partially_paid_guest_ob_ch13/', reports13.march_partially_paid_guest_ob_ch13, name='march_partially_paid_guest_ob_ch13'),
    path('table_march_partially_paid_guest_ob_ch13/', reports13.table_march_partially_paid_guest_ob_ch13,name='table_march_partially_paid_guest_ob_ch13'),

    path('april_paid_rent_ob_ch13/', branch13.april_paid_rent_ob_ch13, name='april_paid_rent_ob_ch13'),
    path('table_april_paid_rent_ob_ch13/', branch13.table_april_paid_rent_ob_ch13, name='table_april_paid_rent_ob_ch13'),
    path('april_full_paid_guest_ob_ch13/', reports13.april_full_paid_guest_ob_ch13, name='april_full_paid_guest_ob_ch13'),
    path('april_partially_paid_guest_ob_ch13/', reports13.april_partially_paid_guest_ob_ch13, name='april_partially_paid_guest_ob_ch13'),
    path('table_april_partially_paid_guest_ob_ch13/', reports13.table_april_partially_paid_guest_ob_ch13,name='table_april_partially_paid_guest_ob_ch13'),

    path('may_paid_rent_ob_ch13/', branch13.may_paid_rent_ob_ch13, name='may_paid_rent_ob_ch13'),
    path('table_may_paid_rent_ob_ch13/', branch13.table_may_paid_rent_ob_ch13, name='table_may_paid_rent_ob_ch13'),
    path('may_full_paid_guest_ob_ch13/', reports13.may_full_paid_guest_ob_ch13, name='may_full_paid_guest_ob_ch13'),
    path('may_partially_paid_guest_ob_ch13/', reports13.may_partially_paid_guest_ob_ch13, name='may_partially_paid_guest_ob_ch13'),
    path('table_may_partially_paid_guest_ob_ch13/', reports13.table_may_partially_paid_guest_ob_ch13, name='table_may_partially_paid_guest_ob_ch13'),

    path('june_paid_rent_ob_ch13/', branch13.june_paid_rent_ob_ch13, name='june_paid_rent_ob_ch13'),
    path('table_june_paid_rent_ob_ch13/', branch13.table_june_paid_rent_ob_ch13, name='table_june_paid_rent_ob_ch13'),
    path('june_full_paid_guest_ob_ch13/', reports13.june_full_paid_guest_ob_ch13, name='june_full_paid_guest_ob_ch13'),
    path('june_partially_paid_guest_ob_ch13/', reports13.june_partially_paid_guest_ob_ch13, name='june_partially_paid_guest_ob_ch13'),
    path('table_june_partially_paid_guest_ob_ch13/', reports13.table_june_partially_paid_guest_ob_ch13, name='table_june_partially_paid_guest_ob_ch13'),

    path('july_paid_rent_ob_ch13/', branch13.july_paid_rent_ob_ch13, name='july_paid_rent_ob_ch13'),
    path('table_july_paid_rent_ob_ch13/', branch13.table_july_paid_rent_ob_ch13, name='table_july_paid_rent_ob_ch13'),
    path('july_full_paid_guest_ob_ch13/', reports13.july_full_paid_guest_ob_ch13, name='july_full_paid_guest_ob_ch13'),
    path('july_partially_paid_guest_ob_ch13/', reports13.july_partially_paid_guest_ob_ch13, name='july_partially_paid_guest_ob_ch13'),
    path('table_july_partially_paid_guest_ob_ch13/', reports13.table_july_partially_paid_guest_ob_ch13, name='table_july_partially_paid_guest_ob_ch13'),

    path('aug_paid_rent_ob_ch13/', branch13.aug_paid_rent_ob_ch13, name='aug_paid_rent_ob_ch13'),
    path('table_aug_paid_rent_ob_ch13/', branch13.table_aug_paid_rent_ob_ch13, name='table_aug_paid_rent_ob_ch13'),
    path('auguest_full_paid_guest_ob_ch13/', reports13.auguest_full_paid_guest_ob_ch13, name='auguest_full_paid_guest_ob_ch13'),
    path('auguest_partially_paid_guest_ob_ch13/', reports13.auguest_partially_paid_guest_ob_ch13,name='auguest_partially_paid_guest_ob_ch13'),
    path('table_auguest_partially_paid_guest_ob_ch13/', reports13.table_auguest_partially_paid_guest_ob_ch13,name='table_auguest_partially_paid_guest_ob_ch13'),

    path('sept_paid_rent_ob_ch13/', branch13.sept_paid_rent_ob_ch13, name='sept_paid_rent_ob_ch13'),
    path('table_sept_paid_rent_ob_ch13/', branch13.table_sept_paid_rent_ob_ch13, name='table_sept_paid_rent_ob_ch13'),
    path('sept_full_paid_guest_ob_ch13/', reports13.sept_full_paid_guest_ob_ch13, name='sept_full_paid_guest_ob_ch13'),
    path('sept_partially_paid_guest_ob_ch13/', reports13.sept_partially_paid_guest_ob_ch13, name='sept_partially_paid_guest_ob_ch13'),
    path('table_sept_partially_paid_guest_ob_ch13/', reports13.table_sept_partially_paid_guest_ob_ch13,name='table_sept_partially_paid_guest_ob_ch13'),

    path('oct_paid_rent_ob_ch13/', branch13.oct_paid_rent_ob_ch13, name='oct_paid_rent_ob_ch13'),
    path('table_oct_paid_rent_ob_ch13/', branch13.table_oct_paid_rent_ob_ch13, name='table_oct_paid_rent_ob_ch13'),
    path('october_full_paid_guest_ob_ch13/', reports13.october_full_paid_guest_ob_ch13, name='october_full_paid_guest_ob_ch13'),
    path('october_partially_paid_guest_ob_ch13/', reports13.october_partially_paid_guest_ob_ch13,name='october_partially_paid_guest_ob_ch13'),
    path('table_october_partially_paid_guest_ob_ch13/', reports13.table_october_partially_paid_guest_ob_ch13,name='table_october_partially_paid_guest_ob_ch13'),

    path('nov_paid_rent_ob_ch13/', branch13.nov_paid_rent_ob_ch13, name='nov_paid_rent_ob_ch13'),
    path('table_nov_paid_rent_ob_ch13/', branch13.table_nov_paid_rent_ob_ch13, name='table_nov_paid_rent_ob_ch13'),
    path('nov_full_paid_guest_ob_ch13/', reports13.nov_full_paid_guest_ob_ch13, name='nov_full_paid_guest_ob_ch13'),
    path('nov_partially_paid_guest_ob_ch13/', reports13.nov_partially_paid_guest_ob_ch13, name='nov_partially_paid_guest_ob_ch13'),
    path('table_nov_partially_paid_guest_ob_ch13/', reports13.table_nov_partially_paid_guest_ob_ch13,name='table_nov_partially_paid_guest_ob_ch13'),

    path('dec_paid_rent_ob_ch13/', branch13.dec_paid_rent_ob_ch13, name='dec_paid_rent_ob_ch13'),
    path('table_dec_paid_rent_ob_ch13/', branch13.table_dec_paid_rent_ob_ch13, name='table_dec_paid_rent_ob_ch13'),
    path('dec_full_paid_guest_ob_ch13/', reports13.dec_full_paid_guest_ob_ch13, name='dec_full_paid_guest_ob_ch13'),
    path('dec_partially_paid_guest_ob_ch13/', reports13.dec_partially_paid_guest_ob_ch13, name='dec_partially_paid_guest_ob_ch13'),
    path('table_dec_partially_paid_guest_ob_ch13/', reports13.table_dec_partially_paid_guest_ob_ch13,name='table_dec_partially_paid_guest_ob_ch13'),

    path('details_of_paid_guests_ob_ch13/<id>',branch13.details_of_paid_guests_ob_ch13,name='details_of_paid_guests_ob_ch13'),
    path('full_paid_guest_ob_ch13/',reports13.full_paid_guest_ob_ch13,name='full_paid_guest_ob_ch13'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch13/',branch13.viewall_vacate_guest_ob_ch13,name='viewall_vacate_guest_ob_ch13'),
    path('details_of_vacate_guest_ob_ch13/<id>',branch13.details_of_vacate_guest_ob_ch13,name='details_of_vacate_guest_ob_ch13'),
    path('full_vacated_guest_details_ob_ch13',branch13.full_vacated_guest_details_ob_ch13,name='full_vacated_guest_details_ob_ch13'),
    path('full_vacated_guest_table_ob_ch13',branch13.full_vacated_guest_table_ob_ch13,name='full_vacated_guest_table_ob_ch13'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch13/<id>', branch13.jan_manke_payments_vacate_ob_ch13, name='jan_manke_payments_vacate_ob_ch13'),
    path('feb_manke_payments_vacate_ob_ch13/<id>', branch13.feb_manke_payments_vacate_ob_ch13, name='feb_manke_payments_vacate_ob_ch13'),
    path('march_manke_payments_vacate_ob_ch13/<id>', branch13.march_manke_payments_vacate_ob_ch13, name='march_manke_payments_vacate_ob_ch13'),
    path('april_make_payments_vacate_ob_ch13/<id>', branch13.april_make_payments_vacate_ob_ch13, name='april_make_payments_vacate_ob_ch13'),

    path('may_make_payments_vacate_ob_ch13/<id>', branch13.may_make_payments_vacate_ob_ch13, name='may_make_payments_vacate_ob_ch13'),
    path('june_make_payments_vacate_ob_ch13/<id>', branch13.june_make_payments_vacate_ob_ch13, name='june_make_payments_vacate_ob_ch13'),
    path('july_make_payments_vacate_ob_ch13/<id>', branch13.july_make_payments_vacate_ob_ch13, name='july_make_payments_vacate_ob_ch13'),
    path('aug_make_payments_vacate_ob_ch13/<id>', branch13.aug_make_payments_vacate_ob_ch13, name='aug_make_payments_vacate_ob_ch13'),

    path('sept_make_payments_vacate_ob_ch13/<id>', branch13.sept_make_payments_vacate_ob_ch13, name='sept_make_payments_vacate_ob_ch13'),
    path('oct_make_payments_vacate_ob_ch13/<id>', branch13.oct_make_payments_vacate_ob_ch13, name='oct_make_payments_vacate_ob_ch13'),
    path('nov_make_payments_vacate_ob_ch13/<id>', branch13.nov_make_payments_vacate_ob_ch13, name='nov_make_payments_vacate_ob_ch13'),
    path('dec_make_payments_vacate_ob_ch13/<id>', branch13.dec_make_payments_vacate_ob_ch13, name='dec_make_payments_vacate_ob_ch13'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch13/',branch13.detail_guest_general_ob_ch13,name='detail_guest_general_ob_ch13'),

    path('jan_print_ob_ch13/',branch13.jan_print_ob_ch13,name='jan_print_ob_ch13'),
    path('feb_print_ob_ch13/',branch13.feb_print_ob_ch13,name='feb_print_ob_ch13'),
    path('march_print_ob_ch13/',branch13.march_print_ob_ch13,name='march_print_ob_ch13'),
    path('april_print_ob_ch13/',branch13.april_print_ob_ch13,name='april_print_ob_ch13'),

    path('may_print_ob_ch13/',branch13.may_print_ob_ch13,name='may_print_ob_ch13'),
    path('june_print_ob_ch13/',branch13.june_print_ob_ch13,name='june_print_ob_ch13'),
    path('july_print_ob_ch13/', branch13.july_print_ob_ch13, name='july_print_ob_ch13'),
    path('aug_print_ob_ch13/', branch13.aug_print_ob_ch13, name='aug_print_ob_ch13'),

    path('sept_print_ob_ch13/', branch13.sept_print_ob_ch13, name='sept_print_ob_ch13'),
    path('oct_print_ob_ch13/', branch13.oct_print_ob_ch13, name='oct_print_ob_ch13'),
    path('nov_print_ob_ch13/', branch13.nov_print_ob_ch13, name='nov_print_ob_ch13'),
    path('dec_print_ob_ch13/', branch13.dec_print_ob_ch13, name='dec_print_ob_ch13'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch13/', branch13.jan_close_ob_ch13, name='jan_close_ob_ch13'),
    path('jan_close_decision_page_ob_ch13/', branch13.jan_close_decision_page_ob_ch13, name='jan_close_decision_page_ob_ch13'),
    path('feb_close/', branch13.feb_close_ob_ch13, name='feb_close_ob_ch13'),
    path('feb_close_decision_page_ob_ch13/', branch13.feb_close_decision_page_ob_ch13, name='feb_close_decision_page_ob_ch13'),
    path('mar_close_ob_ch13/', branch13.mar_close_ob_ch13, name='mar_close_ob_ch13'),
    path('mar_close_decision_page/', branch13.mar_close_decision_page_ob_ch13, name='mar_close_decision_page_ob_ch13'),
    path('apr_close_ob_ch13/', branch13.apr_close_ob_ch13, name='apr_close_ob_ch13'),
    path('apr_close_decision_page_ob_ch13/', branch13.apr_close_decision_page_ob_ch13, name='apr_close_decision_page_ob_ch13'),

    path('may_close_ob_ch13/', branch13.may_close_ob_ch13, name='may_close_ob_ch13'),
    path('may_close_decision_page_ob_ch13/', branch13.may_close_decision_page_ob_ch13, name='may_close_decision_page_ob_ch13'),
    path('jun_close_ob_ch13/', branch13.jun_close_ob_ch13, name='jun_close_ob_ch13'),
    path('jun_close_decision_page_ob_ch13/', branch13.jun_close_decision_page_ob_ch13, name='jun_close_decision_page_ob_ch13'),
    path('jul_close_ob_ch13/', branch13.jul_close_ob_ch13, name='jul_close_ob_ch13'),
    path('jul_close_decision_page_ob_ch13/', branch13.jul_close_decision_page_ob_ch13, name='jul_close_decision_page_ob_ch13'),
    path('aug_close_ob_ch13/', branch13.aug_close_ob_ch13, name='aug_close_ob_ch13'),
    path('aug_close_decision_page_ob_ch13/', branch13.aug_close_decision_page_ob_ch13, name='aug_close_decision_page_ob_ch13'),

    path('sep_close_ob_ch13/', branch13.sep_close_ob_ch13, name='sep_close_ob_ch13'),
    path('sep_close_decision_page_ob_ch13/', branch13.sep_close_decision_page_ob_ch13, name='sep_close_decision_page_ob_ch13'),
    path('oct_close_ob_ch13/', branch13.oct_close_ob_ch13, name='oct_close_ob_ch13'),
    path('oct_close_decision_page_ob_ch13/', branch13.oct_close_decision_page_ob_ch13, name='oct_close_decision_page_ob_ch13'),
    path('nov_close_ob_ch13/', branch13.nov_close_ob_ch13, name='nov_close_ob_ch13'),
    path('nov_close_decision_page_ob_ch13/', branch13.nov_close_decision_page_ob_ch13, name='nov_close_decision_page_ob_ch13'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch13/',reports13.detailed_report_choose_months_ob_ch13,name='detailed_report_choose_months_ob_ch13'),

    path('jan_details_live_ob_ch13/', reports13.jan_details_live_ob_ch13, name='jan_details_live_ob_ch13'),
    path('jan_print_live_ob_ch13/', reports13.jan_print_live_ob_ch13, name='jan_print_live_ob_ch13'),
    path('feb_details_live_ob_ch13/', reports13.feb_details_live_ob_ch13, name='feb_details_live_ob_ch13'),
    path('feb_print_live_ob_ch13/', reports13.feb_print_live_ob_ch13, name='feb_print_live_ob_ch13'),
    path('march_details_live_ob_ch13/', reports13.march_details_live_ob_ch13, name='march_details_live_ob_ch13'),
    path('march_print_live_ob_ch13/', reports13.march_print_live_ob_ch13, name='march_print_live_ob_ch13'),

    path('april_details_live_ob_ch13/', reports13.april_details_live_ob_ch13, name='april_details_live_ob_ch13'),
    path('april_print_live_ob_ch13/', reports13.april_print_live_ob_ch13, name='april_print_live_ob_ch13'),
    path('may_details_live_ob_ch13/', reports13.may_details_live_ob_ch13, name='may_details_live_ob_ch13'),
    path('may_print_live_ob_ch13/', reports13.may_print_live_ob_ch13, name='may_print_live_ob_ch13'),
    path('june_details_live_ob_ch13/',reports13.june_details_live_ob_ch13,name='june_details_live_ob_ch13'),
    path('june_print_live_ob_ch13/', reports13.june_print_live_ob_ch13, name='june_print_live_ob_ch13'),

    path('july_details_live_ob_ch13/', reports13.july_details_live_ob_ch13, name='july_details_live_ob_ch13'),
    path('july_print_live_ob_ch13/', reports13.july_print_live_ob_ch13, name='july_print_live_ob_ch13'),
    path('auguest_details_live_ob_ch13/', reports13.auguest_details_live_ob_ch13, name='auguest_details_live_ob_ch13'),
    path('auguest_print_live_ob_ch13/', reports13.auguest_print_live_ob_ch13, name='auguest_print_live_ob_ch13'),
    path('sept_details_live_ob_ch13/', reports13.sept_details_live_ob_ch13, name='sept_details_live_ob_ch13'),
    path('sept_print_live_ob_ch13/', reports13.sept_print_live_ob_ch13, name='sept_print_live_ob_ch13'),

    path('october_details_live_ob_ch13/', reports13.october_details_live_ob_ch13, name='october_details_live_ob_ch13'),
    path('october_print_live_ob_ch13/', reports13.october_print_live_ob_ch13, name='october_print_live_ob_ch13'),
    path('nov_details_live_ob_ch13/', reports13.nov_details_live_ob_ch13, name='nov_details_live_ob_ch13'),
    path('nov_print_live_ob_ch13/', reports13.nov_print_live_ob_ch13, name='nov_print_live_ob_ch13'),
    path('dec_details_live_ob_ch13/', reports13.dec_details_live_ob_ch13, name='dec_details_live_ob_ch13'),
    path('dec_print_live_ob_ch13/', reports13.dec_print_live_ob_ch13, name='dec_print_live_ob_ch13'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch13/', reports13.viewall_vaccant_room_ob_ch13, name='viewall_vaccant_room_ob_ch13'),

    path('d_ob_ch13/', branch13.dynamic, name='dynamic'),

    path('manage_bed_ob_ch13/', branch13.manage_bed_ob_ch13, name='manage_bed_ob_ch13'),
    path('manage_new_guest_ob_ch13/', branch13.manage_new_guest_ob_ch13, name='manage_new_guest_ob_ch13'),
    path('manage_update_new_guest_ob_ch13/<id>', branch13.manage_update_new_guest_ob_ch13, name='manage_update_new_guest_ob_ch13'),
    path('manage_update_beds_ob_ch13/<id>', branch13.manage_update_beds_ob_ch13, name='manage_update_beds_ob_ch13'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch13/', branch13.view_all_due_amt_ob_ch13, name='view_all_due_amt_ob_ch13'),
    path('due_amt_mgt_choose_months_ob_ch13/', branch13.due_amt_mgt_choose_months_ob_ch13, name='due_amt_mgt_choose_months_ob_ch13'),

    path('view_jan_account_details_ob_ch13/', branch13.view_jan_account_details_ob_ch13, name='view_jan_account_details_ob_ch13'),
    path('jan_account_mgt_ob_ch13/<id>',branch13.jan_account_mgt_ob_ch13,name='jan_account_mgt_ob_ch13'),
    path('view_feb_account_details_ob_ch13/', branch13.view_feb_account_details_ob_ch13, name='view_feb_account_details_ob_ch13'),
    path('feb_account_mgt_ob_ch13/<id>',branch13.feb_account_mgt_ob_ch13,name='feb_account_mgt_ob_ch13'),
    path('view_march_account_details_ob_ch13/', branch13.view_march_account_details_ob_ch13, name='view_march_account_details_ob_ch13'),
    path('march_account_mgt_ob_ch13/<id>',branch13.march_account_mgt_ob_ch13,name='march_account_mgt_ob_ch13'),
    path('view_april_account_details_ob_ch13/', branch13.view_april_account_details_ob_ch13, name='view_april_account_details_ob_ch13'),
    path('april_account_mgt_ob_ch13/<id>',branch13.april_account_mgt_ob_ch13,name='april_account_mgt_ob_ch13'),

    path('view_may_account_details_ob_ch13/',branch13.view_may_account_details_ob_ch13,name='view_may_account_details_ob_ch13'),
    path('may_account_mgt_ob_ch13/<id>', branch13.may_account_mgt_ob_ch13, name='may_account_mgt_ob_ch13'),
    path('view_june_account_details_ob_ch13/', branch13.view_june_account_details_ob_ch13, name='view_june_account_details_ob_ch13'),
    path('june_account_mgt_ob_ch13/<id>',branch13.june_account_mgt_ob_ch13,name='june_account_mgt_ob_ch13'),
    path('view_july_account_details_ob_ch13/', branch13.view_july_account_details_ob_ch13, name='view_july_account_details_ob_ch13'),
    path('july_account_mgt_ob_ch13/<id>',branch13.july_account_mgt_ob_ch13,name='july_account_mgt_ob_ch13'),
    path('view_auguest_account_details_ob_ch13/', branch13.view_auguest_account_details_ob_ch13, name='view_auguest_account_details_ob_ch13'),
    path('auguest_account_mgt_ob_ch13/<id>',branch13.auguest_account_mgt_ob_ch13,name='auguest_account_mgt_ob_ch13'),

    path('view_sept_account_details_ob_ch13/', branch13.view_sept_account_details_ob_ch13, name='view_sept_account_details_ob_ch13'),
    path('sept_account_mgt_ob_ch13/<id>',branch13.sept_account_mgt_ob_ch13,name='sept_account_mgt_ob_ch13'),
    path('view_october_account_details_ob_ch13/', branch13.view_october_account_details_ob_ch13, name='view_october_account_details_ob_ch13'),
    path('october_account_mgt_ob_ch13/<id>',branch13.october_account_mgt_ob_ch13,name='october_account_mgt_ob_ch13'),
    path('view_nov_account_details_ob_ch13/', branch13.view_nov_account_details_ob_ch13, name='view_nov_account_details_ob_ch13'),
    path('nov_account_mgt_ob_ch13/<id>',branch13.nov_account_mgt_ob_ch13,name='nov_account_mgt_ob_ch13'),
    path('view_dec_account_details_ob_ch13/', branch13.view_dec_account_details_ob_ch13, name='view_dec_account_details_ob_ch13'),
    path('dec_account_mgt_ob_ch13/<id>',branch13.dec_account_mgt_ob_ch13,name='dec_account_mgt_ob_ch13'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch13', admin_dashboard_calculations_br13.monthly_details_due_ob_ch13, name='monthly_details_due_ob_ch13'),
    path('monthly_collection_details_ob_ch13/', admin_dashboard_calculations_br13.monthly_collection_details_ob_ch13, name='monthly_collection_details_ob_ch13'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch13/',branch13.guest_all_ob_ch13,name='guest_all_ob_ch13'),








#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category13/', accounts13.view_all_category13, name='view_all_category13'),
    path('create_new_category13/', accounts13.create_new_category13, name='create_new_category13'),
    path('regi_new_category13/', accounts13.regi_new_category13, name='regi_new_category13'),
    path('update_category13/<id>',accounts13.update_category13,name='update_category13'),

    path('delete_category13/<id>', accounts13.delete_category13, name='delete_category13'),
    path('view_all_category_delete13/', accounts13.view_all_category_delete13, name='view_all_category_delete13'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items13/', accounts13.view_all_items13, name='view_all_items13'),
    path('create_new_item13/', accounts13.create_new_item13, name='create_new_item13'),
    path('regi_new_item13/', accounts13.regi_new_item13, name='regi_new_item13'),
    path('delete_item13/<id>',accounts13.delete_item13,name='delete_item13'),
    path('update_item13/<id>', accounts13.update_item13, name='update_item13'),
    path('view_all_items_delete13/',accounts13.view_all_items_delete13,name='view_all_items_delete13'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger13/', accounts13.view_all_ledger13, name='view_all_ledger13'),
    path('create_new_ledger13/', accounts13.create_new_ledger13, name='create_new_ledger13'),
    path('regi_new_ledger13/', accounts13.regi_new_ledger13, name='regi_new_ledger13'),
    path('delete_ledger13/<id>',accounts13.delete_ledger13,name='delete_ledger13'),
    path('update_ledger13/<id>',accounts13.update_ledger13,name='update_ledger13'),
    path('view_all_ledger_delete13/',accounts13.view_all_ledger_delete13,name='view_all_ledger_delete13'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book13/', accounts13.view_all_accounts_book13, name='view_all_accounts_book13'),
    path('create_new_accounts_book13/', accounts13.create_new_accounts_book13, name='create_new_accounts_book13'),
    path('regi_new_accounts_book13/', accounts13.regi_new_accounts_book13, name='regi_new_accounts_book13'),
    path('update_accounts_book13/<id>',accounts13.update_accounts_book13,name='update_accounts_book13'),
    path('delete_accounts_book13/<id>',accounts13.delete_accounts_book13,name='delete_accounts_book13'),
    path('view_all_accounts_book_delete13/',accounts13.view_all_accounts_book_delete13,name='view_all_accounts_book_delete13'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries13/', accounts13.get_countries13, name='get_countries13'),

    path('in_exp_items_entry13/', accounts13.in_exp_items_entry13, name='in_exp_items_entry13'),
    path('reg_in_exp_items_entry13/', accounts13.reg_in_exp_items_entry13, name='reg_in_exp_items_entry13'),
    path('delete_journal13/<id>',accounts13.delete_journal13,name='delete_journal13'),
    path('update_in_exp_items_entry13/<id>',accounts13.update_in_exp_items_entry13,name='update_in_exp_items_entry13'),
    path('detailed_journal_report13/',accounts13.detailed_journal_report13,name='detailed_journal_report13'),
    path('journal_report_deleted13/',accounts13.journal_report_deleted13,name='journal_report_deleted13'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise13/', accounts13.daily_category_wise13, name='daily_category_wise13'),
    path('monthly_category_based_reports13/',accounts13.monthly_category_based_reports13,name='monthly_category_based_reports13'),
    path('yearly_category_based_reports13/', accounts13.yearly_category_based_reports13,name='yearly_category_based_reports13'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed13/', accounts13.daily_detailed13, name='daily_detailed13'),
    path('monthly_detailed13/',accounts13.monthly_detailed13,name='monthly_detailed13'),
    path('yearly_detailed13/',accounts13.yearly_detailed13,name='yearly_detailed13'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports13/', accounts13.item_based_reports13, name='item_based_reports13'),
    path('daily_item_based_reports13/',accounts13.daily_item_based_reports13,name='daily_item_based_reports13'),
    path('monthly_item_based_reports13/',accounts13.monthly_item_based_reports13,name='monthly_item_based_reports13'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports13/', accounts13.ledger_based_reports13, name='ledger_based_reports13'),
    path('monthly_ledger_based_reports13/', accounts13.monthly_ledger_based_reports13, name='monthly_ledger_based_reports13'),
    path('daily_ledger_based_reports13/',accounts13.daily_ledger_based_reports13,name='daily_ledger_based_reports13'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports13/', accounts13.accounts_book_based_reports13, name='accounts_book_based_reports13'),
    path('daily_accounts_book_based_reports13/',accounts13.daily_accounts_book_based_reports13,name='daily_accounts_book_based_reports13'),
    path('monthly_accounts_book_based_reports13/',accounts13.monthly_accounts_book_based_reports13,name='monthly_accounts_book_based_reports13'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months13/', accounts13.monthly_reports_choose_months13, name='monthly_reports_choose_months13'),
    path('monthly_detailed_daily_in_exp_items_report13/<mo>',accounts13.monthly_detailed_daily_in_exp_items_report13,name='monthly_detailed_daily_in_exp_items_report13'),

    path('single_monthly_reports_choose_months13/', accounts13.single_monthly_reports_choose_months13,name='single_monthly_reports_choose_months13'),
    path('single_monthly_daily_in_exp_items_report13/<mo>',accounts13.single_monthly_daily_in_exp_items_report13,name='single_monthly_daily_in_exp_items_report13'),

    path('accounts_dash_board_ob_ch13/',accounts13.accounts_dash_board_ob_ch13,name='accounts_dash_board_ob_ch13'),

    path('profit_sharing_choose_months13', accounts13.profit_sharing_choose_months13,name='profit_sharing_choose_months13'),
    path('profit_sharing13/<mo>', accounts13.profit_sharing13, name='profit_sharing13'),
    path('view_share_holders13', accounts13.view_share_holders13, name='view_share_holders13'),
    path('create_share_holders13', accounts13.create_share_holders13, name='create_share_holders13'),
    path('regi_share_holders13', accounts13.regi_share_holders13, name='regi_share_holders13'),
    path('update_share_holders13/<id>', accounts13.update_share_holders13, name='update_share_holders13'),
    path('delete_share_holders13/<id>', accounts13.delete_share_holders13, name='delete_share_holders13'),
    path('view_deleted_share_holders13', accounts13.view_deleted_share_holders13, name='view_deleted_share_holders13'),

]

