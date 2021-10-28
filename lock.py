
def PatternUnlock(N,hits = []):
    case = ['15','51','26','62','18','81','29','92','27','72','38','83','24','42','53','35']
    case_2 = ['91','21','61','82','52','32','65','54','98','87','43','73']
    list_to_string = " ".join(str(x) for x in hits)
    string_split = list_to_string.split()
    hits_string = ''.join(string_split)
    lenght = 0
    for i in range(len(case)):
        if case[i] in hits_string:
            lenght = lenght + 1.40515
    for l in range(len(case_2)):
        if case_2[l] in hits_string:
            lenght = lenght + 1
    
    for i in range(N-1):
        if hits[i+1] - hits[i] == 1:
            lenght = lenght + 1
    int_to_str = ''.join(str(lenght))
    res_str_1 = int_to_str.replace('.', '') 
    res_str_2 = res_str_1.replace('0', '')
    list_lenght = list(res_str_2)
    new_list_lenght = []

    for i in range(len( list_lenght)):
        new_list_lenght.append( list_lenght[i])
            
    int_to_str = ''.join(new_list_lenght)
    
    return int_to_str
