from breach_compilation_utils import BreachCompilation
import sys
import operator

if __name__ == "__main__":
    bc = BreachCompilation(sys.argv[1])

    domain_map = {}
    for login, pwd in bc.iter_credentials():
        try:
            login, domain = login.split("@")
        except ValueError:
            continue
            #print("Not enough values:", login)
        if domain in domain_map:
            domain_map[domain] += 1
        else:
            domain_map[domain] = 1

    with open("output.txt", "w") as out:
        for dn, hit in domain_map.items():
            out.write('%d %s\n' % (dn, hit))
