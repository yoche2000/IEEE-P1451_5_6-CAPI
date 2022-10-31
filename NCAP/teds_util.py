def csv_parse():
    """
    :csv_parse(): Automatically detect the TEDS csv files and transform the data into dictionaries. The returned objects are the PHY and SEN TEDS are dictionaries with the form of {FieldName: [type, value]}
    """
    sd = SD()
    mntpt = "/s"+str(time.ticks_ms())
    print("[SYS] SD Card Mounted on " +mntpt)
    os.mount(sd, mntpt)
    ls = os.listdir(mntpt)
    for path in ls:                                         ##Scanning Physical TEDS path
        if ("phy" in path) and ("csv" in path):
            p_path = path
            print("[SYS] Physical TEDS found: "+ p_path)

        if ("sen" in path) and ("csv" in path):             ##Scanning Sensor TEDS path
            s_path = path
            print("[SYS] Sensor TEDS found: "+ s_path)

    f = open( mntpt+"/"+p_path, 'r')                        ##Reading Physical TEDS
    data = f.read()
    f.close()
    print("[SYS] Reading CSV file")
    lines = data.split()
    fname = []
    value=[]
    for line in lines:
        t = line.split(',')
        fname.append(t[1])
        value.append([t[3], t[4]])
    p_teds_dict = dict(zip(fname, value))

    f = open( mntpt+"/"+s_path, 'r')                        ##Reading Sensor TEDS path
    data = f.read()
    f.close()
    print("[SYS] Reading CSV file")
    lines = data.split()
    fname = []
    value=[]

    for line in lines:
        t = line.split(',')
        fname.append(t[1])
        value.append([t[3], t[4]])
    s_teds_dict = dict(zip(fname, value))

    return p_teds_dict, s_teds_dict

def print_teds(teds_dict):
    """
    :print_teds(): Input a dictionary in the form of {FieldName: [type, value]} to print the TEDS in a readable format.
    """
    print("{:<16} {:<10} {:<10}".format('Key','Type','Value'))
    print("="*(32+24))
    for k, v in teds_dict.items():
        tp, vl = v
        print("{:<16} {:<10} {:<10}".format(k, tp, vl))
    print("-\n")
