import sys


if sys.argv is None:
    exit(0)

m_argLen = len(sys.argv)

if m_argLen == 1:
    exit(0)

if (m_argLen > 2 or sys.argv[1] is None or
   (m_argLen == 2 and sys.argv[1].lstrip('-+').isdigit() is False)):
    print("ERROR")

elif (m_argLen == 2):
    m_res = int(sys.argv[1])
    m_text = "I'm "
    m_text += "Zero" if m_res == 0 else "Even" if int(sys.argv[1]) % 2 == 0 else "Odd"
    m_text += "."
    print(m_text)