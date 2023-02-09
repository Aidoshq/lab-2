#nested dict
myfamily = {
  "child1" : {
    "name" : "Ardak",
    "year" : 1999
  },
  "child2" : {
    "name" : "Aidana",
    "year" : 2004
  },
  "child3" : {
    "name" : "Zhanna",
    "year" : 2005
  }
}

print(myfamily)




child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)




myfamily = {
  "child1" : {
    "name" : "Ardak",
    "year" : 2004
  },
  "child2" : {
    "name" : "Aidana",
    "year" : 2007
  },
  "child3" : {
    "name" : "Zhanna",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"],"Mukhadilova")



