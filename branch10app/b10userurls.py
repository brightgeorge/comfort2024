from django.urls import path, include

from . import admin_branch10
from . import admin_branch10
from . import branch10
from . import reports10
from . import payment10
from . import admin_dashboard_calculations_br10
from . import accounts10

urlpatterns = [

    path('branch1_dashboard_ob_ch/', branch10.branch1_dashboard_ob_ch, name='branch1_dashboard_ob_ch'),
    path('user_dashboard_calculations_ob_ch/',branch10.user_dashboard_calculations_ob_ch,name='user_dashboard_calculations_ob_ch'),

    path('background_ob_ch',branch10.background_ob_ch,name='background_ob_ch'),
    path('background_regi_ob_ch',branch10.background_regi_ob_ch,name='background_regi_ob_ch'),
    path('custom_background_regi_ob_ch',branch10.custom_background_regi_ob_ch,name='custom_background_regi_ob_ch'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch/',admin_branch10.branch1_room_create_regi_ob_ch,name='branch1_room_create_regi_ob_ch'),
    path('view_all_room_ob_ch/',admin_branch10.view_all_room_ob_ch,name='view_all_room_ob_ch'),
    path('delete_room_ob_ch/<id>',admin_branch10.delete_room_ob_ch,name='delete_room_ob_ch'),

    path('branch1_room_create_ob_ch/',admin_branch10.branch1_room_create_ob_ch,name='branch1_room_create_ob_ch'),

    path('multiple_branch1_room_create_regi10/',admin_branch10.multiple_branch1_room_create_regi10,name='multiple_branch1_room_create_regi10'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch/', admin_branch10.pg1_bed_create_regi_ob_ch, name='pg1_bed_create_regi_ob_ch'),
    path('pg1_view_all_beds_ob_ch/', admin_branch10.pg1_view_all_beds_ob_ch, name='pg1_view_all_beds_ob_ch'),
    path('delete_bed_ob_ch/<id>', admin_branch10.delete_bed_ob_ch, name='delete_bed_ob_ch'),

    path('pg1_bed_create_ob_ch/', admin_branch10.pg1_bed_create_ob_ch, name='pg1_bed_create_ob_ch'),

    path('single_pg1_bed_create_regi_ob_ch/',admin_branch10.single_pg1_bed_create_regi_ob_ch,name='single_pg1_bed_create_regi_ob_ch'),
    path('update_bed_basic_details_ob_ch/<id>',admin_branch10.update_bed_basic_details_ob_ch, name='update_bed_basic_details_ob_ch'),

    path('multiple_single_pg1_bed_create_regi10/',admin_branch10.multiple_single_pg1_bed_create_regi10,name='multiple_single_pg1_bed_create_regi10'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch/<id>',branch10.br1_admit_guest_ob_ch,name='br1_admit_guest_ob_ch'),
    path('view_all_new_guest_ob_ch/',branch10.view_all_new_guest_ob_ch,name='view_all_new_guest_ob_ch'),
    path('update_br1_admit_guest_ob_ch/<id>',branch10.update_br1_admit_guest_ob_ch,name='update_br1_admit_guest_ob_ch'),
    path('vacate_br1_guest_ob_ch/<id>',branch10.vacate_br1_guest_ob_ch,name='vacate_br1_guest_ob_ch'),

    path('active_guest_details_ob_ch/<guest_code>',branch10.active_guest_details_ob_ch,name='active_guest_details_ob_ch'),
    path('view_all_guest_ob_ch/',branch10.view_all_guest_ob_ch,name='view_all_guest_ob_ch'),
    path('shift_guest_ob_ch/<id>',branch10.shift_guest_ob_ch,name='shift_guest_ob_ch'),
    path('shift_guest_regi_ob_ch/',branch10.shift_guest_regi_ob_ch,name='shift_guest_regi_ob_ch'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch/',branch10.update_all_rent_ob_ch,name='update_all_rent_ob_ch'),

    path('multiple_br1_admit_guest10/<id>',branch10.multiple_br1_admit_guest10,name='multiple_br1_admit_guest10'),

#guest end here


##################################
#_ADVANCE_ob_ch START HERE
################################


    path('choose_months_advance_ob_ch/',branch10.choose_months_advance_ob_ch,name='choose_months_advance_ob_ch'),

    path('jan_advance_ob_ch/', branch10.jan_advance_ob_ch, name='jan_advance_ob_ch'),
    path('jan_make_payments_advance_ob_ch/<id>', branch10.jan_make_payments_advance_ob_ch,name='jan_make_payments_advance_ob_ch'),
    path('feb_advance_ob_ch/', branch10.feb_advance_ob_ch, name='feb_advance_ob_ch'),
    path('feb_make_payments_advance_ob_ch/<id>', branch10.feb_make_payments_advance_ob_ch,name='feb_make_payments_advance_ob_ch'),
    path('march_advance_ob_ch/', branch10.march_advance_ob_ch, name='march_advance_ob_ch'),
    path('march_make_payments_advance_ob_ch/<id>', branch10.march_make_payments_advance_ob_ch,name='march_make_payments_advance_ob_ch'),
    path('april_advance_ob_ch/', branch10.april_advance_ob_ch, name='april_advance_ob_ch'),
    path('april_make_payments_advance_ob_ch/<id>', branch10.april_make_payments_advance_ob_ch, name='april_make_payments_advance_ob_ch'),

    path('may_advance_ob_ch/',branch10.may_advance_ob_ch,name='may_advance_ob_ch'),
    path('may_make_payments_advance_ob_ch/<id>', branch10.may_make_payments_advance_ob_ch, name='may_make_payments_advance_ob_ch'),
    path('june_advance_ob_ch/',branch10.june_advance_ob_ch,name='june_advance_ob_ch'),
    path('june_make_payments_advance_ob_ch/<id>', branch10.june_make_payments_advance_ob_ch, name='june_make_payments_advance_ob_ch'),
    path('july_advance_ob_ch/',branch10.july_advance_ob_ch,name='july_advance_ob_ch'),
    path('july_make_payments_advance_ob_ch/<id>', branch10.july_make_payments_advance_ob_ch, name='july_make_payments_advance_ob_ch'),
    path('auguest_advance_ob_ch/', branch10.auguest_advance_ob_ch, name='auguest_advance_ob_ch'),
    path('auguest_make_payments_advance_ob_ch/<id>', branch10.auguest_make_payments_advance_ob_ch, name='auguest_make_payments_advance_ob_ch'),

    path('sept_advance_ob_ch/', branch10.sept_advance_ob_ch, name='sept_advance_ob_ch'),
    path('sept_make_payments_advance_ob_ch/<id>', branch10.sept_make_payments_advance_ob_ch,name='sept_make_payments_advance_ob_ch'),
    path('october_advance_ob_ch/', branch10.october_advance_ob_ch, name='october_advance_ob_ch'),
    path('october_make_payments_advance_ob_ch/<id>', branch10.october_make_payments_advance_ob_ch, name='october_make_payments_advance_ob_ch'),
    path('nov_advance_ob_ch/', branch10.nov_advance_ob_ch, name='nov_advance_ob_ch'),
    path('nov_make_payments_advance_ob_ch/<id>', branch10.nov_make_payments_advance_ob_ch,name='nov_make_payments_advance_ob_ch'),
    path('dec_advance_ob_ch/', branch10.dec_advance_ob_ch, name='dec_advance_ob_ch'),
    path('dec_make_payments_advance_ob_ch/<id>', branch10.dec_make_payments_advance_ob_ch, name='dec_make_payments_advance_ob_ch'),



##################################
#_ADVANCE_ob_ch END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch/',branch10.choose_months_ob_ch,name='choose_months_ob_ch'),

    path('jan_ob_ch/',branch10.jan_ob_ch,name='jan_ob_ch'),
    path('jan_manke_payments_ob_ch/<id>',branch10.jan_manke_payments_ob_ch,name='jan_manke_payments_ob_ch'),

    path('feb_ob_ch/',branch10.feb_ob_ch,name='feb_ob_ch'),
    path('feb_manke_payments_ob_ch/<id>',branch10.feb_manke_payments_ob_ch,name='feb_manke_payments_ob_ch'),

    path('march_ob_ch/',branch10.march_ob_ch,name='march_ob_ch'),
    path('march_manke_payments_ob_ch/<id>',branch10.march_manke_payments_ob_ch,name='march_manke_payments_ob_ch'),

    path('april_ob_ch/',branch10.april_ob_ch,name='april_ob_ch'),
    path('april_make_payments_ob_ch/<id>',branch10.april_make_payments_ob_ch,name='april_make_payments_ob_ch'),

    path('may_ob_ch/',branch10.may_ob_ch,name='may_ob_ch'),
    path('may_make_payments_ob_ch/<id>',branch10.may_make_payments_ob_ch,name='may_make_payments_ob_ch'),

    path('june_ob_ch/',branch10.june_ob_ch,name='june_ob_ch'),
    path('june_make_payments_ob_ch/<id>',branch10.june_make_payments_ob_ch,name='june_make_payments_ob_ch'),

    path('july_ob_ch/',branch10.july_ob_ch,name='july_ob_ch'),
    path('july_make_payments_ob_ch/<id>',branch10.july_make_payments_ob_ch,name='july_make_payments_ob_ch'),

    path('aug_ob_ch/',branch10.aug_ob_ch,name='aug_ob_ch'),
    path('aug_make_payments_ob_ch/<id>',branch10.aug_make_payments_ob_ch,name='aug_make_payments_ob_ch'),

    path('sept_ob_ch/',branch10.sept_ob_ch,name='sept_ob_ch'),
    path('sept_make_payments_ob_ch/<id>',branch10.sept_make_payments_ob_ch,name='sept_make_payments_ob_ch'),

    path('oct_ob_ch/',branch10.oct_ob_ch,name='oct_ob_ch'),
    path('oct_make_payments_ob_ch/<id>',branch10.oct_make_payments_ob_ch,name='oct_make_payments_ob_ch'),

    path('nov_ob_ch/',branch10.nov_ob_ch,name='nov_ob_ch'),
    path('nov_make_payments_ob_ch/<id>',branch10.nov_make_payments_ob_ch,name='nov_make_payments_ob_ch'),

    path('dec_ob_ch/',branch10.dec_ob_ch,name='dec_ob_ch'),
    path('dec_make_payments_ob_ch/<id>',branch10.dec_make_payments_ob_ch,name='dec_make_payments_ob_ch'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch/', payment10.choose_user_ob_ch, name='choose_user_ob_ch'),
    path('payment_user_details_ob_ch/<id>', payment10.payment_user_details_ob_ch, name='payment_user_details_ob_ch'),
    path('close_choose_user_ob_ch/<id>',payment10.close_choose_user_ob_ch,name='close_choose_user_ob_ch'),

    path('monthly_jan_make_payments_ob_ch/<id>', payment10.monthly_jan_make_payments_ob_ch, name='monthly_jan_make_payments_ob_ch'),
    path('monthly_feb_make_payments_ob_ch/<id>', payment10.monthly_feb_make_payments_ob_ch, name='monthly_feb_make_payments_ob_ch'),
    path('monthly_march_make_payments_ob_ch/<id>', payment10.monthly_march_make_payments_ob_ch, name='monthly_march_make_payments_ob_ch'),
    path('monthly_april_make_payments_ob_ch/<id>', payment10.monthly_april_make_payments_ob_ch, name='monthly_april_make_payments_ob_ch'),
    path('monthly_may_make_payments_ob_ch/<id>', payment10.monthly_may_make_payments_ob_ch, name='monthly_may_make_payments_ob_ch'),
    path('monthly_june_make_payments_ob_ch/<id>', payment10.monthly_june_make_payments_ob_ch, name='monthly_june_make_payments_ob_ch'),

    path('monthly_july_make_payments_ob_ch/<id>', payment10.monthly_july_make_payments_ob_ch, name='monthly_july_make_payments_ob_ch'),
    path('monthly_aug_make_payments_ob_ch/<id>', payment10.monthly_aug_make_payments_ob_ch, name='monthly_aug_make_payments_ob_ch'),
    path('monthly_sept_make_payments_ob_ch/<id>', payment10.monthly_sept_make_payments_ob_ch, name='monthly_sept_make_payments_ob_ch'),
    path('monthly_oct_make_payments_ob_ch/<id>', payment10.monthly_oct_make_payments_ob_ch, name='monthly_oct_make_payments_ob_ch'),
    path('monthly_nov_make_payments_ob_ch/<id>', payment10.monthly_nov_make_payments_ob_ch, name='monthly_nov_make_payments_ob_ch'),
    path('monthly_dec_make_payments_ob_ch/<id>', payment10.monthly_dec_make_payments_ob_ch, name='monthly_dec_make_payments_ob_ch'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch/',branch10.unpaid_rent_choose_months_ob_ch,name='unpaid_rent_choose_months_ob_ch'),

    path('jan_unpaid_rent_ob_ch/', branch10.jan_unpaid_rent_ob_ch, name='jan_unpaid_rent_ob_ch'),
    path('table_jan_unpaid_rent_ob_ch/', branch10.table_jan_unpaid_rent_ob_ch, name='table_jan_unpaid_rent_ob_ch'),
    path('feb_unpaid_rent_ob_ch/', branch10.feb_unpaid_rent_ob_ch, name='feb_unpaid_rent_ob_ch'),
    path('table_feb_unpaid_rent_ob_ch/', branch10.table_feb_unpaid_rent_ob_ch, name='table_feb_unpaid_rent_ob_ch'),
    path('mar_unpaid_rent_ob_ch/', branch10.mar_unpaid_rent_ob_ch, name='mar_unpaid_rent_ob_ch'),
    path('table_mar_unpaid_rent_ob_ch/', branch10.table_mar_unpaid_rent_ob_ch, name='table_mar_unpaid_rent_ob_ch'),
    path('april_unpaid_rent_ob_ch/', branch10.april_unpaid_rent_ob_ch, name='april_unpaid_rent_ob_ch'),
    path('table_april_unpaid_rent_ob_ch/', branch10.table_april_unpaid_rent_ob_ch, name='table_april_unpaid_rent_ob_ch'),

    path('may_unpaid_rent_ob_ch/', branch10.may_unpaid_rent_ob_ch, name='may_unpaid_rent_ob_ch'),
    path('table_may_unpaid_rent_ob_ch/', branch10.table_may_unpaid_rent_ob_ch, name='table_may_unpaid_rent_ob_ch'),
    path('june_unpaid_rent_ob_ch/', branch10.june_unpaid_rent_ob_ch, name='june_unpaid_rent_ob_ch'),
    path('table_june_unpaid_rent_ob_ch/', branch10.table_june_unpaid_rent_ob_ch, name='table_june_unpaid_rent_ob_ch'),
    path('july_unpaid_rent_ob_ch/', branch10.july_unpaid_rent_ob_ch, name='july_unpaid_rent_ob_ch'),
    path('table_july_unpaid_rent_ob_ch',branch10.table_july_unpaid_rent_ob_ch,name='table_july_unpaid_rent_ob_ch'),
    path('aug_unpaid_rent_ob_ch/', branch10.aug_unpaid_rent_ob_ch, name='aug_unpaid_rent_ob_ch'),
    path('table_aug_unpaid_rent_ob_ch/',branch10.table_aug_unpaid_rent_ob_ch,name='table_aug_unpaid_rent_ob_ch'),

    path('sept_unpaid_rent_ob_ch/', branch10.sept_unpaid_rent_ob_ch, name='sept_unpaid_rent_ob_ch'),
    path('table_sept_unpaid_rent_ob_ch/', branch10.table_sept_unpaid_rent_ob_ch, name='table_sept_unpaid_rent_ob_ch'),
    path('oct_unpaid_rent_ob_ch/', branch10.oct_unpaid_rent_ob_ch, name='oct_unpaid_rent_ob_ch'),
    path('table_oct_unpaid_rent_ob_ch/', branch10.table_oct_unpaid_rent_ob_ch, name='table_oct_unpaid_rent_ob_ch'),
    path('nov_unpaid_rent_ob_ch/', branch10.nov_unpaid_rent_ob_ch, name='nov_unpaid_rent_ob_ch'),
    path('table_nov_unpaid_rent_ob_ch/', branch10.table_nov_unpaid_rent_ob_ch, name='table_nov_unpaid_rent_ob_ch'),
    path('dec_unpaid_rent_ob_ch/', branch10.dec_unpaid_rent_ob_ch, name='dec_unpaid_rent_ob_ch'),
    path('table_dec_unpaid_rent_ob_ch/', branch10.table_dec_unpaid_rent_ob_ch, name='table_dec_unpaid_rent_ob_ch'),

    path('details_of_unpaid_guests_ob_ch/<id>',branch10.details_of_unpaid_guests_ob_ch,name='details_of_unpaid_guests_ob_ch'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch/',branch10.paid_rent_choose_months_ob_ch,name='paid_rent_choose_months_ob_ch'),
    path('partially_paid_guest_choose_months_ob_ch/',reports10.partially_paid_guest_choose_months_ob_ch,name='partially_paid_guest_choose_months_ob_ch'),

    path('jan_paid_rent_ob_ch/', branch10.jan_paid_rent_ob_ch, name='jan_paid_rent_ob_ch'),
    path('table_jan_paid_rent_ob_ch/', branch10.table_jan_paid_rent_ob_ch, name='table_jan_paid_rent_ob_ch'),
    path('jan_full_paid_guest_ob_ch/', reports10.jan_full_paid_guest_ob_ch, name='jan_full_paid_guest_ob_ch'),
    path('jan_partially_paid_guest_ob_ch/', reports10.jan_partially_paid_guest_ob_ch, name='jan_partially_paid_guest_ob_ch'),
    path('table_jan_partially_paid_guest_ob_ch/', reports10.table_jan_partially_paid_guest_ob_ch,name='table_jan_partially_paid_guest_ob_ch'),

    path('feb_paid_rent_ob_ch/', branch10.feb_paid_rent_ob_ch, name='feb_paid_rent_ob_ch'),
    path('table_feb_paid_rent_ob_ch/', branch10.table_feb_paid_rent_ob_ch, name='table_feb_paid_rent_ob_ch'),
    path('feb_full_paid_guest_ob_ch/', reports10.feb_full_paid_guest_ob_ch, name='feb_full_paid_guest_ob_ch'),
    path('feb_partially_paid_guest_ob_ch/', reports10.feb_partially_paid_guest_ob_ch, name='feb_partially_paid_guest_ob_ch'),
    path('table_feb_partially_paid_guest_ob_ch/', reports10.table_feb_partially_paid_guest_ob_ch,name='table_feb_partially_paid_guest_ob_ch'),

    path('mar_paid_rent_ob_ch/', branch10.mar_paid_rent_ob_ch, name='mar_paid_rent_ob_ch'),
    path('table_mar_paid_rent_ob_ch/', branch10.table_mar_paid_rent_ob_ch, name='table_mar_paid_rent_ob_ch'),
    path('march_full_paid_guest_ob_ch/', reports10.march_full_paid_guest_ob_ch, name='march_full_paid_guest_ob_ch'),
    path('march_partially_paid_guest_ob_ch/', reports10.march_partially_paid_guest_ob_ch, name='march_partially_paid_guest_ob_ch'),
    path('table_march_partially_paid_guest_ob_ch/', reports10.table_march_partially_paid_guest_ob_ch,name='table_march_partially_paid_guest_ob_ch'),

    path('april_paid_rent_ob_ch/', branch10.april_paid_rent_ob_ch, name='april_paid_rent_ob_ch'),
    path('table_april_paid_rent_ob_ch/', branch10.table_april_paid_rent_ob_ch, name='table_april_paid_rent_ob_ch'),
    path('april_full_paid_guest_ob_ch/', reports10.april_full_paid_guest_ob_ch, name='april_full_paid_guest_ob_ch'),
    path('april_partially_paid_guest_ob_ch/', reports10.april_partially_paid_guest_ob_ch, name='april_partially_paid_guest_ob_ch'),
    path('table_april_partially_paid_guest_ob_ch/', reports10.table_april_partially_paid_guest_ob_ch,name='table_april_partially_paid_guest_ob_ch'),

    path('may_paid_rent_ob_ch/', branch10.may_paid_rent_ob_ch, name='may_paid_rent_ob_ch'),
    path('table_may_paid_rent_ob_ch/', branch10.table_may_paid_rent_ob_ch, name='table_may_paid_rent_ob_ch'),
    path('may_full_paid_guest_ob_ch/', reports10.may_full_paid_guest_ob_ch, name='may_full_paid_guest_ob_ch'),
    path('may_partially_paid_guest_ob_ch/', reports10.may_partially_paid_guest_ob_ch, name='may_partially_paid_guest_ob_ch'),
    path('table_may_partially_paid_guest_ob_ch/', reports10.table_may_partially_paid_guest_ob_ch, name='table_may_partially_paid_guest_ob_ch'),

    path('june_paid_rent_ob_ch/', branch10.june_paid_rent_ob_ch, name='june_paid_rent_ob_ch'),
    path('table_june_paid_rent_ob_ch/', branch10.table_june_paid_rent_ob_ch, name='table_june_paid_rent_ob_ch'),
    path('june_full_paid_guest_ob_ch/', reports10.june_full_paid_guest_ob_ch, name='june_full_paid_guest_ob_ch'),
    path('june_partially_paid_guest_ob_ch/', reports10.june_partially_paid_guest_ob_ch, name='june_partially_paid_guest_ob_ch'),
    path('table_june_partially_paid_guest_ob_ch/', reports10.table_june_partially_paid_guest_ob_ch, name='table_june_partially_paid_guest_ob_ch'),

    path('july_paid_rent_ob_ch/', branch10.july_paid_rent_ob_ch, name='july_paid_rent_ob_ch'),
    path('table_july_paid_rent_ob_ch/', branch10.table_july_paid_rent_ob_ch, name='table_july_paid_rent_ob_ch'),
    path('july_full_paid_guest_ob_ch/', reports10.july_full_paid_guest_ob_ch, name='july_full_paid_guest_ob_ch'),
    path('july_partially_paid_guest_ob_ch/', reports10.july_partially_paid_guest_ob_ch, name='july_partially_paid_guest_ob_ch'),
    path('table_july_partially_paid_guest_ob_ch/', reports10.table_july_partially_paid_guest_ob_ch, name='table_july_partially_paid_guest_ob_ch'),

    path('aug_paid_rent_ob_ch/', branch10.aug_paid_rent_ob_ch, name='aug_paid_rent_ob_ch'),
    path('table_aug_paid_rent_ob_ch/', branch10.table_aug_paid_rent_ob_ch, name='table_aug_paid_rent_ob_ch'),
    path('auguest_full_paid_guest_ob_ch/', reports10.auguest_full_paid_guest_ob_ch, name='auguest_full_paid_guest_ob_ch'),
    path('auguest_partially_paid_guest_ob_ch/', reports10.auguest_partially_paid_guest_ob_ch,name='auguest_partially_paid_guest_ob_ch'),
    path('table_auguest_partially_paid_guest_ob_ch/', reports10.table_auguest_partially_paid_guest_ob_ch,name='table_auguest_partially_paid_guest_ob_ch'),

    path('sept_paid_rent_ob_ch/', branch10.sept_paid_rent_ob_ch, name='sept_paid_rent_ob_ch'),
    path('table_sept_paid_rent_ob_ch/', branch10.table_sept_paid_rent_ob_ch, name='table_sept_paid_rent_ob_ch'),
    path('sept_full_paid_guest_ob_ch/', reports10.sept_full_paid_guest_ob_ch, name='sept_full_paid_guest_ob_ch'),
    path('sept_partially_paid_guest_ob_ch/', reports10.sept_partially_paid_guest_ob_ch, name='sept_partially_paid_guest_ob_ch'),
    path('table_sept_partially_paid_guest_ob_ch/', reports10.table_sept_partially_paid_guest_ob_ch,name='table_sept_partially_paid_guest_ob_ch'),

    path('oct_paid_rent_ob_ch/', branch10.oct_paid_rent_ob_ch, name='oct_paid_rent_ob_ch'),
    path('table_oct_paid_rent_ob_ch/', branch10.table_oct_paid_rent_ob_ch, name='table_oct_paid_rent_ob_ch'),
    path('october_full_paid_guest_ob_ch/', reports10.october_full_paid_guest_ob_ch, name='october_full_paid_guest_ob_ch'),
    path('october_partially_paid_guest_ob_ch/', reports10.october_partially_paid_guest_ob_ch,name='october_partially_paid_guest_ob_ch'),
    path('table_october_partially_paid_guest_ob_ch/', reports10.table_october_partially_paid_guest_ob_ch,name='table_october_partially_paid_guest_ob_ch'),

    path('nov_paid_rent_ob_ch/', branch10.nov_paid_rent_ob_ch, name='nov_paid_rent_ob_ch'),
    path('table_nov_paid_rent_ob_ch/', branch10.table_nov_paid_rent_ob_ch, name='table_nov_paid_rent_ob_ch'),
    path('nov_full_paid_guest_ob_ch/', reports10.nov_full_paid_guest_ob_ch, name='nov_full_paid_guest_ob_ch'),
    path('nov_partially_paid_guest_ob_ch/', reports10.nov_partially_paid_guest_ob_ch, name='nov_partially_paid_guest_ob_ch'),
    path('table_nov_partially_paid_guest_ob_ch/', reports10.table_nov_partially_paid_guest_ob_ch,name='table_nov_partially_paid_guest_ob_ch'),

    path('dec_paid_rent_ob_ch/', branch10.dec_paid_rent_ob_ch, name='dec_paid_rent_ob_ch'),
    path('table_dec_paid_rent_ob_ch/', branch10.table_dec_paid_rent_ob_ch, name='table_dec_paid_rent_ob_ch'),
    path('dec_full_paid_guest_ob_ch/', reports10.dec_full_paid_guest_ob_ch, name='dec_full_paid_guest_ob_ch'),
    path('dec_partially_paid_guest_ob_ch/', reports10.dec_partially_paid_guest_ob_ch, name='dec_partially_paid_guest_ob_ch'),
    path('table_dec_partially_paid_guest_ob_ch/', reports10.table_dec_partially_paid_guest_ob_ch,name='table_dec_partially_paid_guest_ob_ch'),

    path('details_of_paid_guests_ob_ch/<id>',branch10.details_of_paid_guests_ob_ch,name='details_of_paid_guests_ob_ch'),
    path('full_paid_guest_ob_ch/',reports10.full_paid_guest_ob_ch,name='full_paid_guest_ob_ch'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch/',branch10.viewall_vacate_guest_ob_ch,name='viewall_vacate_guest_ob_ch'),
    path('details_of_vacate_guest_ob_ch/<id>',branch10.details_of_vacate_guest_ob_ch,name='details_of_vacate_guest_ob_ch'),
    path('full_vacated_guest_details_ob_ch',branch10.full_vacated_guest_details_ob_ch,name='full_vacated_guest_details_ob_ch'),
    path('full_vacated_guest_table_ob_ch',branch10.full_vacated_guest_table_ob_ch,name='full_vacated_guest_table_ob_ch'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch/<id>', branch10.jan_manke_payments_vacate_ob_ch, name='jan_manke_payments_vacate_ob_ch'),
    path('feb_manke_payments_vacate_ob_ch/<id>', branch10.feb_manke_payments_vacate_ob_ch, name='feb_manke_payments_vacate_ob_ch'),
    path('march_manke_payments_vacate_ob_ch/<id>', branch10.march_manke_payments_vacate_ob_ch, name='march_manke_payments_vacate_ob_ch'),
    path('april_make_payments_vacate_ob_ch/<id>', branch10.april_make_payments_vacate_ob_ch, name='april_make_payments_vacate_ob_ch'),

    path('may_make_payments_vacate_ob_ch/<id>', branch10.may_make_payments_vacate_ob_ch, name='may_make_payments_vacate_ob_ch'),
    path('june_make_payments_vacate_ob_ch/<id>', branch10.june_make_payments_vacate_ob_ch, name='june_make_payments_vacate_ob_ch'),
    path('july_make_payments_vacate_ob_ch/<id>', branch10.july_make_payments_vacate_ob_ch, name='july_make_payments_vacate_ob_ch'),
    path('aug_make_payments_vacate_ob_ch/<id>', branch10.aug_make_payments_vacate_ob_ch, name='aug_make_payments_vacate_ob_ch'),

    path('sept_make_payments_vacate_ob_ch/<id>', branch10.sept_make_payments_vacate_ob_ch, name='sept_make_payments_vacate_ob_ch'),
    path('oct_make_payments_vacate_ob_ch/<id>', branch10.oct_make_payments_vacate_ob_ch, name='oct_make_payments_vacate_ob_ch'),
    path('nov_make_payments_vacate_ob_ch/<id>', branch10.nov_make_payments_vacate_ob_ch, name='nov_make_payments_vacate_ob_ch'),
    path('dec_make_payments_vacate_ob_ch/<id>', branch10.dec_make_payments_vacate_ob_ch, name='dec_make_payments_vacate_ob_ch'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch/',branch10.detail_guest_general_ob_ch,name='detail_guest_general_ob_ch'),

    path('jan_print_ob_ch/',branch10.jan_print_ob_ch,name='jan_print_ob_ch'),
    path('feb_print_ob_ch/',branch10.feb_print_ob_ch,name='feb_print_ob_ch'),
    path('march_print_ob_ch/',branch10.march_print_ob_ch,name='march_print_ob_ch'),
    path('april_print_ob_ch/',branch10.april_print_ob_ch,name='april_print_ob_ch'),

    path('may_print_ob_ch/',branch10.may_print_ob_ch,name='may_print_ob_ch'),
    path('june_print_ob_ch/',branch10.june_print_ob_ch,name='june_print_ob_ch'),
    path('july_print_ob_ch/', branch10.july_print_ob_ch, name='july_print_ob_ch'),
    path('aug_print_ob_ch/', branch10.aug_print_ob_ch, name='aug_print_ob_ch'),

    path('sept_print_ob_ch/', branch10.sept_print_ob_ch, name='sept_print_ob_ch'),
    path('oct_print_ob_ch/', branch10.oct_print_ob_ch, name='oct_print_ob_ch'),
    path('nov_print_ob_ch/', branch10.nov_print_ob_ch, name='nov_print_ob_ch'),
    path('dec_print_ob_ch/', branch10.dec_print_ob_ch, name='dec_print_ob_ch'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch/', branch10.jan_close_ob_ch, name='jan_close_ob_ch'),
    path('jan_close_decision_page_ob_ch/', branch10.jan_close_decision_page_ob_ch, name='jan_close_decision_page_ob_ch'),
    path('feb_close/', branch10.feb_close_ob_ch, name='feb_close_ob_ch'),
    path('feb_close_decision_page_ob_ch/', branch10.feb_close_decision_page_ob_ch, name='feb_close_decision_page_ob_ch'),
    path('mar_close_ob_ch/', branch10.mar_close_ob_ch, name='mar_close_ob_ch'),
    path('mar_close_decision_page/', branch10.mar_close_decision_page_ob_ch, name='mar_close_decision_page_ob_ch'),
    path('apr_close_ob_ch/', branch10.apr_close_ob_ch, name='apr_close_ob_ch'),
    path('apr_close_decision_page_ob_ch/', branch10.apr_close_decision_page_ob_ch, name='apr_close_decision_page_ob_ch'),

    path('may_close_ob_ch/', branch10.may_close_ob_ch, name='may_close_ob_ch'),
    path('may_close_decision_page_ob_ch/', branch10.may_close_decision_page_ob_ch, name='may_close_decision_page_ob_ch'),
    path('jun_close_ob_ch/', branch10.jun_close_ob_ch, name='jun_close_ob_ch'),
    path('jun_close_decision_page_ob_ch/', branch10.jun_close_decision_page_ob_ch, name='jun_close_decision_page_ob_ch'),
    path('jul_close_ob_ch/', branch10.jul_close_ob_ch, name='jul_close_ob_ch'),
    path('jul_close_decision_page_ob_ch/', branch10.jul_close_decision_page_ob_ch, name='jul_close_decision_page_ob_ch'),
    path('aug_close_ob_ch/', branch10.aug_close_ob_ch, name='aug_close_ob_ch'),
    path('aug_close_decision_page_ob_ch/', branch10.aug_close_decision_page_ob_ch, name='aug_close_decision_page_ob_ch'),

    path('sep_close_ob_ch/', branch10.sep_close_ob_ch, name='sep_close_ob_ch'),
    path('sep_close_decision_page_ob_ch/', branch10.sep_close_decision_page_ob_ch, name='sep_close_decision_page_ob_ch'),
    path('oct_close_ob_ch/', branch10.oct_close_ob_ch, name='oct_close_ob_ch'),
    path('oct_close_decision_page_ob_ch/', branch10.oct_close_decision_page_ob_ch, name='oct_close_decision_page_ob_ch'),
    path('nov_close_ob_ch/', branch10.nov_close_ob_ch, name='nov_close_ob_ch'),
    path('nov_close_decision_page_ob_ch/', branch10.nov_close_decision_page_ob_ch, name='nov_close_decision_page_ob_ch'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch/',reports10.detailed_report_choose_months_ob_ch,name='detailed_report_choose_months_ob_ch'),

    path('jan_details_live_ob_ch/', reports10.jan_details_live_ob_ch, name='jan_details_live_ob_ch'),
    path('jan_print_live_ob_ch/', reports10.jan_print_live_ob_ch, name='jan_print_live_ob_ch'),
    path('feb_details_live_ob_ch/', reports10.feb_details_live_ob_ch, name='feb_details_live_ob_ch'),
    path('feb_print_live_ob_ch/', reports10.feb_print_live_ob_ch, name='feb_print_live_ob_ch'),
    path('march_details_live_ob_ch/', reports10.march_details_live_ob_ch, name='march_details_live_ob_ch'),
    path('march_print_live_ob_ch/', reports10.march_print_live_ob_ch, name='march_print_live_ob_ch'),

    path('april_details_live_ob_ch/', reports10.april_details_live_ob_ch, name='april_details_live_ob_ch'),
    path('april_print_live_ob_ch/', reports10.april_print_live_ob_ch, name='april_print_live_ob_ch'),
    path('may_details_live_ob_ch/', reports10.may_details_live_ob_ch, name='may_details_live_ob_ch'),
    path('may_print_live_ob_ch/', reports10.may_print_live_ob_ch, name='may_print_live_ob_ch'),
    path('june_details_live_ob_ch/',reports10.june_details_live_ob_ch,name='june_details_live_ob_ch'),
    path('june_print_live_ob_ch/', reports10.june_print_live_ob_ch, name='june_print_live_ob_ch'),

    path('july_details_live_ob_ch/', reports10.july_details_live_ob_ch, name='july_details_live_ob_ch'),
    path('july_print_live_ob_ch/', reports10.july_print_live_ob_ch, name='july_print_live_ob_ch'),
    path('auguest_details_live_ob_ch/', reports10.auguest_details_live_ob_ch, name='auguest_details_live_ob_ch'),
    path('auguest_print_live_ob_ch/', reports10.auguest_print_live_ob_ch, name='auguest_print_live_ob_ch'),
    path('sept_details_live_ob_ch/', reports10.sept_details_live_ob_ch, name='sept_details_live_ob_ch'),
    path('sept_print_live_ob_ch/', reports10.sept_print_live_ob_ch, name='sept_print_live_ob_ch'),

    path('october_details_live_ob_ch/', reports10.october_details_live_ob_ch, name='october_details_live_ob_ch'),
    path('october_print_live_ob_ch/', reports10.october_print_live_ob_ch, name='october_print_live_ob_ch'),
    path('nov_details_live_ob_ch/', reports10.nov_details_live_ob_ch, name='nov_details_live_ob_ch'),
    path('nov_print_live_ob_ch/', reports10.nov_print_live_ob_ch, name='nov_print_live_ob_ch'),
    path('dec_details_live_ob_ch/', reports10.dec_details_live_ob_ch, name='dec_details_live_ob_ch'),
    path('dec_print_live_ob_ch/', reports10.dec_print_live_ob_ch, name='dec_print_live_ob_ch'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch/', reports10.viewall_vaccant_room_ob_ch, name='viewall_vaccant_room_ob_ch'),

    path('d_ob_ch/', branch10.dynamic, name='dynamic'),

    path('manage_bed_ob_ch/', branch10.manage_bed_ob_ch, name='manage_bed_ob_ch'),
    path('manage_new_guest_ob_ch/', branch10.manage_new_guest_ob_ch, name='manage_new_guest_ob_ch'),
    path('manage_update_new_guest_ob_ch/<id>', branch10.manage_update_new_guest_ob_ch, name='manage_update_new_guest_ob_ch'),
    path('manage_update_beds_ob_ch/<id>', branch10.manage_update_beds_ob_ch, name='manage_update_beds_ob_ch'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch/', branch10.view_all_due_amt_ob_ch, name='view_all_due_amt_ob_ch'),
    path('due_amt_mgt_choose_months_ob_ch/', branch10.due_amt_mgt_choose_months_ob_ch, name='due_amt_mgt_choose_months_ob_ch'),

    path('view_jan_account_details_ob_ch/', branch10.view_jan_account_details_ob_ch, name='view_jan_account_details_ob_ch'),
    path('jan_account_mgt_ob_ch/<id>',branch10.jan_account_mgt_ob_ch,name='jan_account_mgt_ob_ch'),
    path('view_feb_account_details_ob_ch/', branch10.view_feb_account_details_ob_ch, name='view_feb_account_details_ob_ch'),
    path('feb_account_mgt_ob_ch/<id>',branch10.feb_account_mgt_ob_ch,name='feb_account_mgt_ob_ch'),
    path('view_march_account_details_ob_ch/', branch10.view_march_account_details_ob_ch, name='view_march_account_details_ob_ch'),
    path('march_account_mgt_ob_ch/<id>',branch10.march_account_mgt_ob_ch,name='march_account_mgt_ob_ch'),
    path('view_april_account_details_ob_ch/', branch10.view_april_account_details_ob_ch, name='view_april_account_details_ob_ch'),
    path('april_account_mgt_ob_ch/<id>',branch10.april_account_mgt_ob_ch,name='april_account_mgt_ob_ch'),

    path('view_may_account_details_ob_ch/',branch10.view_may_account_details_ob_ch,name='view_may_account_details_ob_ch'),
    path('may_account_mgt_ob_ch/<id>', branch10.may_account_mgt_ob_ch, name='may_account_mgt_ob_ch'),
    path('view_june_account_details_ob_ch/', branch10.view_june_account_details_ob_ch, name='view_june_account_details_ob_ch'),
    path('june_account_mgt_ob_ch/<id>',branch10.june_account_mgt_ob_ch,name='june_account_mgt_ob_ch'),
    path('view_july_account_details_ob_ch/', branch10.view_july_account_details_ob_ch, name='view_july_account_details_ob_ch'),
    path('july_account_mgt_ob_ch/<id>',branch10.july_account_mgt_ob_ch,name='july_account_mgt_ob_ch'),
    path('view_auguest_account_details_ob_ch/', branch10.view_auguest_account_details_ob_ch, name='view_auguest_account_details_ob_ch'),
    path('auguest_account_mgt_ob_ch/<id>',branch10.auguest_account_mgt_ob_ch,name='auguest_account_mgt_ob_ch'),

    path('view_sept_account_details_ob_ch/', branch10.view_sept_account_details_ob_ch, name='view_sept_account_details_ob_ch'),
    path('sept_account_mgt_ob_ch/<id>',branch10.sept_account_mgt_ob_ch,name='sept_account_mgt_ob_ch'),
    path('view_october_account_details_ob_ch/', branch10.view_october_account_details_ob_ch, name='view_october_account_details_ob_ch'),
    path('october_account_mgt_ob_ch/<id>',branch10.october_account_mgt_ob_ch,name='october_account_mgt_ob_ch'),
    path('view_nov_account_details_ob_ch/', branch10.view_nov_account_details_ob_ch, name='view_nov_account_details_ob_ch'),
    path('nov_account_mgt_ob_ch/<id>',branch10.nov_account_mgt_ob_ch,name='nov_account_mgt_ob_ch'),
    path('view_dec_account_details_ob_ch/', branch10.view_dec_account_details_ob_ch, name='view_dec_account_details_ob_ch'),
    path('dec_account_mgt_ob_ch/<id>',branch10.dec_account_mgt_ob_ch,name='dec_account_mgt_ob_ch'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch', admin_dashboard_calculations_br10.monthly_details_due_ob_ch, name='monthly_details_due_ob_ch'),
    path('monthly_collection_details_ob_ch/', admin_dashboard_calculations_br10.monthly_collection_details_ob_ch, name='monthly_collection_details_ob_ch'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch/',branch10.guest_all_ob_ch,name='guest_all_ob_ch'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category10/', accounts10.view_all_category10, name='view_all_category10'),
    path('create_new_category10/', accounts10.create_new_category10, name='create_new_category10'),
    path('regi_new_category10/', accounts10.regi_new_category10, name='regi_new_category10'),
    path('update_category10/<id>',accounts10.update_category10,name='update_category10'),

    path('delete_category10/<id>', accounts10.delete_category10, name='delete_category10'),
    path('view_all_category_delete10/', accounts10.view_all_category_delete10, name='view_all_category_delete10'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items10/', accounts10.view_all_items10, name='view_all_items10'),
    path('create_new_item10/', accounts10.create_new_item10, name='create_new_item10'),
    path('regi_new_item10/', accounts10.regi_new_item10, name='regi_new_item10'),
    path('delete_item10/<id>',accounts10.delete_item10,name='delete_item10'),
    path('update_item10/<id>', accounts10.update_item10, name='update_item10'),
    path('view_all_items_delete10/',accounts10.view_all_items_delete10,name='view_all_items_delete10'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger10/', accounts10.view_all_ledger10, name='view_all_ledger10'),
    path('create_new_ledger10/', accounts10.create_new_ledger10, name='create_new_ledger10'),
    path('regi_new_ledger10/', accounts10.regi_new_ledger10, name='regi_new_ledger10'),
    path('delete_ledger10/<id>',accounts10.delete_ledger10,name='delete_ledger10'),
    path('update_ledger10/<id>',accounts10.update_ledger10,name='update_ledger10'),
    path('view_all_ledger_delete10/',accounts10.view_all_ledger_delete10,name='view_all_ledger_delete10'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book10/', accounts10.view_all_accounts_book10, name='view_all_accounts_book10'),
    path('create_new_accounts_book10/', accounts10.create_new_accounts_book10, name='create_new_accounts_book10'),
    path('regi_new_accounts_book10/', accounts10.regi_new_accounts_book10, name='regi_new_accounts_book10'),
    path('update_accounts_book10/<id>',accounts10.update_accounts_book10,name='update_accounts_book10'),
    path('delete_accounts_book10/<id>',accounts10.delete_accounts_book10,name='delete_accounts_book10'),
    path('view_all_accounts_book_delete10/',accounts10.view_all_accounts_book_delete10,name='view_all_accounts_book_delete10'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries10/', accounts10.get_countries10, name='get_countries10'),

    path('in_exp_items_entry10/', accounts10.in_exp_items_entry10, name='in_exp_items_entry10'),
    path('reg_in_exp_items_entry10/', accounts10.reg_in_exp_items_entry10, name='reg_in_exp_items_entry10'),
    path('delete_journal10/<id>',accounts10.delete_journal10,name='delete_journal10'),
    path('update_in_exp_items_entry10/<id>',accounts10.update_in_exp_items_entry10,name='update_in_exp_items_entry10'),
    path('detailed_journal_report10/',accounts10.detailed_journal_report10,name='detailed_journal_report10'),
    path('journal_report_deleted10/',accounts10.journal_report_deleted10,name='journal_report_deleted10'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise10/', accounts10.daily_category_wise10, name='daily_category_wise10'),
    path('monthly_category_based_reports10/',accounts10.monthly_category_based_reports10,name='monthly_category_based_reports10'),
    path('yearly_category_based_reports10/', accounts10.yearly_category_based_reports10,name='yearly_category_based_reports10'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed10/', accounts10.daily_detailed10, name='daily_detailed10'),
    path('monthly_detailed10/',accounts10.monthly_detailed10,name='monthly_detailed10'),
    path('yearly_detailed10/',accounts10.yearly_detailed10,name='yearly_detailed10'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports10/', accounts10.item_based_reports10, name='item_based_reports10'),
    path('daily_item_based_reports10/',accounts10.daily_item_based_reports10,name='daily_item_based_reports10'),
    path('monthly_item_based_reports10/',accounts10.monthly_item_based_reports10,name='monthly_item_based_reports10'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports10/', accounts10.ledger_based_reports10, name='ledger_based_reports10'),
    path('monthly_ledger_based_reports10/', accounts10.monthly_ledger_based_reports10, name='monthly_ledger_based_reports10'),
    path('daily_ledger_based_reports10/',accounts10.daily_ledger_based_reports10,name='daily_ledger_based_reports10'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports10/', accounts10.accounts_book_based_reports10, name='accounts_book_based_reports10'),
    path('daily_accounts_book_based_reports10/',accounts10.daily_accounts_book_based_reports10,name='daily_accounts_book_based_reports10'),
    path('monthly_accounts_book_based_reports10/',accounts10.monthly_accounts_book_based_reports10,name='monthly_accounts_book_based_reports10'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months10/', accounts10.monthly_reports_choose_months10, name='monthly_reports_choose_months10'),
    path('monthly_detailed_daily_in_exp_items_report10/<mo>',accounts10.monthly_detailed_daily_in_exp_items_report10,name='monthly_detailed_daily_in_exp_items_report10'),

    path('single_monthly_reports_choose_months10/', accounts10.single_monthly_reports_choose_months10,name='single_monthly_reports_choose_months10'),
    path('single_monthly_daily_in_exp_items_report10/<mo>',accounts10.single_monthly_daily_in_exp_items_report10,name='single_monthly_daily_in_exp_items_report10'),

    path('accounts_dash_board_ob_ch/',accounts10.accounts_dash_board_ob_ch,name='accounts_dash_board_ob_ch'),

    path('profit_sharing_choose_months10', accounts10.profit_sharing_choose_months10,name='profit_sharing_choose_months10'),
    path('profit_sharing10/<mo>', accounts10.profit_sharing10, name='profit_sharing10'),
    path('view_share_holders10', accounts10.view_share_holders10, name='view_share_holders10'),
    path('create_share_holders10', accounts10.create_share_holders10, name='create_share_holders10'),
    path('regi_share_holders10', accounts10.regi_share_holders10, name='regi_share_holders10'),
    path('update_share_holders10/<id>', accounts10.update_share_holders10, name='update_share_holders10'),
    path('delete_share_holders10/<id>', accounts10.delete_share_holders10, name='delete_share_holders10'),
    path('view_deleted_share_holders10', accounts10.view_deleted_share_holders10, name='view_deleted_share_holders10'),


]