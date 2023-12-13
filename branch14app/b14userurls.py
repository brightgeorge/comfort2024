from django.urls import path, include

from . import admin_branch14
from . import admin_branch14
from . import branch14
from . import reports14
from . import payment14
from . import admin_dashboard_calculations_br14
from . import accounts14

urlpatterns = [

    path('branch1_dashboard_ob_ch14/', branch14.branch1_dashboard_ob_ch14, name='branch1_dashboard_ob_ch14'),
    path('background_ob_ch14',branch14.background_ob_ch14,name='background_ob_ch14'),
    path('background_regi_ob_ch14',branch14.background_regi_ob_ch14,name='background_regi_ob_ch14'),
    path('custom_background_regi_ob_ch14',branch14.custom_background_regi_ob_ch14,name='custom_background_regi_ob_ch14'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch14/',admin_branch14.branch1_room_create_regi_ob_ch14,name='branch1_room_create_regi_ob_ch14'),
    path('view_all_room_ob_ch14/',admin_branch14.view_all_room_ob_ch14,name='view_all_room_ob_ch14'),
    path('delete_room_ob_ch14/<id>',admin_branch14.delete_room_ob_ch14,name='delete_room_ob_ch14'),

    path('branch1_room_create_ob_ch14/',admin_branch14.branch1_room_create_ob_ch14,name='branch1_room_create_ob_ch14'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch14/', admin_branch14.pg1_bed_create_regi_ob_ch14, name='pg1_bed_create_regi_ob_ch14'),
    path('pg1_view_all_beds_ob_ch14/', admin_branch14.pg1_view_all_beds_ob_ch14, name='pg1_view_all_beds_ob_ch14'),
    path('delete_bed_ob_ch14/<id>', admin_branch14.delete_bed_ob_ch14, name='delete_bed_ob_ch14'),

    path('pg1_bed_create_ob_ch14/', admin_branch14.pg1_bed_create_ob_ch14, name='pg1_bed_create_ob_ch14'),

    path('single_pg1_bed_create_regi_ob_ch14/',admin_branch14.single_pg1_bed_create_regi_ob_ch14,name='single_pg1_bed_create_regi_ob_ch14'),
    path('update_bed_basic_details_ob_ch14/<id>',admin_branch14.update_bed_basic_details_ob_ch14, name='update_bed_basic_details_ob_ch14'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch14/<id>',branch14.br1_admit_guest_ob_ch14,name='br1_admit_guest_ob_ch14'),
    path('view_all_new_guest_ob_ch14/',branch14.view_all_new_guest_ob_ch14,name='view_all_new_guest_ob_ch14'),
    path('update_br1_admit_guest_ob_ch14/<id>',branch14.update_br1_admit_guest_ob_ch14,name='update_br1_admit_guest_ob_ch14'),
    path('vacate_br1_guest_ob_ch14/<id>',branch14.vacate_br1_guest_ob_ch14,name='vacate_br1_guest_ob_ch14'),

    path('active_guest_details_ob_ch14/<guest_code>',branch14.active_guest_details_ob_ch14,name='active_guest_details_ob_ch14'),
    path('view_all_guest_ob_ch14/',branch14.view_all_guest_ob_ch14,name='view_all_guest_ob_ch14'),
    path('change_duplicate_guest_status_ob_ch14/<id>', branch14.change_duplicate_guest_status_ob_ch14,name='change_duplicate_guest_status_ob_ch14'),
    path('shift_guest_ob_ch14/<id>',branch14.shift_guest_ob_ch14,name='shift_guest_ob_ch14'),
    path('shift_guest_regi_ob_ch14/',branch14.shift_guest_regi_ob_ch14,name='shift_guest_regi_ob_ch14'),

    path('view_all_duplicate_entry_ob_ch14/',branch14.view_all_duplicate_entry_ob_ch14,name='view_all_duplicate_entry_ob_ch14'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),

#guest end here


##################################
#_ADVANCE_ob_ch14 START HERE
################################


    path('choose_months_advance_ob_ch14/',branch14.choose_months_advance_ob_ch14,name='choose_months_advance_ob_ch14'),

    path('jan_advance_ob_ch14/', branch14.jan_advance_ob_ch14, name='jan_advance_ob_ch14'),
    path('jan_make_payments_advance_ob_ch14/<id>', branch14.jan_make_payments_advance_ob_ch14,name='jan_make_payments_advance_ob_ch14'),
    path('feb_advance_ob_ch14/', branch14.feb_advance_ob_ch14, name='feb_advance_ob_ch14'),
    path('feb_make_payments_advance_ob_ch14/<id>', branch14.feb_make_payments_advance_ob_ch14,name='feb_make_payments_advance_ob_ch14'),
    path('march_advance_ob_ch14/', branch14.march_advance_ob_ch14, name='march_advance_ob_ch14'),
    path('march_make_payments_advance_ob_ch14/<id>', branch14.march_make_payments_advance_ob_ch14,name='march_make_payments_advance_ob_ch14'),
    path('april_advance_ob_ch14/', branch14.april_advance_ob_ch14, name='april_advance_ob_ch14'),
    path('april_make_payments_advance_ob_ch14/<id>', branch14.april_make_payments_advance_ob_ch14, name='april_make_payments_advance_ob_ch14'),

    path('may_advance_ob_ch14/',branch14.may_advance_ob_ch14,name='may_advance_ob_ch14'),
    path('may_make_payments_advance_ob_ch14/<id>', branch14.may_make_payments_advance_ob_ch14, name='may_make_payments_advance_ob_ch14'),
    path('june_advance_ob_ch14/',branch14.june_advance_ob_ch14,name='june_advance_ob_ch14'),
    path('june_make_payments_advance_ob_ch14/<id>', branch14.june_make_payments_advance_ob_ch14, name='june_make_payments_advance_ob_ch14'),
    path('july_advance_ob_ch14/',branch14.july_advance_ob_ch14,name='july_advance_ob_ch14'),
    path('july_make_payments_advance_ob_ch14/<id>', branch14.july_make_payments_advance_ob_ch14, name='july_make_payments_advance_ob_ch14'),
    path('auguest_advance_ob_ch14/', branch14.auguest_advance_ob_ch14, name='auguest_advance_ob_ch14'),
    path('auguest_make_payments_advance_ob_ch14/<id>', branch14.auguest_make_payments_advance_ob_ch14, name='auguest_make_payments_advance_ob_ch14'),

    path('sept_advance_ob_ch14/', branch14.sept_advance_ob_ch14, name='sept_advance_ob_ch14'),
    path('sept_make_payments_advance_ob_ch14/<id>', branch14.sept_make_payments_advance_ob_ch14,name='sept_make_payments_advance_ob_ch14'),
    path('october_advance_ob_ch14/', branch14.october_advance_ob_ch14, name='october_advance_ob_ch14'),
    path('october_make_payments_advance_ob_ch14/<id>', branch14.october_make_payments_advance_ob_ch14, name='october_make_payments_advance_ob_ch14'),
    path('nov_advance_ob_ch14/', branch14.nov_advance_ob_ch14, name='nov_advance_ob_ch14'),
    path('nov_make_payments_advance_ob_ch14/<id>', branch14.nov_make_payments_advance_ob_ch14,name='nov_make_payments_advance_ob_ch14'),
    path('dec_advance_ob_ch14/', branch14.dec_advance_ob_ch14, name='dec_advance_ob_ch14'),
    path('dec_make_payments_advance_ob_ch14/<id>', branch14.dec_make_payments_advance_ob_ch14, name='dec_make_payments_advance_ob_ch14'),



##################################
#_ADVANCE_ob_ch14 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch14/',branch14.choose_months_ob_ch14,name='choose_months_ob_ch14'),

    path('jan_ob_ch14/',branch14.jan_ob_ch14,name='jan_ob_ch14'),
    path('jan_manke_payments_ob_ch14/<id>',branch14.jan_manke_payments_ob_ch14,name='jan_manke_payments_ob_ch14'),

    path('feb_ob_ch14/',branch14.feb_ob_ch14,name='feb_ob_ch14'),
    path('feb_manke_payments_ob_ch14/<id>',branch14.feb_manke_payments_ob_ch14,name='feb_manke_payments_ob_ch14'),

    path('march_ob_ch14/',branch14.march_ob_ch14,name='march_ob_ch14'),
    path('march_manke_payments_ob_ch14/<id>',branch14.march_manke_payments_ob_ch14,name='march_manke_payments_ob_ch14'),

    path('april_ob_ch14/',branch14.april_ob_ch14,name='april_ob_ch14'),
    path('april_make_payments_ob_ch14/<id>',branch14.april_make_payments_ob_ch14,name='april_make_payments_ob_ch14'),

    path('may_ob_ch14/',branch14.may_ob_ch14,name='may_ob_ch14'),
    path('may_make_payments_ob_ch14/<id>',branch14.may_make_payments_ob_ch14,name='may_make_payments_ob_ch14'),

    path('june_ob_ch14/',branch14.june_ob_ch14,name='june_ob_ch14'),
    path('june_make_payments_ob_ch14/<id>',branch14.june_make_payments_ob_ch14,name='june_make_payments_ob_ch14'),

    path('july_ob_ch14/',branch14.july_ob_ch14,name='july_ob_ch14'),
    path('july_make_payments_ob_ch14/<id>',branch14.july_make_payments_ob_ch14,name='july_make_payments_ob_ch14'),

    path('aug_ob_ch14/',branch14.aug_ob_ch14,name='aug_ob_ch14'),
    path('aug_make_payments_ob_ch14/<id>',branch14.aug_make_payments_ob_ch14,name='aug_make_payments_ob_ch14'),

    path('sept_ob_ch14/',branch14.sept_ob_ch14,name='sept_ob_ch14'),
    path('sept_make_payments_ob_ch14/<id>',branch14.sept_make_payments_ob_ch14,name='sept_make_payments_ob_ch14'),

    path('oct_ob_ch14/',branch14.oct_ob_ch14,name='oct_ob_ch14'),
    path('oct_make_payments_ob_ch14/<id>',branch14.oct_make_payments_ob_ch14,name='oct_make_payments_ob_ch14'),

    path('nov_ob_ch14/',branch14.nov_ob_ch14,name='nov_ob_ch14'),
    path('nov_make_payments_ob_ch14/<id>',branch14.nov_make_payments_ob_ch14,name='nov_make_payments_ob_ch14'),

    path('dec_ob_ch14/',branch14.dec_ob_ch14,name='dec_ob_ch14'),
    path('dec_make_payments_ob_ch14/<id>',branch14.dec_make_payments_ob_ch14,name='dec_make_payments_ob_ch14'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch14/', payment14.choose_user_ob_ch14, name='choose_user_ob_ch14'),
    path('payment_user_details_ob_ch14/<id>', payment14.payment_user_details_ob_ch14, name='payment_user_details_ob_ch14'),
    path('close_choose_user_ob_ch14/<id>',payment14.close_choose_user_ob_ch14,name='close_choose_user_ob_ch14'),

    path('monthly_jan_make_payments_ob_ch14/<id>', payment14.monthly_jan_make_payments_ob_ch14, name='monthly_jan_make_payments_ob_ch14'),
    path('monthly_feb_make_payments_ob_ch14/<id>', payment14.monthly_feb_make_payments_ob_ch14, name='monthly_feb_make_payments_ob_ch14'),
    path('monthly_march_make_payments_ob_ch14/<id>', payment14.monthly_march_make_payments_ob_ch14, name='monthly_march_make_payments_ob_ch14'),
    path('monthly_april_make_payments_ob_ch14/<id>', payment14.monthly_april_make_payments_ob_ch14, name='monthly_april_make_payments_ob_ch14'),
    path('monthly_may_make_payments_ob_ch14/<id>', payment14.monthly_may_make_payments_ob_ch14, name='monthly_may_make_payments_ob_ch14'),
    path('monthly_june_make_payments_ob_ch14/<id>', payment14.monthly_june_make_payments_ob_ch14, name='monthly_june_make_payments_ob_ch14'),

    path('monthly_july_make_payments_ob_ch14/<id>', payment14.monthly_july_make_payments_ob_ch14, name='monthly_july_make_payments_ob_ch14'),
    path('monthly_aug_make_payments_ob_ch14/<id>', payment14.monthly_aug_make_payments_ob_ch14, name='monthly_aug_make_payments_ob_ch14'),
    path('monthly_sept_make_payments_ob_ch14/<id>', payment14.monthly_sept_make_payments_ob_ch14, name='monthly_sept_make_payments_ob_ch14'),
    path('monthly_oct_make_payments_ob_ch14/<id>', payment14.monthly_oct_make_payments_ob_ch14, name='monthly_oct_make_payments_ob_ch14'),
    path('monthly_nov_make_payments_ob_ch14/<id>', payment14.monthly_nov_make_payments_ob_ch14, name='monthly_nov_make_payments_ob_ch14'),
    path('monthly_dec_make_payments_ob_ch14/<id>', payment14.monthly_dec_make_payments_ob_ch14, name='monthly_dec_make_payments_ob_ch14'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch14/',branch14.unpaid_rent_choose_months_ob_ch14,name='unpaid_rent_choose_months_ob_ch14'),

    path('jan_unpaid_rent_ob_ch14/', branch14.jan_unpaid_rent_ob_ch14, name='jan_unpaid_rent_ob_ch14'),
    path('table_jan_unpaid_rent_ob_ch14/', branch14.table_jan_unpaid_rent_ob_ch14, name='table_jan_unpaid_rent_ob_ch14'),
    path('feb_unpaid_rent_ob_ch14/', branch14.feb_unpaid_rent_ob_ch14, name='feb_unpaid_rent_ob_ch14'),
    path('table_feb_unpaid_rent_ob_ch14/', branch14.table_feb_unpaid_rent_ob_ch14, name='table_feb_unpaid_rent_ob_ch14'),
    path('mar_unpaid_rent_ob_ch14/', branch14.mar_unpaid_rent_ob_ch14, name='mar_unpaid_rent_ob_ch14'),
    path('table_mar_unpaid_rent_ob_ch14/', branch14.table_mar_unpaid_rent_ob_ch14, name='table_mar_unpaid_rent_ob_ch14'),
    path('april_unpaid_rent_ob_ch14/', branch14.april_unpaid_rent_ob_ch14, name='april_unpaid_rent_ob_ch14'),
    path('table_april_unpaid_rent_ob_ch14/', branch14.table_april_unpaid_rent_ob_ch14, name='table_april_unpaid_rent_ob_ch14'),

    path('may_unpaid_rent_ob_ch14/', branch14.may_unpaid_rent_ob_ch14, name='may_unpaid_rent_ob_ch14'),
    path('table_may_unpaid_rent_ob_ch14/', branch14.table_may_unpaid_rent_ob_ch14, name='table_may_unpaid_rent_ob_ch14'),
    path('june_unpaid_rent_ob_ch14/', branch14.june_unpaid_rent_ob_ch14, name='june_unpaid_rent_ob_ch14'),
    path('table_june_unpaid_rent_ob_ch14/', branch14.table_june_unpaid_rent_ob_ch14, name='table_june_unpaid_rent_ob_ch14'),
    path('july_unpaid_rent_ob_ch14/', branch14.july_unpaid_rent_ob_ch14, name='july_unpaid_rent_ob_ch14'),
    path('table_july_unpaid_rent_ob_ch14',branch14.table_july_unpaid_rent_ob_ch14,name='table_july_unpaid_rent_ob_ch14'),
    path('aug_unpaid_rent_ob_ch14/', branch14.aug_unpaid_rent_ob_ch14, name='aug_unpaid_rent_ob_ch14'),
    path('table_aug_unpaid_rent_ob_ch14/',branch14.table_aug_unpaid_rent_ob_ch14,name='table_aug_unpaid_rent_ob_ch14'),

    path('sept_unpaid_rent_ob_ch14/', branch14.sept_unpaid_rent_ob_ch14, name='sept_unpaid_rent_ob_ch14'),
    path('table_sept_unpaid_rent_ob_ch14/', branch14.table_sept_unpaid_rent_ob_ch14, name='table_sept_unpaid_rent_ob_ch14'),
    path('oct_unpaid_rent_ob_ch14/', branch14.oct_unpaid_rent_ob_ch14, name='oct_unpaid_rent_ob_ch14'),
    path('table_oct_unpaid_rent_ob_ch14/', branch14.table_oct_unpaid_rent_ob_ch14, name='table_oct_unpaid_rent_ob_ch14'),
    path('nov_unpaid_rent_ob_ch14/', branch14.nov_unpaid_rent_ob_ch14, name='nov_unpaid_rent_ob_ch14'),
    path('table_nov_unpaid_rent_ob_ch14/', branch14.table_nov_unpaid_rent_ob_ch14, name='table_nov_unpaid_rent_ob_ch14'),
    path('dec_unpaid_rent_ob_ch14/', branch14.dec_unpaid_rent_ob_ch14, name='dec_unpaid_rent_ob_ch14'),
    path('table_dec_unpaid_rent_ob_ch14/', branch14.table_dec_unpaid_rent_ob_ch14, name='table_dec_unpaid_rent_ob_ch14'),

    path('details_of_unpaid_guests_ob_ch14/<id>',branch14.details_of_unpaid_guests_ob_ch14,name='details_of_unpaid_guests_ob_ch14'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch14/',branch14.paid_rent_choose_months_ob_ch14,name='paid_rent_choose_months_ob_ch14'),
    path('partially_paid_guest_choose_months_ob_ch14/',reports14.partially_paid_guest_choose_months_ob_ch14,name='partially_paid_guest_choose_months_ob_ch14'),

    path('jan_paid_rent_ob_ch14/', branch14.jan_paid_rent_ob_ch14, name='jan_paid_rent_ob_ch14'),
    path('table_jan_paid_rent_ob_ch14/', branch14.table_jan_paid_rent_ob_ch14, name='table_jan_paid_rent_ob_ch14'),
    path('jan_full_paid_guest_ob_ch14/', reports14.jan_full_paid_guest_ob_ch14, name='jan_full_paid_guest_ob_ch14'),
    path('jan_partially_paid_guest_ob_ch14/', reports14.jan_partially_paid_guest_ob_ch14, name='jan_partially_paid_guest_ob_ch14'),
    path('table_jan_partially_paid_guest_ob_ch14/', reports14.table_jan_partially_paid_guest_ob_ch14,name='table_jan_partially_paid_guest_ob_ch14'),

    path('feb_paid_rent_ob_ch14/', branch14.feb_paid_rent_ob_ch14, name='feb_paid_rent_ob_ch14'),
    path('table_feb_paid_rent_ob_ch14/', branch14.table_feb_paid_rent_ob_ch14, name='table_feb_paid_rent_ob_ch14'),
    path('feb_full_paid_guest_ob_ch14/', reports14.feb_full_paid_guest_ob_ch14, name='feb_full_paid_guest_ob_ch14'),
    path('feb_partially_paid_guest_ob_ch14/', reports14.feb_partially_paid_guest_ob_ch14, name='feb_partially_paid_guest_ob_ch14'),
    path('table_feb_partially_paid_guest_ob_ch14/', reports14.table_feb_partially_paid_guest_ob_ch14,name='table_feb_partially_paid_guest_ob_ch14'),

    path('mar_paid_rent_ob_ch14/', branch14.mar_paid_rent_ob_ch14, name='mar_paid_rent_ob_ch14'),
    path('table_mar_paid_rent_ob_ch14/', branch14.table_mar_paid_rent_ob_ch14, name='table_mar_paid_rent_ob_ch14'),
    path('march_full_paid_guest_ob_ch14/', reports14.march_full_paid_guest_ob_ch14, name='march_full_paid_guest_ob_ch14'),
    path('march_partially_paid_guest_ob_ch14/', reports14.march_partially_paid_guest_ob_ch14, name='march_partially_paid_guest_ob_ch14'),
    path('table_march_partially_paid_guest_ob_ch14/', reports14.table_march_partially_paid_guest_ob_ch14,name='table_march_partially_paid_guest_ob_ch14'),

    path('april_paid_rent_ob_ch14/', branch14.april_paid_rent_ob_ch14, name='april_paid_rent_ob_ch14'),
    path('table_april_paid_rent_ob_ch14/', branch14.table_april_paid_rent_ob_ch14, name='table_april_paid_rent_ob_ch14'),
    path('april_full_paid_guest_ob_ch14/', reports14.april_full_paid_guest_ob_ch14, name='april_full_paid_guest_ob_ch14'),
    path('april_partially_paid_guest_ob_ch14/', reports14.april_partially_paid_guest_ob_ch14, name='april_partially_paid_guest_ob_ch14'),
    path('table_april_partially_paid_guest_ob_ch14/', reports14.table_april_partially_paid_guest_ob_ch14,name='table_april_partially_paid_guest_ob_ch14'),

    path('may_paid_rent_ob_ch14/', branch14.may_paid_rent_ob_ch14, name='may_paid_rent_ob_ch14'),
    path('table_may_paid_rent_ob_ch14/', branch14.table_may_paid_rent_ob_ch14, name='table_may_paid_rent_ob_ch14'),
    path('may_full_paid_guest_ob_ch14/', reports14.may_full_paid_guest_ob_ch14, name='may_full_paid_guest_ob_ch14'),
    path('may_partially_paid_guest_ob_ch14/', reports14.may_partially_paid_guest_ob_ch14, name='may_partially_paid_guest_ob_ch14'),
    path('table_may_partially_paid_guest_ob_ch14/', reports14.table_may_partially_paid_guest_ob_ch14, name='table_may_partially_paid_guest_ob_ch14'),

    path('june_paid_rent_ob_ch14/', branch14.june_paid_rent_ob_ch14, name='june_paid_rent_ob_ch14'),
    path('table_june_paid_rent_ob_ch14/', branch14.table_june_paid_rent_ob_ch14, name='table_june_paid_rent_ob_ch14'),
    path('june_full_paid_guest_ob_ch14/', reports14.june_full_paid_guest_ob_ch14, name='june_full_paid_guest_ob_ch14'),
    path('june_partially_paid_guest_ob_ch14/', reports14.june_partially_paid_guest_ob_ch14, name='june_partially_paid_guest_ob_ch14'),
    path('table_june_partially_paid_guest_ob_ch14/', reports14.table_june_partially_paid_guest_ob_ch14, name='table_june_partially_paid_guest_ob_ch14'),

    path('july_paid_rent_ob_ch14/', branch14.july_paid_rent_ob_ch14, name='july_paid_rent_ob_ch14'),
    path('table_july_paid_rent_ob_ch14/', branch14.table_july_paid_rent_ob_ch14, name='table_july_paid_rent_ob_ch14'),
    path('july_full_paid_guest_ob_ch14/', reports14.july_full_paid_guest_ob_ch14, name='july_full_paid_guest_ob_ch14'),
    path('july_partially_paid_guest_ob_ch14/', reports14.july_partially_paid_guest_ob_ch14, name='july_partially_paid_guest_ob_ch14'),
    path('table_july_partially_paid_guest_ob_ch14/', reports14.table_july_partially_paid_guest_ob_ch14, name='table_july_partially_paid_guest_ob_ch14'),

    path('aug_paid_rent_ob_ch14/', branch14.aug_paid_rent_ob_ch14, name='aug_paid_rent_ob_ch14'),
    path('table_aug_paid_rent_ob_ch14/', branch14.table_aug_paid_rent_ob_ch14, name='table_aug_paid_rent_ob_ch14'),
    path('auguest_full_paid_guest_ob_ch14/', reports14.auguest_full_paid_guest_ob_ch14, name='auguest_full_paid_guest_ob_ch14'),
    path('auguest_partially_paid_guest_ob_ch14/', reports14.auguest_partially_paid_guest_ob_ch14,name='auguest_partially_paid_guest_ob_ch14'),
    path('table_auguest_partially_paid_guest_ob_ch14/', reports14.table_auguest_partially_paid_guest_ob_ch14,name='table_auguest_partially_paid_guest_ob_ch14'),

    path('sept_paid_rent_ob_ch14/', branch14.sept_paid_rent_ob_ch14, name='sept_paid_rent_ob_ch14'),
    path('table_sept_paid_rent_ob_ch14/', branch14.table_sept_paid_rent_ob_ch14, name='table_sept_paid_rent_ob_ch14'),
    path('sept_full_paid_guest_ob_ch14/', reports14.sept_full_paid_guest_ob_ch14, name='sept_full_paid_guest_ob_ch14'),
    path('sept_partially_paid_guest_ob_ch14/', reports14.sept_partially_paid_guest_ob_ch14, name='sept_partially_paid_guest_ob_ch14'),
    path('table_sept_partially_paid_guest_ob_ch14/', reports14.table_sept_partially_paid_guest_ob_ch14,name='table_sept_partially_paid_guest_ob_ch14'),

    path('oct_paid_rent_ob_ch14/', branch14.oct_paid_rent_ob_ch14, name='oct_paid_rent_ob_ch14'),
    path('table_oct_paid_rent_ob_ch14/', branch14.table_oct_paid_rent_ob_ch14, name='table_oct_paid_rent_ob_ch14'),
    path('october_full_paid_guest_ob_ch14/', reports14.october_full_paid_guest_ob_ch14, name='october_full_paid_guest_ob_ch14'),
    path('october_partially_paid_guest_ob_ch14/', reports14.october_partially_paid_guest_ob_ch14,name='october_partially_paid_guest_ob_ch14'),
    path('table_october_partially_paid_guest_ob_ch14/', reports14.table_october_partially_paid_guest_ob_ch14,name='table_october_partially_paid_guest_ob_ch14'),

    path('nov_paid_rent_ob_ch14/', branch14.nov_paid_rent_ob_ch14, name='nov_paid_rent_ob_ch14'),
    path('table_nov_paid_rent_ob_ch14/', branch14.table_nov_paid_rent_ob_ch14, name='table_nov_paid_rent_ob_ch14'),
    path('nov_full_paid_guest_ob_ch14/', reports14.nov_full_paid_guest_ob_ch14, name='nov_full_paid_guest_ob_ch14'),
    path('nov_partially_paid_guest_ob_ch14/', reports14.nov_partially_paid_guest_ob_ch14, name='nov_partially_paid_guest_ob_ch14'),
    path('table_nov_partially_paid_guest_ob_ch14/', reports14.table_nov_partially_paid_guest_ob_ch14,name='table_nov_partially_paid_guest_ob_ch14'),

    path('dec_paid_rent_ob_ch14/', branch14.dec_paid_rent_ob_ch14, name='dec_paid_rent_ob_ch14'),
    path('table_dec_paid_rent_ob_ch14/', branch14.table_dec_paid_rent_ob_ch14, name='table_dec_paid_rent_ob_ch14'),
    path('dec_full_paid_guest_ob_ch14/', reports14.dec_full_paid_guest_ob_ch14, name='dec_full_paid_guest_ob_ch14'),
    path('dec_partially_paid_guest_ob_ch14/', reports14.dec_partially_paid_guest_ob_ch14, name='dec_partially_paid_guest_ob_ch14'),
    path('table_dec_partially_paid_guest_ob_ch14/', reports14.table_dec_partially_paid_guest_ob_ch14,name='table_dec_partially_paid_guest_ob_ch14'),

    path('details_of_paid_guests_ob_ch14/<id>',branch14.details_of_paid_guests_ob_ch14,name='details_of_paid_guests_ob_ch14'),
    path('full_paid_guest_ob_ch14/',reports14.full_paid_guest_ob_ch14,name='full_paid_guest_ob_ch14'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch14/',branch14.viewall_vacate_guest_ob_ch14,name='viewall_vacate_guest_ob_ch14'),
    path('details_of_vacate_guest_ob_ch14/<id>',branch14.details_of_vacate_guest_ob_ch14,name='details_of_vacate_guest_ob_ch14'),
    path('full_vacated_guest_details_ob_ch14',branch14.full_vacated_guest_details_ob_ch14,name='full_vacated_guest_details_ob_ch14'),
    path('full_vacated_guest_table_ob_ch14',branch14.full_vacated_guest_table_ob_ch14,name='full_vacated_guest_table_ob_ch14'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch14/<id>', branch14.jan_manke_payments_vacate_ob_ch14, name='jan_manke_payments_vacate_ob_ch14'),
    path('feb_manke_payments_vacate_ob_ch14/<id>', branch14.feb_manke_payments_vacate_ob_ch14, name='feb_manke_payments_vacate_ob_ch14'),
    path('march_manke_payments_vacate_ob_ch14/<id>', branch14.march_manke_payments_vacate_ob_ch14, name='march_manke_payments_vacate_ob_ch14'),
    path('april_make_payments_vacate_ob_ch14/<id>', branch14.april_make_payments_vacate_ob_ch14, name='april_make_payments_vacate_ob_ch14'),

    path('may_make_payments_vacate_ob_ch14/<id>', branch14.may_make_payments_vacate_ob_ch14, name='may_make_payments_vacate_ob_ch14'),
    path('june_make_payments_vacate_ob_ch14/<id>', branch14.june_make_payments_vacate_ob_ch14, name='june_make_payments_vacate_ob_ch14'),
    path('july_make_payments_vacate_ob_ch14/<id>', branch14.july_make_payments_vacate_ob_ch14, name='july_make_payments_vacate_ob_ch14'),
    path('aug_make_payments_vacate_ob_ch14/<id>', branch14.aug_make_payments_vacate_ob_ch14, name='aug_make_payments_vacate_ob_ch14'),

    path('sept_make_payments_vacate_ob_ch14/<id>', branch14.sept_make_payments_vacate_ob_ch14, name='sept_make_payments_vacate_ob_ch14'),
    path('oct_make_payments_vacate_ob_ch14/<id>', branch14.oct_make_payments_vacate_ob_ch14, name='oct_make_payments_vacate_ob_ch14'),
    path('nov_make_payments_vacate_ob_ch14/<id>', branch14.nov_make_payments_vacate_ob_ch14, name='nov_make_payments_vacate_ob_ch14'),
    path('dec_make_payments_vacate_ob_ch14/<id>', branch14.dec_make_payments_vacate_ob_ch14, name='dec_make_payments_vacate_ob_ch14'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch14/',branch14.detail_guest_general_ob_ch14,name='detail_guest_general_ob_ch14'),

    path('jan_print_ob_ch14/',branch14.jan_print_ob_ch14,name='jan_print_ob_ch14'),
    path('feb_print_ob_ch14/',branch14.feb_print_ob_ch14,name='feb_print_ob_ch14'),
    path('march_print_ob_ch14/',branch14.march_print_ob_ch14,name='march_print_ob_ch14'),
    path('april_print_ob_ch14/',branch14.april_print_ob_ch14,name='april_print_ob_ch14'),

    path('may_print_ob_ch14/',branch14.may_print_ob_ch14,name='may_print_ob_ch14'),
    path('june_print_ob_ch14/',branch14.june_print_ob_ch14,name='june_print_ob_ch14'),
    path('july_print_ob_ch14/', branch14.july_print_ob_ch14, name='july_print_ob_ch14'),
    path('aug_print_ob_ch14/', branch14.aug_print_ob_ch14, name='aug_print_ob_ch14'),

    path('sept_print_ob_ch14/', branch14.sept_print_ob_ch14, name='sept_print_ob_ch14'),
    path('oct_print_ob_ch14/', branch14.oct_print_ob_ch14, name='oct_print_ob_ch14'),
    path('nov_print_ob_ch14/', branch14.nov_print_ob_ch14, name='nov_print_ob_ch14'),
    path('dec_print_ob_ch14/', branch14.dec_print_ob_ch14, name='dec_print_ob_ch14'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch14/', branch14.jan_close_ob_ch14, name='jan_close_ob_ch14'),
    path('jan_close_decision_page_ob_ch14/', branch14.jan_close_decision_page_ob_ch14, name='jan_close_decision_page_ob_ch14'),
    path('feb_close/', branch14.feb_close_ob_ch14, name='feb_close_ob_ch14'),
    path('feb_close_decision_page_ob_ch14/', branch14.feb_close_decision_page_ob_ch14, name='feb_close_decision_page_ob_ch14'),
    path('mar_close_ob_ch14/', branch14.mar_close_ob_ch14, name='mar_close_ob_ch14'),
    path('mar_close_decision_page/', branch14.mar_close_decision_page_ob_ch14, name='mar_close_decision_page_ob_ch14'),
    path('apr_close_ob_ch14/', branch14.apr_close_ob_ch14, name='apr_close_ob_ch14'),
    path('apr_close_decision_page_ob_ch14/', branch14.apr_close_decision_page_ob_ch14, name='apr_close_decision_page_ob_ch14'),

    path('may_close_ob_ch14/', branch14.may_close_ob_ch14, name='may_close_ob_ch14'),
    path('may_close_decision_page_ob_ch14/', branch14.may_close_decision_page_ob_ch14, name='may_close_decision_page_ob_ch14'),
    path('jun_close_ob_ch14/', branch14.jun_close_ob_ch14, name='jun_close_ob_ch14'),
    path('jun_close_decision_page_ob_ch14/', branch14.jun_close_decision_page_ob_ch14, name='jun_close_decision_page_ob_ch14'),
    path('jul_close_ob_ch14/', branch14.jul_close_ob_ch14, name='jul_close_ob_ch14'),
    path('jul_close_decision_page_ob_ch14/', branch14.jul_close_decision_page_ob_ch14, name='jul_close_decision_page_ob_ch14'),
    path('aug_close_ob_ch14/', branch14.aug_close_ob_ch14, name='aug_close_ob_ch14'),
    path('aug_close_decision_page_ob_ch14/', branch14.aug_close_decision_page_ob_ch14, name='aug_close_decision_page_ob_ch14'),

    path('sep_close_ob_ch14/', branch14.sep_close_ob_ch14, name='sep_close_ob_ch14'),
    path('sep_close_decision_page_ob_ch14/', branch14.sep_close_decision_page_ob_ch14, name='sep_close_decision_page_ob_ch14'),
    path('oct_close_ob_ch14/', branch14.oct_close_ob_ch14, name='oct_close_ob_ch14'),
    path('oct_close_decision_page_ob_ch14/', branch14.oct_close_decision_page_ob_ch14, name='oct_close_decision_page_ob_ch14'),
    path('nov_close_ob_ch14/', branch14.nov_close_ob_ch14, name='nov_close_ob_ch14'),
    path('nov_close_decision_page_ob_ch14/', branch14.nov_close_decision_page_ob_ch14, name='nov_close_decision_page_ob_ch14'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch14/',reports14.detailed_report_choose_months_ob_ch14,name='detailed_report_choose_months_ob_ch14'),

    path('jan_details_live_ob_ch14/', reports14.jan_details_live_ob_ch14, name='jan_details_live_ob_ch14'),
    path('jan_print_live_ob_ch14/', reports14.jan_print_live_ob_ch14, name='jan_print_live_ob_ch14'),
    path('feb_details_live_ob_ch14/', reports14.feb_details_live_ob_ch14, name='feb_details_live_ob_ch14'),
    path('feb_print_live_ob_ch14/', reports14.feb_print_live_ob_ch14, name='feb_print_live_ob_ch14'),
    path('march_details_live_ob_ch14/', reports14.march_details_live_ob_ch14, name='march_details_live_ob_ch14'),
    path('march_print_live_ob_ch14/', reports14.march_print_live_ob_ch14, name='march_print_live_ob_ch14'),

    path('april_details_live_ob_ch14/', reports14.april_details_live_ob_ch14, name='april_details_live_ob_ch14'),
    path('april_print_live_ob_ch14/', reports14.april_print_live_ob_ch14, name='april_print_live_ob_ch14'),
    path('may_details_live_ob_ch14/', reports14.may_details_live_ob_ch14, name='may_details_live_ob_ch14'),
    path('may_print_live_ob_ch14/', reports14.may_print_live_ob_ch14, name='may_print_live_ob_ch14'),
    path('june_details_live_ob_ch14/',reports14.june_details_live_ob_ch14,name='june_details_live_ob_ch14'),
    path('june_print_live_ob_ch14/', reports14.june_print_live_ob_ch14, name='june_print_live_ob_ch14'),

    path('july_details_live_ob_ch14/', reports14.july_details_live_ob_ch14, name='july_details_live_ob_ch14'),
    path('july_print_live_ob_ch14/', reports14.july_print_live_ob_ch14, name='july_print_live_ob_ch14'),
    path('auguest_details_live_ob_ch14/', reports14.auguest_details_live_ob_ch14, name='auguest_details_live_ob_ch14'),
    path('auguest_print_live_ob_ch14/', reports14.auguest_print_live_ob_ch14, name='auguest_print_live_ob_ch14'),
    path('sept_details_live_ob_ch14/', reports14.sept_details_live_ob_ch14, name='sept_details_live_ob_ch14'),
    path('sept_print_live_ob_ch14/', reports14.sept_print_live_ob_ch14, name='sept_print_live_ob_ch14'),

    path('october_details_live_ob_ch14/', reports14.october_details_live_ob_ch14, name='october_details_live_ob_ch14'),
    path('october_print_live_ob_ch14/', reports14.october_print_live_ob_ch14, name='october_print_live_ob_ch14'),
    path('nov_details_live_ob_ch14/', reports14.nov_details_live_ob_ch14, name='nov_details_live_ob_ch14'),
    path('nov_print_live_ob_ch14/', reports14.nov_print_live_ob_ch14, name='nov_print_live_ob_ch14'),
    path('dec_details_live_ob_ch14/', reports14.dec_details_live_ob_ch14, name='dec_details_live_ob_ch14'),
    path('dec_print_live_ob_ch14/', reports14.dec_print_live_ob_ch14, name='dec_print_live_ob_ch14'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch14/', reports14.viewall_vaccant_room_ob_ch14, name='viewall_vaccant_room_ob_ch14'),

    path('d_ob_ch14/', branch14.dynamic, name='dynamic'),

    path('manage_bed_ob_ch14/', branch14.manage_bed_ob_ch14, name='manage_bed_ob_ch14'),
    path('manage_new_guest_ob_ch14/', branch14.manage_new_guest_ob_ch14, name='manage_new_guest_ob_ch14'),
    path('manage_update_new_guest_ob_ch14/<id>', branch14.manage_update_new_guest_ob_ch14, name='manage_update_new_guest_ob_ch14'),
    path('manage_update_beds_ob_ch14/<id>', branch14.manage_update_beds_ob_ch14, name='manage_update_beds_ob_ch14'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch14/', branch14.view_all_due_amt_ob_ch14, name='view_all_due_amt_ob_ch14'),
    path('due_amt_mgt_choose_months_ob_ch14/', branch14.due_amt_mgt_choose_months_ob_ch14, name='due_amt_mgt_choose_months_ob_ch14'),

    path('view_jan_account_details_ob_ch14/', branch14.view_jan_account_details_ob_ch14, name='view_jan_account_details_ob_ch14'),
    path('jan_account_mgt_ob_ch14/<id>',branch14.jan_account_mgt_ob_ch14,name='jan_account_mgt_ob_ch14'),
    path('view_feb_account_details_ob_ch14/', branch14.view_feb_account_details_ob_ch14, name='view_feb_account_details_ob_ch14'),
    path('feb_account_mgt_ob_ch14/<id>',branch14.feb_account_mgt_ob_ch14,name='feb_account_mgt_ob_ch14'),
    path('view_march_account_details_ob_ch14/', branch14.view_march_account_details_ob_ch14, name='view_march_account_details_ob_ch14'),
    path('march_account_mgt_ob_ch14/<id>',branch14.march_account_mgt_ob_ch14,name='march_account_mgt_ob_ch14'),
    path('view_april_account_details_ob_ch14/', branch14.view_april_account_details_ob_ch14, name='view_april_account_details_ob_ch14'),
    path('april_account_mgt_ob_ch14/<id>',branch14.april_account_mgt_ob_ch14,name='april_account_mgt_ob_ch14'),

    path('view_may_account_details_ob_ch14/',branch14.view_may_account_details_ob_ch14,name='view_may_account_details_ob_ch14'),
    path('may_account_mgt_ob_ch14/<id>', branch14.may_account_mgt_ob_ch14, name='may_account_mgt_ob_ch14'),
    path('view_june_account_details_ob_ch14/', branch14.view_june_account_details_ob_ch14, name='view_june_account_details_ob_ch14'),
    path('june_account_mgt_ob_ch14/<id>',branch14.june_account_mgt_ob_ch14,name='june_account_mgt_ob_ch14'),
    path('view_july_account_details_ob_ch14/', branch14.view_july_account_details_ob_ch14, name='view_july_account_details_ob_ch14'),
    path('july_account_mgt_ob_ch14/<id>',branch14.july_account_mgt_ob_ch14,name='july_account_mgt_ob_ch14'),
    path('view_auguest_account_details_ob_ch14/', branch14.view_auguest_account_details_ob_ch14, name='view_auguest_account_details_ob_ch14'),
    path('auguest_account_mgt_ob_ch14/<id>',branch14.auguest_account_mgt_ob_ch14,name='auguest_account_mgt_ob_ch14'),

    path('view_sept_account_details_ob_ch14/', branch14.view_sept_account_details_ob_ch14, name='view_sept_account_details_ob_ch14'),
    path('sept_account_mgt_ob_ch14/<id>',branch14.sept_account_mgt_ob_ch14,name='sept_account_mgt_ob_ch14'),
    path('view_october_account_details_ob_ch14/', branch14.view_october_account_details_ob_ch14, name='view_october_account_details_ob_ch14'),
    path('october_account_mgt_ob_ch14/<id>',branch14.october_account_mgt_ob_ch14,name='october_account_mgt_ob_ch14'),
    path('view_nov_account_details_ob_ch14/', branch14.view_nov_account_details_ob_ch14, name='view_nov_account_details_ob_ch14'),
    path('nov_account_mgt_ob_ch14/<id>',branch14.nov_account_mgt_ob_ch14,name='nov_account_mgt_ob_ch14'),
    path('view_dec_account_details_ob_ch14/', branch14.view_dec_account_details_ob_ch14, name='view_dec_account_details_ob_ch14'),
    path('dec_account_mgt_ob_ch14/<id>',branch14.dec_account_mgt_ob_ch14,name='dec_account_mgt_ob_ch14'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch14', admin_dashboard_calculations_br14.monthly_details_due_ob_ch14, name='monthly_details_due_ob_ch14'),
    path('monthly_collection_details_ob_ch14/', admin_dashboard_calculations_br14.monthly_collection_details_ob_ch14, name='monthly_collection_details_ob_ch14'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch14/',branch14.guest_all_ob_ch14,name='guest_all_ob_ch14'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************

#########################################################
###******CREATER MASTER START HERE
###################################################################################

##******************CATERGORY CREATER START HERE

    path('view_all_category14/', accounts14.view_all_category14, name='view_all_category14'),
    path('create_new_category14/', accounts14.create_new_category14, name='create_new_category14'),
    path('regi_new_category14/', accounts14.regi_new_category14, name='regi_new_category14'),
    path('update_category14/<id>',accounts14.update_category14,name='update_category14'),

    path('delete_category14/<id>', accounts14.delete_category14, name='delete_category14'),
    path('view_all_category_delete14/', accounts14.view_all_category_delete14, name='view_all_category_delete14'),

    ##*****************CATERY CREATER END HERE

##******************ITEM CREATER START HERE

    path('view_all_items14/', accounts14.view_all_items14, name='view_all_items14'),
    path('create_new_item14/', accounts14.create_new_item14, name='create_new_item14'),
    path('regi_new_item14/', accounts14.regi_new_item14, name='regi_new_item14'),
    path('delete_item14/<id>',accounts14.delete_item14,name='delete_item14'),
    path('update_item14/<id>', accounts14.update_item14, name='update_item14'),
    path('view_all_items_delete14/',accounts14.view_all_items_delete14,name='view_all_items_delete14'),

    ##*****************ITEM CREATER END HERE

##******************LEDGER CREATER START HERE

    path('view_all_ledger14/', accounts14.view_all_ledger14, name='view_all_ledger14'),
    path('create_new_ledger14/', accounts14.create_new_ledger14, name='create_new_ledger14'),
    path('regi_new_ledger14/', accounts14.regi_new_ledger14, name='regi_new_ledger14'),
    path('delete_ledger14/<id>',accounts14.delete_ledger14,name='delete_ledger14'),
    path('update_ledger14/<id>',accounts14.update_ledger14,name='update_ledger14'),
    path('view_all_ledger_delete14/',accounts14.view_all_ledger_delete14,name='view_all_ledger_delete14'),

##*****************LEDGER CREATER END HERE

##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book14/', accounts14.view_all_accounts_book14, name='view_all_accounts_book14'),
    path('create_new_accounts_book14/', accounts14.create_new_accounts_book14, name='create_new_accounts_book14'),
    path('regi_new_accounts_book14/', accounts14.regi_new_accounts_book14, name='regi_new_accounts_book14'),
    path('update_accounts_book14/<id>',accounts14.update_accounts_book14,name='update_accounts_book14'),
    path('delete_accounts_book14/<id>',accounts14.delete_accounts_book14,name='delete_accounts_book14'),
    path('view_all_accounts_book_delete14/',accounts14.view_all_accounts_book_delete14,name='view_all_accounts_book_delete14'),

##*****************ACCOUNTS_BOOK CREATER END HERE

#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries14/', accounts14.get_countries14, name='get_countries14'),

    path('in_exp_items_entry14/', accounts14.in_exp_items_entry14, name='in_exp_items_entry14'),
    path('reg_in_exp_items_entry14/', accounts14.reg_in_exp_items_entry14, name='reg_in_exp_items_entry14'),
    path('delete_journal14/<id>',accounts14.delete_journal14,name='delete_journal14'),
    path('update_in_exp_items_entry14/<id>',accounts14.update_in_exp_items_entry14,name='update_in_exp_items_entry14'),
    path('detailed_journal_report14/',accounts14.detailed_journal_report14,name='detailed_journal_report14'),
    path('journal_report_deleted14/',accounts14.journal_report_deleted14,name='journal_report_deleted14'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################

###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise14/', accounts14.daily_category_wise14, name='daily_category_wise14'),
    path('monthly_category_based_reports14/',accounts14.monthly_category_based_reports14,name='monthly_category_based_reports14'),
    path('yearly_category_based_reports14/', accounts14.yearly_category_based_reports14,name='yearly_category_based_reports14'),

###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed14/', accounts14.daily_detailed14, name='daily_detailed14'),
    path('monthly_detailed14/',accounts14.monthly_detailed14,name='monthly_detailed14'),
    path('yearly_detailed14/',accounts14.yearly_detailed14,name='yearly_detailed14'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports14/', accounts14.item_based_reports14, name='item_based_reports14'),
    path('daily_item_based_reports14/',accounts14.daily_item_based_reports14,name='daily_item_based_reports14'),
    path('monthly_item_based_reports14/',accounts14.monthly_item_based_reports14,name='monthly_item_based_reports14'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports14/', accounts14.ledger_based_reports14, name='ledger_based_reports14'),
    path('monthly_ledger_based_reports14/', accounts14.monthly_ledger_based_reports14, name='monthly_ledger_based_reports14'),
    path('daily_ledger_based_reports14/',accounts14.daily_ledger_based_reports14,name='daily_ledger_based_reports14'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports14/', accounts14.accounts_book_based_reports14, name='accounts_book_based_reports14'),
    path('daily_accounts_book_based_reports14/',accounts14.daily_accounts_book_based_reports14,name='daily_accounts_book_based_reports14'),
    path('monthly_accounts_book_based_reports14/',accounts14.monthly_accounts_book_based_reports14,name='monthly_accounts_book_based_reports14'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE


#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months14/', accounts14.monthly_reports_choose_months14, name='monthly_reports_choose_months14'),
    path('monthly_detailed_daily_in_exp_items_report14/<mo>',accounts14.monthly_detailed_daily_in_exp_items_report14,name='monthly_detailed_daily_in_exp_items_report14'),

    path('single_monthly_reports_choose_months14/', accounts14.single_monthly_reports_choose_months14,name='single_monthly_reports_choose_months14'),
    path('single_monthly_daily_in_exp_items_report14/<mo>',accounts14.single_monthly_daily_in_exp_items_report14,name='single_monthly_daily_in_exp_items_report14'),

    path('accounts_dash_board_ob_ch14/',accounts14.accounts_dash_board_ob_ch14,name='accounts_dash_board_ob_ch14'),

    path('profit_sharing_choose_months14', accounts14.profit_sharing_choose_months14,name='profit_sharing_choose_months14'),
    path('profit_sharing14/<mo>', accounts14.profit_sharing14, name='profit_sharing14'),
    path('view_share_holders14', accounts14.view_share_holders14, name='view_share_holders14'),
    path('create_share_holders14', accounts14.create_share_holders14, name='create_share_holders14'),
    path('regi_share_holders14', accounts14.regi_share_holders14, name='regi_share_holders14'),
    path('update_share_holders14/<id>', accounts14.update_share_holders14, name='update_share_holders14'),
    path('delete_share_holders14/<id>', accounts14.delete_share_holders14, name='delete_share_holders14'),
    path('view_deleted_share_holders14', accounts14.view_deleted_share_holders14, name='view_deleted_share_holders14'),

]

