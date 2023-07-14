def validip(input_string):
    lst=input_string.split('.')
    if len(lst)!=4:
        return False
    lst = [int(i) if i.isdigit() else i for i in lst]
    if not all([isinstance(i,int) for i in lst]):
        return False
    if not all([int(i)>=0 and int(i)<=255 for i in lst]):
        return False
    return True

print(validip('255.23.12.23'))
print(validip('255.23.12.278'))
print(validip('255.23.12.-2'))
print(validip('255.23.12.2.12'))
print(validip('255.23.12. a'))