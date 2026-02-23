def sign_match(donor, reciptient):
    if donor[-1:] == '-' or (donor[-1:] == '+' and reciptient[-1:] == '+'): return True
    else: return False

def can_donate(donor, recipient):
    # check donor 'AB' compatibles
    if donor[:2] == 'AB':
        # check leter compatibility
        if recipient[:2] == 'AB':
            # check sign compatibility
            if sign_match(donor,recipient): return True
            else: return False
        else:return False
    # check donor 'B' compatibles    
    elif donor[:1] == 'B':
        # check leter compatibility
        if (recipient[:2] == 'AB' or recipient[:1] == 'B'):
            # check sign compatibility
            if sign_match(donor,recipient): return True
            else: return False
        else:return False
    # check donor 'A' compatibles
    elif donor[:1] == 'A':
        # check leter compatibility
        if (recipient[:2] == 'AB' or recipient[:1] == 'A'):
            # check sign compatibility
            if sign_match(donor,recipient): return True
            else: return False
        else:return False
    # check donor 'O' compatibility and sign compatibility
    elif sign_match(donor,recipient): return True
    else: return False

    return donor

if __name__ == '__main__':
    print(can_donate("B+", "B+"))
    print('-----True')
    print(can_donate("O-", "AB-"))
    print('-----True')
    print(can_donate("O+", "A-"))
    print('-----False')
    print(can_donate("A+", "AB+"))
    print('-----True')
    print(can_donate("A-", "B-"))
    print('-----False')
    print(can_donate("B-", "AB+"))
    print('-----True')
    print(can_donate("B-", "A+"))
    print('-----False')
    print(can_donate("O-", "O+"))
    print('-----True')
    print(can_donate("O+", "O-"))
    print('-----False')
    print(can_donate("AB+", "AB-"))
    print('-----False')
    print(can_donate("AB-", "A-"))
    print('-----')