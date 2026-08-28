def twenty_twenty_six():
    """Come up with the most creative expression that evaluates to 2026
    using only numbers and the +, *, and - operators (or ** and % if you'd like).

    >>> twenty_twenty_six()
    2026
    """
    return 2*1000 + 2* 10 + 6


passphrase = 'abc'

def presem_survey(p):
    """
    You do not need to understand this code.
    >>> presem_survey(passphrase)
    '490cbafdbd19352a62ff3988211180244329a1d311d1ee5e4a452791'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

