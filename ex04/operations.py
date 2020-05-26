import sys


if sys.argv is not None and len(sys.argv) > 3:
    print("InputError: too many arguments\n")

if (sys.argv is None or len(sys.argv) != 3 or sys.argv[1] is None or sys.argv[2] is None
   or sys.argv[1].lstrip('+-').isdigit() is False or sys.argv[2].lstrip('+-').isdigit() is False):
    print("Usage: python %s <number1> <number2>" % sys.argv[0].replace('.\\', ''))
    print("Example:\n   python %s 10 3" % sys.argv[0].replace('.\\', ''))
    exit(0)

m_a = int(sys.argv[1])
m_b = int(sys.argv[2])
m_sum = m_a + m_b
m_diff = abs(m_a - m_b)
m_product = m_a * m_b
m_quotient = m_a / m_b if m_a != 0 and m_b != 0 else "ERROR (div by zero)"
m_remainder = m_a % m_b if m_a != 0 and m_b != 0 else "ERROR (modulo by zero)"

print("Sum:         %s" % m_sum)
print("Difference:  %s" % m_diff)
print("Product:     %s" % m_product)
print("Quotient:    %s" % m_quotient)
print("Remainder:   %s" % m_remainder)
