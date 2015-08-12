#检查是否为合法标识符

def idcheck(flag):
    import string

    alpha = string.letters
    nums  = string.digits

    print 'welcome to the identifier checker'
    print 'testees must be at least 2 chars long.'

    if(len(flag)) > 1:
        if flag[0] not in alpha:
            print '''invalid: first symbol must be alphabetic'''
        else:
            for other in flag[1:]:
                if other not in alpha+nums:
                    print'''invalid: remaining symbols must be alphanumeric'''
                    break
            print '''okay as an identifier'''
