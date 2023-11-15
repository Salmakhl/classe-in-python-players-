class player():
    def __init__(self,name,ova,rank,natio) :
        self.name=name
        self.ova = ova
        self.rank = rank
        self.Nationality = natio
       

    def information(self):
        print("the player name is :{} his ova {} , his rank {} and nationality {}. "
              .format(self.name,self.ova,self.rank,self.Nationality))


#the main programe
pl1=player("Kylian Mbappé ",91,1,"FRANCE")
pl2=player("Erling Haaland",91,2,"Norway")
pl3=player("Kevin De Bruyne",91,3,"Germany")
pl4=player("Lionel Messi",90,4,"Norway")


pl1.information()
pl2.information()
pl3.information()
pl4.information()