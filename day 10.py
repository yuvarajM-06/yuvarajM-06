# exercise 1

class Homo_Erectus:
      def func1(self):
          print("Kingdom:Animalia \nPhylum:Chordata \nClass:Mammalia \nOrder:Primates \nSuborder:Haplorhini \nInfraorder:Simiiformes \nFamily:Hominidae \nSubfamily:Homininae \nTribe:Hominini \nGenus:Homo \nSpecies:H. erectus")
class Homo_Sapiens_Neanderthalensis(Homo_Erectus):
      def func2(self):
          print("Kingdom:Animalia \nPhylum:Chordata \nClass:Mammalia \nOrder:Primates \nSuborder:Haplorhini \nInfraorder:Simiiformes \nFamily:Hominidae \nSubfamily:Homininae \nTribe:Hominini \nGenus:Homo \nSpecies:†H.neanderthalensis")
class Homo_Sapiens_Sapiens(Homo_Erectus):
      def func3(self):
          print("Kingdom:Animalia \nPhylum:Chordata \nClass:Mammalia \nOrder:Primates \nSuborder:Haplorhini \nInfraorder:Simiiformes \nFamily:Hominidae \nSubfamily:Homininae \nTribe:Hominini \nGenus:Homo Linnaeus, 1758 \n species: homo sapiens")
 
ancestor_1 = Homo_Sapiens_Neanderthalensis()
ancestor_2 = Homo_Sapiens_Sapiens()

ancestor_1.func1()
print ("\n")
ancestor_1.func2()
print ("\n")
ancestor_2.func3()