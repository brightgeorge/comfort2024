from django.urls import path, include

from . import admin_branch17
from . import admin_branch17
from . import branch17
from . import reports17
from . import payment17
from . import admin_dashboard_calculations_br17
from . import accounts17

urlpatterns = [

    path('branch1_dashboard_ob_ch17/', branch17.branch1_dashboard_ob_ch17, name='branch1_dashboard_ob_ch17'),
    path('branch1_dashboard17/',branch17.branch1_dashboard17,name='branch1_dashboard17'),
    path('user_dashboard_calculations_ob_ch17/',branch17.user_dashboard_calculations_ob_ch17,name='user_dashboard_calculations_ob_ch17'),

    path('background_ob_ch17',branch17.background_ob_ch17,name='background_ob_ch17'),
    path('background_regi_ob_ch17',branch17.background_regi_ob_ch17,name='background_regi_ob_ch17'),
    path('custom_background_regi_ob_ch17',branch17.custom_background_regi_ob_ch17,name='custom_background_regi_ob_ch17'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch17/',admin_branch17.branch1_room_create_regi_ob_ch17,name='branch1_room_create_regi_ob_ch17'),
    path('view_all_room_ob_ch17/',admin_branch17.view_all_room_ob_ch17,name='view_all_room_ob_ch17'),
    path('delete_room_ob_ch17/<id>',admin_branch17.delete_room_ob_ch17,name='delete_room_ob_ch17'),

    path('branch1_room_create_ob_ch17/',admin_branch17.branch1_room_create_ob_ch17,name='branch1_room_create_ob_ch17'),

    path('multiple_branch1_room_create_regi17/',admin_branch17.multiple_branch1_room_create_regi17,name='multiple_branch1_room_create_regi17'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch17/', admin_branch17.pg1_bed_create_regi_ob_ch17, name='pg1_bed_create_regi_ob_ch17'),
    path('pg1_view_all_beds_ob_ch17/', admin_branch17.pg1_view_all_beds_ob_ch17, name='pg1_view_all_beds_ob_ch17'),
    path('delete_bed_ob_ch17/<id>', admin_branch17.delete_bed_ob_ch17, name='delete_bed_ob_ch17'),

    path('pg1_bed_create_ob_ch17/', admin_branch17.pg1_bed_create_ob_ch17, name='pg1_bed_create_ob_ch17'),

    path('single_pg1_bed_create_regi_ob_ch17/',admin_branch17.single_pg1_bed_create_regi_ob_ch17,name='single_pg1_bed_create_regi_ob_ch17'),
    path('update_bed_basic_details_ob_ch17/<id>',admin_branch17.update_bed_basic_details_ob_ch17, name='update_bed_basic_details_ob_ch17'),

    path('multiple_single_pg1_bed_create_regi17/',admin_branch17.multiple_single_pg1_bed_create_regi17,name='multiple_single_pg1_bed_create_regi17'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch17/<id>',branch17.br1_admit_guest_ob_ch17,name='br1_admit_guest_ob_ch17'),
    path('view_all_new_guest_ob_ch17/',branch17.view_all_new_guest_ob_ch17,name='view_all_new_guest_ob_ch17'),
    path('update_br1_admit_guest_ob_ch17/<id>',branch17.update_br1_admit_guest_ob_ch17,name='update_br1_admit_guest_ob_ch17'),
    path('vacate_br1_guest_ob_ch17/<id>',branch17.vacate_br1_guest_ob_ch17,name='vacate_br1_guest_ob_ch17'),

    path('active_guest_details_ob_ch17/<guest_code>',branch17.active_guest_details_ob_ch17,name='active_guest_details_ob_ch17'),
    path('view_all_guest_ob_ch17/',branch17.view_all_guest_ob_ch17,name='view_all_guest_ob_ch17'),
    path('shift_guest_ob_ch17/<id>',branch17.shift_guest_ob_ch17,name='shift_guest_ob_ch17'),
    path('shift_guest_regi_ob_ch17/',branch17.shift_guest_regi_ob_ch17,name='shift_guest_regi_ob_ch17'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch17/',branch17.update_all_rent_ob_ch17,name='update_all_rent_ob_ch17'),

    path('multiple_br1_admit_guest17/<id>',branch17.multiple_br1_admit_guest17,name='multiple_br1_admit_guest17'),

#guest end here


##################################
#_ADVANCE_ob_ch17 START HERE
################################


    path('choose_months_advance_ob_ch17/',branch17.choose_months_advance_ob_ch17,name='choose_months_advance_ob_ch17'),

    path('jan_advance_ob_ch17/', branch17.jan_advance_ob_ch17, name='jan_advance_ob_ch17'),
    path('jan_make_payments_advance_ob_ch17/<id>', branch17.jan_make_payments_advance_ob_ch17,name='jan_make_payments_advance_ob_ch17'),
    path('feb_advance_ob_ch17/', branch17.feb_advance_ob_ch17, name='feb_advance_ob_ch17'),
    path('feb_make_payments_advance_ob_ch17/<id>', branch17.feb_make_payments_advance_ob_ch17,name='feb_make_payments_advance_ob_ch17'),
    path('march_advance_ob_ch17/', branch17.march_advance_ob_ch17, name='march_advance_ob_ch17'),
    path('march_make_payments_advance_ob_ch17/<id>', branch17.march_make_payments_advance_ob_ch17,name='march_make_payments_advance_ob_ch17'),
    path('april_advance_ob_ch17/', branch17.april_advance_ob_ch17, name='april_advance_ob_ch17'),
    path('april_make_payments_advance_ob_ch17/<id>', branch17.april_make_payments_advance_ob_ch17, name='april_make_payments_advance_ob_ch17'),

    path('may_advance_ob_ch17/',branch17.may_advance_ob_ch17,name='may_advance_ob_ch17'),
    path('may_make_payments_advance_ob_ch17/<id>', branch17.may_make_payments_advance_ob_ch17, name='may_make_payments_advance_ob_ch17'),
    path('june_advance_ob_ch17/',branch17.june_advance_ob_ch17,name='june_advance_ob_ch17'),
    path('june_make_payments_advance_ob_ch17/<id>', branch17.june_make_payments_advance_ob_ch17, name='june_make_payments_advance_ob_ch17'),
    path('july_advance_ob_ch17/',branch17.july_advance_ob_ch17,name='july_advance_ob_ch17'),
    path('july_make_payments_advance_ob_ch17/<id>', branch17.july_make_payments_advance_ob_ch17, name='july_make_payments_advance_ob_ch17'),
    path('auguest_advance_ob_ch17/', branch17.auguest_advance_ob_ch17, name='auguest_advance_ob_ch17'),
    path('auguest_make_payments_advance_ob_ch17/<id>', branch17.auguest_make_payments_advance_ob_ch17, name='auguest_make_payments_advance_ob_ch17'),

    path('sept_advance_ob_ch17/', branch17.sept_advance_ob_ch17, name='sept_advance_ob_ch17'),
    path('sept_make_payments_advance_ob_ch17/<id>', branch17.sept_make_payments_advance_ob_ch17,name='sept_make_payments_advance_ob_ch17'),
    path('october_advance_ob_ch17/', branch17.october_advance_ob_ch17, name='october_advance_ob_ch17'),
    path('october_make_payments_advance_ob_ch17/<id>', branch17.october_make_payments_advance_ob_ch17, name='october_make_payments_advance_ob_ch17'),
    path('nov_advance_ob_ch17/', branch17.nov_advance_ob_ch17, name='nov_advance_ob_ch17'),
    path('nov_make_payments_advance_ob_ch17/<id>', branch17.nov_make_payments_advance_ob_ch17,name='nov_make_payments_advance_ob_ch17'),
    path('dec_advance_ob_ch17/', branch17.dec_advance_ob_ch17, name='dec_advance_ob_ch17'),
    path('dec_make_payments_advance_ob_ch17/<id>', branch17.dec_make_payments_advance_ob_ch17, name='dec_make_payments_advance_ob_ch17'),



##################################
#_ADVANCE_ob_ch17 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch17/',branch17.choose_months_ob_ch17,name='choose_months_ob_ch17'),

    path('jan_ob_ch17/',branch17.jan_ob_ch17,name='jan_ob_ch17'),
    path('jan_manke_payments_ob_ch17/<id>',branch17.jan_manke_payments_ob_ch17,name='jan_manke_payments_ob_ch17'),

    path('feb_ob_ch17/',branch17.feb_ob_ch17,name='feb_ob_ch17'),
    path('feb_manke_payments_ob_ch17/<id>',branch17.feb_manke_payments_ob_ch17,name='feb_manke_payments_ob_ch17'),

    path('march_ob_ch17/',branch17.march_ob_ch17,name='march_ob_ch17'),
    path('march_manke_payments_ob_ch17/<id>',branch17.march_manke_payments_ob_ch17,name='march_manke_payments_ob_ch17'),

    path('april_ob_ch17/',branch17.april_ob_ch17,name='april_ob_ch17'),
    path('april_make_payments_ob_ch17/<id>',branch17.april_make_payments_ob_ch17,name='april_make_payments_ob_ch17'),

    path('may_ob_ch17/',branch17.may_ob_ch17,name='may_ob_ch17'),
    path('may_make_payments_ob_ch17/<id>',branch17.may_make_payments_ob_ch17,name='may_make_payments_ob_ch17'),

    path('june_ob_ch17/',branch17.june_ob_ch17,name='june_ob_ch17'),
    path('june_make_payments_ob_ch17/<id>',branch17.june_make_payments_ob_ch17,name='june_make_payments_ob_ch17'),

    path('july_ob_ch17/',branch17.july_ob_ch17,name='july_ob_ch17'),
    path('july_make_payments_ob_ch17/<id>',branch17.july_make_payments_ob_ch17,name='july_make_payments_ob_ch17'),

    path('aug_ob_ch17/',branch17.aug_ob_ch17,name='aug_ob_ch17'),
    path('aug_make_payments_ob_ch17/<id>',branch17.aug_make_payments_ob_ch17,name='aug_make_payments_ob_ch17'),

    path('sept_ob_ch17/',branch17.sept_ob_ch17,name='sept_ob_ch17'),
    path('sept_make_payments_ob_ch17/<id>',branch17.sept_make_payments_ob_ch17,name='sept_make_payments_ob_ch17'),

    path('oct_ob_ch17/',branch17.oct_ob_ch17,name='oct_ob_ch17'),
    path('oct_make_payments_ob_ch17/<id>',branch17.oct_make_payments_ob_ch17,name='oct_make_payments_ob_ch17'),

    path('nov_ob_ch17/',branch17.nov_ob_ch17,name='nov_ob_ch17'),
    path('nov_make_payments_ob_ch17/<id>',branch17.nov_make_payments_ob_ch17,name='nov_make_payments_ob_ch17'),

    path('dec_ob_ch17/',branch17.dec_ob_ch17,name='dec_ob_ch17'),
    path('dec_make_payments_ob_ch17/<id>',branch17.dec_make_payments_ob_ch17,name='dec_make_payments_ob_ch17'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch17/', payment17.choose_user_ob_ch17, name='choose_user_ob_ch17'),
    path('payment_user_details_ob_ch17/<id>', payment17.payment_user_details_ob_ch17, name='payment_user_details_ob_ch17'),
    path('close_choose_user_ob_ch17/<id>',payment17.close_choose_user_ob_ch17,name='close_choose_user_ob_ch17'),

    path('monthly_jan_make_payments_ob_ch17/<id>', payment17.monthly_jan_make_payments_ob_ch17, name='monthly_jan_make_payments_ob_ch17'),
    path('monthly_feb_make_payments_ob_ch17/<id>', payment17.monthly_feb_make_payments_ob_ch17, name='monthly_feb_make_payments_ob_ch17'),
    path('monthly_march_make_payments_ob_ch17/<id>', payment17.monthly_march_make_payments_ob_ch17, name='monthly_march_make_payments_ob_ch17'),
    path('monthly_april_make_payments_ob_ch17/<id>', payment17.monthly_april_make_payments_ob_ch17, name='monthly_april_make_payments_ob_ch17'),
    path('monthly_may_make_payments_ob_ch17/<id>', payment17.monthly_may_make_payments_ob_ch17, name='monthly_may_make_payments_ob_ch17'),
    path('monthly_june_make_payments_ob_ch17/<id>', payment17.monthly_june_make_payments_ob_ch17, name='monthly_june_make_payments_ob_ch17'),

    path('monthly_july_make_payments_ob_ch17/<id>', payment17.monthly_july_make_payments_ob_ch17, name='monthly_july_make_payments_ob_ch17'),
    path('monthly_aug_make_payments_ob_ch17/<id>', payment17.monthly_aug_make_payments_ob_ch17, name='monthly_aug_make_payments_ob_ch17'),
    path('monthly_sept_make_payments_ob_ch17/<id>', payment17.monthly_sept_make_payments_ob_ch17, name='monthly_sept_make_payments_ob_ch17'),
    path('monthly_oct_make_payments_ob_ch17/<id>', payment17.monthly_oct_make_payments_ob_ch17, name='monthly_oct_make_payments_ob_ch17'),
    path('monthly_nov_make_payments_ob_ch17/<id>', payment17.monthly_nov_make_payments_ob_ch17, name='monthly_nov_make_payments_ob_ch17'),
    path('monthly_dec_make_payments_ob_ch17/<id>', payment17.monthly_dec_make_payments_ob_ch17, name='monthly_dec_make_payments_ob_ch17'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch17/',branch17.unpaid_rent_choose_months_ob_ch17,name='unpaid_rent_choose_months_ob_ch17'),

    path('jan_unpaid_rent_ob_ch17/', branch17.jan_unpaid_rent_ob_ch17, name='jan_unpaid_rent_ob_ch17'),
    path('table_jan_unpaid_rent_ob_ch17/', branch17.table_jan_unpaid_rent_ob_ch17, name='table_jan_unpaid_rent_ob_ch17'),
    path('feb_unpaid_rent_ob_ch17/', branch17.feb_unpaid_rent_ob_ch17, name='feb_unpaid_rent_ob_ch17'),
    path('table_feb_unpaid_rent_ob_ch17/', branch17.table_feb_unpaid_rent_ob_ch17, name='table_feb_unpaid_rent_ob_ch17'),
    path('mar_unpaid_rent_ob_ch17/', branch17.mar_unpaid_rent_ob_ch17, name='mar_unpaid_rent_ob_ch17'),
    path('table_mar_unpaid_rent_ob_ch17/', branch17.table_mar_unpaid_rent_ob_ch17, name='table_mar_unpaid_rent_ob_ch17'),
    path('april_unpaid_rent_ob_ch17/', branch17.april_unpaid_rent_ob_ch17, name='april_unpaid_rent_ob_ch17'),
    path('table_april_unpaid_rent_ob_ch17/', branch17.table_april_unpaid_rent_ob_ch17, name='table_april_unpaid_rent_ob_ch17'),

    path('may_unpaid_rent_ob_ch17/', branch17.may_unpaid_rent_ob_ch17, name='may_unpaid_rent_ob_ch17'),
    path('table_may_unpaid_rent_ob_ch17/', branch17.table_may_unpaid_rent_ob_ch17, name='table_may_unpaid_rent_ob_ch17'),
    path('june_unpaid_rent_ob_ch17/', branch17.june_unpaid_rent_ob_ch17, name='june_unpaid_rent_ob_ch17'),
    path('table_june_unpaid_rent_ob_ch17/', branch17.table_june_unpaid_rent_ob_ch17, name='table_june_unpaid_rent_ob_ch17'),
    path('july_unpaid_rent_ob_ch17/', branch17.july_unpaid_rent_ob_ch17, name='july_unpaid_rent_ob_ch17'),
    path('table_july_unpaid_rent_ob_ch17',branch17.table_july_unpaid_rent_ob_ch17,name='table_july_unpaid_rent_ob_ch17'),
    path('aug_unpaid_rent_ob_ch17/', branch17.aug_unpaid_rent_ob_ch17, name='aug_unpaid_rent_ob_ch17'),
    path('table_aug_unpaid_rent_ob_ch17/',branch17.table_aug_unpaid_rent_ob_ch17,name='table_aug_unpaid_rent_ob_ch17'),

    path('sept_unpaid_rent_ob_ch17/', branch17.sept_unpaid_rent_ob_ch17, name='sept_unpaid_rent_ob_ch17'),
    path('table_sept_unpaid_rent_ob_ch17/', branch17.table_sept_unpaid_rent_ob_ch17, name='table_sept_unpaid_rent_ob_ch17'),
    path('oct_unpaid_rent_ob_ch17/', branch17.oct_unpaid_rent_ob_ch17, name='oct_unpaid_rent_ob_ch17'),
    path('table_oct_unpaid_rent_ob_ch17/', branch17.table_oct_unpaid_rent_ob_ch17, name='table_oct_unpaid_rent_ob_ch17'),
    path('nov_unpaid_rent_ob_ch17/', branch17.nov_unpaid_rent_ob_ch17, name='nov_unpaid_rent_ob_ch17'),
    path('table_nov_unpaid_rent_ob_ch17/', branch17.table_nov_unpaid_rent_ob_ch17, name='table_nov_unpaid_rent_ob_ch17'),
    path('dec_unpaid_rent_ob_ch17/', branch17.dec_unpaid_rent_ob_ch17, name='dec_unpaid_rent_ob_ch17'),
    path('table_dec_unpaid_rent_ob_ch17/', branch17.table_dec_unpaid_rent_ob_ch17, name='table_dec_unpaid_rent_ob_ch17'),

    path('details_of_unpaid_guests_ob_ch17/<id>',branch17.details_of_unpaid_guests_ob_ch17,name='details_of_unpaid_guests_ob_ch17'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch17/',branch17.paid_rent_choose_months_ob_ch17,name='paid_rent_choose_months_ob_ch17'),
    path('partially_paid_guest_choose_months_ob_ch17/',reports17.partially_paid_guest_choose_months_ob_ch17,name='partially_paid_guest_choose_months_ob_ch17'),

    path('jan_paid_rent_ob_ch17/', branch17.jan_paid_rent_ob_ch17, name='jan_paid_rent_ob_ch17'),
    path('table_jan_paid_rent_ob_ch17/', branch17.table_jan_paid_rent_ob_ch17, name='table_jan_paid_rent_ob_ch17'),
    path('jan_full_paid_guest_ob_ch17/', reports17.jan_full_paid_guest_ob_ch17, name='jan_full_paid_guest_ob_ch17'),
    path('jan_partially_paid_guest_ob_ch17/', reports17.jan_partially_paid_guest_ob_ch17, name='jan_partially_paid_guest_ob_ch17'),
    path('table_jan_partially_paid_guest_ob_ch17/', reports17.table_jan_partially_paid_guest_ob_ch17,name='table_jan_partially_paid_guest_ob_ch17'),

    path('feb_paid_rent_ob_ch17/', branch17.feb_paid_rent_ob_ch17, name='feb_paid_rent_ob_ch17'),
    path('table_feb_paid_rent_ob_ch17/', branch17.table_feb_paid_rent_ob_ch17, name='table_feb_paid_rent_ob_ch17'),
    path('feb_full_paid_guest_ob_ch17/', reports17.feb_full_paid_guest_ob_ch17, name='feb_full_paid_guest_ob_ch17'),
    path('feb_partially_paid_guest_ob_ch17/', reports17.feb_partially_paid_guest_ob_ch17, name='feb_partially_paid_guest_ob_ch17'),
    path('table_feb_partially_paid_guest_ob_ch17/', reports17.table_feb_partially_paid_guest_ob_ch17,name='table_feb_partially_paid_guest_ob_ch17'),

    path('mar_paid_rent_ob_ch17/', branch17.mar_paid_rent_ob_ch17, name='mar_paid_rent_ob_ch17'),
    path('table_mar_paid_rent_ob_ch17/', branch17.table_mar_paid_rent_ob_ch17, name='table_mar_paid_rent_ob_ch17'),
    path('march_full_paid_guest_ob_ch17/', reports17.march_full_paid_guest_ob_ch17, name='march_full_paid_guest_ob_ch17'),
    path('march_partially_paid_guest_ob_ch17/', reports17.march_partially_paid_guest_ob_ch17, name='march_partially_paid_guest_ob_ch17'),
    path('table_march_partially_paid_guest_ob_ch17/', reports17.table_march_partially_paid_guest_ob_ch17,name='table_march_partially_paid_guest_ob_ch17'),

    path('april_paid_rent_ob_ch17/', branch17.april_paid_rent_ob_ch17, name='april_paid_rent_ob_ch17'),
    path('table_april_paid_rent_ob_ch17/', branch17.table_april_paid_rent_ob_ch17, name='table_april_paid_rent_ob_ch17'),
    path('april_full_paid_guest_ob_ch17/', reports17.april_full_paid_guest_ob_ch17, name='april_full_paid_guest_ob_ch17'),
    path('april_partially_paid_guest_ob_ch17/', reports17.april_partially_paid_guest_ob_ch17, name='april_partially_paid_guest_ob_ch17'),
    path('table_april_partially_paid_guest_ob_ch17/', reports17.table_april_partially_paid_guest_ob_ch17,name='table_april_partially_paid_guest_ob_ch17'),

    path('may_paid_rent_ob_ch17/', branch17.may_paid_rent_ob_ch17, name='may_paid_rent_ob_ch17'),
    path('table_may_paid_rent_ob_ch17/', branch17.table_may_paid_rent_ob_ch17, name='table_may_paid_rent_ob_ch17'),
    path('may_full_paid_guest_ob_ch17/', reports17.may_full_paid_guest_ob_ch17, name='may_full_paid_guest_ob_ch17'),
    path('may_partially_paid_guest_ob_ch17/', reports17.may_partially_paid_guest_ob_ch17, name='may_partially_paid_guest_ob_ch17'),
    path('table_may_partially_paid_guest_ob_ch17/', reports17.table_may_partially_paid_guest_ob_ch17, name='table_may_partially_paid_guest_ob_ch17'),

    path('june_paid_rent_ob_ch17/', branch17.june_paid_rent_ob_ch17, name='june_paid_rent_ob_ch17'),
    path('table_june_paid_rent_ob_ch17/', branch17.table_june_paid_rent_ob_ch17, name='table_june_paid_rent_ob_ch17'),
    path('june_full_paid_guest_ob_ch17/', reports17.june_full_paid_guest_ob_ch17, name='june_full_paid_guest_ob_ch17'),
    path('june_partially_paid_guest_ob_ch17/', reports17.june_partially_paid_guest_ob_ch17, name='june_partially_paid_guest_ob_ch17'),
    path('table_june_partially_paid_guest_ob_ch17/', reports17.table_june_partially_paid_guest_ob_ch17, name='table_june_partially_paid_guest_ob_ch17'),

    path('july_paid_rent_ob_ch17/', branch17.july_paid_rent_ob_ch17, name='july_paid_rent_ob_ch17'),
    path('table_july_paid_rent_ob_ch17/', branch17.table_july_paid_rent_ob_ch17, name='table_july_paid_rent_ob_ch17'),
    path('july_full_paid_guest_ob_ch17/', reports17.july_full_paid_guest_ob_ch17, name='july_full_paid_guest_ob_ch17'),
    path('july_partially_paid_guest_ob_ch17/', reports17.july_partially_paid_guest_ob_ch17, name='july_partially_paid_guest_ob_ch17'),
    path('table_july_partially_paid_guest_ob_ch17/', reports17.table_july_partially_paid_guest_ob_ch17, name='table_july_partially_paid_guest_ob_ch17'),

    path('aug_paid_rent_ob_ch17/', branch17.aug_paid_rent_ob_ch17, name='aug_paid_rent_ob_ch17'),
    path('table_aug_paid_rent_ob_ch17/', branch17.table_aug_paid_rent_ob_ch17, name='table_aug_paid_rent_ob_ch17'),
    path('auguest_full_paid_guest_ob_ch17/', reports17.auguest_full_paid_guest_ob_ch17, name='auguest_full_paid_guest_ob_ch17'),
    path('auguest_partially_paid_guest_ob_ch17/', reports17.auguest_partially_paid_guest_ob_ch17,name='auguest_partially_paid_guest_ob_ch17'),
    path('table_auguest_partially_paid_guest_ob_ch17/', reports17.table_auguest_partially_paid_guest_ob_ch17,name='table_auguest_partially_paid_guest_ob_ch17'),

    path('sept_paid_rent_ob_ch17/', branch17.sept_paid_rent_ob_ch17, name='sept_paid_rent_ob_ch17'),
    path('table_sept_paid_rent_ob_ch17/', branch17.table_sept_paid_rent_ob_ch17, name='table_sept_paid_rent_ob_ch17'),
    path('sept_full_paid_guest_ob_ch17/', reports17.sept_full_paid_guest_ob_ch17, name='sept_full_paid_guest_ob_ch17'),
    path('sept_partially_paid_guest_ob_ch17/', reports17.sept_partially_paid_guest_ob_ch17, name='sept_partially_paid_guest_ob_ch17'),
    path('table_sept_partially_paid_guest_ob_ch17/', reports17.table_sept_partially_paid_guest_ob_ch17,name='table_sept_partially_paid_guest_ob_ch17'),

    path('oct_paid_rent_ob_ch17/', branch17.oct_paid_rent_ob_ch17, name='oct_paid_rent_ob_ch17'),
    path('table_oct_paid_rent_ob_ch17/', branch17.table_oct_paid_rent_ob_ch17, name='table_oct_paid_rent_ob_ch17'),
    path('october_full_paid_guest_ob_ch17/', reports17.october_full_paid_guest_ob_ch17, name='october_full_paid_guest_ob_ch17'),
    path('october_partially_paid_guest_ob_ch17/', reports17.october_partially_paid_guest_ob_ch17,name='october_partially_paid_guest_ob_ch17'),
    path('table_october_partially_paid_guest_ob_ch17/', reports17.table_october_partially_paid_guest_ob_ch17,name='table_october_partially_paid_guest_ob_ch17'),

    path('nov_paid_rent_ob_ch17/', branch17.nov_paid_rent_ob_ch17, name='nov_paid_rent_ob_ch17'),
    path('table_nov_paid_rent_ob_ch17/', branch17.table_nov_paid_rent_ob_ch17, name='table_nov_paid_rent_ob_ch17'),
    path('nov_full_paid_guest_ob_ch17/', reports17.nov_full_paid_guest_ob_ch17, name='nov_full_paid_guest_ob_ch17'),
    path('nov_partially_paid_guest_ob_ch17/', reports17.nov_partially_paid_guest_ob_ch17, name='nov_partially_paid_guest_ob_ch17'),
    path('table_nov_partially_paid_guest_ob_ch17/', reports17.table_nov_partially_paid_guest_ob_ch17,name='table_nov_partially_paid_guest_ob_ch17'),

    path('dec_paid_rent_ob_ch17/', branch17.dec_paid_rent_ob_ch17, name='dec_paid_rent_ob_ch17'),
    path('table_dec_paid_rent_ob_ch17/', branch17.table_dec_paid_rent_ob_ch17, name='table_dec_paid_rent_ob_ch17'),
    path('dec_full_paid_guest_ob_ch17/', reports17.dec_full_paid_guest_ob_ch17, name='dec_full_paid_guest_ob_ch17'),
    path('dec_partially_paid_guest_ob_ch17/', reports17.dec_partially_paid_guest_ob_ch17, name='dec_partially_paid_guest_ob_ch17'),
    path('table_dec_partially_paid_guest_ob_ch17/', reports17.table_dec_partially_paid_guest_ob_ch17,name='table_dec_partially_paid_guest_ob_ch17'),

    path('details_of_paid_guests_ob_ch17/<id>',branch17.details_of_paid_guests_ob_ch17,name='details_of_paid_guests_ob_ch17'),
    path('full_paid_guest_ob_ch17/',reports17.full_paid_guest_ob_ch17,name='full_paid_guest_ob_ch17'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch17/',branch17.viewall_vacate_guest_ob_ch17,name='viewall_vacate_guest_ob_ch17'),
    path('details_of_vacate_guest_ob_ch17/<id>',branch17.details_of_vacate_guest_ob_ch17,name='details_of_vacate_guest_ob_ch17'),
    path('full_vacated_guest_details_ob_ch17',branch17.full_vacated_guest_details_ob_ch17,name='full_vacated_guest_details_ob_ch17'),
    path('full_vacated_guest_table_ob_ch17',branch17.full_vacated_guest_table_ob_ch17,name='full_vacated_guest_table_ob_ch17'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch17/<id>', branch17.jan_manke_payments_vacate_ob_ch17, name='jan_manke_payments_vacate_ob_ch17'),
    path('feb_manke_payments_vacate_ob_ch17/<id>', branch17.feb_manke_payments_vacate_ob_ch17, name='feb_manke_payments_vacate_ob_ch17'),
    path('march_manke_payments_vacate_ob_ch17/<id>', branch17.march_manke_payments_vacate_ob_ch17, name='march_manke_payments_vacate_ob_ch17'),
    path('april_make_payments_vacate_ob_ch17/<id>', branch17.april_make_payments_vacate_ob_ch17, name='april_make_payments_vacate_ob_ch17'),

    path('may_make_payments_vacate_ob_ch17/<id>', branch17.may_make_payments_vacate_ob_ch17, name='may_make_payments_vacate_ob_ch17'),
    path('june_make_payments_vacate_ob_ch17/<id>', branch17.june_make_payments_vacate_ob_ch17, name='june_make_payments_vacate_ob_ch17'),
    path('july_make_payments_vacate_ob_ch17/<id>', branch17.july_make_payments_vacate_ob_ch17, name='july_make_payments_vacate_ob_ch17'),
    path('aug_make_payments_vacate_ob_ch17/<id>', branch17.aug_make_payments_vacate_ob_ch17, name='aug_make_payments_vacate_ob_ch17'),

    path('sept_make_payments_vacate_ob_ch17/<id>', branch17.sept_make_payments_vacate_ob_ch17, name='sept_make_payments_vacate_ob_ch17'),
    path('oct_make_payments_vacate_ob_ch17/<id>', branch17.oct_make_payments_vacate_ob_ch17, name='oct_make_payments_vacate_ob_ch17'),
    path('nov_make_payments_vacate_ob_ch17/<id>', branch17.nov_make_payments_vacate_ob_ch17, name='nov_make_payments_vacate_ob_ch17'),
    path('dec_make_payments_vacate_ob_ch17/<id>', branch17.dec_make_payments_vacate_ob_ch17, name='dec_make_payments_vacate_ob_ch17'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch17/',branch17.detail_guest_general_ob_ch17,name='detail_guest_general_ob_ch17'),

    path('jan_print_ob_ch17/',branch17.jan_print_ob_ch17,name='jan_print_ob_ch17'),
    path('feb_print_ob_ch17/',branch17.feb_print_ob_ch17,name='feb_print_ob_ch17'),
    path('march_print_ob_ch17/',branch17.march_print_ob_ch17,name='march_print_ob_ch17'),
    path('april_print_ob_ch17/',branch17.april_print_ob_ch17,name='april_print_ob_ch17'),

    path('may_print_ob_ch17/',branch17.may_print_ob_ch17,name='may_print_ob_ch17'),
    path('june_print_ob_ch17/',branch17.june_print_ob_ch17,name='june_print_ob_ch17'),
    path('july_print_ob_ch17/', branch17.july_print_ob_ch17, name='july_print_ob_ch17'),
    path('aug_print_ob_ch17/', branch17.aug_print_ob_ch17, name='aug_print_ob_ch17'),

    path('sept_print_ob_ch17/', branch17.sept_print_ob_ch17, name='sept_print_ob_ch17'),
    path('oct_print_ob_ch17/', branch17.oct_print_ob_ch17, name='oct_print_ob_ch17'),
    path('nov_print_ob_ch17/', branch17.nov_print_ob_ch17, name='nov_print_ob_ch17'),
    path('dec_print_ob_ch17/', branch17.dec_print_ob_ch17, name='dec_print_ob_ch17'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch17/', branch17.jan_close_ob_ch17, name='jan_close_ob_ch17'),
    path('jan_close_decision_page_ob_ch17/', branch17.jan_close_decision_page_ob_ch17, name='jan_close_decision_page_ob_ch17'),
    path('feb_close/', branch17.feb_close_ob_ch17, name='feb_close_ob_ch17'),
    path('feb_close_decision_page_ob_ch17/', branch17.feb_close_decision_page_ob_ch17, name='feb_close_decision_page_ob_ch17'),
    path('mar_close_ob_ch17/', branch17.mar_close_ob_ch17, name='mar_close_ob_ch17'),
    path('mar_close_decision_page/', branch17.mar_close_decision_page_ob_ch17, name='mar_close_decision_page_ob_ch17'),
    path('apr_close_ob_ch17/', branch17.apr_close_ob_ch17, name='apr_close_ob_ch17'),
    path('apr_close_decision_page_ob_ch17/', branch17.apr_close_decision_page_ob_ch17, name='apr_close_decision_page_ob_ch17'),

    path('may_close_ob_ch17/', branch17.may_close_ob_ch17, name='may_close_ob_ch17'),
    path('may_close_decision_page_ob_ch17/', branch17.may_close_decision_page_ob_ch17, name='may_close_decision_page_ob_ch17'),
    path('jun_close_ob_ch17/', branch17.jun_close_ob_ch17, name='jun_close_ob_ch17'),
    path('jun_close_decision_page_ob_ch17/', branch17.jun_close_decision_page_ob_ch17, name='jun_close_decision_page_ob_ch17'),
    path('jul_close_ob_ch17/', branch17.jul_close_ob_ch17, name='jul_close_ob_ch17'),
    path('jul_close_decision_page_ob_ch17/', branch17.jul_close_decision_page_ob_ch17, name='jul_close_decision_page_ob_ch17'),
    path('aug_close_ob_ch17/', branch17.aug_close_ob_ch17, name='aug_close_ob_ch17'),
    path('aug_close_decision_page_ob_ch17/', branch17.aug_close_decision_page_ob_ch17, name='aug_close_decision_page_ob_ch17'),

    path('sep_close_ob_ch17/', branch17.sep_close_ob_ch17, name='sep_close_ob_ch17'),
    path('sep_close_decision_page_ob_ch17/', branch17.sep_close_decision_page_ob_ch17, name='sep_close_decision_page_ob_ch17'),
    path('oct_close_ob_ch17/', branch17.oct_close_ob_ch17, name='oct_close_ob_ch17'),
    path('oct_close_decision_page_ob_ch17/', branch17.oct_close_decision_page_ob_ch17, name='oct_close_decision_page_ob_ch17'),
    path('nov_close_ob_ch17/', branch17.nov_close_ob_ch17, name='nov_close_ob_ch17'),
    path('nov_close_decision_page_ob_ch17/', branch17.nov_close_decision_page_ob_ch17, name='nov_close_decision_page_ob_ch17'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch17/',reports17.detailed_report_choose_months_ob_ch17,name='detailed_report_choose_months_ob_ch17'),

    path('jan_details_live_ob_ch17/', reports17.jan_details_live_ob_ch17, name='jan_details_live_ob_ch17'),
    path('jan_print_live_ob_ch17/', reports17.jan_print_live_ob_ch17, name='jan_print_live_ob_ch17'),
    path('feb_details_live_ob_ch17/', reports17.feb_details_live_ob_ch17, name='feb_details_live_ob_ch17'),
    path('feb_print_live_ob_ch17/', reports17.feb_print_live_ob_ch17, name='feb_print_live_ob_ch17'),
    path('march_details_live_ob_ch17/', reports17.march_details_live_ob_ch17, name='march_details_live_ob_ch17'),
    path('march_print_live_ob_ch17/', reports17.march_print_live_ob_ch17, name='march_print_live_ob_ch17'),

    path('april_details_live_ob_ch17/', reports17.april_details_live_ob_ch17, name='april_details_live_ob_ch17'),
    path('april_print_live_ob_ch17/', reports17.april_print_live_ob_ch17, name='april_print_live_ob_ch17'),
    path('may_details_live_ob_ch17/', reports17.may_details_live_ob_ch17, name='may_details_live_ob_ch17'),
    path('may_print_live_ob_ch17/', reports17.may_print_live_ob_ch17, name='may_print_live_ob_ch17'),
    path('june_details_live_ob_ch17/',reports17.june_details_live_ob_ch17,name='june_details_live_ob_ch17'),
    path('june_print_live_ob_ch17/', reports17.june_print_live_ob_ch17, name='june_print_live_ob_ch17'),

    path('july_details_live_ob_ch17/', reports17.july_details_live_ob_ch17, name='july_details_live_ob_ch17'),
    path('july_print_live_ob_ch17/', reports17.july_print_live_ob_ch17, name='july_print_live_ob_ch17'),
    path('auguest_details_live_ob_ch17/', reports17.auguest_details_live_ob_ch17, name='auguest_details_live_ob_ch17'),
    path('auguest_print_live_ob_ch17/', reports17.auguest_print_live_ob_ch17, name='auguest_print_live_ob_ch17'),
    path('sept_details_live_ob_ch17/', reports17.sept_details_live_ob_ch17, name='sept_details_live_ob_ch17'),
    path('sept_print_live_ob_ch17/', reports17.sept_print_live_ob_ch17, name='sept_print_live_ob_ch17'),

    path('october_details_live_ob_ch17/', reports17.october_details_live_ob_ch17, name='october_details_live_ob_ch17'),
    path('october_print_live_ob_ch17/', reports17.october_print_live_ob_ch17, name='october_print_live_ob_ch17'),
    path('nov_details_live_ob_ch17/', reports17.nov_details_live_ob_ch17, name='nov_details_live_ob_ch17'),
    path('nov_print_live_ob_ch17/', reports17.nov_print_live_ob_ch17, name='nov_print_live_ob_ch17'),
    path('dec_details_live_ob_ch17/', reports17.dec_details_live_ob_ch17, name='dec_details_live_ob_ch17'),
    path('dec_print_live_ob_ch17/', reports17.dec_print_live_ob_ch17, name='dec_print_live_ob_ch17'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch17/', reports17.viewall_vaccant_room_ob_ch17, name='viewall_vaccant_room_ob_ch17'),

    path('d_ob_ch17/', branch17.dynamic, name='dynamic'),

    path('manage_bed_ob_ch17/', branch17.manage_bed_ob_ch17, name='manage_bed_ob_ch17'),
    path('manage_new_guest_ob_ch17/', branch17.manage_new_guest_ob_ch17, name='manage_new_guest_ob_ch17'),
    path('manage_update_new_guest_ob_ch17/<id>', branch17.manage_update_new_guest_ob_ch17, name='manage_update_new_guest_ob_ch17'),
    path('manage_update_beds_ob_ch17/<id>', branch17.manage_update_beds_ob_ch17, name='manage_update_beds_ob_ch17'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch17/', branch17.view_all_due_amt_ob_ch17, name='view_all_due_amt_ob_ch17'),
    path('due_amt_mgt_choose_months_ob_ch17/', branch17.due_amt_mgt_choose_months_ob_ch17, name='due_amt_mgt_choose_months_ob_ch17'),

    path('view_jan_account_details_ob_ch17/', branch17.view_jan_account_details_ob_ch17, name='view_jan_account_details_ob_ch17'),
    path('jan_account_mgt_ob_ch17/<id>',branch17.jan_account_mgt_ob_ch17,name='jan_account_mgt_ob_ch17'),
    path('view_feb_account_details_ob_ch17/', branch17.view_feb_account_details_ob_ch17, name='view_feb_account_details_ob_ch17'),
    path('feb_account_mgt_ob_ch17/<id>',branch17.feb_account_mgt_ob_ch17,name='feb_account_mgt_ob_ch17'),
    path('view_march_account_details_ob_ch17/', branch17.view_march_account_details_ob_ch17, name='view_march_account_details_ob_ch17'),
    path('march_account_mgt_ob_ch17/<id>',branch17.march_account_mgt_ob_ch17,name='march_account_mgt_ob_ch17'),
    path('view_april_account_details_ob_ch17/', branch17.view_april_account_details_ob_ch17, name='view_april_account_details_ob_ch17'),
    path('april_account_mgt_ob_ch17/<id>',branch17.april_account_mgt_ob_ch17,name='april_account_mgt_ob_ch17'),

    path('view_may_account_details_ob_ch17/',branch17.view_may_account_details_ob_ch17,name='view_may_account_details_ob_ch17'),
    path('may_account_mgt_ob_ch17/<id>', branch17.may_account_mgt_ob_ch17, name='may_account_mgt_ob_ch17'),
    path('view_june_account_details_ob_ch17/', branch17.view_june_account_details_ob_ch17, name='view_june_account_details_ob_ch17'),
    path('june_account_mgt_ob_ch17/<id>',branch17.june_account_mgt_ob_ch17,name='june_account_mgt_ob_ch17'),
    path('view_july_account_details_ob_ch17/', branch17.view_july_account_details_ob_ch17, name='view_july_account_details_ob_ch17'),
    path('july_account_mgt_ob_ch17/<id>',branch17.july_account_mgt_ob_ch17,name='july_account_mgt_ob_ch17'),
    path('view_auguest_account_details_ob_ch17/', branch17.view_auguest_account_details_ob_ch17, name='view_auguest_account_details_ob_ch17'),
    path('auguest_account_mgt_ob_ch17/<id>',branch17.auguest_account_mgt_ob_ch17,name='auguest_account_mgt_ob_ch17'),

    path('view_sept_account_details_ob_ch17/', branch17.view_sept_account_details_ob_ch17, name='view_sept_account_details_ob_ch17'),
    path('sept_account_mgt_ob_ch17/<id>',branch17.sept_account_mgt_ob_ch17,name='sept_account_mgt_ob_ch17'),
    path('view_october_account_details_ob_ch17/', branch17.view_october_account_details_ob_ch17, name='view_october_account_details_ob_ch17'),
    path('october_account_mgt_ob_ch17/<id>',branch17.october_account_mgt_ob_ch17,name='october_account_mgt_ob_ch17'),
    path('view_nov_account_details_ob_ch17/', branch17.view_nov_account_details_ob_ch17, name='view_nov_account_details_ob_ch17'),
    path('nov_account_mgt_ob_ch17/<id>',branch17.nov_account_mgt_ob_ch17,name='nov_account_mgt_ob_ch17'),
    path('view_dec_account_details_ob_ch17/', branch17.view_dec_account_details_ob_ch17, name='view_dec_account_details_ob_ch17'),
    path('dec_account_mgt_ob_ch17/<id>',branch17.dec_account_mgt_ob_ch17,name='dec_account_mgt_ob_ch17'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch17', admin_dashboard_calculations_br17.monthly_details_due_ob_ch17, name='monthly_details_due_ob_ch17'),
    path('monthly_collection_details_ob_ch17/', admin_dashboard_calculations_br17.monthly_collection_details_ob_ch17, name='monthly_collection_details_ob_ch17'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch17/',branch17.guest_all_ob_ch17,name='guest_all_ob_ch17'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category17/', accounts17.view_all_category17, name='view_all_category17'),
    path('create_new_category17/', accounts17.create_new_category17, name='create_new_category17'),
    path('regi_new_category17/', accounts17.regi_new_category17, name='regi_new_category17'),
    path('update_category17/<id>',accounts17.update_category17,name='update_category17'),

    path('delete_category17/<id>', accounts17.delete_category17, name='delete_category17'),
    path('view_all_category_delete17/', accounts17.view_all_category_delete17, name='view_all_category_delete17'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items17/', accounts17.view_all_items17, name='view_all_items17'),
    path('create_new_item17/', accounts17.create_new_item17, name='create_new_item17'),
    path('regi_new_item17/', accounts17.regi_new_item17, name='regi_new_item17'),
    path('delete_item17/<id>',accounts17.delete_item17,name='delete_item17'),
    path('update_item17/<id>', accounts17.update_item17, name='update_item17'),
    path('view_all_items_delete17/',accounts17.view_all_items_delete17,name='view_all_items_delete17'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger17/', accounts17.view_all_ledger17, name='view_all_ledger17'),
    path('create_new_ledger17/', accounts17.create_new_ledger17, name='create_new_ledger17'),
    path('regi_new_ledger17/', accounts17.regi_new_ledger17, name='regi_new_ledger17'),
    path('delete_ledger17/<id>',accounts17.delete_ledger17,name='delete_ledger17'),
    path('update_ledger17/<id>',accounts17.update_ledger17,name='update_ledger17'),
    path('view_all_ledger_delete17/',accounts17.view_all_ledger_delete17,name='view_all_ledger_delete17'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book17/', accounts17.view_all_accounts_book17, name='view_all_accounts_book17'),
    path('create_new_accounts_book17/', accounts17.create_new_accounts_book17, name='create_new_accounts_book17'),
    path('regi_new_accounts_book17/', accounts17.regi_new_accounts_book17, name='regi_new_accounts_book17'),
    path('update_accounts_book17/<id>',accounts17.update_accounts_book17,name='update_accounts_book17'),
    path('delete_accounts_book17/<id>',accounts17.delete_accounts_book17,name='delete_accounts_book17'),
    path('view_all_accounts_book_delete17/',accounts17.view_all_accounts_book_delete17,name='view_all_accounts_book_delete17'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries17/', accounts17.get_countries17, name='get_countries17'),

    path('in_exp_items_entry17/', accounts17.in_exp_items_entry17, name='in_exp_items_entry17'),
    path('reg_in_exp_items_entry17/', accounts17.reg_in_exp_items_entry17, name='reg_in_exp_items_entry17'),
    path('delete_journal17/<id>',accounts17.delete_journal17,name='delete_journal17'),
    path('update_in_exp_items_entry17/<id>',accounts17.update_in_exp_items_entry17,name='update_in_exp_items_entry17'),
    path('detailed_journal_report17/',accounts17.detailed_journal_report17,name='detailed_journal_report17'),
    path('journal_report_deleted17/',accounts17.journal_report_deleted17,name='journal_report_deleted17'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise17/', accounts17.daily_category_wise17, name='daily_category_wise17'),
    path('monthly_category_based_reports17/',accounts17.monthly_category_based_reports17,name='monthly_category_based_reports17'),
    path('yearly_category_based_reports17/', accounts17.yearly_category_based_reports17,name='yearly_category_based_reports17'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed17/', accounts17.daily_detailed17, name='daily_detailed17'),
    path('monthly_detailed17/',accounts17.monthly_detailed17,name='monthly_detailed17'),
    path('yearly_detailed17/',accounts17.yearly_detailed17,name='yearly_detailed17'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports17/', accounts17.item_based_reports17, name='item_based_reports17'),
    path('daily_item_based_reports17/',accounts17.daily_item_based_reports17,name='daily_item_based_reports17'),
    path('monthly_item_based_reports17/',accounts17.monthly_item_based_reports17,name='monthly_item_based_reports17'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports17/', accounts17.ledger_based_reports17, name='ledger_based_reports17'),
    path('monthly_ledger_based_reports17/', accounts17.monthly_ledger_based_reports17, name='monthly_ledger_based_reports17'),
    path('daily_ledger_based_reports17/',accounts17.daily_ledger_based_reports17,name='daily_ledger_based_reports17'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports17/', accounts17.accounts_book_based_reports17, name='accounts_book_based_reports17'),
    path('daily_accounts_book_based_reports17/',accounts17.daily_accounts_book_based_reports17,name='daily_accounts_book_based_reports17'),
    path('monthly_accounts_book_based_reports17/',accounts17.monthly_accounts_book_based_reports17,name='monthly_accounts_book_based_reports17'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months17/', accounts17.monthly_reports_choose_months17, name='monthly_reports_choose_months17'),
    path('monthly_detailed_daily_in_exp_items_report17/<mo>',accounts17.monthly_detailed_daily_in_exp_items_report17,name='monthly_detailed_daily_in_exp_items_report17'),

    path('single_monthly_reports_choose_months17/', accounts17.single_monthly_reports_choose_months17,name='single_monthly_reports_choose_months17'),
    path('single_monthly_daily_in_exp_items_report17/<mo>',accounts17.single_monthly_daily_in_exp_items_report17,name='single_monthly_daily_in_exp_items_report17'),

    path('accounts_dash_board_ob_ch17/',accounts17.accounts_dash_board_ob_ch17,name='accounts_dash_board_ob_ch17'),
    path('accounts_dash_board17/',accounts17.accounts_dash_board17,name='accounts_dash_board17'),

    path('profit_sharing_choose_months17', accounts17.profit_sharing_choose_months17,name='profit_sharing_choose_months17'),
    path('profit_sharing17/<mo>', accounts17.profit_sharing17, name='profit_sharing17'),
    path('view_share_holders17', accounts17.view_share_holders17, name='view_share_holders17'),
    path('create_share_holders17', accounts17.create_share_holders17, name='create_share_holders17'),
    path('regi_share_holders17', accounts17.regi_share_holders17, name='regi_share_holders17'),
    path('update_share_holders17/<id>', accounts17.update_share_holders17, name='update_share_holders17'),
    path('delete_share_holders17/<id>', accounts17.delete_share_holders17, name='delete_share_holders17'),
    path('view_deleted_share_holders17', accounts17.view_deleted_share_holders17, name='view_deleted_share_holders17'),


]

