su=0
for i in range(0,5):
    x=int(raw_input("Enter marks:"))
    su=su+x
per=su/5
if per<35:
    print "SORRY! YOU ARE FAIL "
else:
    print "CONGO!!! YOU ARE PASS"
