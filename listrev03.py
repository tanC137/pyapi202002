#!/usr/bin/python3

def main():
    ##create list already containing IP addresses
    iplist = ["10.0.0.1", "10.0.1.1", "10.3.2.1"]

    ##create list of ports
    iplist2 = ["5060", "80", "22"]

    print(iplist)

    iplist.extend(iplist2)

    print(iplist)


if __name__ == "__main__":
    main()
