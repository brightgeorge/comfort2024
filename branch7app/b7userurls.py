from django.urls import path, include

#from . import admin_branch7
from . import admin_branch7
from . import branch7
from . import reports7
from . import payment7
from . import admin_dashboard_calculations_br7
from . import accounts7


urlpatterns = [
    path('branch1_dashboard7/', branch7.branch1_dashboard7, name='branch1_dashboard7'),
    path('user_dashboard_calculations_ob_ch7/',branch7.user_dashboard_calculations_ob_ch7,name='user_dashboard_calculations_ob_ch7'),

#**room creation start here
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi7/',admin_branch7.branch1_room_create_regi7,name='branch1_room_create_regi7'),
    path('view_all_room7/',admin_branch7.view_all_room7,name='view_all_room7'),
    path('delete_room7/<id>',admin_branch7.delete_room7,name='delete_room7'),

    path('branch1_room_create7/',admin_branch7.branch1_room_create7,name='branch1_room_create7'),

    path('multiple_branch1_room_create_regi7/',admin_branch7.multiple_branch1_room_create_regi7,name='multiple_branch1_room_create_regi7'),

#**room creation end here


#bed creation start here

    path('pg1_bed_create_regi7/', admin_branch7.pg1_bed_create_regi7, name='pg1_bed_create_regi7'),
    path('pg1_view_all_beds7/', admin_branch7.pg1_view_all_beds7, name='pg1_view_all_beds7'),
    path('delete_bed7/<id>', admin_branch7.delete_bed7, name='delete_bed7'),

    path('pg1_bed_create7/', admin_branch7.pg1_bed_create7, name='pg1_bed_create7'),

    path('single_pg1_bed_create_regi7/',admin_branch7.single_pg1_bed_create_regi7,name='single_pg1_bed_create_regi7'),
    path('update_bed_basic_details7/<id>',admin_branch7.update_bed_basic_details7, name='update_bed_basic_details7'),

    path('multiple_single_pg1_bed_create_regi7/',admin_branch7.multiple_single_pg1_bed_create_regi7,name='multiple_single_pg1_bed_create_regi7'),

#bed creation end here

#guest
    path('br1_admit_guest7/<id>',branch7.br1_admit_guest7,name='br1_admit_guest7'),
    path('view_all_new_guest7/',branch7.view_all_new_guest7,name='view_all_new_guest7'),
    path('update_br1_admit_guest7/<id>',branch7.update_br1_admit_guest7,name='update_br1_admit_guest7'),
    path('vacate_br1_guest7/<id>',branch7.vacate_br1_guest7,name='vacate_br1_guest7'),

    path('active_guest_details7/<guest_code>',branch7.active_guest_details7,name='active_guest_details7'),
    path('view_all_guest7/',branch7.view_all_guest7,name='view_all_guest7'),
    path('shift_guest7/<id>',branch7.shift_guest7,name='shift_guest7'),
    path('shift_guest_regi7/',branch7.shift_guest_regi7,name='shift_guest_regi7'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),

    path('multiple_br1_admit_guest7/<id>',branch7.multiple_br1_admit_guest7,name='multiple_br1_admit_guest7'),

#guest end here


#*********reports start here

#unpaid rent start here
    path('unpaid_rent_choose_months7/',branch7.unpaid_rent_choose_months7,name='unpaid_rent_choose_months7'),

    path('jan_unpaid_rent7/', branch7.jan_unpaid_rent7, name='jan_unpaid_rent7'),
    path('table_jan_unpaid_rent7/', branch7.table_jan_unpaid_rent7, name='table_jan_unpaid_rent7'),
    path('feb_unpaid_rent7/', branch7.feb_unpaid_rent7, name='feb_unpaid_rent7'),
    path('table_feb_unpaid_rent7/', branch7.table_feb_unpaid_rent7, name='table_feb_unpaid_rent7'),
    path('mar_unpaid_rent7/', branch7.mar_unpaid_rent7, name='mar_unpaid_rent7'),
    path('table_mar_unpaid_rent7/', branch7.table_mar_unpaid_rent7, name='table_mar_unpaid_rent7'),
    path('april_unpaid_rent7/', branch7.april_unpaid_rent7, name='april_unpaid_rent7'),
    path('table_april_unpaid_rent7/', branch7.table_april_unpaid_rent7, name='table_april_unpaid_rent7'),

    path('may_unpaid_rent7/', branch7.may_unpaid_rent7, name='may_unpaid_rent7'),
    path('table_may_unpaid_rent7/', branch7.table_may_unpaid_rent7, name='table_may_unpaid_rent7'),
    path('june_unpaid_rent7/', branch7.june_unpaid_rent7, name='june_unpaid_rent7'),
    path('table_june_unpaid_rent7/', branch7.table_june_unpaid_rent7, name='table_june_unpaid_rent7'),
    path('july_unpaid_rent7/', branch7.july_unpaid_rent7, name='july_unpaid_rent7'),
    path('table_july_unpaid_rent7',branch7.table_july_unpaid_rent7,name='table_july_unpaid_rent7'),
    path('aug_unpaid_rent7/', branch7.aug_unpaid_rent7, name='aug_unpaid_rent7'),
    path('table_aug_unpaid_rent7/',branch7.table_aug_unpaid_rent7,name='table_aug_unpaid_rent7'),

    path('sept_unpaid_rent7/', branch7.sept_unpaid_rent7, name='sept_unpaid_rent7'),
    path('table_sept_unpaid_rent7/', branch7.table_sept_unpaid_rent7, name='table_sept_unpaid_rent7'),
    path('oct_unpaid_rent7/', branch7.oct_unpaid_rent7, name='oct_unpaid_rent7'),
    path('table_oct_unpaid_rent7/', branch7.table_oct_unpaid_rent7, name='table_oct_unpaid_rent7'),
    path('nov_unpaid_rent7/', branch7.nov_unpaid_rent7, name='nov_unpaid_rent7'),
    path('table_nov_unpaid_rent7/', branch7.table_nov_unpaid_rent7, name='table_nov_unpaid_rent7'),
    path('dec_unpaid_rent7/', branch7.dec_unpaid_rent7, name='dec_unpaid_rent7'),
    path('table_dec_unpaid_rent7/', branch7.table_dec_unpaid_rent7, name='table_dec_unpaid_rent7'),

    path('details_of_unpaid_guests7/<id>',branch7.details_of_unpaid_guests7,name='details_of_unpaid_guests7'),

#unpaid rent end here

#paid rent start here


path('paid_rent_choose_months7/',branch7.paid_rent_choose_months7,name='paid_rent_choose_months7'),
path('partially_paid_guest_choose_months7/',reports7.partially_paid_guest_choose_months7,name='partially_paid_guest_choose_months7'),

path('jan_paid_rent7/', branch7.jan_paid_rent7, name='jan_paid_rent7'),
path('table_jan_paid_rent7/', branch7.table_jan_paid_rent7, name='table_jan_paid_rent7'),
path('jan_full_paid_guest7/', reports7.jan_full_paid_guest7, name='jan_full_paid_guest7'),
path('jan_partially_paid_guest7/', reports7.jan_partially_paid_guest7, name='jan_partially_paid_guest7'),
path('table_jan_partially_paid_guest7/', reports7.table_jan_partially_paid_guest7,name='table_jan_partially_paid_guest7'),

path('feb_paid_rent7/', branch7.feb_paid_rent7, name='feb_paid_rent7'),
path('table_feb_paid_rent7/', branch7.table_feb_paid_rent7, name='table_feb_paid_rent7'),
path('feb_full_paid_guest7/', reports7.feb_full_paid_guest7, name='feb_full_paid_guest7'),
path('feb_partially_paid_guest7/', reports7.feb_partially_paid_guest7, name='feb_partially_paid_guest7'),
path('table_feb_partially_paid_guest7/', reports7.table_feb_partially_paid_guest7,name='table_feb_partially_paid_guest7'),

path('mar_paid_rent7/', branch7.mar_paid_rent7, name='mar_paid_rent7'),
path('table_mar_paid_rent7/', branch7.table_mar_paid_rent7, name='table_mar_paid_rent7'),
path('march_full_paid_guest7/', reports7.march_full_paid_guest7, name='march_full_paid_guest7'),
path('march_partially_paid_guest7/', reports7.march_partially_paid_guest7, name='march_partially_paid_guest7'),
path('table_march_partially_paid_guest7/', reports7.table_march_partially_paid_guest7,name='table_march_partially_paid_guest7'),

path('april_paid_rent7/', branch7.april_paid_rent7, name='april_paid_rent7'),
path('table_april_paid_rent7/', branch7.table_april_paid_rent7, name='table_april_paid_rent7'),
path('april_full_paid_guest7/', reports7.april_full_paid_guest7, name='april_full_paid_guest7'),
path('april_partially_paid_guest7/', reports7.april_partially_paid_guest7, name='april_partially_paid_guest7'),
path('table_april_partially_paid_guest7/', reports7.table_april_partially_paid_guest7,name='table_april_partially_paid_guest7'),

path('may_paid_rent7/', branch7.may_paid_rent7, name='may_paid_rent7'),
path('table_may_paid_rent7/', branch7.table_may_paid_rent7, name='table_may_paid_rent7'),
path('may_full_paid_guest7/', reports7.may_full_paid_guest7, name='may_full_paid_guest7'),
path('may_partially_paid_guest7/', reports7.may_partially_paid_guest7, name='may_partially_paid_guest7'),
path('table_may_partially_paid_guest7/', reports7.table_may_partially_paid_guest7, name='table_may_partially_paid_guest7'),

path('june_paid_rent7/', branch7.june_paid_rent7, name='june_paid_rent7'),
path('table_june_paid_rent7/', branch7.table_june_paid_rent7, name='table_june_paid_rent7'),
path('june_full_paid_guest7/', reports7.june_full_paid_guest7, name='june_full_paid_guest7'),
path('june_partially_paid_guest7/', reports7.june_partially_paid_guest7, name='june_partially_paid_guest7'),
path('table_june_partially_paid_guest7/', reports7.table_june_partially_paid_guest7, name='table_june_partially_paid_guest7'),

path('july_paid_rent7/', branch7.july_paid_rent7, name='july_paid_rent7'),
path('table_july_paid_rent7/', branch7.table_july_paid_rent7, name='table_july_paid_rent7'),
path('july_full_paid_guest7/', reports7.july_full_paid_guest7, name='july_full_paid_guest7'),
path('july_partially_paid_guest7/', reports7.july_partially_paid_guest7, name='july_partially_paid_guest7'),
path('table_july_partially_paid_guest7/', reports7.table_july_partially_paid_guest7, name='table_july_partially_paid_guest7'),

path('aug_paid_rent7/', branch7.aug_paid_rent7, name='aug_paid_rent7'),
path('table_aug_paid_rent7/', branch7.table_aug_paid_rent7, name='table_aug_paid_rent7'),
path('auguest_full_paid_guest7/', reports7.auguest_full_paid_guest7, name='auguest_full_paid_guest7'),
path('auguest_partially_paid_guest7/', reports7.auguest_partially_paid_guest7,name='auguest_partially_paid_guest7'),
path('table_auguest_partially_paid_guest7/', reports7.table_auguest_partially_paid_guest7,name='table_auguest_partially_paid_guest7'),

path('sept_paid_rent7/', branch7.sept_paid_rent7, name='sept_paid_rent7'),
path('table_sept_paid_rent7/', branch7.table_sept_paid_rent7, name='table_sept_paid_rent7'),
path('sept_full_paid_guest7/', reports7.sept_full_paid_guest7, name='sept_full_paid_guest7'),
path('sept_partially_paid_guest7/', reports7.sept_partially_paid_guest7, name='sept_partially_paid_guest7'),
path('table_sept_partially_paid_guest7/', reports7.table_sept_partially_paid_guest7,name='table_sept_partially_paid_guest7'),

path('oct_paid_rent7/', branch7.oct_paid_rent7, name='oct_paid_rent7'),
path('table_oct_paid_rent7/', branch7.table_oct_paid_rent7, name='table_oct_paid_rent7'),
path('october_full_paid_guest7/', reports7.october_full_paid_guest7, name='october_full_paid_guest7'),
path('october_partially_paid_guest7/', reports7.october_partially_paid_guest7,name='october_partially_paid_guest7'),
path('table_october_partially_paid_guest7/', reports7.table_october_partially_paid_guest7,name='table_october_partially_paid_guest7'),

path('nov_paid_rent7/', branch7.nov_paid_rent7, name='nov_paid_rent7'),
path('table_nov_paid_rent7/', branch7.table_nov_paid_rent7, name='table_nov_paid_rent7'),
path('nov_full_paid_guest7/', reports7.nov_full_paid_guest7, name='nov_full_paid_guest7'),
path('nov_partially_paid_guest7/', reports7.nov_partially_paid_guest7, name='nov_partially_paid_guest7'),
path('table_nov_partially_paid_guest7/', reports7.table_nov_partially_paid_guest7,name='table_nov_partially_paid_guest7'),

path('dec_paid_rent7/', branch7.dec_paid_rent7, name='dec_paid_rent7'),
path('table_dec_paid_rent7/', branch7.table_dec_paid_rent7, name='table_dec_paid_rent7'),
path('dec_full_paid_guest7/', reports7.dec_full_paid_guest7, name='dec_full_paid_guest7'),
path('dec_partially_paid_guest7/', reports7.dec_partially_paid_guest7, name='dec_partially_paid_guest7'),
path('table_dec_partially_paid_guest7/', reports7.table_dec_partially_paid_guest7,name='table_dec_partially_paid_guest7'),

path('details_of_paid_guests7/<id>',branch7.details_of_paid_guests7,name='details_of_paid_guests7'),
path('full_paid_guest7/',reports7.full_paid_guest7,name='full_paid_guest7'),

path('paid_rent_choose_months7/',branch7.paid_rent_choose_months7,name='paid_rent_choose_months7'),
path('partially_paid_guest_choose_months7/',reports7.partially_paid_guest_choose_months7,name='partially_paid_guest_choose_months7'),

path('jan_paid_rent7/', branch7.jan_paid_rent7, name='jan_paid_rent7'),
path('table_jan_paid_rent7/', branch7.table_jan_paid_rent7, name='table_jan_paid_rent7'),
path('jan_full_paid_guest7/', reports7.jan_full_paid_guest7, name='jan_full_paid_guest7'),
path('jan_partially_paid_guest7/', reports7.jan_partially_paid_guest7, name='jan_partially_paid_guest7'),
path('table_jan_partially_paid_guest7/', reports7.table_jan_partially_paid_guest7,name='table_jan_partially_paid_guest7'),

path('feb_paid_rent7/', branch7.feb_paid_rent7, name='feb_paid_rent7'),
path('table_feb_paid_rent7/', branch7.table_feb_paid_rent7, name='table_feb_paid_rent7'),
path('feb_full_paid_guest7/', reports7.feb_full_paid_guest7, name='feb_full_paid_guest7'),
path('feb_partially_paid_guest7/', reports7.feb_partially_paid_guest7, name='feb_partially_paid_guest7'),
path('table_feb_partially_paid_guest7/', reports7.table_feb_partially_paid_guest7,name='table_feb_partially_paid_guest7'),

path('mar_paid_rent7/', branch7.mar_paid_rent7, name='mar_paid_rent7'),
path('table_mar_paid_rent7/', branch7.table_mar_paid_rent7, name='table_mar_paid_rent7'),
path('march_full_paid_guest7/', reports7.march_full_paid_guest7, name='march_full_paid_guest7'),
path('march_partially_paid_guest7/', reports7.march_partially_paid_guest7, name='march_partially_paid_guest7'),
path('table_march_partially_paid_guest7/', reports7.table_march_partially_paid_guest7,name='table_march_partially_paid_guest7'),

path('april_paid_rent7/', branch7.april_paid_rent7, name='april_paid_rent7'),
path('table_april_paid_rent7/', branch7.table_april_paid_rent7, name='table_april_paid_rent7'),
path('april_full_paid_guest7/', reports7.april_full_paid_guest7, name='april_full_paid_guest7'),
path('april_partially_paid_guest7/', reports7.april_partially_paid_guest7, name='april_partially_paid_guest7'),
path('table_april_partially_paid_guest7/', reports7.table_april_partially_paid_guest7,name='table_april_partially_paid_guest7'),

path('may_paid_rent7/', branch7.may_paid_rent7, name='may_paid_rent7'),
path('table_may_paid_rent7/', branch7.table_may_paid_rent7, name='table_may_paid_rent7'),
path('may_full_paid_guest7/', reports7.may_full_paid_guest7, name='may_full_paid_guest7'),
path('may_partially_paid_guest7/', reports7.may_partially_paid_guest7, name='may_partially_paid_guest7'),
path('table_may_partially_paid_guest7/', reports7.table_may_partially_paid_guest7, name='table_may_partially_paid_guest7'),

path('june_paid_rent7/', branch7.june_paid_rent7, name='june_paid_rent7'),
path('table_june_paid_rent7/', branch7.table_june_paid_rent7, name='table_june_paid_rent7'),
path('june_full_paid_guest7/', reports7.june_full_paid_guest7, name='june_full_paid_guest7'),
path('june_partially_paid_guest7/', reports7.june_partially_paid_guest7, name='june_partially_paid_guest7'),
path('table_june_partially_paid_guest7/', reports7.table_june_partially_paid_guest7, name='table_june_partially_paid_guest7'),

path('july_paid_rent7/', branch7.july_paid_rent7, name='july_paid_rent7'),
path('table_july_paid_rent7/', branch7.table_july_paid_rent7, name='table_july_paid_rent7'),
path('july_full_paid_guest7/', reports7.july_full_paid_guest7, name='july_full_paid_guest7'),
path('july_partially_paid_guest7/', reports7.july_partially_paid_guest7, name='july_partially_paid_guest7'),
path('table_july_partially_paid_guest7/', reports7.table_july_partially_paid_guest7, name='table_july_partially_paid_guest7'),

path('aug_paid_rent7/', branch7.aug_paid_rent7, name='aug_paid_rent7'),
path('table_aug_paid_rent7/', branch7.table_aug_paid_rent7, name='table_aug_paid_rent7'),
path('auguest_full_paid_guest7/', reports7.auguest_full_paid_guest7, name='auguest_full_paid_guest7'),
path('auguest_partially_paid_guest7/', reports7.auguest_partially_paid_guest7,name='auguest_partially_paid_guest7'),
path('table_auguest_partially_paid_guest7/', reports7.table_auguest_partially_paid_guest7,name='table_auguest_partially_paid_guest7'),

path('sept_paid_rent7/', branch7.sept_paid_rent7, name='sept_paid_rent7'),
path('table_sept_paid_rent7/', branch7.table_sept_paid_rent7, name='table_sept_paid_rent7'),
path('sept_full_paid_guest7/', reports7.sept_full_paid_guest7, name='sept_full_paid_guest7'),
path('sept_partially_paid_guest7/', reports7.sept_partially_paid_guest7, name='sept_partially_paid_guest7'),
path('table_sept_partially_paid_guest7/', reports7.table_sept_partially_paid_guest7,name='table_sept_partially_paid_guest7'),

path('oct_paid_rent7/', branch7.oct_paid_rent7, name='oct_paid_rent7'),
path('table_oct_paid_rent7/', branch7.table_oct_paid_rent7, name='table_oct_paid_rent7'),
path('october_full_paid_guest7/', reports7.october_full_paid_guest7, name='october_full_paid_guest7'),
path('october_partially_paid_guest7/', reports7.october_partially_paid_guest7,name='october_partially_paid_guest7'),
path('table_october_partially_paid_guest7/', reports7.table_october_partially_paid_guest7,name='table_october_partially_paid_guest7'),

path('nov_paid_rent7/', branch7.nov_paid_rent7, name='nov_paid_rent7'),
path('table_nov_paid_rent7/', branch7.table_nov_paid_rent7, name='table_nov_paid_rent7'),
path('nov_full_paid_guest7/', reports7.nov_full_paid_guest7, name='nov_full_paid_guest7'),
path('nov_partially_paid_guest7/', reports7.nov_partially_paid_guest7, name='nov_partially_paid_guest7'),
path('table_nov_partially_paid_guest7/', reports7.table_nov_partially_paid_guest7,name='table_nov_partially_paid_guest7'),

path('dec_paid_rent7/', branch7.dec_paid_rent7, name='dec_paid_rent7'),
path('table_dec_paid_rent7/', branch7.table_dec_paid_rent7, name='table_dec_paid_rent7'),
path('dec_full_paid_guest7/', reports7.dec_full_paid_guest7, name='dec_full_paid_guest7'),
path('dec_partially_paid_guest7/', reports7.dec_partially_paid_guest7, name='dec_partially_paid_guest7'),
path('table_dec_partially_paid_guest7/', reports7.table_dec_partially_paid_guest7,name='table_dec_partially_paid_guest7'),

path('details_of_paid_guests7/<id>',branch7.details_of_paid_guests7,name='details_of_paid_guests7'),
path('full_paid_guest7/',reports7.full_paid_guest7,name='full_paid_guest7'),



#paid rent end here

#*********reports end here



##################################
#_ADVANCE7 START HERE
################################


path('choose_months_advance7/',branch7.choose_months_advance7,name='choose_months_advance7'),

path('jan_advance7/', branch7.jan_advance7, name='jan_advance7'),
path('jan_make_payments_advance7/<id>', branch7.jan_make_payments_advance7,name='jan_make_payments_advance7'),
path('feb_advance7/', branch7.feb_advance7, name='feb_advance7'),
path('feb_make_payments_advance7/<id>', branch7.feb_make_payments_advance7,name='feb_make_payments_advance7'),
path('march_advance7/', branch7.march_advance7, name='march_advance7'),
path('march_make_payments_advance7/<id>', branch7.march_make_payments_advance7,name='march_make_payments_advance7'),
path('april_advance7/', branch7.april_advance7, name='april_advance7'),
path('april_make_payments_advance7/<id>', branch7.april_make_payments_advance7, name='april_make_payments_advance7'),

path('may_advance7/',branch7.may_advance7,name='may_advance7'),
path('may_make_payments_advance7/<id>', branch7.may_make_payments_advance7, name='may_make_payments_advance7'),
path('june_advance7/',branch7.june_advance7,name='june_advance7'),
path('june_make_payments_advance7/<id>', branch7.june_make_payments_advance7, name='june_make_payments_advance7'),
path('july_advance7/',branch7.july_advance7,name='july_advance7'),
path('july_make_payments_advance7/<id>', branch7.july_make_payments_advance7, name='july_make_payments_advance7'),
path('auguest_advance7/', branch7.auguest_advance7, name='auguest_advance7'),
path('auguest_make_payments_advance7/<id>', branch7.auguest_make_payments_advance7, name='auguest_make_payments_advance7'),

path('sept_advance7/', branch7.sept_advance7, name='sept_advance7'),
path('sept_make_payments_advance7/<id>', branch7.sept_make_payments_advance7,name='sept_make_payments_advance7'),
path('october_advance7/', branch7.october_advance7, name='october_advance7'),
path('october_make_payments_advance7/<id>', branch7.october_make_payments_advance7, name='october_make_payments_advance7'),
path('nov_advance7/', branch7.nov_advance7, name='nov_advance7'),
path('nov_make_payments_advance7/<id>', branch7.nov_make_payments_advance7,name='nov_make_payments_advance7'),
path('dec_advance7/', branch7.dec_advance7, name='dec_advance7'),
path('dec_make_payments_advance7/<id>', branch7.dec_make_payments_advance7, name='dec_make_payments_advance7'),



##################################
#_ADVANCE7 END HERE
################################


##################################
#PAYMENTS START HERE
################################

    path('choose_months7/',branch7.choose_months7,name='choose_months7'),

    path('jan7/',branch7.jan7,name='jan7'),
    path('jan_manke_payments7/<id>',branch7.jan_manke_payments7,name='jan_manke_payments7'),

    path('feb7/',branch7.feb7,name='feb7'),
    path('feb_manke_payments7/<id>',branch7.feb_manke_payments7,name='feb_manke_payments7'),

    path('march7/',branch7.march7,name='march7'),
    path('march_manke_payments7/<id>',branch7.march_manke_payments7,name='march_manke_payments7'),

    path('april7/',branch7.april7,name='april7'),
    path('april_make_payments7/<id>',branch7.april_make_payments7,name='april_make_payments7'),

    path('may7/',branch7.may7,name='may7'),
    path('may_make_payments7/<id>',branch7.may_make_payments7,name='may_make_payments7'),

    path('june7/',branch7.june7,name='june7'),
    path('june_make_payments7/<id>',branch7.june_make_payments7,name='june_make_payments7'),

    path('july7/',branch7.july7,name='july7'),
    path('july_make_payments7/<id>',branch7.july_make_payments7,name='july_make_payments7'),

    path('aug7/',branch7.aug7,name='aug7'),
    path('aug_make_payments7/<id>',branch7.aug_make_payments7,name='aug_make_payments7'),

    path('sept7/',branch7.sept7,name='sept7'),
    path('sept_make_payments7/<id>',branch7.sept_make_payments7,name='sept_make_payments7'),

    path('oct7/',branch7.oct7,name='oct7'),
    path('oct_make_payments7/<id>',branch7.oct_make_payments7,name='oct_make_payments7'),

    path('nov7/',branch7.nov7,name='nov7'),
    path('nov_make_payments7/<id>',branch7.nov_make_payments7,name='nov_make_payments7'),

    path('dec7/',branch7.dec7,name='dec7'),
    path('dec_make_payments7/<id>',branch7.dec_make_payments7,name='dec_make_payments7'),

##################################
#PAYMENTS END HERE
################################


##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user7/', payment7.choose_user7, name='choose_user7'),
    path('payment_user_details7/<id>', payment7.payment_user_details7, name='payment_user_details7'),
    path('close_choose_user7/<id>', payment7.close_choose_user7, name='close_choose_user7'),

    path('monthly_jan_make_payments7/<id>', payment7.monthly_jan_make_payments7, name='monthly_jan_make_payments7'),
    path('monthly_feb_make_payments7/<id>', payment7.monthly_feb_make_payments7, name='monthly_feb_make_payments7'),
    path('monthly_march_make_payments7/<id>', payment7.monthly_march_make_payments7, name='monthly_march_make_payments7'),
    path('monthly_april_make_payments7/<id>', payment7.monthly_april_make_payments7, name='monthly_april_make_payments7'),
    path('monthly_may_make_payments7/<id>', payment7.monthly_may_make_payments7, name='monthly_may_make_payments7'),
    path('monthly_june_make_payments7/<id>', payment7.monthly_june_make_payments7, name='monthly_june_make_payments7'),

    path('monthly_july_make_payments7/<id>', payment7.monthly_july_make_payments7, name='monthly_july_make_payments7'),
    path('monthly_aug_make_payments7/<id>', payment7.monthly_aug_make_payments7, name='monthly_aug_make_payments7'),
    path('monthly_sept_make_payments7/<id>', payment7.monthly_sept_make_payments7, name='monthly_sept_make_payments7'),
    path('monthly_oct_make_payments7/<id>', payment7.monthly_oct_make_payments7, name='monthly_oct_make_payments7'),
    path('monthly_nov_make_payments7/<id>', payment7.monthly_nov_make_payments7, name='monthly_nov_make_payments7'),
    path('monthly_dec_make_payments7/<id>', payment7.monthly_dec_make_payments7, name='monthly_dec_make_payments7'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################



##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user7/', payment7.choose_user7, name='choose_user7'),
    path('payment_user_details7/<id>', payment7.payment_user_details7, name='payment_user_details7'),

    path('monthly_jan_make_payments7/<id>', payment7.monthly_jan_make_payments7, name='monthly_jan_make_payments7'),
    path('monthly_feb_make_payments7/<id>', payment7.monthly_feb_make_payments7, name='monthly_feb_make_payments7'),
    path('monthly_march_make_payments7/<id>', payment7.monthly_march_make_payments7, name='monthly_march_make_payments7'),
    path('monthly_april_make_payments7/<id>', payment7.monthly_april_make_payments7, name='monthly_april_make_payments7'),
    path('monthly_may_make_payments7/<id>', payment7.monthly_may_make_payments7, name='monthly_may_make_payments7'),
    path('monthly_june_make_payments7/<id>', payment7.monthly_june_make_payments7, name='monthly_june_make_payments7'),

    path('monthly_july_make_payments7/<id>', payment7.monthly_july_make_payments7, name='monthly_july_make_payments7'),
    path('monthly_aug_make_payments7/<id>', payment7.monthly_aug_make_payments7, name='monthly_aug_make_payments7'),
    path('monthly_sept_make_payments7/<id>', payment7.monthly_sept_make_payments7, name='monthly_sept_make_payments7'),
    path('monthly_oct_make_payments7/<id>', payment7.monthly_oct_make_payments7, name='monthly_oct_make_payments7'),
    path('monthly_nov_make_payments7/<id>', payment7.monthly_nov_make_payments7, name='monthly_nov_make_payments7'),
    path('monthly_dec_make_payments7/<id>', payment7.monthly_dec_make_payments7, name='monthly_dec_make_payments7'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################

##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general7/',branch7.detail_guest_general7,name='detail_guest_general7'),

    path('jan_print7/',branch7.jan_print7,name='jan_print7'),
    path('feb_print7/',branch7.feb_print7,name='feb_print7'),
    path('march_print7/',branch7.march_print7,name='march_print7'),
    path('april_print7/',branch7.april_print7,name='april_print7'),

    path('may_print7/',branch7.may_print7,name='may_print7'),
    path('june_print7/',branch7.june_print7,name='june_print7'),
    path('july_print7/', branch7.july_print7, name='july_print7'),
    path('aug_print7/', branch7.aug_print7, name='aug_print7'),

    path('sept_print7/', branch7.sept_print7, name='sept_print7'),
    path('oct_print7/', branch7.oct_print7, name='oct_print7'),
    path('nov_print7/', branch7.nov_print7, name='nov_print7'),
    path('dec_print7/', branch7.dec_print7, name='dec_print7'),

    path('new_year_jan_print7/', branch7.new_year_jan_print7, name='new_year_jan_print7'),

##################################
#PRINT OUTS END HERE
################################


########################################
# CLOSE MONTHS START HERE
###########################

    path('jan_close7/', branch7.jan_close7, name='jan_close7'),
    path('jan_close_decision_page7/', branch7.jan_close_decision_page7, name='jan_close_decision_page7'),
    path('feb_close7/', branch7.feb_close7, name='feb_close7'),
    path('feb_close_decision_page7/', branch7.feb_close_decision_page7, name='feb_close_decision_page7'),
    path('mar_close7/', branch7.mar_close7, name='mar_close7'),
    path('mar_close_decision_page/', branch7.mar_close_decision_page7, name='mar_close_decision_page7'),
    path('apr_close7/', branch7.apr_close7, name='apr_close7'),
    path('apr_close_decision_page7/', branch7.apr_close_decision_page7, name='apr_close_decision_page7'),

    path('may_close7/', branch7.may_close7, name='may_close7'),
    path('may_close_decision_page7/', branch7.may_close_decision_page7, name='may_close_decision_page7'),
    path('jun_close7/', branch7.jun_close7, name='jun_close7'),
    path('jun_close_decision_page7/', branch7.jun_close_decision_page7, name='jun_close_decision_page7'),
    path('jul_close7/', branch7.jul_close7, name='jul_close7'),
    path('jul_close_decision_page7/', branch7.jul_close_decision_page7, name='jul_close_decision_page7'),
    path('aug_close7/', branch7.aug_close7, name='aug_close7'),
    path('aug_close_decision_page7/', branch7.aug_close_decision_page7, name='aug_close_decision_page7'),

    path('sep_close7/', branch7.sep_close7, name='sep_close7'),
    path('sep_close_decision_page7/', branch7.sep_close_decision_page7, name='sep_close_decision_page7'),
    path('oct_close7/', branch7.oct_close7, name='oct_close7'),
    path('oct_close_decision_page7/', branch7.oct_close_decision_page7, name='oct_close_decision_page7'),
    path('nov_close7/', branch7.nov_close7, name='nov_close7'),
    path('nov_close_decision_page7/', branch7.nov_close_decision_page7, name='nov_close_decision_page7'),

########################################
# CLOSE MONTHS END HERE
###########################


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months7/',reports7.detailed_report_choose_months7,name='detailed_report_choose_months7'),

    path('jan_details_live7/', reports7.jan_details_live7, name='jan_details_live7'),
    path('jan_print_live7/', reports7.jan_print_live7, name='jan_print_live7'),
    path('feb_details_live7/', reports7.feb_details_live7, name='feb_details_live7'),
    path('feb_print_live7/', reports7.feb_print_live7, name='feb_print_live7'),
    path('march_details_live7/', reports7.march_details_live7, name='march_details_live7'),
    path('march_print_live7/', reports7.march_print_live7, name='march_print_live7'),

    path('april_details_live7/', reports7.april_details_live7, name='april_details_live7'),
    path('april_print_live7/', reports7.april_print_live7, name='april_print_live7'),
    path('may_details_live7/', reports7.may_details_live7, name='may_details_live7'),
    path('may_print_live7/', reports7.may_print_live7, name='may_print_live7'),
    path('june_details_live7/',reports7.june_details_live7,name='june_details_live7'),
    path('june_print_live7/', reports7.june_print_live7, name='june_print_live7'),

    path('july_details_live7/', reports7.july_details_live7, name='july_details_live7'),
    path('july_print_live7/', reports7.july_print_live7, name='july_print_live7'),
    path('auguest_details_live7/', reports7.auguest_details_live7, name='auguest_details_live7'),
    path('auguest_print_live7/', reports7.auguest_print_live7, name='auguest_print_live7'),
    path('sept_details_live7/', reports7.sept_details_live7, name='sept_details_live7'),
    path('sept_print_live7/', reports7.sept_print_live7, name='sept_print_live7'),

    path('october_details_live7/', reports7.october_details_live7, name='october_details_live7'),
    path('october_print_live7/', reports7.october_print_live7, name='october_print_live7'),
    path('nov_details_live7/', reports7.nov_details_live7, name='nov_details_live7'),
    path('nov_print_live7/', reports7.nov_print_live7, name='nov_print_live7'),
    path('dec_details_live7/', reports7.dec_details_live7, name='dec_details_live7'),
    path('dec_print_live7/', reports7.dec_print_live7, name='dec_print_live7'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room7/', reports7.viewall_vaccant_room7, name='viewall_vaccant_room7'),

########################################
# DUE AMT MANAGEMENT START HERE
###########################

path('view_all_due_amt7/', branch7.view_all_due_amt7, name='view_all_due_amt7'),
path('due_amt_mgt_choose_months7/', branch7.due_amt_mgt_choose_months7, name='due_amt_mgt_choose_months7'),

path('view_jan_account_details7/', branch7.view_jan_account_details7, name='view_jan_account_details7'),
path('jan_account_mgt7/<id>',branch7.jan_account_mgt7,name='jan_account_mgt7'),
path('view_feb_account_details7/', branch7.view_feb_account_details7, name='view_feb_account_details7'),
path('feb_account_mgt7/<id>',branch7.feb_account_mgt7,name='feb_account_mgt7'),
path('view_march_account_details7/', branch7.view_march_account_details7, name='view_march_account_details7'),
path('march_account_mgt7/<id>',branch7.march_account_mgt7,name='march_account_mgt7'),
path('view_april_account_details7/', branch7.view_april_account_details7, name='view_april_account_details7'),
path('april_account_mgt7/<id>',branch7.april_account_mgt7,name='april_account_mgt7'),

path('view_may_account_details7/',branch7.view_may_account_details7,name='view_may_account_details7'),
path('may_account_mgt7/<id>', branch7.may_account_mgt7, name='may_account_mgt7'),
path('view_june_account_details7/', branch7.view_june_account_details7, name='view_june_account_details7'),
path('june_account_mgt7/<id>',branch7.june_account_mgt7,name='june_account_mgt7'),
path('view_july_account_details7/', branch7.view_july_account_details7, name='view_july_account_details7'),
path('july_account_mgt7/<id>',branch7.july_account_mgt7,name='july_account_mgt7'),
path('view_auguest_account_details7/', branch7.view_auguest_account_details7, name='view_auguest_account_details7'),
path('auguest_account_mgt7/<id>',branch7.auguest_account_mgt7,name='auguest_account_mgt7'),

path('view_sept_account_details7/', branch7.view_sept_account_details7, name='view_sept_account_details7'),
path('sept_account_mgt7/<id>',branch7.sept_account_mgt7,name='sept_account_mgt7'),
path('view_october_account_details7/', branch7.view_october_account_details7, name='view_october_account_details7'),
path('october_account_mgt7/<id>',branch7.october_account_mgt7,name='october_account_mgt7'),
path('view_nov_account_details7/', branch7.view_nov_account_details7, name='view_nov_account_details7'),
path('nov_account_mgt7/<id>',branch7.nov_account_mgt7,name='nov_account_mgt7'),
path('view_dec_account_details7/', branch7.view_dec_account_details7, name='view_dec_account_details7'),
path('dec_account_mgt7/<id>',branch7.dec_account_mgt7,name='dec_account_mgt7'),


########################################
# DUE AMT MANAGEMENT END HERE
###########################



##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest7/',branch7.viewall_vacate_guest7,name='viewall_vacate_guest7'),
    path('details_of_vacate_guest7/<id>',branch7.details_of_vacate_guest7,name='details_of_vacate_guest7'),
    path('full_vacated_guest_details7', branch7.full_vacated_guest_details7, name='full_vacated_guest_details7'),
    path('full_vacated_guest_table7', branch7.full_vacated_guest_table7, name='full_vacated_guest_table7'),

    path('guest_details7/<guest_code>', branch7.guest_details7, name='guest_details7'),

    #********vacate guest payments start here**********

    path('jan_manke_payments_vacate7/<id>', branch7.jan_manke_payments_vacate7, name='jan_manke_payments_vacate7'),
    path('feb_manke_payments_vacate7/<id>', branch7.feb_manke_payments_vacate7, name='feb_manke_payments_vacate7'),
    path('march_manke_payments_vacate7/<id>', branch7.march_manke_payments_vacate7, name='march_manke_payments_vacate7'),
    path('april_make_payments_vacate7/<id>', branch7.april_make_payments_vacate7, name='april_make_payments_vacate7'),

    path('may_make_payments_vacate7/<id>', branch7.may_make_payments_vacate7, name='may_make_payments_vacate7'),
    path('june_make_payments_vacate7/<id>', branch7.june_make_payments_vacate7, name='june_make_payments_vacate7'),
    path('july_make_payments_vacate7/<id>', branch7.july_make_payments_vacate7, name='july_make_payments_vacate7'),
    path('aug_make_payments_vacate7/<id>', branch7.aug_make_payments_vacate7, name='aug_make_payments_vacate7'),

    path('sept_make_payments_vacate7/<id>', branch7.sept_make_payments_vacate7, name='sept_make_payments_vacate7'),
    path('oct_make_payments_vacate7/<id>', branch7.oct_make_payments_vacate7, name='oct_make_payments_vacate7'),
    path('nov_make_payments_vacate7/<id>', branch7.nov_make_payments_vacate7, name='nov_make_payments_vacate7'),
    path('dec_make_payments_vacate7/<id>', branch7.dec_make_payments_vacate7, name='dec_make_payments_vacate7'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due7', admin_dashboard_calculations_br7.monthly_details_due7, name='monthly_details_due7'),
    path('monthly_collection_details7/', admin_dashboard_calculations_br7.monthly_collection_details7, name='monthly_collection_details7'),

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

    path('view_all_category7/', accounts7.view_all_category7, name='view_all_category7'),
    path('create_new_category7/', accounts7.create_new_category7, name='create_new_category7'),
    path('regi_new_category7/', accounts7.regi_new_category7, name='regi_new_category7'),
    path('update_category7/<id>',accounts7.update_category7,name='update_category7'),

    path('delete_category7/<id>', accounts7.delete_category7, name='delete_category7'),
    path('view_all_category_delete7/', accounts7.view_all_category_delete7, name='view_all_category_delete7'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items7/', accounts7.view_all_items7, name='view_all_items7'),
    path('create_new_item7/', accounts7.create_new_item7, name='create_new_item7'),
    path('regi_new_item7/', accounts7.regi_new_item7, name='regi_new_item7'),
    path('delete_item7/<id>',accounts7.delete_item7,name='delete_item7'),
    path('update_item7/<id>', accounts7.update_item7, name='update_item7'),
    path('view_all_items_delete7/',accounts7.view_all_items_delete7,name='view_all_items_delete7'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger7/', accounts7.view_all_ledger7, name='view_all_ledger7'),
    path('create_new_ledger7/', accounts7.create_new_ledger7, name='create_new_ledger7'),
    path('regi_new_ledger7/', accounts7.regi_new_ledger7, name='regi_new_ledger7'),
    path('delete_ledger7/<id>',accounts7.delete_ledger7,name='delete_ledger7'),
    path('update_ledger7/<id>',accounts7.update_ledger7,name='update_ledger7'),
    path('view_all_ledger_delete7/',accounts7.view_all_ledger_delete7,name='view_all_ledger_delete7'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book7/', accounts7.view_all_accounts_book7, name='view_all_accounts_book7'),
    path('create_new_accounts_book7/', accounts7.create_new_accounts_book7, name='create_new_accounts_book7'),
    path('regi_new_accounts_book7/', accounts7.regi_new_accounts_book7, name='regi_new_accounts_book7'),
    path('update_accounts_book7/<id>',accounts7.update_accounts_book7,name='update_accounts_book7'),
    path('delete_accounts_book7/<id>',accounts7.delete_accounts_book7,name='delete_accounts_book7'),
    path('view_all_accounts_book_delete7/',accounts7.view_all_accounts_book_delete7,name='view_all_accounts_book_delete7'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries7/', accounts7.get_countries7, name='get_countries7'),

    path('in_exp_items_entry7/', accounts7.in_exp_items_entry7, name='in_exp_items_entry7'),
    path('reg_in_exp_items_entry7/', accounts7.reg_in_exp_items_entry7, name='reg_in_exp_items_entry7'),
    path('delete_journal7/<id>',accounts7.delete_journal7,name='delete_journal7'),
    path('update_in_exp_items_entry7/<id>',accounts7.update_in_exp_items_entry7,name='update_in_exp_items_entry7'),
    path('detailed_journal_report7/',accounts7.detailed_journal_report7,name='detailed_journal_report7'),
    path('journal_report_deleted7/',accounts7.journal_report_deleted7,name='journal_report_deleted7'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise7/', accounts7.daily_category_wise7, name='daily_category_wise7'),
    path('monthly_category_based_reports7/',accounts7.monthly_category_based_reports7,name='monthly_category_based_reports7'),
    path('yearly_category_based_reports7/', accounts7.yearly_category_based_reports7,name='yearly_category_based_reports7'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed7/', accounts7.daily_detailed7, name='daily_detailed7'),
    path('monthly_detailed7/',accounts7.monthly_detailed7,name='monthly_detailed7'),
    path('yearly_detailed7/',accounts7.yearly_detailed7,name='yearly_detailed7'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports7/', accounts7.item_based_reports7, name='item_based_reports7'),
    path('daily_item_based_reports7/',accounts7.daily_item_based_reports7,name='daily_item_based_reports7'),
    path('monthly_item_based_reports7/',accounts7.monthly_item_based_reports7,name='monthly_item_based_reports7'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports7/', accounts7.ledger_based_reports7, name='ledger_based_reports7'),
    path('monthly_ledger_based_reports7/', accounts7.monthly_ledger_based_reports7, name='monthly_ledger_based_reports7'),
    path('daily_ledger_based_reports7/',accounts7.daily_ledger_based_reports7,name='daily_ledger_based_reports7'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports7/', accounts7.accounts_book_based_reports7, name='accounts_book_based_reports7'),
    path('daily_accounts_book_based_reports7/',accounts7.daily_accounts_book_based_reports7,name='daily_accounts_book_based_reports7'),
    path('monthly_accounts_book_based_reports7/',accounts7.monthly_accounts_book_based_reports7,name='monthly_accounts_book_based_reports7'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months7/', accounts7.monthly_reports_choose_months7, name='monthly_reports_choose_months7'),
    path('monthly_detailed_daily_in_exp_items_report7/<mo>',accounts7.monthly_detailed_daily_in_exp_items_report7,name='monthly_detailed_daily_in_exp_items_report7'),

    path('single_monthly_reports_choose_months7/', accounts7.single_monthly_reports_choose_months7,name='single_monthly_reports_choose_months7'),
    path('single_monthly_daily_in_exp_items_report7/<mo>',accounts7.single_monthly_daily_in_exp_items_report7,name='single_monthly_daily_in_exp_items_report7'),

    path('accounts_dash_board7/',accounts7.accounts_dash_board7,name='accounts_dash_board7'),



    path('profit_sharing_choose_months7', accounts7.profit_sharing_choose_months7,name='profit_sharing_choose_months7'),
    path('profit_sharing7/<mo>', accounts7.profit_sharing7, name='profit_sharing7'),
    path('view_share_holders7', accounts7.view_share_holders7, name='view_share_holders7'),
    path('create_share_holders7', accounts7.create_share_holders7, name='create_share_holders7'),
    path('regi_share_holders7', accounts7.regi_share_holders7, name='regi_share_holders7'),
    path('update_share_holders7/<id>', accounts7.update_share_holders7, name='update_share_holders7'),
    path('delete_share_holders7/<id>', accounts7.delete_share_holders7, name='delete_share_holders7'),
    path('view_deleted_share_holders7', accounts7.view_deleted_share_holders7, name='view_deleted_share_holders7'),

]