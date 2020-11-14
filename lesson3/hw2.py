def my_func():
    rec = {a_name: 'a_name',
           a_fam: 'a_fam',
           old: 'old',
           city: 'city',
           email: 'email',
           phone: 'phone'}
    return rec

a_name = input("enter name:")
a_fam = input("enter family:")
old = input('enter year of birth:')
city = input('enter your city:')
email = input('enter your email:')
phone = input('enter your phone:+7')
print(my_func())
a = my_func()
print(','.join(a))

