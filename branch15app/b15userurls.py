from django.urls import path, include

from . import admin_branch15
from . import admin_branch15
from . import branch15
from . import reports15
from . import payment15
from . import admin_dashboard_calculations_br15
from . import accounts15

urlpatterns = [

    path('branch1_dashboard_ob_ch15/', branch15.branch1_dashboard_ob_ch15, name='branch1_dashboard_ob_ch15'),
    path('branch1_dashboard15/',branch15.branch1_dashboard15,name='branch1_dashboard15'),
    path('user_dashboard_calculations_ob_ch15/',branch15.user_dashboard_calculations_ob_ch15,name='user_dashboard_calculations_ob_ch15'),

    path('background_ob_ch15',branch15.background_ob_ch15,name='background_ob_ch15'),
    path('background_regi_ob_ch15',branch15.background_regi_ob_ch15,name='background_regi_ob_ch15'),
    path('custom_background_regi_ob_ch15',branch15.custom_background_regi_ob_ch15,name='custom_background_regi_ob_ch15'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch15/',admin_branch15.branch1_room_create_regi_ob_ch15,name='branch1_room_create_regi_ob_ch15'),
    path('view_all_room_ob_ch15/',admin_branch15.view_all_room_ob_ch15,name='view_all_room_ob_ch15'),
    path('delete_room_ob_ch15/<id>',admin_branch15.delete_room_ob_ch15,name='delete_room_ob_ch15'),

    path('branch1_room_create_ob_ch15/',admin_branch15.branch1_room_create_ob_ch15,name='branch1_room_create_ob_ch15'),

    path('multiple_branch1_room_create_regi15/',admin_branch15.multiple_branch1_room_create_regi15,name='multiple_branch1_room_create_regi15'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch15/', admin_branch15.pg1_bed_create_regi_ob_ch15, name='pg1_bed_create_regi_ob_ch15'),
    path('pg1_view_all_beds_ob_ch15/', admin_branch15.pg1_view_all_beds_ob_ch15, name='pg1_view_all_beds_ob_ch15'),
    path('delete_bed_ob_ch15/<id>', admin_branch15.delete_bed_ob_ch15, name='delete_bed_ob_ch15'),

    path('pg1_bed_create_ob_ch15/', admin_branch15.pg1_bed_create_ob_ch15, name='pg1_bed_create_ob_ch15'),

    path('single_pg1_bed_create_regi_ob_ch15/',admin_branch15.single_pg1_bed_create_regi_ob_ch15,name='single_pg1_bed_create_regi_ob_ch15'),
    path('update_bed_basic_details_ob_ch15/<id>',admin_branch15.update_bed_basic_details_ob_ch15, name='update_bed_basic_details_ob_ch15'),

    path('multiple_single_pg1_bed_create_regi15/',admin_branch15.multiple_single_pg1_bed_create_regi15,name='multiple_single_pg1_bed_create_regi15'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch15/<id>',branch15.br1_admit_guest_ob_ch15,name='br1_admit_guest_ob_ch15'),
    path('view_all_new_guest_ob_ch15/',branch15.view_all_new_guest_ob_ch15,name='view_all_new_guest_ob_ch15'),
    path('update_br1_admit_guest_ob_ch15/<id>',branch15.update_br1_admit_guest_ob_ch15,name='update_br1_admit_guest_ob_ch15'),
    path('vacate_br1_guest_ob_ch15/<id>',branch15.vacate_br1_guest_ob_ch15,name='vacate_br1_guest_ob_ch15'),

    path('active_guest_details_ob_ch15/<guest_code>',branch15.active_guest_details_ob_ch15,name='active_guest_details_ob_ch15'),
    path('view_all_guest_ob_ch15/',branch15.view_all_guest_ob_ch15,name='view_all_guest_ob_ch15'),
    path('shift_guest_ob_ch15/<id>',branch15.shift_guest_ob_ch15,name='shift_guest_ob_ch15'),
    path('shift_guest_regi_ob_ch15/',branch15.shift_guest_regi_ob_ch15,name='shift_guest_regi_ob_ch15'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch15/',branch15.update_all_rent_ob_ch15,name='update_all_rent_ob_ch15'),

    path('multiple_br1_admit_guest15/<id>',branch15.multiple_br1_admit_guest15,name='multiple_br1_admit_guest15'),

#guest end here


##################################
#_ADVANCE_ob_ch15 START HERE
################################


    path('choose_months_advance_ob_ch15/',branch15.choose_months_advance_ob_ch15,name='choose_months_advance_ob_ch15'),

    path('jan_advance_ob_ch15/', branch15.jan_advance_ob_ch15, name='jan_advance_ob_ch15'),
    path('jan_make_payments_advance_ob_ch15/<id>', branch15.jan_make_payments_advance_ob_ch15,name='jan_make_payments_advance_ob_ch15'),
    path('feb_advance_ob_ch15/', branch15.feb_advance_ob_ch15, name='feb_advance_ob_ch15'),
    path('feb_make_payments_advance_ob_ch15/<id>', branch15.feb_make_payments_advance_ob_ch15,name='feb_make_payments_advance_ob_ch15'),
    path('march_advance_ob_ch15/', branch15.march_advance_ob_ch15, name='march_advance_ob_ch15'),
    path('march_make_payments_advance_ob_ch15/<id>', branch15.march_make_payments_advance_ob_ch15,name='march_make_payments_advance_ob_ch15'),
    path('april_advance_ob_ch15/', branch15.april_advance_ob_ch15, name='april_advance_ob_ch15'),
    path('april_make_payments_advance_ob_ch15/<id>', branch15.april_make_payments_advance_ob_ch15, name='april_make_payments_advance_ob_ch15'),

    path('may_advance_ob_ch15/',branch15.may_advance_ob_ch15,name='may_advance_ob_ch15'),
    path('may_make_payments_advance_ob_ch15/<id>', branch15.may_make_payments_advance_ob_ch15, name='may_make_payments_advance_ob_ch15'),
    path('june_advance_ob_ch15/',branch15.june_advance_ob_ch15,name='june_advance_ob_ch15'),
    path('june_make_payments_advance_ob_ch15/<id>', branch15.june_make_payments_advance_ob_ch15, name='june_make_payments_advance_ob_ch15'),
    path('july_advance_ob_ch15/',branch15.july_advance_ob_ch15,name='july_advance_ob_ch15'),
    path('july_make_payments_advance_ob_ch15/<id>', branch15.july_make_payments_advance_ob_ch15, name='july_make_payments_advance_ob_ch15'),
    path('auguest_advance_ob_ch15/', branch15.auguest_advance_ob_ch15, name='auguest_advance_ob_ch15'),
    path('auguest_make_payments_advance_ob_ch15/<id>', branch15.auguest_make_payments_advance_ob_ch15, name='auguest_make_payments_advance_ob_ch15'),

    path('sept_advance_ob_ch15/', branch15.sept_advance_ob_ch15, name='sept_advance_ob_ch15'),
    path('sept_make_payments_advance_ob_ch15/<id>', branch15.sept_make_payments_advance_ob_ch15,name='sept_make_payments_advance_ob_ch15'),
    path('october_advance_ob_ch15/', branch15.october_advance_ob_ch15, name='october_advance_ob_ch15'),
    path('october_make_payments_advance_ob_ch15/<id>', branch15.october_make_payments_advance_ob_ch15, name='october_make_payments_advance_ob_ch15'),
    path('nov_advance_ob_ch15/', branch15.nov_advance_ob_ch15, name='nov_advance_ob_ch15'),
    path('nov_make_payments_advance_ob_ch15/<id>', branch15.nov_make_payments_advance_ob_ch15,name='nov_make_payments_advance_ob_ch15'),
    path('dec_advance_ob_ch15/', branch15.dec_advance_ob_ch15, name='dec_advance_ob_ch15'),
    path('dec_make_payments_advance_ob_ch15/<id>', branch15.dec_make_payments_advance_ob_ch15, name='dec_make_payments_advance_ob_ch15'),



##################################
#_ADVANCE_ob_ch15 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch15/',branch15.choose_months_ob_ch15,name='choose_months_ob_ch15'),

    path('jan_ob_ch15/',branch15.jan_ob_ch15,name='jan_ob_ch15'),
    path('jan_manke_payments_ob_ch15/<id>',branch15.jan_manke_payments_ob_ch15,name='jan_manke_payments_ob_ch15'),

    path('feb_ob_ch15/',branch15.feb_ob_ch15,name='feb_ob_ch15'),
    path('feb_manke_payments_ob_ch15/<id>',branch15.feb_manke_payments_ob_ch15,name='feb_manke_payments_ob_ch15'),

    path('march_ob_ch15/',branch15.march_ob_ch15,name='march_ob_ch15'),
    path('march_manke_payments_ob_ch15/<id>',branch15.march_manke_payments_ob_ch15,name='march_manke_payments_ob_ch15'),

    path('april_ob_ch15/',branch15.april_ob_ch15,name='april_ob_ch15'),
    path('april_make_payments_ob_ch15/<id>',branch15.april_make_payments_ob_ch15,name='april_make_payments_ob_ch15'),

    path('may_ob_ch15/',branch15.may_ob_ch15,name='may_ob_ch15'),
    path('may_make_payments_ob_ch15/<id>',branch15.may_make_payments_ob_ch15,name='may_make_payments_ob_ch15'),

    path('june_ob_ch15/',branch15.june_ob_ch15,name='june_ob_ch15'),
    path('june_make_payments_ob_ch15/<id>',branch15.june_make_payments_ob_ch15,name='june_make_payments_ob_ch15'),

    path('july_ob_ch15/',branch15.july_ob_ch15,name='july_ob_ch15'),
    path('july_make_payments_ob_ch15/<id>',branch15.july_make_payments_ob_ch15,name='july_make_payments_ob_ch15'),

    path('aug_ob_ch15/',branch15.aug_ob_ch15,name='aug_ob_ch15'),
    path('aug_make_payments_ob_ch15/<id>',branch15.aug_make_payments_ob_ch15,name='aug_make_payments_ob_ch15'),

    path('sept_ob_ch15/',branch15.sept_ob_ch15,name='sept_ob_ch15'),
    path('sept_make_payments_ob_ch15/<id>',branch15.sept_make_payments_ob_ch15,name='sept_make_payments_ob_ch15'),

    path('oct_ob_ch15/',branch15.oct_ob_ch15,name='oct_ob_ch15'),
    path('oct_make_payments_ob_ch15/<id>',branch15.oct_make_payments_ob_ch15,name='oct_make_payments_ob_ch15'),

    path('nov_ob_ch15/',branch15.nov_ob_ch15,name='nov_ob_ch15'),
    path('nov_make_payments_ob_ch15/<id>',branch15.nov_make_payments_ob_ch15,name='nov_make_payments_ob_ch15'),

    path('dec_ob_ch15/',branch15.dec_ob_ch15,name='dec_ob_ch15'),
    path('dec_make_payments_ob_ch15/<id>',branch15.dec_make_payments_ob_ch15,name='dec_make_payments_ob_ch15'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch15/', payment15.choose_user_ob_ch15, name='choose_user_ob_ch15'),
    path('payment_user_details_ob_ch15/<id>', payment15.payment_user_details_ob_ch15, name='payment_user_details_ob_ch15'),
    path('close_choose_user_ob_ch15/<id>',payment15.close_choose_user_ob_ch15,name='close_choose_user_ob_ch15'),

    path('monthly_jan_make_payments_ob_ch15/<id>', payment15.monthly_jan_make_payments_ob_ch15, name='monthly_jan_make_payments_ob_ch15'),
    path('monthly_feb_make_payments_ob_ch15/<id>', payment15.monthly_feb_make_payments_ob_ch15, name='monthly_feb_make_payments_ob_ch15'),
    path('monthly_march_make_payments_ob_ch15/<id>', payment15.monthly_march_make_payments_ob_ch15, name='monthly_march_make_payments_ob_ch15'),
    path('monthly_april_make_payments_ob_ch15/<id>', payment15.monthly_april_make_payments_ob_ch15, name='monthly_april_make_payments_ob_ch15'),
    path('monthly_may_make_payments_ob_ch15/<id>', payment15.monthly_may_make_payments_ob_ch15, name='monthly_may_make_payments_ob_ch15'),
    path('monthly_june_make_payments_ob_ch15/<id>', payment15.monthly_june_make_payments_ob_ch15, name='monthly_june_make_payments_ob_ch15'),

    path('monthly_july_make_payments_ob_ch15/<id>', payment15.monthly_july_make_payments_ob_ch15, name='monthly_july_make_payments_ob_ch15'),
    path('monthly_aug_make_payments_ob_ch15/<id>', payment15.monthly_aug_make_payments_ob_ch15, name='monthly_aug_make_payments_ob_ch15'),
    path('monthly_sept_make_payments_ob_ch15/<id>', payment15.monthly_sept_make_payments_ob_ch15, name='monthly_sept_make_payments_ob_ch15'),
    path('monthly_oct_make_payments_ob_ch15/<id>', payment15.monthly_oct_make_payments_ob_ch15, name='monthly_oct_make_payments_ob_ch15'),
    path('monthly_nov_make_payments_ob_ch15/<id>', payment15.monthly_nov_make_payments_ob_ch15, name='monthly_nov_make_payments_ob_ch15'),
    path('monthly_dec_make_payments_ob_ch15/<id>', payment15.monthly_dec_make_payments_ob_ch15, name='monthly_dec_make_payments_ob_ch15'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch15/',branch15.unpaid_rent_choose_months_ob_ch15,name='unpaid_rent_choose_months_ob_ch15'),

    path('jan_unpaid_rent_ob_ch15/', branch15.jan_unpaid_rent_ob_ch15, name='jan_unpaid_rent_ob_ch15'),
    path('table_jan_unpaid_rent_ob_ch15/', branch15.table_jan_unpaid_rent_ob_ch15, name='table_jan_unpaid_rent_ob_ch15'),
    path('feb_unpaid_rent_ob_ch15/', branch15.feb_unpaid_rent_ob_ch15, name='feb_unpaid_rent_ob_ch15'),
    path('table_feb_unpaid_rent_ob_ch15/', branch15.table_feb_unpaid_rent_ob_ch15, name='table_feb_unpaid_rent_ob_ch15'),
    path('mar_unpaid_rent_ob_ch15/', branch15.mar_unpaid_rent_ob_ch15, name='mar_unpaid_rent_ob_ch15'),
    path('table_mar_unpaid_rent_ob_ch15/', branch15.table_mar_unpaid_rent_ob_ch15, name='table_mar_unpaid_rent_ob_ch15'),
    path('april_unpaid_rent_ob_ch15/', branch15.april_unpaid_rent_ob_ch15, name='april_unpaid_rent_ob_ch15'),
    path('table_april_unpaid_rent_ob_ch15/', branch15.table_april_unpaid_rent_ob_ch15, name='table_april_unpaid_rent_ob_ch15'),

    path('may_unpaid_rent_ob_ch15/', branch15.may_unpaid_rent_ob_ch15, name='may_unpaid_rent_ob_ch15'),
    path('table_may_unpaid_rent_ob_ch15/', branch15.table_may_unpaid_rent_ob_ch15, name='table_may_unpaid_rent_ob_ch15'),
    path('june_unpaid_rent_ob_ch15/', branch15.june_unpaid_rent_ob_ch15, name='june_unpaid_rent_ob_ch15'),
    path('table_june_unpaid_rent_ob_ch15/', branch15.table_june_unpaid_rent_ob_ch15, name='table_june_unpaid_rent_ob_ch15'),
    path('july_unpaid_rent_ob_ch15/', branch15.july_unpaid_rent_ob_ch15, name='july_unpaid_rent_ob_ch15'),
    path('table_july_unpaid_rent_ob_ch15',branch15.table_july_unpaid_rent_ob_ch15,name='table_july_unpaid_rent_ob_ch15'),
    path('aug_unpaid_rent_ob_ch15/', branch15.aug_unpaid_rent_ob_ch15, name='aug_unpaid_rent_ob_ch15'),
    path('table_aug_unpaid_rent_ob_ch15/',branch15.table_aug_unpaid_rent_ob_ch15,name='table_aug_unpaid_rent_ob_ch15'),

    path('sept_unpaid_rent_ob_ch15/', branch15.sept_unpaid_rent_ob_ch15, name='sept_unpaid_rent_ob_ch15'),
    path('table_sept_unpaid_rent_ob_ch15/', branch15.table_sept_unpaid_rent_ob_ch15, name='table_sept_unpaid_rent_ob_ch15'),
    path('oct_unpaid_rent_ob_ch15/', branch15.oct_unpaid_rent_ob_ch15, name='oct_unpaid_rent_ob_ch15'),
    path('table_oct_unpaid_rent_ob_ch15/', branch15.table_oct_unpaid_rent_ob_ch15, name='table_oct_unpaid_rent_ob_ch15'),
    path('nov_unpaid_rent_ob_ch15/', branch15.nov_unpaid_rent_ob_ch15, name='nov_unpaid_rent_ob_ch15'),
    path('table_nov_unpaid_rent_ob_ch15/', branch15.table_nov_unpaid_rent_ob_ch15, name='table_nov_unpaid_rent_ob_ch15'),
    path('dec_unpaid_rent_ob_ch15/', branch15.dec_unpaid_rent_ob_ch15, name='dec_unpaid_rent_ob_ch15'),
    path('table_dec_unpaid_rent_ob_ch15/', branch15.table_dec_unpaid_rent_ob_ch15, name='table_dec_unpaid_rent_ob_ch15'),

    path('details_of_unpaid_guests_ob_ch15/<id>',branch15.details_of_unpaid_guests_ob_ch15,name='details_of_unpaid_guests_ob_ch15'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch15/',branch15.paid_rent_choose_months_ob_ch15,name='paid_rent_choose_months_ob_ch15'),
    path('partially_paid_guest_choose_months_ob_ch15/',reports15.partially_paid_guest_choose_months_ob_ch15,name='partially_paid_guest_choose_months_ob_ch15'),

    path('jan_paid_rent_ob_ch15/', branch15.jan_paid_rent_ob_ch15, name='jan_paid_rent_ob_ch15'),
    path('table_jan_paid_rent_ob_ch15/', branch15.table_jan_paid_rent_ob_ch15, name='table_jan_paid_rent_ob_ch15'),
    path('jan_full_paid_guest_ob_ch15/', reports15.jan_full_paid_guest_ob_ch15, name='jan_full_paid_guest_ob_ch15'),
    path('jan_partially_paid_guest_ob_ch15/', reports15.jan_partially_paid_guest_ob_ch15, name='jan_partially_paid_guest_ob_ch15'),
    path('table_jan_partially_paid_guest_ob_ch15/', reports15.table_jan_partially_paid_guest_ob_ch15,name='table_jan_partially_paid_guest_ob_ch15'),

    path('feb_paid_rent_ob_ch15/', branch15.feb_paid_rent_ob_ch15, name='feb_paid_rent_ob_ch15'),
    path('table_feb_paid_rent_ob_ch15/', branch15.table_feb_paid_rent_ob_ch15, name='table_feb_paid_rent_ob_ch15'),
    path('feb_full_paid_guest_ob_ch15/', reports15.feb_full_paid_guest_ob_ch15, name='feb_full_paid_guest_ob_ch15'),
    path('feb_partially_paid_guest_ob_ch15/', reports15.feb_partially_paid_guest_ob_ch15, name='feb_partially_paid_guest_ob_ch15'),
    path('table_feb_partially_paid_guest_ob_ch15/', reports15.table_feb_partially_paid_guest_ob_ch15,name='table_feb_partially_paid_guest_ob_ch15'),

    path('mar_paid_rent_ob_ch15/', branch15.mar_paid_rent_ob_ch15, name='mar_paid_rent_ob_ch15'),
    path('table_mar_paid_rent_ob_ch15/', branch15.table_mar_paid_rent_ob_ch15, name='table_mar_paid_rent_ob_ch15'),
    path('march_full_paid_guest_ob_ch15/', reports15.march_full_paid_guest_ob_ch15, name='march_full_paid_guest_ob_ch15'),
    path('march_partially_paid_guest_ob_ch15/', reports15.march_partially_paid_guest_ob_ch15, name='march_partially_paid_guest_ob_ch15'),
    path('table_march_partially_paid_guest_ob_ch15/', reports15.table_march_partially_paid_guest_ob_ch15,name='table_march_partially_paid_guest_ob_ch15'),

    path('april_paid_rent_ob_ch15/', branch15.april_paid_rent_ob_ch15, name='april_paid_rent_ob_ch15'),
    path('table_april_paid_rent_ob_ch15/', branch15.table_april_paid_rent_ob_ch15, name='table_april_paid_rent_ob_ch15'),
    path('april_full_paid_guest_ob_ch15/', reports15.april_full_paid_guest_ob_ch15, name='april_full_paid_guest_ob_ch15'),
    path('april_partially_paid_guest_ob_ch15/', reports15.april_partially_paid_guest_ob_ch15, name='april_partially_paid_guest_ob_ch15'),
    path('table_april_partially_paid_guest_ob_ch15/', reports15.table_april_partially_paid_guest_ob_ch15,name='table_april_partially_paid_guest_ob_ch15'),

    path('may_paid_rent_ob_ch15/', branch15.may_paid_rent_ob_ch15, name='may_paid_rent_ob_ch15'),
    path('table_may_paid_rent_ob_ch15/', branch15.table_may_paid_rent_ob_ch15, name='table_may_paid_rent_ob_ch15'),
    path('may_full_paid_guest_ob_ch15/', reports15.may_full_paid_guest_ob_ch15, name='may_full_paid_guest_ob_ch15'),
    path('may_partially_paid_guest_ob_ch15/', reports15.may_partially_paid_guest_ob_ch15, name='may_partially_paid_guest_ob_ch15'),
    path('table_may_partially_paid_guest_ob_ch15/', reports15.table_may_partially_paid_guest_ob_ch15, name='table_may_partially_paid_guest_ob_ch15'),

    path('june_paid_rent_ob_ch15/', branch15.june_paid_rent_ob_ch15, name='june_paid_rent_ob_ch15'),
    path('table_june_paid_rent_ob_ch15/', branch15.table_june_paid_rent_ob_ch15, name='table_june_paid_rent_ob_ch15'),
    path('june_full_paid_guest_ob_ch15/', reports15.june_full_paid_guest_ob_ch15, name='june_full_paid_guest_ob_ch15'),
    path('june_partially_paid_guest_ob_ch15/', reports15.june_partially_paid_guest_ob_ch15, name='june_partially_paid_guest_ob_ch15'),
    path('table_june_partially_paid_guest_ob_ch15/', reports15.table_june_partially_paid_guest_ob_ch15, name='table_june_partially_paid_guest_ob_ch15'),

    path('july_paid_rent_ob_ch15/', branch15.july_paid_rent_ob_ch15, name='july_paid_rent_ob_ch15'),
    path('table_july_paid_rent_ob_ch15/', branch15.table_july_paid_rent_ob_ch15, name='table_july_paid_rent_ob_ch15'),
    path('july_full_paid_guest_ob_ch15/', reports15.july_full_paid_guest_ob_ch15, name='july_full_paid_guest_ob_ch15'),
    path('july_partially_paid_guest_ob_ch15/', reports15.july_partially_paid_guest_ob_ch15, name='july_partially_paid_guest_ob_ch15'),
    path('table_july_partially_paid_guest_ob_ch15/', reports15.table_july_partially_paid_guest_ob_ch15, name='table_july_partially_paid_guest_ob_ch15'),

    path('aug_paid_rent_ob_ch15/', branch15.aug_paid_rent_ob_ch15, name='aug_paid_rent_ob_ch15'),
    path('table_aug_paid_rent_ob_ch15/', branch15.table_aug_paid_rent_ob_ch15, name='table_aug_paid_rent_ob_ch15'),
    path('auguest_full_paid_guest_ob_ch15/', reports15.auguest_full_paid_guest_ob_ch15, name='auguest_full_paid_guest_ob_ch15'),
    path('auguest_partially_paid_guest_ob_ch15/', reports15.auguest_partially_paid_guest_ob_ch15,name='auguest_partially_paid_guest_ob_ch15'),
    path('table_auguest_partially_paid_guest_ob_ch15/', reports15.table_auguest_partially_paid_guest_ob_ch15,name='table_auguest_partially_paid_guest_ob_ch15'),

    path('sept_paid_rent_ob_ch15/', branch15.sept_paid_rent_ob_ch15, name='sept_paid_rent_ob_ch15'),
    path('table_sept_paid_rent_ob_ch15/', branch15.table_sept_paid_rent_ob_ch15, name='table_sept_paid_rent_ob_ch15'),
    path('sept_full_paid_guest_ob_ch15/', reports15.sept_full_paid_guest_ob_ch15, name='sept_full_paid_guest_ob_ch15'),
    path('sept_partially_paid_guest_ob_ch15/', reports15.sept_partially_paid_guest_ob_ch15, name='sept_partially_paid_guest_ob_ch15'),
    path('table_sept_partially_paid_guest_ob_ch15/', reports15.table_sept_partially_paid_guest_ob_ch15,name='table_sept_partially_paid_guest_ob_ch15'),

    path('oct_paid_rent_ob_ch15/', branch15.oct_paid_rent_ob_ch15, name='oct_paid_rent_ob_ch15'),
    path('table_oct_paid_rent_ob_ch15/', branch15.table_oct_paid_rent_ob_ch15, name='table_oct_paid_rent_ob_ch15'),
    path('october_full_paid_guest_ob_ch15/', reports15.october_full_paid_guest_ob_ch15, name='october_full_paid_guest_ob_ch15'),
    path('october_partially_paid_guest_ob_ch15/', reports15.october_partially_paid_guest_ob_ch15,name='october_partially_paid_guest_ob_ch15'),
    path('table_october_partially_paid_guest_ob_ch15/', reports15.table_october_partially_paid_guest_ob_ch15,name='table_october_partially_paid_guest_ob_ch15'),

    path('nov_paid_rent_ob_ch15/', branch15.nov_paid_rent_ob_ch15, name='nov_paid_rent_ob_ch15'),
    path('table_nov_paid_rent_ob_ch15/', branch15.table_nov_paid_rent_ob_ch15, name='table_nov_paid_rent_ob_ch15'),
    path('nov_full_paid_guest_ob_ch15/', reports15.nov_full_paid_guest_ob_ch15, name='nov_full_paid_guest_ob_ch15'),
    path('nov_partially_paid_guest_ob_ch15/', reports15.nov_partially_paid_guest_ob_ch15, name='nov_partially_paid_guest_ob_ch15'),
    path('table_nov_partially_paid_guest_ob_ch15/', reports15.table_nov_partially_paid_guest_ob_ch15,name='table_nov_partially_paid_guest_ob_ch15'),

    path('dec_paid_rent_ob_ch15/', branch15.dec_paid_rent_ob_ch15, name='dec_paid_rent_ob_ch15'),
    path('table_dec_paid_rent_ob_ch15/', branch15.table_dec_paid_rent_ob_ch15, name='table_dec_paid_rent_ob_ch15'),
    path('dec_full_paid_guest_ob_ch15/', reports15.dec_full_paid_guest_ob_ch15, name='dec_full_paid_guest_ob_ch15'),
    path('dec_partially_paid_guest_ob_ch15/', reports15.dec_partially_paid_guest_ob_ch15, name='dec_partially_paid_guest_ob_ch15'),
    path('table_dec_partially_paid_guest_ob_ch15/', reports15.table_dec_partially_paid_guest_ob_ch15,name='table_dec_partially_paid_guest_ob_ch15'),

    path('details_of_paid_guests_ob_ch15/<id>',branch15.details_of_paid_guests_ob_ch15,name='details_of_paid_guests_ob_ch15'),
    path('full_paid_guest_ob_ch15/',reports15.full_paid_guest_ob_ch15,name='full_paid_guest_ob_ch15'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch15/',branch15.viewall_vacate_guest_ob_ch15,name='viewall_vacate_guest_ob_ch15'),
    path('details_of_vacate_guest_ob_ch15/<id>',branch15.details_of_vacate_guest_ob_ch15,name='details_of_vacate_guest_ob_ch15'),
    path('full_vacated_guest_details_ob_ch15',branch15.full_vacated_guest_details_ob_ch15,name='full_vacated_guest_details_ob_ch15'),
    path('full_vacated_guest_table_ob_ch15',branch15.full_vacated_guest_table_ob_ch15,name='full_vacated_guest_table_ob_ch15'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch15/<id>', branch15.jan_manke_payments_vacate_ob_ch15, name='jan_manke_payments_vacate_ob_ch15'),
    path('feb_manke_payments_vacate_ob_ch15/<id>', branch15.feb_manke_payments_vacate_ob_ch15, name='feb_manke_payments_vacate_ob_ch15'),
    path('march_manke_payments_vacate_ob_ch15/<id>', branch15.march_manke_payments_vacate_ob_ch15, name='march_manke_payments_vacate_ob_ch15'),
    path('april_make_payments_vacate_ob_ch15/<id>', branch15.april_make_payments_vacate_ob_ch15, name='april_make_payments_vacate_ob_ch15'),

    path('may_make_payments_vacate_ob_ch15/<id>', branch15.may_make_payments_vacate_ob_ch15, name='may_make_payments_vacate_ob_ch15'),
    path('june_make_payments_vacate_ob_ch15/<id>', branch15.june_make_payments_vacate_ob_ch15, name='june_make_payments_vacate_ob_ch15'),
    path('july_make_payments_vacate_ob_ch15/<id>', branch15.july_make_payments_vacate_ob_ch15, name='july_make_payments_vacate_ob_ch15'),
    path('aug_make_payments_vacate_ob_ch15/<id>', branch15.aug_make_payments_vacate_ob_ch15, name='aug_make_payments_vacate_ob_ch15'),

    path('sept_make_payments_vacate_ob_ch15/<id>', branch15.sept_make_payments_vacate_ob_ch15, name='sept_make_payments_vacate_ob_ch15'),
    path('oct_make_payments_vacate_ob_ch15/<id>', branch15.oct_make_payments_vacate_ob_ch15, name='oct_make_payments_vacate_ob_ch15'),
    path('nov_make_payments_vacate_ob_ch15/<id>', branch15.nov_make_payments_vacate_ob_ch15, name='nov_make_payments_vacate_ob_ch15'),
    path('dec_make_payments_vacate_ob_ch15/<id>', branch15.dec_make_payments_vacate_ob_ch15, name='dec_make_payments_vacate_ob_ch15'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch15/',branch15.detail_guest_general_ob_ch15,name='detail_guest_general_ob_ch15'),

    path('jan_print_ob_ch15/',branch15.jan_print_ob_ch15,name='jan_print_ob_ch15'),
    path('feb_print_ob_ch15/',branch15.feb_print_ob_ch15,name='feb_print_ob_ch15'),
    path('march_print_ob_ch15/',branch15.march_print_ob_ch15,name='march_print_ob_ch15'),
    path('april_print_ob_ch15/',branch15.april_print_ob_ch15,name='april_print_ob_ch15'),

    path('may_print_ob_ch15/',branch15.may_print_ob_ch15,name='may_print_ob_ch15'),
    path('june_print_ob_ch15/',branch15.june_print_ob_ch15,name='june_print_ob_ch15'),
    path('july_print_ob_ch15/', branch15.july_print_ob_ch15, name='july_print_ob_ch15'),
    path('aug_print_ob_ch15/', branch15.aug_print_ob_ch15, name='aug_print_ob_ch15'),

    path('sept_print_ob_ch15/', branch15.sept_print_ob_ch15, name='sept_print_ob_ch15'),
    path('oct_print_ob_ch15/', branch15.oct_print_ob_ch15, name='oct_print_ob_ch15'),
    path('nov_print_ob_ch15/', branch15.nov_print_ob_ch15, name='nov_print_ob_ch15'),
    path('dec_print_ob_ch15/', branch15.dec_print_ob_ch15, name='dec_print_ob_ch15'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch15/', branch15.jan_close_ob_ch15, name='jan_close_ob_ch15'),
    path('jan_close_decision_page_ob_ch15/', branch15.jan_close_decision_page_ob_ch15, name='jan_close_decision_page_ob_ch15'),
    path('feb_close/', branch15.feb_close_ob_ch15, name='feb_close_ob_ch15'),
    path('feb_close_decision_page_ob_ch15/', branch15.feb_close_decision_page_ob_ch15, name='feb_close_decision_page_ob_ch15'),
    path('mar_close_ob_ch15/', branch15.mar_close_ob_ch15, name='mar_close_ob_ch15'),
    path('mar_close_decision_page/', branch15.mar_close_decision_page_ob_ch15, name='mar_close_decision_page_ob_ch15'),
    path('apr_close_ob_ch15/', branch15.apr_close_ob_ch15, name='apr_close_ob_ch15'),
    path('apr_close_decision_page_ob_ch15/', branch15.apr_close_decision_page_ob_ch15, name='apr_close_decision_page_ob_ch15'),

    path('may_close_ob_ch15/', branch15.may_close_ob_ch15, name='may_close_ob_ch15'),
    path('may_close_decision_page_ob_ch15/', branch15.may_close_decision_page_ob_ch15, name='may_close_decision_page_ob_ch15'),
    path('jun_close_ob_ch15/', branch15.jun_close_ob_ch15, name='jun_close_ob_ch15'),
    path('jun_close_decision_page_ob_ch15/', branch15.jun_close_decision_page_ob_ch15, name='jun_close_decision_page_ob_ch15'),
    path('jul_close_ob_ch15/', branch15.jul_close_ob_ch15, name='jul_close_ob_ch15'),
    path('jul_close_decision_page_ob_ch15/', branch15.jul_close_decision_page_ob_ch15, name='jul_close_decision_page_ob_ch15'),
    path('aug_close_ob_ch15/', branch15.aug_close_ob_ch15, name='aug_close_ob_ch15'),
    path('aug_close_decision_page_ob_ch15/', branch15.aug_close_decision_page_ob_ch15, name='aug_close_decision_page_ob_ch15'),

    path('sep_close_ob_ch15/', branch15.sep_close_ob_ch15, name='sep_close_ob_ch15'),
    path('sep_close_decision_page_ob_ch15/', branch15.sep_close_decision_page_ob_ch15, name='sep_close_decision_page_ob_ch15'),
    path('oct_close_ob_ch15/', branch15.oct_close_ob_ch15, name='oct_close_ob_ch15'),
    path('oct_close_decision_page_ob_ch15/', branch15.oct_close_decision_page_ob_ch15, name='oct_close_decision_page_ob_ch15'),
    path('nov_close_ob_ch15/', branch15.nov_close_ob_ch15, name='nov_close_ob_ch15'),
    path('nov_close_decision_page_ob_ch15/', branch15.nov_close_decision_page_ob_ch15, name='nov_close_decision_page_ob_ch15'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch15/',reports15.detailed_report_choose_months_ob_ch15,name='detailed_report_choose_months_ob_ch15'),

    path('jan_details_live_ob_ch15/', reports15.jan_details_live_ob_ch15, name='jan_details_live_ob_ch15'),
    path('jan_print_live_ob_ch15/', reports15.jan_print_live_ob_ch15, name='jan_print_live_ob_ch15'),
    path('feb_details_live_ob_ch15/', reports15.feb_details_live_ob_ch15, name='feb_details_live_ob_ch15'),
    path('feb_print_live_ob_ch15/', reports15.feb_print_live_ob_ch15, name='feb_print_live_ob_ch15'),
    path('march_details_live_ob_ch15/', reports15.march_details_live_ob_ch15, name='march_details_live_ob_ch15'),
    path('march_print_live_ob_ch15/', reports15.march_print_live_ob_ch15, name='march_print_live_ob_ch15'),

    path('april_details_live_ob_ch15/', reports15.april_details_live_ob_ch15, name='april_details_live_ob_ch15'),
    path('april_print_live_ob_ch15/', reports15.april_print_live_ob_ch15, name='april_print_live_ob_ch15'),
    path('may_details_live_ob_ch15/', reports15.may_details_live_ob_ch15, name='may_details_live_ob_ch15'),
    path('may_print_live_ob_ch15/', reports15.may_print_live_ob_ch15, name='may_print_live_ob_ch15'),
    path('june_details_live_ob_ch15/',reports15.june_details_live_ob_ch15,name='june_details_live_ob_ch15'),
    path('june_print_live_ob_ch15/', reports15.june_print_live_ob_ch15, name='june_print_live_ob_ch15'),

    path('july_details_live_ob_ch15/', reports15.july_details_live_ob_ch15, name='july_details_live_ob_ch15'),
    path('july_print_live_ob_ch15/', reports15.july_print_live_ob_ch15, name='july_print_live_ob_ch15'),
    path('auguest_details_live_ob_ch15/', reports15.auguest_details_live_ob_ch15, name='auguest_details_live_ob_ch15'),
    path('auguest_print_live_ob_ch15/', reports15.auguest_print_live_ob_ch15, name='auguest_print_live_ob_ch15'),
    path('sept_details_live_ob_ch15/', reports15.sept_details_live_ob_ch15, name='sept_details_live_ob_ch15'),
    path('sept_print_live_ob_ch15/', reports15.sept_print_live_ob_ch15, name='sept_print_live_ob_ch15'),

    path('october_details_live_ob_ch15/', reports15.october_details_live_ob_ch15, name='october_details_live_ob_ch15'),
    path('october_print_live_ob_ch15/', reports15.october_print_live_ob_ch15, name='october_print_live_ob_ch15'),
    path('nov_details_live_ob_ch15/', reports15.nov_details_live_ob_ch15, name='nov_details_live_ob_ch15'),
    path('nov_print_live_ob_ch15/', reports15.nov_print_live_ob_ch15, name='nov_print_live_ob_ch15'),
    path('dec_details_live_ob_ch15/', reports15.dec_details_live_ob_ch15, name='dec_details_live_ob_ch15'),
    path('dec_print_live_ob_ch15/', reports15.dec_print_live_ob_ch15, name='dec_print_live_ob_ch15'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch15/', reports15.viewall_vaccant_room_ob_ch15, name='viewall_vaccant_room_ob_ch15'),

    path('d_ob_ch15/', branch15.dynamic, name='dynamic'),

    path('manage_bed_ob_ch15/', branch15.manage_bed_ob_ch15, name='manage_bed_ob_ch15'),
    path('manage_new_guest_ob_ch15/', branch15.manage_new_guest_ob_ch15, name='manage_new_guest_ob_ch15'),
    path('manage_update_new_guest_ob_ch15/<id>', branch15.manage_update_new_guest_ob_ch15, name='manage_update_new_guest_ob_ch15'),
    path('manage_update_beds_ob_ch15/<id>', branch15.manage_update_beds_ob_ch15, name='manage_update_beds_ob_ch15'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch15/', branch15.view_all_due_amt_ob_ch15, name='view_all_due_amt_ob_ch15'),
    path('due_amt_mgt_choose_months_ob_ch15/', branch15.due_amt_mgt_choose_months_ob_ch15, name='due_amt_mgt_choose_months_ob_ch15'),

    path('view_jan_account_details_ob_ch15/', branch15.view_jan_account_details_ob_ch15, name='view_jan_account_details_ob_ch15'),
    path('jan_account_mgt_ob_ch15/<id>',branch15.jan_account_mgt_ob_ch15,name='jan_account_mgt_ob_ch15'),
    path('view_feb_account_details_ob_ch15/', branch15.view_feb_account_details_ob_ch15, name='view_feb_account_details_ob_ch15'),
    path('feb_account_mgt_ob_ch15/<id>',branch15.feb_account_mgt_ob_ch15,name='feb_account_mgt_ob_ch15'),
    path('view_march_account_details_ob_ch15/', branch15.view_march_account_details_ob_ch15, name='view_march_account_details_ob_ch15'),
    path('march_account_mgt_ob_ch15/<id>',branch15.march_account_mgt_ob_ch15,name='march_account_mgt_ob_ch15'),
    path('view_april_account_details_ob_ch15/', branch15.view_april_account_details_ob_ch15, name='view_april_account_details_ob_ch15'),
    path('april_account_mgt_ob_ch15/<id>',branch15.april_account_mgt_ob_ch15,name='april_account_mgt_ob_ch15'),

    path('view_may_account_details_ob_ch15/',branch15.view_may_account_details_ob_ch15,name='view_may_account_details_ob_ch15'),
    path('may_account_mgt_ob_ch15/<id>', branch15.may_account_mgt_ob_ch15, name='may_account_mgt_ob_ch15'),
    path('view_june_account_details_ob_ch15/', branch15.view_june_account_details_ob_ch15, name='view_june_account_details_ob_ch15'),
    path('june_account_mgt_ob_ch15/<id>',branch15.june_account_mgt_ob_ch15,name='june_account_mgt_ob_ch15'),
    path('view_july_account_details_ob_ch15/', branch15.view_july_account_details_ob_ch15, name='view_july_account_details_ob_ch15'),
    path('july_account_mgt_ob_ch15/<id>',branch15.july_account_mgt_ob_ch15,name='july_account_mgt_ob_ch15'),
    path('view_auguest_account_details_ob_ch15/', branch15.view_auguest_account_details_ob_ch15, name='view_auguest_account_details_ob_ch15'),
    path('auguest_account_mgt_ob_ch15/<id>',branch15.auguest_account_mgt_ob_ch15,name='auguest_account_mgt_ob_ch15'),

    path('view_sept_account_details_ob_ch15/', branch15.view_sept_account_details_ob_ch15, name='view_sept_account_details_ob_ch15'),
    path('sept_account_mgt_ob_ch15/<id>',branch15.sept_account_mgt_ob_ch15,name='sept_account_mgt_ob_ch15'),
    path('view_october_account_details_ob_ch15/', branch15.view_october_account_details_ob_ch15, name='view_october_account_details_ob_ch15'),
    path('october_account_mgt_ob_ch15/<id>',branch15.october_account_mgt_ob_ch15,name='october_account_mgt_ob_ch15'),
    path('view_nov_account_details_ob_ch15/', branch15.view_nov_account_details_ob_ch15, name='view_nov_account_details_ob_ch15'),
    path('nov_account_mgt_ob_ch15/<id>',branch15.nov_account_mgt_ob_ch15,name='nov_account_mgt_ob_ch15'),
    path('view_dec_account_details_ob_ch15/', branch15.view_dec_account_details_ob_ch15, name='view_dec_account_details_ob_ch15'),
    path('dec_account_mgt_ob_ch15/<id>',branch15.dec_account_mgt_ob_ch15,name='dec_account_mgt_ob_ch15'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch15', admin_dashboard_calculations_br15.monthly_details_due_ob_ch15, name='monthly_details_due_ob_ch15'),
    path('monthly_collection_details_ob_ch15/', admin_dashboard_calculations_br15.monthly_collection_details_ob_ch15, name='monthly_collection_details_ob_ch15'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch15/',branch15.guest_all_ob_ch15,name='guest_all_ob_ch15'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category15/', accounts15.view_all_category15, name='view_all_category15'),
    path('create_new_category15/', accounts15.create_new_category15, name='create_new_category15'),
    path('regi_new_category15/', accounts15.regi_new_category15, name='regi_new_category15'),
    path('update_category15/<id>',accounts15.update_category15,name='update_category15'),

    path('delete_category15/<id>', accounts15.delete_category15, name='delete_category15'),
    path('view_all_category_delete15/', accounts15.view_all_category_delete15, name='view_all_category_delete15'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items15/', accounts15.view_all_items15, name='view_all_items15'),
    path('create_new_item15/', accounts15.create_new_item15, name='create_new_item15'),
    path('regi_new_item15/', accounts15.regi_new_item15, name='regi_new_item15'),
    path('delete_item15/<id>',accounts15.delete_item15,name='delete_item15'),
    path('update_item15/<id>', accounts15.update_item15, name='update_item15'),
    path('view_all_items_delete15/',accounts15.view_all_items_delete15,name='view_all_items_delete15'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger15/', accounts15.view_all_ledger15, name='view_all_ledger15'),
    path('create_new_ledger15/', accounts15.create_new_ledger15, name='create_new_ledger15'),
    path('regi_new_ledger15/', accounts15.regi_new_ledger15, name='regi_new_ledger15'),
    path('delete_ledger15/<id>',accounts15.delete_ledger15,name='delete_ledger15'),
    path('update_ledger15/<id>',accounts15.update_ledger15,name='update_ledger15'),
    path('view_all_ledger_delete15/',accounts15.view_all_ledger_delete15,name='view_all_ledger_delete15'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book15/', accounts15.view_all_accounts_book15, name='view_all_accounts_book15'),
    path('create_new_accounts_book15/', accounts15.create_new_accounts_book15, name='create_new_accounts_book15'),
    path('regi_new_accounts_book15/', accounts15.regi_new_accounts_book15, name='regi_new_accounts_book15'),
    path('update_accounts_book15/<id>',accounts15.update_accounts_book15,name='update_accounts_book15'),
    path('delete_accounts_book15/<id>',accounts15.delete_accounts_book15,name='delete_accounts_book15'),
    path('view_all_accounts_book_delete15/',accounts15.view_all_accounts_book_delete15,name='view_all_accounts_book_delete15'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries15/', accounts15.get_countries15, name='get_countries15'),

    path('in_exp_items_entry15/', accounts15.in_exp_items_entry15, name='in_exp_items_entry15'),
    path('reg_in_exp_items_entry15/', accounts15.reg_in_exp_items_entry15, name='reg_in_exp_items_entry15'),
    path('delete_journal15/<id>',accounts15.delete_journal15,name='delete_journal15'),
    path('update_in_exp_items_entry15/<id>',accounts15.update_in_exp_items_entry15,name='update_in_exp_items_entry15'),
    path('detailed_journal_report15/',accounts15.detailed_journal_report15,name='detailed_journal_report15'),
    path('journal_report_deleted15/',accounts15.journal_report_deleted15,name='journal_report_deleted15'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise15/', accounts15.daily_category_wise15, name='daily_category_wise15'),
    path('monthly_category_based_reports15/',accounts15.monthly_category_based_reports15,name='monthly_category_based_reports15'),
    path('yearly_category_based_reports15/', accounts15.yearly_category_based_reports15,name='yearly_category_based_reports15'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed15/', accounts15.daily_detailed15, name='daily_detailed15'),
    path('monthly_detailed15/',accounts15.monthly_detailed15,name='monthly_detailed15'),
    path('yearly_detailed15/',accounts15.yearly_detailed15,name='yearly_detailed15'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports15/', accounts15.item_based_reports15, name='item_based_reports15'),
    path('daily_item_based_reports15/',accounts15.daily_item_based_reports15,name='daily_item_based_reports15'),
    path('monthly_item_based_reports15/',accounts15.monthly_item_based_reports15,name='monthly_item_based_reports15'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports15/', accounts15.ledger_based_reports15, name='ledger_based_reports15'),
    path('monthly_ledger_based_reports15/', accounts15.monthly_ledger_based_reports15, name='monthly_ledger_based_reports15'),
    path('daily_ledger_based_reports15/',accounts15.daily_ledger_based_reports15,name='daily_ledger_based_reports15'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports15/', accounts15.accounts_book_based_reports15, name='accounts_book_based_reports15'),
    path('daily_accounts_book_based_reports15/',accounts15.daily_accounts_book_based_reports15,name='daily_accounts_book_based_reports15'),
    path('monthly_accounts_book_based_reports15/',accounts15.monthly_accounts_book_based_reports15,name='monthly_accounts_book_based_reports15'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months15/', accounts15.monthly_reports_choose_months15, name='monthly_reports_choose_months15'),
    path('monthly_detailed_daily_in_exp_items_report15/<mo>',accounts15.monthly_detailed_daily_in_exp_items_report15,name='monthly_detailed_daily_in_exp_items_report15'),

    path('single_monthly_reports_choose_months15/', accounts15.single_monthly_reports_choose_months15,name='single_monthly_reports_choose_months15'),
    path('single_monthly_daily_in_exp_items_report15/<mo>',accounts15.single_monthly_daily_in_exp_items_report15,name='single_monthly_daily_in_exp_items_report15'),

    path('accounts_dash_board_ob_ch15/',accounts15.accounts_dash_board_ob_ch15,name='accounts_dash_board_ob_ch15'),
    path('accounts_dash_board15/',accounts15.accounts_dash_board15,name='accounts_dash_board15'),

    path('profit_sharing_choose_months15', accounts15.profit_sharing_choose_months15,name='profit_sharing_choose_months15'),
    path('profit_sharing15/<mo>', accounts15.profit_sharing15, name='profit_sharing15'),
    path('view_share_holders15', accounts15.view_share_holders15, name='view_share_holders15'),
    path('create_share_holders15', accounts15.create_share_holders15, name='create_share_holders15'),
    path('regi_share_holders15', accounts15.regi_share_holders15, name='regi_share_holders15'),
    path('update_share_holders15/<id>', accounts15.update_share_holders15, name='update_share_holders15'),
    path('delete_share_holders15/<id>', accounts15.delete_share_holders15, name='delete_share_holders15'),
    path('view_deleted_share_holders15', accounts15.view_deleted_share_holders15, name='view_deleted_share_holders15'),


]

