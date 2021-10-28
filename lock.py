def PatternUnlock(N,hits = []):
    case = ['15','51','26','62','18','81','29','92','27','72','38','83','24','42','53','35']
    case_2 = ['91','21','61','82','52','32','65','54','98','87','43','73']
    case_3 = ['19','16','28','25','37']
    list_to_string = " ".join(str(x) for x in hits)
    string_split = list_to_string.split()
    hits_string = ''.join(string_split)
    lenght = 0
    for case1 in range(len(case)):
        if case[case1] in hits_string:
            lenght = lenght + 1.414215
    for case2 in range(len(case_2)):
        if case_2[case2] in hits_string:
            lenght = lenght + 1
    for case in range(len(case_3)):
        if case_2[case ] in hits_string:
            lenght = lenght + 1
    for ind in range(N-1):
        if hits[ind+1] - hits[ind] <= 1 and hits[ind+1] - hits[ind] >= 0 :
            lenght = lenght + 1
    int_to_str = ''.join(str(lenght))
    res_str_1 = int_to_str.replace('.', '') 
    res_str_2 = res_str_1.replace('0', '')
    list_lenght = list(res_str_2)
    new_list_lenght = []
    
    if len(list_lenght) > 6:
        for i in range(len(list_lenght)-1):
            new_list_lenght.append( list_lenght[i])
    elif len(list_lenght) >= 10:
        for i in range(len(list_lenght)-2):
            new_list_lenght.append( list_lenght[i])
    else:
        for i in range(len(list_lenght)):
            new_list_lenght.append( list_lenght[i])
    int_to_str = ''.join(new_list_lenght)
    return int_to_str
