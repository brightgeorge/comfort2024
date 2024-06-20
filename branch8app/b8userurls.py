from django.urls import path, include

#from . import admin_branch8
from . import admin_branch8
from . import branch8
from . import reports8
from . import payment8
from . import admin_dashboard_calculations_br8
from . import accounts8


urlpatterns = [
    path('branch1_dashboard8/', branch8.branch1_dashboard8, name='branch1_dashboard8'),

#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi8/',admin_branch8.branch1_room_create_regi8,name='branch1_room_create_regi8'),
    path('view_all_room8/',admin_branch8.view_all_room8,name='view_all_room8'),
    path('delete_room8/<id>',admin_branch8.delete_room8,name='delete_room8'),

    path('branch1_room_create8/',admin_branch8.branch1_room_create8,name='branch1_room_create8'),

    path('multiple_branch1_room_create_regi8/',admin_branch8.multiple_branch1_room_create_regi8,name='multiple_branch1_room_create_regi8'),

#**room creation end here


#bed creation start here

    path('pg1_bed_create_regi8/', admin_branch8.pg1_bed_create_regi8, name='pg1_bed_create_regi8'),
    path('pg1_view_all_beds8/', admin_branch8.pg1_view_all_beds8, name='pg1_view_all_beds8'),
    path('delete_bed8/<id>', admin_branch8.delete_bed8, name='delete_bed8'),

    path('pg1_bed_create8/', admin_branch8.pg1_bed_create8, name='pg1_bed_create8'),

    path('single_pg1_bed_create_regi8/',admin_branch8.single_pg1_bed_create_regi8,name='single_pg1_bed_create_regi8'),
    path('update_bed_basic_details8/<id>',admin_branch8.update_bed_basic_details8, name='update_bed_basic_details8'),

    path('multiple_single_pg1_bed_create_regi8/',admin_branch8.multiple_single_pg1_bed_create_regi8,name='multiple_single_pg1_bed_create_regi8'),

#bed creation end here

#guest
    path('br1_admit_guest8/<id>',branch8.br1_admit_guest8,name='br1_admit_guest8'),
    path('view_all_new_guest8/',branch8.view_all_new_guest8,name='view_all_new_guest8'),
    path('update_br1_admit_guest8/<id>',branch8.update_br1_admit_guest8,name='update_br1_admit_guest8'),
    path('vacate_br1_guest8/<id>',branch8.vacate_br1_guest8,name='vacate_br1_guest8'),

    path('active_guest_details8/<guest_code>',branch8.active_guest_details8,name='active_guest_details8'),
    path('view_all_guest8/',branch8.view_all_guest8,name='view_all_guest8'),
    path('shift_guest8/<id>',branch8.shift_guest8,name='shift_guest8'),
    path('shift_guest_regi8/',branch8.shift_guest_regi8,name='shift_guest_regi8'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('multiple_br1_admit_guest8/<id>',branch8.multiple_br1_admit_guest8,name='multiple_br1_admit_guest8'),

#guest end here


#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months8/',branch8.unpaid_rent_choose_months8,name='unpaid_rent_choose_months8'),

    path('jan_unpaid_rent8/', branch8.jan_unpaid_rent8, name='jan_unpaid_rent8'),
    path('table_jan_unpaid_rent8/', branch8.table_jan_unpaid_rent8, name='table_jan_unpaid_rent8'),
    path('feb_unpaid_rent8/', branch8.feb_unpaid_rent8, name='feb_unpaid_rent8'),
    path('table_feb_unpaid_rent8/', branch8.table_feb_unpaid_rent8, name='table_feb_unpaid_rent8'),
    path('mar_unpaid_rent8/', branch8.mar_unpaid_rent8, name='mar_unpaid_rent8'),
    path('table_mar_unpaid_rent8/', branch8.table_mar_unpaid_rent8, name='table_mar_unpaid_rent8'),
    path('april_unpaid_rent8/', branch8.april_unpaid_rent8, name='april_unpaid_rent8'),
    path('table_april_unpaid_rent8/', branch8.table_april_unpaid_rent8, name='table_april_unpaid_rent8'),

    path('may_unpaid_rent8/', branch8.may_unpaid_rent8, name='may_unpaid_rent8'),
    path('table_may_unpaid_rent8/', branch8.table_may_unpaid_rent8, name='table_may_unpaid_rent8'),
    path('june_unpaid_rent8/', branch8.june_unpaid_rent8, name='june_unpaid_rent8'),
    path('table_june_unpaid_rent8/', branch8.table_june_unpaid_rent8, name='table_june_unpaid_rent8'),
    path('july_unpaid_rent8/', branch8.july_unpaid_rent8, name='july_unpaid_rent8'),
    path('table_july_unpaid_rent8',branch8.table_july_unpaid_rent8,name='table_july_unpaid_rent8'),
    path('aug_unpaid_rent8/', branch8.aug_unpaid_rent8, name='aug_unpaid_rent8'),
    path('table_aug_unpaid_rent8/',branch8.table_aug_unpaid_rent8,name='table_aug_unpaid_rent8'),

    path('sept_unpaid_rent8/', branch8.sept_unpaid_rent8, name='sept_unpaid_rent8'),
    path('table_sept_unpaid_rent8/', branch8.table_sept_unpaid_rent8, name='table_sept_unpaid_rent8'),
    path('oct_unpaid_rent8/', branch8.oct_unpaid_rent8, name='oct_unpaid_rent8'),
    path('table_oct_unpaid_rent8/', branch8.table_oct_unpaid_rent8, name='table_oct_unpaid_rent8'),
    path('nov_unpaid_rent8/', branch8.nov_unpaid_rent8, name='nov_unpaid_rent8'),
    path('table_nov_unpaid_rent8/', branch8.table_nov_unpaid_rent8, name='table_nov_unpaid_rent8'),
    path('dec_unpaid_rent8/', branch8.dec_unpaid_rent8, name='dec_unpaid_rent8'),
    path('table_dec_unpaid_rent8/', branch8.table_dec_unpaid_rent8, name='table_dec_unpaid_rent8'),

    path('details_of_unpaid_guests8/<id>',branch8.details_of_unpaid_guests8,name='details_of_unpaid_guests8'),

#unpaid rent end here

#paid rent start here


path('paid_rent_choose_months8/',branch8.paid_rent_choose_months8,name='paid_rent_choose_months8'),
path('partially_paid_guest_choose_months8/',reports8.partially_paid_guest_choose_months8,name='partially_paid_guest_choose_months8'),

path('jan_paid_rent8/', branch8.jan_paid_rent8, name='jan_paid_rent8'),
path('table_jan_paid_rent8/', branch8.table_jan_paid_rent8, name='table_jan_paid_rent8'),
path('jan_full_paid_guest8/', reports8.jan_full_paid_guest8, name='jan_full_paid_guest8'),
path('jan_partially_paid_guest8/', reports8.jan_partially_paid_guest8, name='jan_partially_paid_guest8'),
path('table_jan_partially_paid_guest8/', reports8.table_jan_partially_paid_guest8,name='table_jan_partially_paid_guest8'),

path('feb_paid_rent8/', branch8.feb_paid_rent8, name='feb_paid_rent8'),
path('table_feb_paid_rent8/', branch8.table_feb_paid_rent8, name='table_feb_paid_rent8'),
path('feb_full_paid_guest8/', reports8.feb_full_paid_guest8, name='feb_full_paid_guest8'),
path('feb_partially_paid_guest8/', reports8.feb_partially_paid_guest8, name='feb_partially_paid_guest8'),
path('table_feb_partially_paid_guest8/', reports8.table_feb_partially_paid_guest8,name='table_feb_partially_paid_guest8'),

path('mar_paid_rent8/', branch8.mar_paid_rent8, name='mar_paid_rent8'),
path('table_mar_paid_rent8/', branch8.table_mar_paid_rent8, name='table_mar_paid_rent8'),
path('march_full_paid_guest8/', reports8.march_full_paid_guest8, name='march_full_paid_guest8'),
path('march_partially_paid_guest8/', reports8.march_partially_paid_guest8, name='march_partially_paid_guest8'),
path('table_march_partially_paid_guest8/', reports8.table_march_partially_paid_guest8,name='table_march_partially_paid_guest8'),

path('april_paid_rent8/', branch8.april_paid_rent8, name='april_paid_rent8'),
path('table_april_paid_rent8/', branch8.table_april_paid_rent8, name='table_april_paid_rent8'),
path('april_full_paid_guest8/', reports8.april_full_paid_guest8, name='april_full_paid_guest8'),
path('april_partially_paid_guest8/', reports8.april_partially_paid_guest8, name='april_partially_paid_guest8'),
path('table_april_partially_paid_guest8/', reports8.table_april_partially_paid_guest8,name='table_april_partially_paid_guest8'),

path('may_paid_rent8/', branch8.may_paid_rent8, name='may_paid_rent8'),
path('table_may_paid_rent8/', branch8.table_may_paid_rent8, name='table_may_paid_rent8'),
path('may_full_paid_guest8/', reports8.may_full_paid_guest8, name='may_full_paid_guest8'),
path('may_partially_paid_guest8/', reports8.may_partially_paid_guest8, name='may_partially_paid_guest8'),
path('table_may_partially_paid_guest8/', reports8.table_may_partially_paid_guest8, name='table_may_partially_paid_guest8'),

path('june_paid_rent8/', branch8.june_paid_rent8, name='june_paid_rent8'),
path('table_june_paid_rent8/', branch8.table_june_paid_rent8, name='table_june_paid_rent8'),
path('june_full_paid_guest8/', reports8.june_full_paid_guest8, name='june_full_paid_guest8'),
path('june_partially_paid_guest8/', reports8.june_partially_paid_guest8, name='june_partially_paid_guest8'),
path('table_june_partially_paid_guest8/', reports8.table_june_partially_paid_guest8, name='table_june_partially_paid_guest8'),

path('july_paid_rent8/', branch8.july_paid_rent8, name='july_paid_rent8'),
path('table_july_paid_rent8/', branch8.table_july_paid_rent8, name='table_july_paid_rent8'),
path('july_full_paid_guest8/', reports8.july_full_paid_guest8, name='july_full_paid_guest8'),
path('july_partially_paid_guest8/', reports8.july_partially_paid_guest8, name='july_partially_paid_guest8'),
path('table_july_partially_paid_guest8/', reports8.table_july_partially_paid_guest8, name='table_july_partially_paid_guest8'),

path('aug_paid_rent8/', branch8.aug_paid_rent8, name='aug_paid_rent8'),
path('table_aug_paid_rent8/', branch8.table_aug_paid_rent8, name='table_aug_paid_rent8'),
path('auguest_full_paid_guest8/', reports8.auguest_full_paid_guest8, name='auguest_full_paid_guest8'),
path('auguest_partially_paid_guest8/', reports8.auguest_partially_paid_guest8,name='auguest_partially_paid_guest8'),
path('table_auguest_partially_paid_guest8/', reports8.table_auguest_partially_paid_guest8,name='table_auguest_partially_paid_guest8'),

path('sept_paid_rent8/', branch8.sept_paid_rent8, name='sept_paid_rent8'),
path('table_sept_paid_rent8/', branch8.table_sept_paid_rent8, name='table_sept_paid_rent8'),
path('sept_full_paid_guest8/', reports8.sept_full_paid_guest8, name='sept_full_paid_guest8'),
path('sept_partially_paid_guest8/', reports8.sept_partially_paid_guest8, name='sept_partially_paid_guest8'),
path('table_sept_partially_paid_guest8/', reports8.table_sept_partially_paid_guest8,name='table_sept_partially_paid_guest8'),

path('oct_paid_rent8/', branch8.oct_paid_rent8, name='oct_paid_rent8'),
path('table_oct_paid_rent8/', branch8.table_oct_paid_rent8, name='table_oct_paid_rent8'),
path('october_full_paid_guest8/', reports8.october_full_paid_guest8, name='october_full_paid_guest8'),
path('october_partially_paid_guest8/', reports8.october_partially_paid_guest8,name='october_partially_paid_guest8'),
path('table_october_partially_paid_guest8/', reports8.table_october_partially_paid_guest8,name='table_october_partially_paid_guest8'),

path('nov_paid_rent8/', branch8.nov_paid_rent8, name='nov_paid_rent8'),
path('table_nov_paid_rent8/', branch8.table_nov_paid_rent8, name='table_nov_paid_rent8'),
path('nov_full_paid_guest8/', reports8.nov_full_paid_guest8, name='nov_full_paid_guest8'),
path('nov_partially_paid_guest8/', reports8.nov_partially_paid_guest8, name='nov_partially_paid_guest8'),
path('table_nov_partially_paid_guest8/', reports8.table_nov_partially_paid_guest8,name='table_nov_partially_paid_guest8'),

path('dec_paid_rent8/', branch8.dec_paid_rent8, name='dec_paid_rent8'),
path('table_dec_paid_rent8/', branch8.table_dec_paid_rent8, name='table_dec_paid_rent8'),
path('dec_full_paid_guest8/', reports8.dec_full_paid_guest8, name='dec_full_paid_guest8'),
path('dec_partially_paid_guest8/', reports8.dec_partially_paid_guest8, name='dec_partially_paid_guest8'),
path('table_dec_partially_paid_guest8/', reports8.table_dec_partially_paid_guest8,name='table_dec_partially_paid_guest8'),

path('details_of_paid_guests8/<id>',branch8.details_of_paid_guests8,name='details_of_paid_guests8'),
path('full_paid_guest8/',reports8.full_paid_guest8,name='full_paid_guest8'),

path('paid_rent_choose_months8/',branch8.paid_rent_choose_months8,name='paid_rent_choose_months8'),
path('partially_paid_guest_choose_months8/',reports8.partially_paid_guest_choose_months8,name='partially_paid_guest_choose_months8'),

path('jan_paid_rent8/', branch8.jan_paid_rent8, name='jan_paid_rent8'),
path('table_jan_paid_rent8/', branch8.table_jan_paid_rent8, name='table_jan_paid_rent8'),
path('jan_full_paid_guest8/', reports8.jan_full_paid_guest8, name='jan_full_paid_guest8'),
path('jan_partially_paid_guest8/', reports8.jan_partially_paid_guest8, name='jan_partially_paid_guest8'),
path('table_jan_partially_paid_guest8/', reports8.table_jan_partially_paid_guest8,name='table_jan_partially_paid_guest8'),

path('feb_paid_rent8/', branch8.feb_paid_rent8, name='feb_paid_rent8'),
path('table_feb_paid_rent8/', branch8.table_feb_paid_rent8, name='table_feb_paid_rent8'),
path('feb_full_paid_guest8/', reports8.feb_full_paid_guest8, name='feb_full_paid_guest8'),
path('feb_partially_paid_guest8/', reports8.feb_partially_paid_guest8, name='feb_partially_paid_guest8'),
path('table_feb_partially_paid_guest8/', reports8.table_feb_partially_paid_guest8,name='table_feb_partially_paid_guest8'),

path('mar_paid_rent8/', branch8.mar_paid_rent8, name='mar_paid_rent8'),
path('table_mar_paid_rent8/', branch8.table_mar_paid_rent8, name='table_mar_paid_rent8'),
path('march_full_paid_guest8/', reports8.march_full_paid_guest8, name='march_full_paid_guest8'),
path('march_partially_paid_guest8/', reports8.march_partially_paid_guest8, name='march_partially_paid_guest8'),
path('table_march_partially_paid_guest8/', reports8.table_march_partially_paid_guest8,name='table_march_partially_paid_guest8'),

path('april_paid_rent8/', branch8.april_paid_rent8, name='april_paid_rent8'),
path('table_april_paid_rent8/', branch8.table_april_paid_rent8, name='table_april_paid_rent8'),
path('april_full_paid_guest8/', reports8.april_full_paid_guest8, name='april_full_paid_guest8'),
path('april_partially_paid_guest8/', reports8.april_partially_paid_guest8, name='april_partially_paid_guest8'),
path('table_april_partially_paid_guest8/', reports8.table_april_partially_paid_guest8,name='table_april_partially_paid_guest8'),

path('may_paid_rent8/', branch8.may_paid_rent8, name='may_paid_rent8'),
path('table_may_paid_rent8/', branch8.table_may_paid_rent8, name='table_may_paid_rent8'),
path('may_full_paid_guest8/', reports8.may_full_paid_guest8, name='may_full_paid_guest8'),
path('may_partially_paid_guest8/', reports8.may_partially_paid_guest8, name='may_partially_paid_guest8'),
path('table_may_partially_paid_guest8/', reports8.table_may_partially_paid_guest8, name='table_may_partially_paid_guest8'),

path('june_paid_rent8/', branch8.june_paid_rent8, name='june_paid_rent8'),
path('table_june_paid_rent8/', branch8.table_june_paid_rent8, name='table_june_paid_rent8'),
path('june_full_paid_guest8/', reports8.june_full_paid_guest8, name='june_full_paid_guest8'),
path('june_partially_paid_guest8/', reports8.june_partially_paid_guest8, name='june_partially_paid_guest8'),
path('table_june_partially_paid_guest8/', reports8.table_june_partially_paid_guest8, name='table_june_partially_paid_guest8'),

path('july_paid_rent8/', branch8.july_paid_rent8, name='july_paid_rent8'),
path('table_july_paid_rent8/', branch8.table_july_paid_rent8, name='table_july_paid_rent8'),
path('july_full_paid_guest8/', reports8.july_full_paid_guest8, name='july_full_paid_guest8'),
path('july_partially_paid_guest8/', reports8.july_partially_paid_guest8, name='july_partially_paid_guest8'),
path('table_july_partially_paid_guest8/', reports8.table_july_partially_paid_guest8, name='table_july_partially_paid_guest8'),

path('aug_paid_rent8/', branch8.aug_paid_rent8, name='aug_paid_rent8'),
path('table_aug_paid_rent8/', branch8.table_aug_paid_rent8, name='table_aug_paid_rent8'),
path('auguest_full_paid_guest8/', reports8.auguest_full_paid_guest8, name='auguest_full_paid_guest8'),
path('auguest_partially_paid_guest8/', reports8.auguest_partially_paid_guest8,name='auguest_partially_paid_guest8'),
path('table_auguest_partially_paid_guest8/', reports8.table_auguest_partially_paid_guest8,name='table_auguest_partially_paid_guest8'),

path('sept_paid_rent8/', branch8.sept_paid_rent8, name='sept_paid_rent8'),
path('table_sept_paid_rent8/', branch8.table_sept_paid_rent8, name='table_sept_paid_rent8'),
path('sept_full_paid_guest8/', reports8.sept_full_paid_guest8, name='sept_full_paid_guest8'),
path('sept_partially_paid_guest8/', reports8.sept_partially_paid_guest8, name='sept_partially_paid_guest8'),
path('table_sept_partially_paid_guest8/', reports8.table_sept_partially_paid_guest8,name='table_sept_partially_paid_guest8'),

path('oct_paid_rent8/', branch8.oct_paid_rent8, name='oct_paid_rent8'),
path('table_oct_paid_rent8/', branch8.table_oct_paid_rent8, name='table_oct_paid_rent8'),
path('october_full_paid_guest8/', reports8.october_full_paid_guest8, name='october_full_paid_guest8'),
path('october_partially_paid_guest8/', reports8.october_partially_paid_guest8,name='october_partially_paid_guest8'),
path('table_october_partially_paid_guest8/', reports8.table_october_partially_paid_guest8,name='table_october_partially_paid_guest8'),

path('nov_paid_rent8/', branch8.nov_paid_rent8, name='nov_paid_rent8'),
path('table_nov_paid_rent8/', branch8.table_nov_paid_rent8, name='table_nov_paid_rent8'),
path('nov_full_paid_guest8/', reports8.nov_full_paid_guest8, name='nov_full_paid_guest8'),
path('nov_partially_paid_guest8/', reports8.nov_partially_paid_guest8, name='nov_partially_paid_guest8'),
path('table_nov_partially_paid_guest8/', reports8.table_nov_partially_paid_guest8,name='table_nov_partially_paid_guest8'),

path('dec_paid_rent8/', branch8.dec_paid_rent8, name='dec_paid_rent8'),
path('table_dec_paid_rent8/', branch8.table_dec_paid_rent8, name='table_dec_paid_rent8'),
path('dec_full_paid_guest8/', reports8.dec_full_paid_guest8, name='dec_full_paid_guest8'),
path('dec_partially_paid_guest8/', reports8.dec_partially_paid_guest8, name='dec_partially_paid_guest8'),
path('table_dec_partially_paid_guest8/', reports8.table_dec_partially_paid_guest8,name='table_dec_partially_paid_guest8'),

path('details_of_paid_guests8/<id>',branch8.details_of_paid_guests8,name='details_of_paid_guests8'),
path('full_paid_guest8/',reports8.full_paid_guest8,name='full_paid_guest8'),



#paid rent end here

#*********reports end here



##################################
#_ADVANCE8 START HERE
################################


path('choose_months_advance8/',branch8.choose_months_advance8,name='choose_months_advance8'),

path('jan_advance8/', branch8.jan_advance8, name='jan_advance8'),
path('jan_make_payments_advance8/<id>', branch8.jan_make_payments_advance8,name='jan_make_payments_advance8'),
path('feb_advance8/', branch8.feb_advance8, name='feb_advance8'),
path('feb_make_payments_advance8/<id>', branch8.feb_make_payments_advance8,name='feb_make_payments_advance8'),
path('march_advance8/', branch8.march_advance8, name='march_advance8'),
path('march_make_payments_advance8/<id>', branch8.march_make_payments_advance8,name='march_make_payments_advance8'),
path('april_advance8/', branch8.april_advance8, name='april_advance8'),
path('april_make_payments_advance8/<id>', branch8.april_make_payments_advance8, name='april_make_payments_advance8'),

path('may_advance8/',branch8.may_advance8,name='may_advance8'),
path('may_make_payments_advance8/<id>', branch8.may_make_payments_advance8, name='may_make_payments_advance8'),
path('june_advance8/',branch8.june_advance8,name='june_advance8'),
path('june_make_payments_advance8/<id>', branch8.june_make_payments_advance8, name='june_make_payments_advance8'),
path('july_advance8/',branch8.july_advance8,name='july_advance8'),
path('july_make_payments_advance8/<id>', branch8.july_make_payments_advance8, name='july_make_payments_advance8'),
path('auguest_advance8/', branch8.auguest_advance8, name='auguest_advance8'),
path('auguest_make_payments_advance8/<id>', branch8.auguest_make_payments_advance8, name='auguest_make_payments_advance8'),

path('sept_advance8/', branch8.sept_advance8, name='sept_advance8'),
path('sept_make_payments_advance8/<id>', branch8.sept_make_payments_advance8,name='sept_make_payments_advance8'),
path('october_advance8/', branch8.october_advance8, name='october_advance8'),
path('october_make_payments_advance8/<id>', branch8.october_make_payments_advance8, name='october_make_payments_advance8'),
path('nov_advance8/', branch8.nov_advance8, name='nov_advance8'),
path('nov_make_payments_advance8/<id>', branch8.nov_make_payments_advance8,name='nov_make_payments_advance8'),
path('dec_advance8/', branch8.dec_advance8, name='dec_advance8'),
path('dec_make_payments_advance8/<id>', branch8.dec_make_payments_advance8, name='dec_make_payments_advance8'),



##################################
#_ADVANCE8 END HERE
################################


##################################
#PAYMENTS START HERE
################################

    path('choose_months8/',branch8.choose_months8,name='choose_months8'),

    path('jan8/',branch8.jan8,name='jan8'),
    path('jan_manke_payments8/<id>',branch8.jan_manke_payments8,name='jan_manke_payments8'),

    path('feb8/',branch8.feb8,name='feb8'),
    path('feb_manke_payments8/<id>',branch8.feb_manke_payments8,name='feb_manke_payments8'),

    path('march8/',branch8.march8,name='march8'),
    path('march_manke_payments8/<id>',branch8.march_manke_payments8,name='march_manke_payments8'),

    path('april8/',branch8.april8,name='april8'),
    path('april_make_payments8/<id>',branch8.april_make_payments8,name='april_make_payments8'),

    path('may8/',branch8.may8,name='may8'),
    path('may_make_payments8/<id>',branch8.may_make_payments8,name='may_make_payments8'),

    path('june8/',branch8.june8,name='june8'),
    path('june_make_payments8/<id>',branch8.june_make_payments8,name='june_make_payments8'),

    path('july8/',branch8.july8,name='july8'),
    path('july_make_payments8/<id>',branch8.july_make_payments8,name='july_make_payments8'),

    path('aug8/',branch8.aug8,name='aug8'),
    path('aug_make_payments8/<id>',branch8.aug_make_payments8,name='aug_make_payments8'),

    path('sept8/',branch8.sept8,name='sept8'),
    path('sept_make_payments8/<id>',branch8.sept_make_payments8,name='sept_make_payments8'),

    path('oct8/',branch8.oct8,name='oct8'),
    path('oct_make_payments8/<id>',branch8.oct_make_payments8,name='oct_make_payments8'),

    path('nov8/',branch8.nov8,name='nov8'),
    path('nov_make_payments8/<id>',branch8.nov_make_payments8,name='nov_make_payments8'),

    path('dec8/',branch8.dec8,name='dec8'),
    path('dec_make_payments8/<id>',branch8.dec_make_payments8,name='dec_make_payments8'),

##################################
#PAYMENTS END HERE
################################


##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user8/', payment8.choose_user8, name='choose_user8'),
    path('payment_user_details8/<id>', payment8.payment_user_details8, name='payment_user_details8'),
    path('close_choose_user8/<id>', payment8.close_choose_user8, name='close_choose_user8'),

    path('monthly_jan_make_payments8/<id>', payment8.monthly_jan_make_payments8, name='monthly_jan_make_payments8'),
    path('monthly_feb_make_payments8/<id>', payment8.monthly_feb_make_payments8, name='monthly_feb_make_payments8'),
    path('monthly_march_make_payments8/<id>', payment8.monthly_march_make_payments8, name='monthly_march_make_payments8'),
    path('monthly_april_make_payments8/<id>', payment8.monthly_april_make_payments8, name='monthly_april_make_payments8'),
    path('monthly_may_make_payments8/<id>', payment8.monthly_may_make_payments8, name='monthly_may_make_payments8'),
    path('monthly_june_make_payments8/<id>', payment8.monthly_june_make_payments8, name='monthly_june_make_payments8'),

    path('monthly_july_make_payments8/<id>', payment8.monthly_july_make_payments8, name='monthly_july_make_payments8'),
    path('monthly_aug_make_payments8/<id>', payment8.monthly_aug_make_payments8, name='monthly_aug_make_payments8'),
    path('monthly_sept_make_payments8/<id>', payment8.monthly_sept_make_payments8, name='monthly_sept_make_payments8'),
    path('monthly_oct_make_payments8/<id>', payment8.monthly_oct_make_payments8, name='monthly_oct_make_payments8'),
    path('monthly_nov_make_payments8/<id>', payment8.monthly_nov_make_payments8, name='monthly_nov_make_payments8'),
    path('monthly_dec_make_payments8/<id>', payment8.monthly_dec_make_payments8, name='monthly_dec_make_payments8'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################



    ##################################
    # MONTHLY MANAGEMENT PAYMENTS START HERE
    ################################

    path('choose_user8/', payment8.choose_user8, name='choose_user8'),
    path('payment_user_details8/<id>', payment8.payment_user_details8, name='payment_user_details8'),

    path('monthly_jan_make_payments8/<id>', payment8.monthly_jan_make_payments8, name='monthly_jan_make_payments8'),
    path('monthly_feb_make_payments8/<id>', payment8.monthly_feb_make_payments8, name='monthly_feb_make_payments8'),
    path('monthly_march_make_payments8/<id>', payment8.monthly_march_make_payments8,
         name='monthly_march_make_payments8'),
    path('monthly_april_make_payments8/<id>', payment8.monthly_april_make_payments8,
         name='monthly_april_make_payments8'),
    path('monthly_may_make_payments8/<id>', payment8.monthly_may_make_payments8, name='monthly_may_make_payments8'),
    path('monthly_june_make_payments8/<id>', payment8.monthly_june_make_payments8, name='monthly_june_make_payments8'),

    path('monthly_july_make_payments8/<id>', payment8.monthly_july_make_payments8, name='monthly_july_make_payments8'),
    path('monthly_aug_make_payments8/<id>', payment8.monthly_aug_make_payments8, name='monthly_aug_make_payments8'),
    path('monthly_sept_make_payments8/<id>', payment8.monthly_sept_make_payments8, name='monthly_sept_make_payments8'),
    path('monthly_oct_make_payments8/<id>', payment8.monthly_oct_make_payments8, name='monthly_oct_make_payments8'),
    path('monthly_nov_make_payments8/<id>', payment8.monthly_nov_make_payments8, name='monthly_nov_make_payments8'),
    path('monthly_dec_make_payments8/<id>', payment8.monthly_dec_make_payments8, name='monthly_dec_make_payments8'),

    ##################################
    # MONTHLY MANAGEMENT PAYMENTS END HERE
    ################################

    ##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general8/',branch8.detail_guest_general8,name='detail_guest_general8'),

    path('jan_print8/',branch8.jan_print8,name='jan_print8'),
    path('feb_print8/',branch8.feb_print8,name='feb_print8'),
    path('march_print8/',branch8.march_print8,name='march_print8'),
    path('april_print8/',branch8.april_print8,name='april_print8'),

    path('may_print8/',branch8.may_print8,name='may_print8'),
    path('june_print8/',branch8.june_print8,name='june_print8'),
    path('july_print8/', branch8.july_print8, name='july_print8'),
    path('aug_print8/', branch8.aug_print8, name='aug_print8'),

    path('sept_print8/', branch8.sept_print8, name='sept_print8'),
    path('oct_print8/', branch8.oct_print8, name='oct_print8'),
    path('nov_print8/', branch8.nov_print8, name='nov_print8'),
    path('dec_print8/', branch8.dec_print8, name='dec_print8'),

##################################
#PRINT OUTS END HERE
################################


########################################
# CLOSE MONTHS START HERE
###########################

    path('jan_close8/', branch8.jan_close8, name='jan_close8'),
    path('jan_close_decision_page8/', branch8.jan_close_decision_page8, name='jan_close_decision_page8'),
    path('feb_close8/', branch8.feb_close8, name='feb_close8'),
    path('feb_close_decision_page8/', branch8.feb_close_decision_page8, name='feb_close_decision_page8'),
    path('mar_close8/', branch8.mar_close8, name='mar_close8'),
    path('mar_close_decision_page/', branch8.mar_close_decision_page8, name='mar_close_decision_page8'),
    path('apr_close8/', branch8.apr_close8, name='apr_close8'),
    path('apr_close_decision_page8/', branch8.apr_close_decision_page8, name='apr_close_decision_page8'),

    path('may_close8/', branch8.may_close8, name='may_close8'),
    path('may_close_decision_page8/', branch8.may_close_decision_page8, name='may_close_decision_page8'),
    path('jun_close8/', branch8.jun_close8, name='jun_close8'),
    path('jun_close_decision_page8/', branch8.jun_close_decision_page8, name='jun_close_decision_page8'),
    path('jul_close8/', branch8.jul_close8, name='jul_close8'),
    path('jul_close_decision_page8/', branch8.jul_close_decision_page8, name='jul_close_decision_page8'),
    path('aug_close8/', branch8.aug_close8, name='aug_close8'),
    path('aug_close_decision_page8/', branch8.aug_close_decision_page8, name='aug_close_decision_page8'),

    path('sep_close8/', branch8.sep_close8, name='sep_close8'),
    path('sep_close_decision_page8/', branch8.sep_close_decision_page8, name='sep_close_decision_page8'),
    path('oct_close8/', branch8.oct_close8, name='oct_close8'),
    path('oct_close_decision_page8/', branch8.oct_close_decision_page8, name='oct_close_decision_page8'),
    path('nov_close8/', branch8.nov_close8, name='nov_close8'),
    path('nov_close_decision_page8/', branch8.nov_close_decision_page8, name='nov_close_decision_page8'),



########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months8/',reports8.detailed_report_choose_months8,name='detailed_report_choose_months8'),

    path('jan_details_live8/', reports8.jan_details_live8, name='jan_details_live8'),
    path('jan_print_live8/', reports8.jan_print_live8, name='jan_print_live8'),
    path('feb_details_live8/', reports8.feb_details_live8, name='feb_details_live8'),
    path('feb_print_live8/', reports8.feb_print_live8, name='feb_print_live8'),
    path('march_details_live8/', reports8.march_details_live8, name='march_details_live8'),
    path('march_print_live8/', reports8.march_print_live8, name='march_print_live8'),

    path('april_details_live8/', reports8.april_details_live8, name='april_details_live8'),
    path('april_print_live8/', reports8.april_print_live8, name='april_print_live8'),
    path('may_details_live8/', reports8.may_details_live8, name='may_details_live8'),
    path('may_print_live8/', reports8.may_print_live8, name='may_print_live8'),
    path('june_details_live8/',reports8.june_details_live8,name='june_details_live8'),
    path('june_print_live8/', reports8.june_print_live8, name='june_print_live8'),

    path('july_details_live8/', reports8.july_details_live8, name='july_details_live8'),
    path('july_print_live8/', reports8.july_print_live8, name='july_print_live8'),
    path('auguest_details_live8/', reports8.auguest_details_live8, name='auguest_details_live8'),
    path('auguest_print_live8/', reports8.auguest_print_live8, name='auguest_print_live8'),
    path('sept_details_live8/', reports8.sept_details_live8, name='sept_details_live8'),
    path('sept_print_live8/', reports8.sept_print_live8, name='sept_print_live8'),

    path('october_details_live8/', reports8.october_details_live8, name='october_details_live8'),
    path('october_print_live8/', reports8.october_print_live8, name='october_print_live8'),
    path('nov_details_live8/', reports8.nov_details_live8, name='nov_details_live8'),
    path('nov_print_live8/', reports8.nov_print_live8, name='nov_print_live8'),
    path('dec_details_live8/', reports8.dec_details_live8, name='dec_details_live8'),
    path('dec_print_live8/', reports8.dec_print_live8, name='dec_print_live8'),

########################################
#  DETAILED REPORT END HERE
###########################




    path('viewall_vaccant_room8/', reports8.viewall_vaccant_room8, name='viewall_vaccant_room8'),

    #path('d8/', branch8.dynamic, name='dynamic'),

    #path('manage_bed8/', branch8.manage_bed8, name='manage_bed8'),
    #path('manage_new_guest8/', branch8.manage_new_guest8, name='manage_new_guest8'),
    #path('manage_update_new_guest8/<id>', branch8.manage_update_new_guest8, name='manage_update_new_guest8'),
    #path('manage_update_beds8/<id>', branch8.manage_update_beds8, name='manage_update_beds8'),

########################################
# CLOSE MONTHS END HERE
###########################


########################################
# DUE AMT MANAGEMENT START HERE
###########################

path('view_all_due_amt8/', branch8.view_all_due_amt8, name='view_all_due_amt8'),
path('due_amt_mgt_choose_months8/', branch8.due_amt_mgt_choose_months8, name='due_amt_mgt_choose_months8'),

path('view_jan_account_details8/', branch8.view_jan_account_details8, name='view_jan_account_details8'),
path('jan_account_mgt8/<id>',branch8.jan_account_mgt8,name='jan_account_mgt8'),
path('view_feb_account_details8/', branch8.view_feb_account_details8, name='view_feb_account_details8'),
path('feb_account_mgt8/<id>',branch8.feb_account_mgt8,name='feb_account_mgt8'),
path('view_march_account_details8/', branch8.view_march_account_details8, name='view_march_account_details8'),
path('march_account_mgt8/<id>',branch8.march_account_mgt8,name='march_account_mgt8'),
path('view_april_account_details8/', branch8.view_april_account_details8, name='view_april_account_details8'),
path('april_account_mgt8/<id>',branch8.april_account_mgt8,name='april_account_mgt8'),

path('view_may_account_details8/',branch8.view_may_account_details8,name='view_may_account_details8'),
path('may_account_mgt8/<id>', branch8.may_account_mgt8, name='may_account_mgt8'),
path('view_june_account_details8/', branch8.view_june_account_details8, name='view_june_account_details8'),
path('june_account_mgt8/<id>',branch8.june_account_mgt8,name='june_account_mgt8'),
path('view_july_account_details8/', branch8.view_july_account_details8, name='view_july_account_details8'),
path('july_account_mgt8/<id>',branch8.july_account_mgt8,name='july_account_mgt8'),
path('view_auguest_account_details8/', branch8.view_auguest_account_details8, name='view_auguest_account_details8'),
path('auguest_account_mgt8/<id>',branch8.auguest_account_mgt8,name='auguest_account_mgt8'),

path('view_sept_account_details8/', branch8.view_sept_account_details8, name='view_sept_account_details8'),
path('sept_account_mgt8/<id>',branch8.sept_account_mgt8,name='sept_account_mgt8'),
path('view_october_account_details8/', branch8.view_october_account_details8, name='view_october_account_details8'),
path('october_account_mgt8/<id>',branch8.october_account_mgt8,name='october_account_mgt8'),
path('view_nov_account_details8/', branch8.view_nov_account_details8, name='view_nov_account_details8'),
path('nov_account_mgt8/<id>',branch8.nov_account_mgt8,name='nov_account_mgt8'),
path('view_dec_account_details8/', branch8.view_dec_account_details8, name='view_dec_account_details8'),
path('dec_account_mgt8/<id>',branch8.dec_account_mgt8,name='dec_account_mgt8'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################



##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest8/',branch8.viewall_vacate_guest8,name='viewall_vacate_guest8'),
    path('details_of_vacate_guest8/<id>',branch8.details_of_vacate_guest8,name='details_of_vacate_guest8'),
    path('full_vacated_guest_details8',branch8.full_vacated_guest_details8,name='full_vacated_guest_details8'),
    path('full_vacated_guest_table8',branch8.full_vacated_guest_table8,name='full_vacated_guest_table8'),

    path('guest_details8/<guest_code>', branch8.guest_details8, name='guest_details8'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate8/<id>', branch8.jan_manke_payments_vacate8, name='jan_manke_payments_vacate8'),
    path('feb_manke_payments_vacate8/<id>', branch8.feb_manke_payments_vacate8, name='feb_manke_payments_vacate8'),
    path('march_manke_payments_vacate8/<id>', branch8.march_manke_payments_vacate8, name='march_manke_payments_vacate8'),
    path('april_make_payments_vacate8/<id>', branch8.april_make_payments_vacate8, name='april_make_payments_vacate8'),

    path('may_make_payments_vacate8/<id>', branch8.may_make_payments_vacate8, name='may_make_payments_vacate8'),
    path('june_make_payments_vacate8/<id>', branch8.june_make_payments_vacate8, name='june_make_payments_vacate8'),
    path('july_make_payments_vacate8/<id>', branch8.july_make_payments_vacate8, name='july_make_payments_vacate8'),
    path('aug_make_payments_vacate8/<id>', branch8.aug_make_payments_vacate8, name='aug_make_payments_vacate8'),

    path('sept_make_payments_vacate8/<id>', branch8.sept_make_payments_vacate8, name='sept_make_payments_vacate8'),
    path('oct_make_payments_vacate8/<id>', branch8.oct_make_payments_vacate8, name='oct_make_payments_vacate8'),
    path('nov_make_payments_vacate8/<id>', branch8.nov_make_payments_vacate8, name='nov_make_payments_vacate8'),
    path('dec_make_payments_vacate8/<id>', branch8.dec_make_payments_vacate8, name='dec_make_payments_vacate8'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due8', admin_dashboard_calculations_br8.monthly_details_due8, name='monthly_details_due8'),
    path('monthly_collection_details8/', admin_dashboard_calculations_br8.monthly_collection_details8, name='monthly_collection_details8'),

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

    path('view_all_category8/', accounts8.view_all_category8, name='view_all_category8'),
    path('create_new_category8/', accounts8.create_new_category8, name='create_new_category8'),
    path('regi_new_category8/', accounts8.regi_new_category8, name='regi_new_category8'),
    path('update_category8/<id>',accounts8.update_category8,name='update_category8'),

    path('delete_category8/<id>', accounts8.delete_category8, name='delete_category8'),
    path('view_all_category_delete8/', accounts8.view_all_category_delete8, name='view_all_category_delete8'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items8/', accounts8.view_all_items8, name='view_all_items8'),
    path('create_new_item8/', accounts8.create_new_item8, name='create_new_item8'),
    path('regi_new_item8/', accounts8.regi_new_item8, name='regi_new_item8'),
    path('delete_item8/<id>',accounts8.delete_item8,name='delete_item8'),
    path('update_item8/<id>', accounts8.update_item8, name='update_item8'),
    path('view_all_items_delete8/',accounts8.view_all_items_delete8,name='view_all_items_delete8'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger8/', accounts8.view_all_ledger8, name='view_all_ledger8'),
    path('create_new_ledger8/', accounts8.create_new_ledger8, name='create_new_ledger8'),
    path('regi_new_ledger8/', accounts8.regi_new_ledger8, name='regi_new_ledger8'),
    path('delete_ledger8/<id>',accounts8.delete_ledger8,name='delete_ledger8'),
    path('update_ledger8/<id>',accounts8.update_ledger8,name='update_ledger8'),
    path('view_all_ledger_delete8/',accounts8.view_all_ledger_delete8,name='view_all_ledger_delete8'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book8/', accounts8.view_all_accounts_book8, name='view_all_accounts_book8'),
    path('create_new_accounts_book8/', accounts8.create_new_accounts_book8, name='create_new_accounts_book8'),
    path('regi_new_accounts_book8/', accounts8.regi_new_accounts_book8, name='regi_new_accounts_book8'),
    path('update_accounts_book8/<id>',accounts8.update_accounts_book8,name='update_accounts_book8'),
    path('delete_accounts_book8/<id>',accounts8.delete_accounts_book8,name='delete_accounts_book8'),
    path('view_all_accounts_book_delete8/',accounts8.view_all_accounts_book_delete8,name='view_all_accounts_book_delete8'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries8/', accounts8.get_countries8, name='get_countries8'),

    path('in_exp_items_entry8/', accounts8.in_exp_items_entry8, name='in_exp_items_entry8'),
    path('reg_in_exp_items_entry8/', accounts8.reg_in_exp_items_entry8, name='reg_in_exp_items_entry8'),
    path('delete_journal8/<id>',accounts8.delete_journal8,name='delete_journal8'),
    path('update_in_exp_items_entry8/<id>',accounts8.update_in_exp_items_entry8,name='update_in_exp_items_entry8'),
    path('detailed_journal_report8/',accounts8.detailed_journal_report8,name='detailed_journal_report8'),
    path('journal_report_deleted8/',accounts8.journal_report_deleted8,name='journal_report_deleted8'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise8/', accounts8.daily_category_wise8, name='daily_category_wise8'),
    path('monthly_category_based_reports8/',accounts8.monthly_category_based_reports8,name='monthly_category_based_reports8'),
    path('yearly_category_based_reports8/', accounts8.yearly_category_based_reports8,name='yearly_category_based_reports8'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed8/', accounts8.daily_detailed8, name='daily_detailed8'),
    path('monthly_detailed8/',accounts8.monthly_detailed8,name='monthly_detailed8'),
    path('yearly_detailed8/',accounts8.yearly_detailed8,name='yearly_detailed8'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports8/', accounts8.item_based_reports8, name='item_based_reports8'),
    path('daily_item_based_reports8/',accounts8.daily_item_based_reports8,name='daily_item_based_reports8'),
    path('monthly_item_based_reports8/',accounts8.monthly_item_based_reports8,name='monthly_item_based_reports8'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports8/', accounts8.ledger_based_reports8, name='ledger_based_reports8'),
    path('monthly_ledger_based_reports8/', accounts8.monthly_ledger_based_reports8, name='monthly_ledger_based_reports8'),
    path('daily_ledger_based_reports8/',accounts8.daily_ledger_based_reports8,name='daily_ledger_based_reports8'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports8/', accounts8.accounts_book_based_reports8, name='accounts_book_based_reports8'),
    path('daily_accounts_book_based_reports8/',accounts8.daily_accounts_book_based_reports8,name='daily_accounts_book_based_reports8'),
    path('monthly_accounts_book_based_reports8/',accounts8.monthly_accounts_book_based_reports8,name='monthly_accounts_book_based_reports8'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months8/', accounts8.monthly_reports_choose_months8, name='monthly_reports_choose_months8'),
    path('monthly_detailed_daily_in_exp_items_report8/<mo>',accounts8.monthly_detailed_daily_in_exp_items_report8,name='monthly_detailed_daily_in_exp_items_report8'),

    path('single_monthly_reports_choose_months8/', accounts8.single_monthly_reports_choose_months8,name='single_monthly_reports_choose_months8'),
    path('single_monthly_daily_in_exp_items_report8/<mo>',accounts8.single_monthly_daily_in_exp_items_report8,name='single_monthly_daily_in_exp_items_report8'),

    path('accounts_dash_board8/',accounts8.accounts_dash_board8,name='accounts_dash_board8'),

    path('profit_sharing_choose_months8', accounts8.profit_sharing_choose_months8,name='profit_sharing_choose_months8'),
    path('profit_sharing8/<mo>', accounts8.profit_sharing8, name='profit_sharing8'),
    path('view_share_holders8', accounts8.view_share_holders8, name='view_share_holders8'),
    path('create_share_holders8', accounts8.create_share_holders8, name='create_share_holders8'),
    path('regi_share_holders8', accounts8.regi_share_holders8, name='regi_share_holders8'),
    path('update_share_holders8/<id>', accounts8.update_share_holders8, name='update_share_holders8'),
    path('delete_share_holders8/<id>', accounts8.delete_share_holders8, name='delete_share_holders8'),
    path('view_deleted_share_holders8', accounts8.view_deleted_share_holders8, name='view_deleted_share_holders8'),

]

