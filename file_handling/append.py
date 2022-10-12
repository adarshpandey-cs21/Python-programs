

fp=open("b.txt",'a')
fp.write(" hii")
fp.write(" ki hal")
fp.write(" hii adarsh")
fp.close()


fp=open("b.txt",'a')
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
fp.writelines(L)
fp.close()

