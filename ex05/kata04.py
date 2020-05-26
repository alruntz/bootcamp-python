t = (0, 4, 132.42222, 10000, 12345.67)

day = "day_{:0>2}".format(t[0])
ex = "ex_{:0>2}".format(t[1])
value_a = "{:.2f}".format(float(t[2]))
value_b = "{:.2e}".format(int(t[3]))
value_c = "{:.2e}".format(float(t[4]))

print ("%s, %s : %s, %s, %s" % (day, ex, value_a, value_b, value_c))