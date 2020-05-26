import string


def text_analyzer(text=None):
    "... function description ..."

    if isinstance(text, str) is False or text is None:
        text_analyzer(input("What is in the text to analyse ?\n"))
    
    else:
        m_nbCharacters = len(text)
        m_upperLetters = sum(1 for c in text if c.isupper())
        m_lowerLetters = sum(1 for c in text if c.islower())
        m_punctuation = sum(1 for c in text if c in list(string.punctuation))
        m_spaces = sum(1 for c in text if c == ' ')
        
        print ("The text contains %s characters:\n" % m_nbCharacters)
        print("- %s upper letters\n" % m_upperLetters)
        print("- %s lower letters\n" % m_lowerLetters)
        print("- %s punctuation marks\n" % m_punctuation)
        print("- %s spaces" % m_spaces)
