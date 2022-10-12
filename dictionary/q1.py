d={'1':'h','2':'b','3':'go','4':'bolo'}

#key=input()
#print(d[key])
#print(d.get(key,"key nhi hai"))

p=d.setdefault('4',99)
print(p,d)