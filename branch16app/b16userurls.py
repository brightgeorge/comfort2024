from django.urls import path, include

from . import admin_branch16
from . import admin_branch16
from . import branch16
from . import reports16
from . import payment16
from . import admin_dashboard_calculations_br16
from . import accounts16

urlpatterns = [

    path('branch1_dashboard_ob_ch16/', branch16.branch1_dashboard_ob_ch16, name='branch1_dashboard_ob_ch16'),
    path('branch1_dashboard16/',branch16.branch1_dashboard16,name='branch1_dashboard16'),
    path('user_dashboard_calculations_ob_ch16/',branch16.user_dashboard_calculations_ob_ch16,name='user_dashboard_calculations_ob_ch16'),

    path('background_ob_ch16',branch16.background_ob_ch16,name='background_ob_ch16'),
    path('background_regi_ob_ch16',branch16.background_regi_ob_ch16,name='background_regi_ob_ch16'),
    path('custom_background_regi_ob_ch16',branch16.custom_background_regi_ob_ch16,name='custom_background_regi_ob_ch16'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch16/',admin_branch16.branch1_room_create_regi_ob_ch16,name='branch1_room_create_regi_ob_ch16'),
    path('view_all_room_ob_ch16/',admin_branch16.view_all_room_ob_ch16,name='view_all_room_ob_ch16'),
    path('delete_room_ob_ch16/<id>',admin_branch16.delete_room_ob_ch16,name='delete_room_ob_ch16'),

    path('branch1_room_create_ob_ch16/',admin_branch16.branch1_room_create_ob_ch16,name='branch1_room_create_ob_ch16'),

    path('multiple_branch1_room_create_regi16/',admin_branch16.multiple_branch1_room_create_regi16,name='multiple_branch1_room_create_regi16'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch16/', admin_branch16.pg1_bed_create_regi_ob_ch16, name='pg1_bed_create_regi_ob_ch16'),
    path('pg1_view_all_beds_ob_ch16/', admin_branch16.pg1_view_all_beds_ob_ch16, name='pg1_view_all_beds_ob_ch16'),
    path('delete_bed_ob_ch16/<id>', admin_branch16.delete_bed_ob_ch16, name='delete_bed_ob_ch16'),

    path('pg1_bed_create_ob_ch16/', admin_branch16.pg1_bed_create_ob_ch16, name='pg1_bed_create_ob_ch16'),

    path('single_pg1_bed_create_regi_ob_ch16/',admin_branch16.single_pg1_bed_create_regi_ob_ch16,name='single_pg1_bed_create_regi_ob_ch16'),
    path('update_bed_basic_details_ob_ch16/<id>',admin_branch16.update_bed_basic_details_ob_ch16, name='update_bed_basic_details_ob_ch16'),

    path('multiple_single_pg1_bed_create_regi16/',admin_branch16.multiple_single_pg1_bed_create_regi16,name='multiple_single_pg1_bed_create_regi16'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch16/<id>',branch16.br1_admit_guest_ob_ch16,name='br1_admit_guest_ob_ch16'),
    path('view_all_new_guest_ob_ch16/',branch16.view_all_new_guest_ob_ch16,name='view_all_new_guest_ob_ch16'),
    path('update_br1_admit_guest_ob_ch16/<id>',branch16.update_br1_admit_guest_ob_ch16,name='update_br1_admit_guest_ob_ch16'),
    path('vacate_br1_guest_ob_ch16/<id>',branch16.vacate_br1_guest_ob_ch16,name='vacate_br1_guest_ob_ch16'),

    path('active_guest_details_ob_ch16/<guest_code>',branch16.active_guest_details_ob_ch16,name='active_guest_details_ob_ch16'),
    path('view_all_guest_ob_ch16/',branch16.view_all_guest_ob_ch16,name='view_all_guest_ob_ch16'),
    path('shift_guest_ob_ch16/<id>',branch16.shift_guest_ob_ch16,name='shift_guest_ob_ch16'),
    path('shift_guest_regi_ob_ch16/',branch16.shift_guest_regi_ob_ch16,name='shift_guest_regi_ob_ch16'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch16/',branch16.update_all_rent_ob_ch16,name='update_all_rent_ob_ch16'),

    path('multiple_br1_admit_guest16/<id>',branch16.multiple_br1_admit_guest16,name='multiple_br1_admit_guest16'),

#guest end here


##################################
#_ADVANCE_ob_ch16 START HERE
################################


    path('choose_months_advance_ob_ch16/',branch16.choose_months_advance_ob_ch16,name='choose_months_advance_ob_ch16'),

    path('jan_advance_ob_ch16/', branch16.jan_advance_ob_ch16, name='jan_advance_ob_ch16'),
    path('jan_make_payments_advance_ob_ch16/<id>', branch16.jan_make_payments_advance_ob_ch16,name='jan_make_payments_advance_ob_ch16'),
    path('feb_advance_ob_ch16/', branch16.feb_advance_ob_ch16, name='feb_advance_ob_ch16'),
    path('feb_make_payments_advance_ob_ch16/<id>', branch16.feb_make_payments_advance_ob_ch16,name='feb_make_payments_advance_ob_ch16'),
    path('march_advance_ob_ch16/', branch16.march_advance_ob_ch16, name='march_advance_ob_ch16'),
    path('march_make_payments_advance_ob_ch16/<id>', branch16.march_make_payments_advance_ob_ch16,name='march_make_payments_advance_ob_ch16'),
    path('april_advance_ob_ch16/', branch16.april_advance_ob_ch16, name='april_advance_ob_ch16'),
    path('april_make_payments_advance_ob_ch16/<id>', branch16.april_make_payments_advance_ob_ch16, name='april_make_payments_advance_ob_ch16'),

    path('may_advance_ob_ch16/',branch16.may_advance_ob_ch16,name='may_advance_ob_ch16'),
    path('may_make_payments_advance_ob_ch16/<id>', branch16.may_make_payments_advance_ob_ch16, name='may_make_payments_advance_ob_ch16'),
    path('june_advance_ob_ch16/',branch16.june_advance_ob_ch16,name='june_advance_ob_ch16'),
    path('june_make_payments_advance_ob_ch16/<id>', branch16.june_make_payments_advance_ob_ch16, name='june_make_payments_advance_ob_ch16'),
    path('july_advance_ob_ch16/',branch16.july_advance_ob_ch16,name='july_advance_ob_ch16'),
    path('july_make_payments_advance_ob_ch16/<id>', branch16.july_make_payments_advance_ob_ch16, name='july_make_payments_advance_ob_ch16'),
    path('auguest_advance_ob_ch16/', branch16.auguest_advance_ob_ch16, name='auguest_advance_ob_ch16'),
    path('auguest_make_payments_advance_ob_ch16/<id>', branch16.auguest_make_payments_advance_ob_ch16, name='auguest_make_payments_advance_ob_ch16'),

    path('sept_advance_ob_ch16/', branch16.sept_advance_ob_ch16, name='sept_advance_ob_ch16'),
    path('sept_make_payments_advance_ob_ch16/<id>', branch16.sept_make_payments_advance_ob_ch16,name='sept_make_payments_advance_ob_ch16'),
    path('october_advance_ob_ch16/', branch16.october_advance_ob_ch16, name='october_advance_ob_ch16'),
    path('october_make_payments_advance_ob_ch16/<id>', branch16.october_make_payments_advance_ob_ch16, name='october_make_payments_advance_ob_ch16'),
    path('nov_advance_ob_ch16/', branch16.nov_advance_ob_ch16, name='nov_advance_ob_ch16'),
    path('nov_make_payments_advance_ob_ch16/<id>', branch16.nov_make_payments_advance_ob_ch16,name='nov_make_payments_advance_ob_ch16'),
    path('dec_advance_ob_ch16/', branch16.dec_advance_ob_ch16, name='dec_advance_ob_ch16'),
    path('dec_make_payments_advance_ob_ch16/<id>', branch16.dec_make_payments_advance_ob_ch16, name='dec_make_payments_advance_ob_ch16'),



##################################
#_ADVANCE_ob_ch16 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch16/',branch16.choose_months_ob_ch16,name='choose_months_ob_ch16'),

    path('jan_ob_ch16/',branch16.jan_ob_ch16,name='jan_ob_ch16'),
    path('jan_manke_payments_ob_ch16/<id>',branch16.jan_manke_payments_ob_ch16,name='jan_manke_payments_ob_ch16'),

    path('feb_ob_ch16/',branch16.feb_ob_ch16,name='feb_ob_ch16'),
    path('feb_manke_payments_ob_ch16/<id>',branch16.feb_manke_payments_ob_ch16,name='feb_manke_payments_ob_ch16'),

    path('march_ob_ch16/',branch16.march_ob_ch16,name='march_ob_ch16'),
    path('march_manke_payments_ob_ch16/<id>',branch16.march_manke_payments_ob_ch16,name='march_manke_payments_ob_ch16'),

    path('april_ob_ch16/',branch16.april_ob_ch16,name='april_ob_ch16'),
    path('april_make_payments_ob_ch16/<id>',branch16.april_make_payments_ob_ch16,name='april_make_payments_ob_ch16'),

    path('may_ob_ch16/',branch16.may_ob_ch16,name='may_ob_ch16'),
    path('may_make_payments_ob_ch16/<id>',branch16.may_make_payments_ob_ch16,name='may_make_payments_ob_ch16'),

    path('june_ob_ch16/',branch16.june_ob_ch16,name='june_ob_ch16'),
    path('june_make_payments_ob_ch16/<id>',branch16.june_make_payments_ob_ch16,name='june_make_payments_ob_ch16'),

    path('july_ob_ch16/',branch16.july_ob_ch16,name='july_ob_ch16'),
    path('july_make_payments_ob_ch16/<id>',branch16.july_make_payments_ob_ch16,name='july_make_payments_ob_ch16'),

    path('aug_ob_ch16/',branch16.aug_ob_ch16,name='aug_ob_ch16'),
    path('aug_make_payments_ob_ch16/<id>',branch16.aug_make_payments_ob_ch16,name='aug_make_payments_ob_ch16'),

    path('sept_ob_ch16/',branch16.sept_ob_ch16,name='sept_ob_ch16'),
    path('sept_make_payments_ob_ch16/<id>',branch16.sept_make_payments_ob_ch16,name='sept_make_payments_ob_ch16'),

    path('oct_ob_ch16/',branch16.oct_ob_ch16,name='oct_ob_ch16'),
    path('oct_make_payments_ob_ch16/<id>',branch16.oct_make_payments_ob_ch16,name='oct_make_payments_ob_ch16'),

    path('nov_ob_ch16/',branch16.nov_ob_ch16,name='nov_ob_ch16'),
    path('nov_make_payments_ob_ch16/<id>',branch16.nov_make_payments_ob_ch16,name='nov_make_payments_ob_ch16'),

    path('dec_ob_ch16/',branch16.dec_ob_ch16,name='dec_ob_ch16'),
    path('dec_make_payments_ob_ch16/<id>',branch16.dec_make_payments_ob_ch16,name='dec_make_payments_ob_ch16'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch16/', payment16.choose_user_ob_ch16, name='choose_user_ob_ch16'),
    path('payment_user_details_ob_ch16/<id>', payment16.payment_user_details_ob_ch16, name='payment_user_details_ob_ch16'),
    path('close_choose_user_ob_ch16/<id>',payment16.close_choose_user_ob_ch16,name='close_choose_user_ob_ch16'),

    path('monthly_jan_make_payments_ob_ch16/<id>', payment16.monthly_jan_make_payments_ob_ch16, name='monthly_jan_make_payments_ob_ch16'),
    path('monthly_feb_make_payments_ob_ch16/<id>', payment16.monthly_feb_make_payments_ob_ch16, name='monthly_feb_make_payments_ob_ch16'),
    path('monthly_march_make_payments_ob_ch16/<id>', payment16.monthly_march_make_payments_ob_ch16, name='monthly_march_make_payments_ob_ch16'),
    path('monthly_april_make_payments_ob_ch16/<id>', payment16.monthly_april_make_payments_ob_ch16, name='monthly_april_make_payments_ob_ch16'),
    path('monthly_may_make_payments_ob_ch16/<id>', payment16.monthly_may_make_payments_ob_ch16, name='monthly_may_make_payments_ob_ch16'),
    path('monthly_june_make_payments_ob_ch16/<id>', payment16.monthly_june_make_payments_ob_ch16, name='monthly_june_make_payments_ob_ch16'),

    path('monthly_july_make_payments_ob_ch16/<id>', payment16.monthly_july_make_payments_ob_ch16, name='monthly_july_make_payments_ob_ch16'),
    path('monthly_aug_make_payments_ob_ch16/<id>', payment16.monthly_aug_make_payments_ob_ch16, name='monthly_aug_make_payments_ob_ch16'),
    path('monthly_sept_make_payments_ob_ch16/<id>', payment16.monthly_sept_make_payments_ob_ch16, name='monthly_sept_make_payments_ob_ch16'),
    path('monthly_oct_make_payments_ob_ch16/<id>', payment16.monthly_oct_make_payments_ob_ch16, name='monthly_oct_make_payments_ob_ch16'),
    path('monthly_nov_make_payments_ob_ch16/<id>', payment16.monthly_nov_make_payments_ob_ch16, name='monthly_nov_make_payments_ob_ch16'),
    path('monthly_dec_make_payments_ob_ch16/<id>', payment16.monthly_dec_make_payments_ob_ch16, name='monthly_dec_make_payments_ob_ch16'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch16/',branch16.unpaid_rent_choose_months_ob_ch16,name='unpaid_rent_choose_months_ob_ch16'),

    path('jan_unpaid_rent_ob_ch16/', branch16.jan_unpaid_rent_ob_ch16, name='jan_unpaid_rent_ob_ch16'),
    path('table_jan_unpaid_rent_ob_ch16/', branch16.table_jan_unpaid_rent_ob_ch16, name='table_jan_unpaid_rent_ob_ch16'),
    path('feb_unpaid_rent_ob_ch16/', branch16.feb_unpaid_rent_ob_ch16, name='feb_unpaid_rent_ob_ch16'),
    path('table_feb_unpaid_rent_ob_ch16/', branch16.table_feb_unpaid_rent_ob_ch16, name='table_feb_unpaid_rent_ob_ch16'),
    path('mar_unpaid_rent_ob_ch16/', branch16.mar_unpaid_rent_ob_ch16, name='mar_unpaid_rent_ob_ch16'),
    path('table_mar_unpaid_rent_ob_ch16/', branch16.table_mar_unpaid_rent_ob_ch16, name='table_mar_unpaid_rent_ob_ch16'),
    path('april_unpaid_rent_ob_ch16/', branch16.april_unpaid_rent_ob_ch16, name='april_unpaid_rent_ob_ch16'),
    path('table_april_unpaid_rent_ob_ch16/', branch16.table_april_unpaid_rent_ob_ch16, name='table_april_unpaid_rent_ob_ch16'),

    path('may_unpaid_rent_ob_ch16/', branch16.may_unpaid_rent_ob_ch16, name='may_unpaid_rent_ob_ch16'),
    path('table_may_unpaid_rent_ob_ch16/', branch16.table_may_unpaid_rent_ob_ch16, name='table_may_unpaid_rent_ob_ch16'),
    path('june_unpaid_rent_ob_ch16/', branch16.june_unpaid_rent_ob_ch16, name='june_unpaid_rent_ob_ch16'),
    path('table_june_unpaid_rent_ob_ch16/', branch16.table_june_unpaid_rent_ob_ch16, name='table_june_unpaid_rent_ob_ch16'),
    path('july_unpaid_rent_ob_ch16/', branch16.july_unpaid_rent_ob_ch16, name='july_unpaid_rent_ob_ch16'),
    path('table_july_unpaid_rent_ob_ch16',branch16.table_july_unpaid_rent_ob_ch16,name='table_july_unpaid_rent_ob_ch16'),
    path('aug_unpaid_rent_ob_ch16/', branch16.aug_unpaid_rent_ob_ch16, name='aug_unpaid_rent_ob_ch16'),
    path('table_aug_unpaid_rent_ob_ch16/',branch16.table_aug_unpaid_rent_ob_ch16,name='table_aug_unpaid_rent_ob_ch16'),

    path('sept_unpaid_rent_ob_ch16/', branch16.sept_unpaid_rent_ob_ch16, name='sept_unpaid_rent_ob_ch16'),
    path('table_sept_unpaid_rent_ob_ch16/', branch16.table_sept_unpaid_rent_ob_ch16, name='table_sept_unpaid_rent_ob_ch16'),
    path('oct_unpaid_rent_ob_ch16/', branch16.oct_unpaid_rent_ob_ch16, name='oct_unpaid_rent_ob_ch16'),
    path('table_oct_unpaid_rent_ob_ch16/', branch16.table_oct_unpaid_rent_ob_ch16, name='table_oct_unpaid_rent_ob_ch16'),
    path('nov_unpaid_rent_ob_ch16/', branch16.nov_unpaid_rent_ob_ch16, name='nov_unpaid_rent_ob_ch16'),
    path('table_nov_unpaid_rent_ob_ch16/', branch16.table_nov_unpaid_rent_ob_ch16, name='table_nov_unpaid_rent_ob_ch16'),
    path('dec_unpaid_rent_ob_ch16/', branch16.dec_unpaid_rent_ob_ch16, name='dec_unpaid_rent_ob_ch16'),
    path('table_dec_unpaid_rent_ob_ch16/', branch16.table_dec_unpaid_rent_ob_ch16, name='table_dec_unpaid_rent_ob_ch16'),

    path('details_of_unpaid_guests_ob_ch16/<id>',branch16.details_of_unpaid_guests_ob_ch16,name='details_of_unpaid_guests_ob_ch16'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch16/',branch16.paid_rent_choose_months_ob_ch16,name='paid_rent_choose_months_ob_ch16'),
    path('partially_paid_guest_choose_months_ob_ch16/',reports16.partially_paid_guest_choose_months_ob_ch16,name='partially_paid_guest_choose_months_ob_ch16'),

    path('jan_paid_rent_ob_ch16/', branch16.jan_paid_rent_ob_ch16, name='jan_paid_rent_ob_ch16'),
    path('table_jan_paid_rent_ob_ch16/', branch16.table_jan_paid_rent_ob_ch16, name='table_jan_paid_rent_ob_ch16'),
    path('jan_full_paid_guest_ob_ch16/', reports16.jan_full_paid_guest_ob_ch16, name='jan_full_paid_guest_ob_ch16'),
    path('jan_partially_paid_guest_ob_ch16/', reports16.jan_partially_paid_guest_ob_ch16, name='jan_partially_paid_guest_ob_ch16'),
    path('table_jan_partially_paid_guest_ob_ch16/', reports16.table_jan_partially_paid_guest_ob_ch16,name='table_jan_partially_paid_guest_ob_ch16'),

    path('feb_paid_rent_ob_ch16/', branch16.feb_paid_rent_ob_ch16, name='feb_paid_rent_ob_ch16'),
    path('table_feb_paid_rent_ob_ch16/', branch16.table_feb_paid_rent_ob_ch16, name='table_feb_paid_rent_ob_ch16'),
    path('feb_full_paid_guest_ob_ch16/', reports16.feb_full_paid_guest_ob_ch16, name='feb_full_paid_guest_ob_ch16'),
    path('feb_partially_paid_guest_ob_ch16/', reports16.feb_partially_paid_guest_ob_ch16, name='feb_partially_paid_guest_ob_ch16'),
    path('table_feb_partially_paid_guest_ob_ch16/', reports16.table_feb_partially_paid_guest_ob_ch16,name='table_feb_partially_paid_guest_ob_ch16'),

    path('mar_paid_rent_ob_ch16/', branch16.mar_paid_rent_ob_ch16, name='mar_paid_rent_ob_ch16'),
    path('table_mar_paid_rent_ob_ch16/', branch16.table_mar_paid_rent_ob_ch16, name='table_mar_paid_rent_ob_ch16'),
    path('march_full_paid_guest_ob_ch16/', reports16.march_full_paid_guest_ob_ch16, name='march_full_paid_guest_ob_ch16'),
    path('march_partially_paid_guest_ob_ch16/', reports16.march_partially_paid_guest_ob_ch16, name='march_partially_paid_guest_ob_ch16'),
    path('table_march_partially_paid_guest_ob_ch16/', reports16.table_march_partially_paid_guest_ob_ch16,name='table_march_partially_paid_guest_ob_ch16'),

    path('april_paid_rent_ob_ch16/', branch16.april_paid_rent_ob_ch16, name='april_paid_rent_ob_ch16'),
    path('table_april_paid_rent_ob_ch16/', branch16.table_april_paid_rent_ob_ch16, name='table_april_paid_rent_ob_ch16'),
    path('april_full_paid_guest_ob_ch16/', reports16.april_full_paid_guest_ob_ch16, name='april_full_paid_guest_ob_ch16'),
    path('april_partially_paid_guest_ob_ch16/', reports16.april_partially_paid_guest_ob_ch16, name='april_partially_paid_guest_ob_ch16'),
    path('table_april_partially_paid_guest_ob_ch16/', reports16.table_april_partially_paid_guest_ob_ch16,name='table_april_partially_paid_guest_ob_ch16'),

    path('may_paid_rent_ob_ch16/', branch16.may_paid_rent_ob_ch16, name='may_paid_rent_ob_ch16'),
    path('table_may_paid_rent_ob_ch16/', branch16.table_may_paid_rent_ob_ch16, name='table_may_paid_rent_ob_ch16'),
    path('may_full_paid_guest_ob_ch16/', reports16.may_full_paid_guest_ob_ch16, name='may_full_paid_guest_ob_ch16'),
    path('may_partially_paid_guest_ob_ch16/', reports16.may_partially_paid_guest_ob_ch16, name='may_partially_paid_guest_ob_ch16'),
    path('table_may_partially_paid_guest_ob_ch16/', reports16.table_may_partially_paid_guest_ob_ch16, name='table_may_partially_paid_guest_ob_ch16'),

    path('june_paid_rent_ob_ch16/', branch16.june_paid_rent_ob_ch16, name='june_paid_rent_ob_ch16'),
    path('table_june_paid_rent_ob_ch16/', branch16.table_june_paid_rent_ob_ch16, name='table_june_paid_rent_ob_ch16'),
    path('june_full_paid_guest_ob_ch16/', reports16.june_full_paid_guest_ob_ch16, name='june_full_paid_guest_ob_ch16'),
    path('june_partially_paid_guest_ob_ch16/', reports16.june_partially_paid_guest_ob_ch16, name='june_partially_paid_guest_ob_ch16'),
    path('table_june_partially_paid_guest_ob_ch16/', reports16.table_june_partially_paid_guest_ob_ch16, name='table_june_partially_paid_guest_ob_ch16'),

    path('july_paid_rent_ob_ch16/', branch16.july_paid_rent_ob_ch16, name='july_paid_rent_ob_ch16'),
    path('table_july_paid_rent_ob_ch16/', branch16.table_july_paid_rent_ob_ch16, name='table_july_paid_rent_ob_ch16'),
    path('july_full_paid_guest_ob_ch16/', reports16.july_full_paid_guest_ob_ch16, name='july_full_paid_guest_ob_ch16'),
    path('july_partially_paid_guest_ob_ch16/', reports16.july_partially_paid_guest_ob_ch16, name='july_partially_paid_guest_ob_ch16'),
    path('table_july_partially_paid_guest_ob_ch16/', reports16.table_july_partially_paid_guest_ob_ch16, name='table_july_partially_paid_guest_ob_ch16'),

    path('aug_paid_rent_ob_ch16/', branch16.aug_paid_rent_ob_ch16, name='aug_paid_rent_ob_ch16'),
    path('table_aug_paid_rent_ob_ch16/', branch16.table_aug_paid_rent_ob_ch16, name='table_aug_paid_rent_ob_ch16'),
    path('auguest_full_paid_guest_ob_ch16/', reports16.auguest_full_paid_guest_ob_ch16, name='auguest_full_paid_guest_ob_ch16'),
    path('auguest_partially_paid_guest_ob_ch16/', reports16.auguest_partially_paid_guest_ob_ch16,name='auguest_partially_paid_guest_ob_ch16'),
    path('table_auguest_partially_paid_guest_ob_ch16/', reports16.table_auguest_partially_paid_guest_ob_ch16,name='table_auguest_partially_paid_guest_ob_ch16'),

    path('sept_paid_rent_ob_ch16/', branch16.sept_paid_rent_ob_ch16, name='sept_paid_rent_ob_ch16'),
    path('table_sept_paid_rent_ob_ch16/', branch16.table_sept_paid_rent_ob_ch16, name='table_sept_paid_rent_ob_ch16'),
    path('sept_full_paid_guest_ob_ch16/', reports16.sept_full_paid_guest_ob_ch16, name='sept_full_paid_guest_ob_ch16'),
    path('sept_partially_paid_guest_ob_ch16/', reports16.sept_partially_paid_guest_ob_ch16, name='sept_partially_paid_guest_ob_ch16'),
    path('table_sept_partially_paid_guest_ob_ch16/', reports16.table_sept_partially_paid_guest_ob_ch16,name='table_sept_partially_paid_guest_ob_ch16'),

    path('oct_paid_rent_ob_ch16/', branch16.oct_paid_rent_ob_ch16, name='oct_paid_rent_ob_ch16'),
    path('table_oct_paid_rent_ob_ch16/', branch16.table_oct_paid_rent_ob_ch16, name='table_oct_paid_rent_ob_ch16'),
    path('october_full_paid_guest_ob_ch16/', reports16.october_full_paid_guest_ob_ch16, name='october_full_paid_guest_ob_ch16'),
    path('october_partially_paid_guest_ob_ch16/', reports16.october_partially_paid_guest_ob_ch16,name='october_partially_paid_guest_ob_ch16'),
    path('table_october_partially_paid_guest_ob_ch16/', reports16.table_october_partially_paid_guest_ob_ch16,name='table_october_partially_paid_guest_ob_ch16'),

    path('nov_paid_rent_ob_ch16/', branch16.nov_paid_rent_ob_ch16, name='nov_paid_rent_ob_ch16'),
    path('table_nov_paid_rent_ob_ch16/', branch16.table_nov_paid_rent_ob_ch16, name='table_nov_paid_rent_ob_ch16'),
    path('nov_full_paid_guest_ob_ch16/', reports16.nov_full_paid_guest_ob_ch16, name='nov_full_paid_guest_ob_ch16'),
    path('nov_partially_paid_guest_ob_ch16/', reports16.nov_partially_paid_guest_ob_ch16, name='nov_partially_paid_guest_ob_ch16'),
    path('table_nov_partially_paid_guest_ob_ch16/', reports16.table_nov_partially_paid_guest_ob_ch16,name='table_nov_partially_paid_guest_ob_ch16'),

    path('dec_paid_rent_ob_ch16/', branch16.dec_paid_rent_ob_ch16, name='dec_paid_rent_ob_ch16'),
    path('table_dec_paid_rent_ob_ch16/', branch16.table_dec_paid_rent_ob_ch16, name='table_dec_paid_rent_ob_ch16'),
    path('dec_full_paid_guest_ob_ch16/', reports16.dec_full_paid_guest_ob_ch16, name='dec_full_paid_guest_ob_ch16'),
    path('dec_partially_paid_guest_ob_ch16/', reports16.dec_partially_paid_guest_ob_ch16, name='dec_partially_paid_guest_ob_ch16'),
    path('table_dec_partially_paid_guest_ob_ch16/', reports16.table_dec_partially_paid_guest_ob_ch16,name='table_dec_partially_paid_guest_ob_ch16'),

    path('details_of_paid_guests_ob_ch16/<id>',branch16.details_of_paid_guests_ob_ch16,name='details_of_paid_guests_ob_ch16'),
    path('full_paid_guest_ob_ch16/',reports16.full_paid_guest_ob_ch16,name='full_paid_guest_ob_ch16'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch16/',branch16.viewall_vacate_guest_ob_ch16,name='viewall_vacate_guest_ob_ch16'),
    path('details_of_vacate_guest_ob_ch16/<id>',branch16.details_of_vacate_guest_ob_ch16,name='details_of_vacate_guest_ob_ch16'),
    path('full_vacated_guest_details_ob_ch16',branch16.full_vacated_guest_details_ob_ch16,name='full_vacated_guest_details_ob_ch16'),
    path('full_vacated_guest_table_ob_ch16',branch16.full_vacated_guest_table_ob_ch16,name='full_vacated_guest_table_ob_ch16'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch16/<id>', branch16.jan_manke_payments_vacate_ob_ch16, name='jan_manke_payments_vacate_ob_ch16'),
    path('feb_manke_payments_vacate_ob_ch16/<id>', branch16.feb_manke_payments_vacate_ob_ch16, name='feb_manke_payments_vacate_ob_ch16'),
    path('march_manke_payments_vacate_ob_ch16/<id>', branch16.march_manke_payments_vacate_ob_ch16, name='march_manke_payments_vacate_ob_ch16'),
    path('april_make_payments_vacate_ob_ch16/<id>', branch16.april_make_payments_vacate_ob_ch16, name='april_make_payments_vacate_ob_ch16'),

    path('may_make_payments_vacate_ob_ch16/<id>', branch16.may_make_payments_vacate_ob_ch16, name='may_make_payments_vacate_ob_ch16'),
    path('june_make_payments_vacate_ob_ch16/<id>', branch16.june_make_payments_vacate_ob_ch16, name='june_make_payments_vacate_ob_ch16'),
    path('july_make_payments_vacate_ob_ch16/<id>', branch16.july_make_payments_vacate_ob_ch16, name='july_make_payments_vacate_ob_ch16'),
    path('aug_make_payments_vacate_ob_ch16/<id>', branch16.aug_make_payments_vacate_ob_ch16, name='aug_make_payments_vacate_ob_ch16'),

    path('sept_make_payments_vacate_ob_ch16/<id>', branch16.sept_make_payments_vacate_ob_ch16, name='sept_make_payments_vacate_ob_ch16'),
    path('oct_make_payments_vacate_ob_ch16/<id>', branch16.oct_make_payments_vacate_ob_ch16, name='oct_make_payments_vacate_ob_ch16'),
    path('nov_make_payments_vacate_ob_ch16/<id>', branch16.nov_make_payments_vacate_ob_ch16, name='nov_make_payments_vacate_ob_ch16'),
    path('dec_make_payments_vacate_ob_ch16/<id>', branch16.dec_make_payments_vacate_ob_ch16, name='dec_make_payments_vacate_ob_ch16'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch16/',branch16.detail_guest_general_ob_ch16,name='detail_guest_general_ob_ch16'),

    path('jan_print_ob_ch16/',branch16.jan_print_ob_ch16,name='jan_print_ob_ch16'),
    path('feb_print_ob_ch16/',branch16.feb_print_ob_ch16,name='feb_print_ob_ch16'),
    path('march_print_ob_ch16/',branch16.march_print_ob_ch16,name='march_print_ob_ch16'),
    path('april_print_ob_ch16/',branch16.april_print_ob_ch16,name='april_print_ob_ch16'),

    path('may_print_ob_ch16/',branch16.may_print_ob_ch16,name='may_print_ob_ch16'),
    path('june_print_ob_ch16/',branch16.june_print_ob_ch16,name='june_print_ob_ch16'),
    path('july_print_ob_ch16/', branch16.july_print_ob_ch16, name='july_print_ob_ch16'),
    path('aug_print_ob_ch16/', branch16.aug_print_ob_ch16, name='aug_print_ob_ch16'),

    path('sept_print_ob_ch16/', branch16.sept_print_ob_ch16, name='sept_print_ob_ch16'),
    path('oct_print_ob_ch16/', branch16.oct_print_ob_ch16, name='oct_print_ob_ch16'),
    path('nov_print_ob_ch16/', branch16.nov_print_ob_ch16, name='nov_print_ob_ch16'),
    path('dec_print_ob_ch16/', branch16.dec_print_ob_ch16, name='dec_print_ob_ch16'),

    path('new_year_jan_print_ob_ch16/', branch16.new_year_jan_print_ob_ch16, name='new_year_jan_print_ob_ch16'),


##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch16/', branch16.jan_close_ob_ch16, name='jan_close_ob_ch16'),
    path('jan_close_decision_page_ob_ch16/', branch16.jan_close_decision_page_ob_ch16, name='jan_close_decision_page_ob_ch16'),
    path('feb_close/', branch16.feb_close_ob_ch16, name='feb_close_ob_ch16'),
    path('feb_close_decision_page_ob_ch16/', branch16.feb_close_decision_page_ob_ch16, name='feb_close_decision_page_ob_ch16'),
    path('mar_close_ob_ch16/', branch16.mar_close_ob_ch16, name='mar_close_ob_ch16'),
    path('mar_close_decision_page/', branch16.mar_close_decision_page_ob_ch16, name='mar_close_decision_page_ob_ch16'),
    path('apr_close_ob_ch16/', branch16.apr_close_ob_ch16, name='apr_close_ob_ch16'),
    path('apr_close_decision_page_ob_ch16/', branch16.apr_close_decision_page_ob_ch16, name='apr_close_decision_page_ob_ch16'),

    path('may_close_ob_ch16/', branch16.may_close_ob_ch16, name='may_close_ob_ch16'),
    path('may_close_decision_page_ob_ch16/', branch16.may_close_decision_page_ob_ch16, name='may_close_decision_page_ob_ch16'),
    path('jun_close_ob_ch16/', branch16.jun_close_ob_ch16, name='jun_close_ob_ch16'),
    path('jun_close_decision_page_ob_ch16/', branch16.jun_close_decision_page_ob_ch16, name='jun_close_decision_page_ob_ch16'),
    path('jul_close_ob_ch16/', branch16.jul_close_ob_ch16, name='jul_close_ob_ch16'),
    path('jul_close_decision_page_ob_ch16/', branch16.jul_close_decision_page_ob_ch16, name='jul_close_decision_page_ob_ch16'),
    path('aug_close_ob_ch16/', branch16.aug_close_ob_ch16, name='aug_close_ob_ch16'),
    path('aug_close_decision_page_ob_ch16/', branch16.aug_close_decision_page_ob_ch16, name='aug_close_decision_page_ob_ch16'),

    path('sep_close_ob_ch16/', branch16.sep_close_ob_ch16, name='sep_close_ob_ch16'),
    path('sep_close_decision_page_ob_ch16/', branch16.sep_close_decision_page_ob_ch16, name='sep_close_decision_page_ob_ch16'),
    path('oct_close_ob_ch16/', branch16.oct_close_ob_ch16, name='oct_close_ob_ch16'),
    path('oct_close_decision_page_ob_ch16/', branch16.oct_close_decision_page_ob_ch16, name='oct_close_decision_page_ob_ch16'),
    path('nov_close_ob_ch16/', branch16.nov_close_ob_ch16, name='nov_close_ob_ch16'),
    path('nov_close_decision_page_ob_ch16/', branch16.nov_close_decision_page_ob_ch16, name='nov_close_decision_page_ob_ch16'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch16/',reports16.detailed_report_choose_months_ob_ch16,name='detailed_report_choose_months_ob_ch16'),

    path('jan_details_live_ob_ch16/', reports16.jan_details_live_ob_ch16, name='jan_details_live_ob_ch16'),
    path('jan_print_live_ob_ch16/', reports16.jan_print_live_ob_ch16, name='jan_print_live_ob_ch16'),
    path('feb_details_live_ob_ch16/', reports16.feb_details_live_ob_ch16, name='feb_details_live_ob_ch16'),
    path('feb_print_live_ob_ch16/', reports16.feb_print_live_ob_ch16, name='feb_print_live_ob_ch16'),
    path('march_details_live_ob_ch16/', reports16.march_details_live_ob_ch16, name='march_details_live_ob_ch16'),
    path('march_print_live_ob_ch16/', reports16.march_print_live_ob_ch16, name='march_print_live_ob_ch16'),

    path('april_details_live_ob_ch16/', reports16.april_details_live_ob_ch16, name='april_details_live_ob_ch16'),
    path('april_print_live_ob_ch16/', reports16.april_print_live_ob_ch16, name='april_print_live_ob_ch16'),
    path('may_details_live_ob_ch16/', reports16.may_details_live_ob_ch16, name='may_details_live_ob_ch16'),
    path('may_print_live_ob_ch16/', reports16.may_print_live_ob_ch16, name='may_print_live_ob_ch16'),
    path('june_details_live_ob_ch16/',reports16.june_details_live_ob_ch16,name='june_details_live_ob_ch16'),
    path('june_print_live_ob_ch16/', reports16.june_print_live_ob_ch16, name='june_print_live_ob_ch16'),

    path('july_details_live_ob_ch16/', reports16.july_details_live_ob_ch16, name='july_details_live_ob_ch16'),
    path('july_print_live_ob_ch16/', reports16.july_print_live_ob_ch16, name='july_print_live_ob_ch16'),
    path('auguest_details_live_ob_ch16/', reports16.auguest_details_live_ob_ch16, name='auguest_details_live_ob_ch16'),
    path('auguest_print_live_ob_ch16/', reports16.auguest_print_live_ob_ch16, name='auguest_print_live_ob_ch16'),
    path('sept_details_live_ob_ch16/', reports16.sept_details_live_ob_ch16, name='sept_details_live_ob_ch16'),
    path('sept_print_live_ob_ch16/', reports16.sept_print_live_ob_ch16, name='sept_print_live_ob_ch16'),

    path('october_details_live_ob_ch16/', reports16.october_details_live_ob_ch16, name='october_details_live_ob_ch16'),
    path('october_print_live_ob_ch16/', reports16.october_print_live_ob_ch16, name='october_print_live_ob_ch16'),
    path('nov_details_live_ob_ch16/', reports16.nov_details_live_ob_ch16, name='nov_details_live_ob_ch16'),
    path('nov_print_live_ob_ch16/', reports16.nov_print_live_ob_ch16, name='nov_print_live_ob_ch16'),
    path('dec_details_live_ob_ch16/', reports16.dec_details_live_ob_ch16, name='dec_details_live_ob_ch16'),
    path('dec_print_live_ob_ch16/', reports16.dec_print_live_ob_ch16, name='dec_print_live_ob_ch16'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch16/', reports16.viewall_vaccant_room_ob_ch16, name='viewall_vaccant_room_ob_ch16'),

    path('d_ob_ch16/', branch16.dynamic, name='dynamic'),

    path('manage_bed_ob_ch16/', branch16.manage_bed_ob_ch16, name='manage_bed_ob_ch16'),
    path('manage_new_guest_ob_ch16/', branch16.manage_new_guest_ob_ch16, name='manage_new_guest_ob_ch16'),
    path('manage_update_new_guest_ob_ch16/<id>', branch16.manage_update_new_guest_ob_ch16, name='manage_update_new_guest_ob_ch16'),
    path('manage_update_beds_ob_ch16/<id>', branch16.manage_update_beds_ob_ch16, name='manage_update_beds_ob_ch16'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch16/', branch16.view_all_due_amt_ob_ch16, name='view_all_due_amt_ob_ch16'),
    path('due_amt_mgt_choose_months_ob_ch16/', branch16.due_amt_mgt_choose_months_ob_ch16, name='due_amt_mgt_choose_months_ob_ch16'),

    path('view_jan_account_details_ob_ch16/', branch16.view_jan_account_details_ob_ch16, name='view_jan_account_details_ob_ch16'),
    path('jan_account_mgt_ob_ch16/<id>',branch16.jan_account_mgt_ob_ch16,name='jan_account_mgt_ob_ch16'),
    path('view_feb_account_details_ob_ch16/', branch16.view_feb_account_details_ob_ch16, name='view_feb_account_details_ob_ch16'),
    path('feb_account_mgt_ob_ch16/<id>',branch16.feb_account_mgt_ob_ch16,name='feb_account_mgt_ob_ch16'),
    path('view_march_account_details_ob_ch16/', branch16.view_march_account_details_ob_ch16, name='view_march_account_details_ob_ch16'),
    path('march_account_mgt_ob_ch16/<id>',branch16.march_account_mgt_ob_ch16,name='march_account_mgt_ob_ch16'),
    path('view_april_account_details_ob_ch16/', branch16.view_april_account_details_ob_ch16, name='view_april_account_details_ob_ch16'),
    path('april_account_mgt_ob_ch16/<id>',branch16.april_account_mgt_ob_ch16,name='april_account_mgt_ob_ch16'),

    path('view_may_account_details_ob_ch16/',branch16.view_may_account_details_ob_ch16,name='view_may_account_details_ob_ch16'),
    path('may_account_mgt_ob_ch16/<id>', branch16.may_account_mgt_ob_ch16, name='may_account_mgt_ob_ch16'),
    path('view_june_account_details_ob_ch16/', branch16.view_june_account_details_ob_ch16, name='view_june_account_details_ob_ch16'),
    path('june_account_mgt_ob_ch16/<id>',branch16.june_account_mgt_ob_ch16,name='june_account_mgt_ob_ch16'),
    path('view_july_account_details_ob_ch16/', branch16.view_july_account_details_ob_ch16, name='view_july_account_details_ob_ch16'),
    path('july_account_mgt_ob_ch16/<id>',branch16.july_account_mgt_ob_ch16,name='july_account_mgt_ob_ch16'),
    path('view_auguest_account_details_ob_ch16/', branch16.view_auguest_account_details_ob_ch16, name='view_auguest_account_details_ob_ch16'),
    path('auguest_account_mgt_ob_ch16/<id>',branch16.auguest_account_mgt_ob_ch16,name='auguest_account_mgt_ob_ch16'),

    path('view_sept_account_details_ob_ch16/', branch16.view_sept_account_details_ob_ch16, name='view_sept_account_details_ob_ch16'),
    path('sept_account_mgt_ob_ch16/<id>',branch16.sept_account_mgt_ob_ch16,name='sept_account_mgt_ob_ch16'),
    path('view_october_account_details_ob_ch16/', branch16.view_october_account_details_ob_ch16, name='view_october_account_details_ob_ch16'),
    path('october_account_mgt_ob_ch16/<id>',branch16.october_account_mgt_ob_ch16,name='october_account_mgt_ob_ch16'),
    path('view_nov_account_details_ob_ch16/', branch16.view_nov_account_details_ob_ch16, name='view_nov_account_details_ob_ch16'),
    path('nov_account_mgt_ob_ch16/<id>',branch16.nov_account_mgt_ob_ch16,name='nov_account_mgt_ob_ch16'),
    path('view_dec_account_details_ob_ch16/', branch16.view_dec_account_details_ob_ch16, name='view_dec_account_details_ob_ch16'),
    path('dec_account_mgt_ob_ch16/<id>',branch16.dec_account_mgt_ob_ch16,name='dec_account_mgt_ob_ch16'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch16', admin_dashboard_calculations_br16.monthly_details_due_ob_ch16, name='monthly_details_due_ob_ch16'),
    path('monthly_collection_details_ob_ch16/', admin_dashboard_calculations_br16.monthly_collection_details_ob_ch16, name='monthly_collection_details_ob_ch16'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch16/',branch16.guest_all_ob_ch16,name='guest_all_ob_ch16'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category16/', accounts16.view_all_category16, name='view_all_category16'),
    path('create_new_category16/', accounts16.create_new_category16, name='create_new_category16'),
    path('regi_new_category16/', accounts16.regi_new_category16, name='regi_new_category16'),
    path('update_category16/<id>',accounts16.update_category16,name='update_category16'),

    path('delete_category16/<id>', accounts16.delete_category16, name='delete_category16'),
    path('view_all_category_delete16/', accounts16.view_all_category_delete16, name='view_all_category_delete16'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items16/', accounts16.view_all_items16, name='view_all_items16'),
    path('create_new_item16/', accounts16.create_new_item16, name='create_new_item16'),
    path('regi_new_item16/', accounts16.regi_new_item16, name='regi_new_item16'),
    path('delete_item16/<id>',accounts16.delete_item16,name='delete_item16'),
    path('update_item16/<id>', accounts16.update_item16, name='update_item16'),
    path('view_all_items_delete16/',accounts16.view_all_items_delete16,name='view_all_items_delete16'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger16/', accounts16.view_all_ledger16, name='view_all_ledger16'),
    path('create_new_ledger16/', accounts16.create_new_ledger16, name='create_new_ledger16'),
    path('regi_new_ledger16/', accounts16.regi_new_ledger16, name='regi_new_ledger16'),
    path('delete_ledger16/<id>',accounts16.delete_ledger16,name='delete_ledger16'),
    path('update_ledger16/<id>',accounts16.update_ledger16,name='update_ledger16'),
    path('view_all_ledger_delete16/',accounts16.view_all_ledger_delete16,name='view_all_ledger_delete16'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book16/', accounts16.view_all_accounts_book16, name='view_all_accounts_book16'),
    path('create_new_accounts_book16/', accounts16.create_new_accounts_book16, name='create_new_accounts_book16'),
    path('regi_new_accounts_book16/', accounts16.regi_new_accounts_book16, name='regi_new_accounts_book16'),
    path('update_accounts_book16/<id>',accounts16.update_accounts_book16,name='update_accounts_book16'),
    path('delete_accounts_book16/<id>',accounts16.delete_accounts_book16,name='delete_accounts_book16'),
    path('view_all_accounts_book_delete16/',accounts16.view_all_accounts_book_delete16,name='view_all_accounts_book_delete16'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries16/', accounts16.get_countries16, name='get_countries16'),

    path('in_exp_items_entry16/', accounts16.in_exp_items_entry16, name='in_exp_items_entry16'),
    path('reg_in_exp_items_entry16/', accounts16.reg_in_exp_items_entry16, name='reg_in_exp_items_entry16'),
    path('delete_journal16/<id>',accounts16.delete_journal16,name='delete_journal16'),
    path('update_in_exp_items_entry16/<id>',accounts16.update_in_exp_items_entry16,name='update_in_exp_items_entry16'),
    path('detailed_journal_report16/',accounts16.detailed_journal_report16,name='detailed_journal_report16'),
    path('journal_report_deleted16/',accounts16.journal_report_deleted16,name='journal_report_deleted16'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise16/', accounts16.daily_category_wise16, name='daily_category_wise16'),
    path('monthly_category_based_reports16/',accounts16.monthly_category_based_reports16,name='monthly_category_based_reports16'),
    path('yearly_category_based_reports16/', accounts16.yearly_category_based_reports16,name='yearly_category_based_reports16'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed16/', accounts16.daily_detailed16, name='daily_detailed16'),
    path('monthly_detailed16/',accounts16.monthly_detailed16,name='monthly_detailed16'),
    path('yearly_detailed16/',accounts16.yearly_detailed16,name='yearly_detailed16'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports16/', accounts16.item_based_reports16, name='item_based_reports16'),
    path('daily_item_based_reports16/',accounts16.daily_item_based_reports16,name='daily_item_based_reports16'),
    path('monthly_item_based_reports16/',accounts16.monthly_item_based_reports16,name='monthly_item_based_reports16'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports16/', accounts16.ledger_based_reports16, name='ledger_based_reports16'),
    path('monthly_ledger_based_reports16/', accounts16.monthly_ledger_based_reports16, name='monthly_ledger_based_reports16'),
    path('daily_ledger_based_reports16/',accounts16.daily_ledger_based_reports16,name='daily_ledger_based_reports16'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports16/', accounts16.accounts_book_based_reports16, name='accounts_book_based_reports16'),
    path('daily_accounts_book_based_reports16/',accounts16.daily_accounts_book_based_reports16,name='daily_accounts_book_based_reports16'),
    path('monthly_accounts_book_based_reports16/',accounts16.monthly_accounts_book_based_reports16,name='monthly_accounts_book_based_reports16'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months16/', accounts16.monthly_reports_choose_months16, name='monthly_reports_choose_months16'),
    path('monthly_detailed_daily_in_exp_items_report16/<mo>',accounts16.monthly_detailed_daily_in_exp_items_report16,name='monthly_detailed_daily_in_exp_items_report16'),

    path('single_monthly_reports_choose_months16/', accounts16.single_monthly_reports_choose_months16,name='single_monthly_reports_choose_months16'),
    path('single_monthly_daily_in_exp_items_report16/<mo>',accounts16.single_monthly_daily_in_exp_items_report16,name='single_monthly_daily_in_exp_items_report16'),

    path('accounts_dash_board_ob_ch16/',accounts16.accounts_dash_board_ob_ch16,name='accounts_dash_board_ob_ch16'),
    path('accounts_dash_board16/',accounts16.accounts_dash_board16,name='accounts_dash_board16'),

    path('profit_sharing_choose_months16', accounts16.profit_sharing_choose_months16,name='profit_sharing_choose_months16'),
    path('profit_sharing16/<mo>', accounts16.profit_sharing16, name='profit_sharing16'),
    path('view_share_holders16', accounts16.view_share_holders16, name='view_share_holders16'),
    path('create_share_holders16', accounts16.create_share_holders16, name='create_share_holders16'),
    path('regi_share_holders16', accounts16.regi_share_holders16, name='regi_share_holders16'),
    path('update_share_holders16/<id>', accounts16.update_share_holders16, name='update_share_holders16'),
    path('delete_share_holders16/<id>', accounts16.delete_share_holders16, name='delete_share_holders16'),
    path('view_deleted_share_holders16', accounts16.view_deleted_share_holders16, name='view_deleted_share_holders16'),


]

