class factory:
    def __init__(self,company_name,material,zips,pockets):
        self.company_name = company_name
        self.material = material
        self.zips = zips
        self.pockets = pockets  
        
    def show(self):
        print(f"Company Name: {self.company_name}")
        print(f"Material: {self.material}")
        print(f"Zips: {self.zips}")
        print(f"Pockets: {self.pockets}")

rebook=factory("Rebook","leather",2,4)
rebook.show()

