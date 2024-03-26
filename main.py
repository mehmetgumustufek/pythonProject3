
class Personel():
    def __init__(self,name, department, workTime, monthlyIncome):
        self.name=name
        self.department=department
        self.workTime=workTime
        self.monthlyIncome=monthlyIncome
    def __str__(self):
        return f"{self.name},{self.department},{self.workTime},{self.monthlyIncome}"

class Firma():
    def __init__(self):
        self.personelList=[]
    def addPersonel(self,personel):
        self.personelList.append(personel)
    def showPersonelList(self):
        if self.personelList==None:
            print("Listede personel bulunmamaktadır.")
        for personel in self.personelList:
            print(personel)
            """""""""
    def increasedSalary(self,personel,increaseRate):
        for p in self.personelList:
            if p==personel.name:
                p.salary+=((increaseRate*p.salary)/100)
                """""

    def increasedSalary(self, p, increaseRate):
        for personel in self.personelList:
            if personel.name==p.name:
                personel.monthlyIncome+=((increaseRate*personel.monthlyIncome)/100)


    def firePersonel(self,personelName):
        if self.personelList==None:
            print("Listede personel bulunmamaktadır")
        self.personelList.remove(personelName)

p1= Personel("Sevgi","bilgisayar","15",30000)
p2= Personel("Ali","IT","10",25000)
f=Firma()
f.addPersonel(p2)
f.addPersonel(p1)
f.showPersonelList()
f.increasedSalary(p1,20)
f.showPersonelList()
f.firePersonel(p1)
f.showPersonelList()