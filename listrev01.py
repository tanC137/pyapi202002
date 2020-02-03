#!/usr/bin/python3

def main():
    ##create empty list
    myemptylist = []
    
    ##add to our list with list method
    ##extend method will add every item to list
    myemptylist.extend("192.168.102.55")

    ##display list
    print(myemptylist)

    #CLASS EXAMPLE
    #myotherlist = []
    #myotherlist.append("192.168.102.55")
    #print(myotherlist)
    #networklist = ["cisco", "juniper"]
    #myemptylist.extend(networklist)
    #print(myemptylist)


if __name__ == "__main__":
    main()
