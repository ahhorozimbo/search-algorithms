from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.cities = [
        "Rio de Janeiro",	
	"São Gonçalo",	
	"Duque de Caxias",	
	"Nova Iguaçu",	
	"Niterói",	
	"Belford Roxo",	
	"Campos dos Goytacazes",	
	"São João de Meriti",	
	"Petrópolis",	
	"Volta Redonda",	
	"Macaé",	
    	"Magé",	
	"Itaboraí",	
	"Cabo Frio",	
	"Angra dos Reis",	 
	"Nova Friburgo",	 
	"Barra Mansa",	 
	"Teresópolis",	 
	"Mesquita",	 
	"Maricá",	 
	"Nilópolis",	 
	"Rio das Ostras",	 
	"Queimados",	 
	"Itaguaí",	 
	"Araruama",	 
	"Resende",	 
	"São Pedro da Aldeia",	 
	"Japeri",	 
	"Itaperuna",	 
	"Barra do Piraí",	 
	"Seropédica",	 
	"Saquarema",	 
	"Três Rios",	 
	"Valença",
	"Guapimirim",	 
	"Rio Bonito",	 
	"Cachoeiras de Macacu",	 
	"Paracambi",	 
	"Mangaratiba",	 
	"Casimiro de Abreu",	 
	"Paraíba do Sul",	 
	"Paraty",	 
	"Santo Antônio de Pádua",	 
	"São Francisco de Itabapoana",	 
	"São Fidélis",	 
	"Bom Jesus do Itabapoana",	 
	"Vassouras",	 
	"São João da Barra",	 
	"Tanguá",	 
	"Armação dos Búzios",	 
	"Itatiaia",	 
	"Arraial do Cabo", 
	"Piraí",	 
	"Iguaba Grande",	 
	"Paty do Alferes",	 
	"Bom Jardim",
	"Miracema",
	"Miguel Pereira",
	"Pinheiral",
	"Quissamã",
	"Conceição de Macabu",	 
	"Itaocara",	 
	"Cordeiro",	 
	"São José do Vale do Rio Preto",	 
	"Silva Jardim",	 
	"Cantagalo",	 
	"Porto Real",	 
	"Carmo",	 
	"Porciúncula",	 
	"Mendes",	 
	"Rio Claro",	 
	"Sapucaia",	 
	"Carapebus",	 
	"Sumidouro",	 
	"Cambuci",	 
	"Natividade",	 
	"Italva", 
	"Quatis",	 
	"Engenheiro Paulo de Frontin",	 
	"Cardoso Moreira	", 
	"Areal",	 
	"Aperibé",	 
	"Duas Barras",	 
	"Varre-Sai",	 
	"Trajano de Moraes",	 
	"Santa Maria Madalena",	 
	"São Sebastião do Alto",	 
	"Rio das Flores",	 
	"Comendador Levy Gasparianv", 
	"Laje do Muriaé",	 
	"São José de Ubá", 
	"Macuco"
        ]

    def addEdge(self, u, v,distance):
        self.graph[u].append(v)

                    
    def DFSUtil(self, v, visited):

        visited.add(v)
        print(v, self.cities[v-1], end=" | ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
g = Graph()

g.addEdge(1, 54, 45)
g.addEdge(1, 69, 26)
g.addEdge(1, 26, 38)
g.addEdge(1, 62, 36)


g.addEdge(2, 53, 21)

g.addEdge(2, 46, 27)
g.addEdge(2, 15, 27)
g.addEdge(2, 10, 11)

g.addEdge(3, 21, 19)
g.addEdge(3, 34, 38)
g.addEdge(3, 25, 34)
g.addEdge(3, 45, 21)
g.addEdge(3, 29, 19)

g.addEdge(3, 46, 34)
g.addEdge(3, 81, 36)

g.addEdge(4, 53, 45)
g.addEdge(4, 76, 37)
g.addEdge(4, 13, 26)
g.addEdge(4, 18, 28)
g.addEdge(4, 59, 21)
g.addEdge(4, 75, 15)
g.addEdge(4, 83, 12)

g.addEdge(5, 91, 5)
g.addEdge(5, 71, 16)
g.addEdge(5, 47, 35)
g.addEdge(5, 70, 8)

g.addEdge(6, 92, 27)
g.addEdge(6, 52, 5)
g.addEdge(6, 84, 9)

g.addEdge(7, 48, 38)
g.addEdge(7, 37, 23)
g.addEdge(7, 40, 18)
g.addEdge(7, 9, 28)




g.addEdge(9, 68, 54)

g.addEdge(9, 7, 28)

g.addEdge(10, 2, 11)
g.addEdge(10, 53, 32)
g.addEdge(10, 75, 30)
g.addEdge(10, 92, 21)

 
g.addEdge(11, 18, 2)
g.addEdge(11, 59, 11)

g.addEdge(12, 27, 29)
g.addEdge(12, 57, 16)
g.addEdge(12, 28, 30)
g.addEdge(12, 34, 45)
g.addEdge(12, 48, 23)


g.addEdge(13, 18, 10)
g.addEdge(13, 4, 26)

g.addEdge(14, 60, 12)
g.addEdge(14, 43, 10)
g.addEdge(14, 38, 6)

g.addEdge(15, 2, 27)
g.addEdge(15, 44, 21)

g.addEdge(15, 92, 37)
g.addEdge(15, 41, 42)

g.addEdge(16, 32, 40)
g.addEdge(16, 45, 14)
g.addEdge(16, 29, 20)
g.addEdge(16, 63, 21)
g.addEdge(16, 81, 32)

g.addEdge(17, 54, 46)
g.addEdge(17, 65, 29)
g.addEdge(17, 51, 35)

g.addEdge(17, 36, 41)

g.addEdge(18, 13, 10)
g.addEdge(18, 11, 2)
g.addEdge(18, 59, 34)
g.addEdge(18, 4, 28)

 
g.addEdge(19, 90, 28)
g.addEdge(19, 61, 26)
g.addEdge(19, 86, 31)

g.addEdge(20, 82, 37)

g.addEdge(20, 87, 17)

g.addEdge(21, 34, 17)

g.addEdge(21, 46, 30)
g.addEdge(21, 3, 19)

g.addEdge(22, 33, 8)
g.addEdge(22, 42, 24)
g.addEdge(22, 60, 6)

g.addEdge(23, 47, 10)
g.addEdge(23, 85, 4)
g.addEdge(23, 52, 12)


g.addEdge(24, 41, 20)
g.addEdge(24, 73, 26)
g.addEdge(24, 30, 23)

g.addEdge(25, 34, 16)
g.addEdge(25, 48, 45)
g.addEdge(25, 40, 37)
g.addEdge(25, 3, 34)
g.addEdge(25, 32, 22)

g.addEdge(26, 1, 38)
g.addEdge(26, 69, 30)
g.addEdge(26, 62, 42)

g.addEdge(27, 86, 25)
g.addEdge(27, 12, 29)
g.addEdge(27, 48, 29)

g.addEdge(28, 57, 14)
g.addEdge(28, 67, 33)
g.addEdge(28, 12, 30)
g.addEdge(28, 34, 32)

g.addEdge(29, 45, 14)
g.addEdge(29, 3, 19)
g.addEdge(29, 16, 20)

g.addEdge(30, 73, 27)
g.addEdge(30, 24, 24)
g.addEdge(30, 74, 21)

g.addEdge(31, 42, 15)
g.addEdge(31, 91, 18)
g.addEdge(31, 56, 16)
g.addEdge(31, 47, 42)

g.addEdge(32, 40, 26)
g.addEdge(32, 25, 22)
g.addEdge(32, 45, 25)
g.addEdge(32, 16, 40)


g.addEdge(33, 89, 12)

g.addEdge(33, 22, 8)

g.addEdge(34, 12, 45)
g.addEdge(34, 28, 32)

g.addEdge(34, 67, 27)
g.addEdge(34, 48, 58)
g.addEdge(34, 25, 16)
g.addEdge(34, 21, 17)
g.addEdge(34, 3, 38)

g.addEdge(35, 44, 62)

g.addEdge(35, 81, 20)
g.addEdge(35, 73, 15)

g.addEdge(36, 54, 40)
g.addEdge(36, 17, 41)

g.addEdge(36, 77, 50)
g.addEdge(36, 62, 32)

g.addEdge(37, 7, 23)
g.addEdge(37, 58, 5)
g.addEdge(37, 66, 21)

g.addEdge(38, 14, 6)
g.addEdge(38, 43, 16)
g.addEdge(38, 79, 20)
g.addEdge(38, 50, 12)

g.addEdge(39, 79, 4)
g.addEdge(39, 50, 10)
g.addEdge(39, 80, 11)

g.addEdge(40, 48, 20)
g.addEdge(40, 7, 18)
g.addEdge(40, 25, 37)
g.addEdge(40, 32, 26)


g.addEdge(41, 15, 42)
g.addEdge(41, 24, 20)
g.addEdge(41, 92, 15)
g.addEdge(41, 84, 12)


g.addEdge(42, 22, 24)
g.addEdge(42, 55, 10)
g.addEdge(42, 91, 17)
g.addEdge(42, 31, 15)

g.addEdge(43, 60, 15)
g.addEdge(43, 14, 10)
g.addEdge(43, 38, 16)
g.addEdge(43, 79, 6)

g.addEdge(44, 15, 21)

g.addEdge(44, 35, 62)


g.addEdge(45, 32, 25)
g.addEdge(45, 16, 28)
g.addEdge(45, 29, 14)
g.addEdge(45, 3, 21)

g.addEdge(46, 2, 27)

g.addEdge(46, 21, 30)
g.addEdge(46, 3, 34)

g.addEdge(47, 70, 27)
g.addEdge(47, 5, 35)
g.addEdge(47, 31, 42)
g.addEdge(47, 83, 24)

g.addEdge(47, 85, 14)
g.addEdge(47, 23, 10)

g.addEdge(48, 64, 32)
g.addEdge(48, 27, 29)
g.addEdge(48, 12, 23)
g.addEdge(48, 34, 58)
g.addEdge(48, 25, 45)
g.addEdge(48, 40, 20)
g.addEdge(48, 7, 38)

g.addEdge(49, 67, 39)
g.addEdge(49, 72, 7)

 
g.addEdge(49, 76, 9)

g.addEdge(50, 38, 12)
g.addEdge(50, 79, 8)
g.addEdge(50, 39, 10)

g.addEdge(51, 65, 21)
g.addEdge(51, 17, 35)
g.addEdge(51, 78, 17)

g.addEdge(52, 75, 24)
g.addEdge(52, 23, 12)
g.addEdge(52, 92, 23)
g.addEdge(52, 6, 5)

 
g.addEdge(53, 76, 4)
g.addEdge(53, 4, 45)
g.addEdge(53, 2, 21)
g.addEdge(53, 10, 32)

g.addEdge(54, 1, 45)
g.addEdge(54, 17, 46)
g.addEdge(54, 36, 40)

g.addEdge(55, 60, 10)
g.addEdge(55, 79, 16)
g.addEdge(55, 42, 10)
g.addEdge(55, 91, 18)
g.addEdge(55, 71, 7)
g.addEdge(55, 80, 2)

g.addEdge(56, 59, 14)
g.addEdge(56, 31, 16)
g.addEdge(56, 83, 8)

g.addEdge(57, 12, 16)
g.addEdge(57, 28, 14)

g.addEdge(58, 90, 39)
g.addEdge(58, 61, 15)
g.addEdge(58, 64, 45)
g.addEdge(58, 66, 7)
g.addEdge(58, 37, 5)

g.addEdge(59, 11, 11)
g.addEdge(59, 18, 34)
g.addEdge(59, 4, 21)
g.addEdge(59, 56, 14)

g.addEdge(60, 14, 12)
g.addEdge(60, 43, 15)
g.addEdge(60, 55, 10)
g.addEdge(60, 22, 6)

g.addEdge(61, 19, 26)
g.addEdge(61, 64, 21)
g.addEdge(61, 58, 15)

g.addEdge(62, 1, 36)
g.addEdge(62, 26, 42)
g.addEdge(62, 36, 32)
g.addEdge(62, 77, 20)


g.addEdge(63, 88, 12)
g.addEdge(63, 16, 21)
g.addEdge(63, 81, 9)

g.addEdge(64, 86, 28)
g.addEdge(64, 61, 21)
g.addEdge(64, 58, 45)
g.addEdge(64, 48, 32)

g.addEdge(65, 17, 29)
g.addEdge(65, 51, 21)

g.addEdge(66, 68, 29)
g.addEdge(66, 58, 7)
g.addEdge(66, 37, 21)

g.addEdge(67, 28, 33)
g.addEdge(67, 34, 27)

g.addEdge(67, 49, 39)
g.addEdge(67, 72, 33)
g.addEdge(67, 82, 26)

g.addEdge(68, 77, 60)
g.addEdge(68, 90, 32)
g.addEdge(68, 66, 29)
g.addEdge(68, 9, 54)

g.addEdge(69, 1, 26)
g.addEdge(69, 26, 30)

g.addEdge(70, 5, 8)
g.addEdge(70, 47, 27)

g.addEdge(71, 55, 7)
g.addEdge(71, 91, 11)
g.addEdge(71, 5, 16)


g.addEdge(72, 82, 22)

g.addEdge(72, 67, 33)
g.addEdge(72, 49, 7)

g.addEdge(73, 74, 6)
g.addEdge(73, 30, 27)
g.addEdge(73, 35, 15)

g.addEdge(73, 24, 26)

g.addEdge(74, 73, 6)
g.addEdge(74, 30, 21)

 
g.addEdge(75, 52, 24)
g.addEdge(75, 10, 30)
g.addEdge(75, 4, 15)
g.addEdge(75, 83, 19)

g.addEdge(76, 49, 9)
g.addEdge(76, 53, 4)
g.addEdge(76, 4, 37)


g.addEdge(77, 62, 20)
g.addEdge(77, 36, 50)
g.addEdge(77, 90, 43)
g.addEdge(77, 68, 60)

g.addEdge(78, 51, 17)

g.addEdge(78, 86, 20)

g.addEdge(79, 43, 6)
g.addEdge(79, 38, 20)
g.addEdge(79, 50, 8)
g.addEdge(79, 55, 16)
g.addEdge(79, 80, 6)
g.addEdge(79, 39, 4)

g.addEdge(80, 55, 2)
g.addEdge(80, 79, 6)
g.addEdge(80, 39, 11)

g.addEdge(81, 35, 20)
g.addEdge(81, 88, 23)
g.addEdge(81, 63, 9)
g.addEdge(81, 16, 32)

g.addEdge(81, 3, 36)

g.addEdge(82, 67, 36)
g.addEdge(82, 72, 22)
g.addEdge(82, 20, 37)

g.addEdge(83, 4, 12)
g.addEdge(83, 56, 8)
g.addEdge(83, 75, 19)

g.addEdge(83, 47, 24)

g.addEdge(84, 92, 10)
g.addEdge(84, 6, 9)
g.addEdge(84, 41, 12)

 
g.addEdge(85, 47, 14)
g.addEdge(85, 23, 4)

g.addEdge(86, 78, 20)

g.addEdge(86, 19, 31)
g.addEdge(86, 64, 28)
g.addEdge(86, 27, 25)

g.addEdge(87, 20, 17)
g.addEdge(87, 89, 10)
 

g.addEdge(88, 63, 12)
g.addEdge(88, 81, 23)

g.addEdge(89, 87, 10)

g.addEdge(89, 33, 12)

g.addEdge(90, 77, 43)
g.addEdge(90, 19, 28)
 
g.addEdge(90, 58, 39)
g.addEdge(90, 68, 32)

g.addEdge(91, 42, 17)
g.addEdge(91, 55, 18)
g.addEdge(91, 31, 18)
g.addEdge(91, 71, 11)
g.addEdge(91, 5, 5)

g.addEdge(92, 15, 37)
g.addEdge(92, 10, 21)

g.addEdge(92, 41, 15)
g.addEdge(92, 84, 10)
g.addEdge(92, 6, 27)
g.addEdge(92, 52, 23)





def main():
    city = [
        "Rio de Janeiro",	
	"São Gonçalo",	
	"Duque de Caxias",	
	"Nova Iguaçu",	
	"Niterói",	
	"Belford Roxo",	
	"Campos dos Goytacazes",	
	"São João de Meriti",	
	"Petrópolis",	
	"Volta Redonda",	
	"Macaé",	
    	"Magé",	
	"Itaboraí",	
	"Cabo Frio",	
	"Angra dos Reis",	 
	"Nova Friburgo",	 
	"Barra Mansa",	 
	"Teresópolis",	 
	"Mesquita",	 
	"Maricá",	 
	"Nilópolis",	 
	"Rio das Ostras",	 
	"Queimados",	 
	"Itaguaí",	 
	"Araruama",	 
	"Resende",	 
	"São Pedro da Aldeia",	 
	"Japeri",	 
	"Itaperuna",	 
	"Barra do Piraí",	 
	"Seropédica",	 
	"Saquarema",	 
	"Três Rios",	 
	"Valença",
	"Guapimirim",	 
	"Rio Bonito",	 
	"Cachoeiras de Macacu",	 
	"Paracambi",	 
	"Mangaratiba",	 
	"Casimiro de Abreu",	 
	"Paraíba do Sul",	 
	"Paraty",	 
	"Santo Antônio de Pádua",	 
	"São Francisco de Itabapoana",	 
	"São Fidélis",	 
	"Bom Jesus do Itabapoana",	 
	"Vassouras",	 
	"São João da Barra",	 
	"Tanguá",	 
	"Armação dos Búzios",	 
	"Itatiaia",	 
	"Arraial do Cabo", 
	"Piraí",	 
	"Iguaba Grande",	 
	"Paty do Alferes",	 
	"Bom Jardim",
	"Miracema",
	"Miguel Pereira",
	"Pinheiral",
	"Quissamã",
	"Conceição de Macabu",	 
	"Itaocara",	 
	"Cordeiro",	 
	"São José do Vale do Rio Preto",	 
	"Silva Jardim",	 
	"Cantagalo",	 
	"Porto Real",	 
	"Carmo",	 
	"Porciúncula",	 
	"Mendes",	 
	"Rio Claro",	 
	"Sapucaia",	 
	"Carapebus",	 
	"Sumidouro",	 
	"Cambuci",	 
	"Natividade",	 
	"Italva", 
	"Quatis",	 
	"Engenheiro Paulo de Frontin",	 
	"Cardoso Moreira	", 
	"Areal",	 
	"Aperibé",	 
	"Duas Barras",	 
	"Varre-Sai",	 
	"Trajano de Moraes",	 
	"Santa Maria Madalena",	 
	"São Sebastião do Alto",	 
	"Rio das Flores",	 
	"Comendador Levy Gasparianv", 
	"Laje do Muriaé",	 
	"São José de Ubá", 
	"Macuco"
        ]
    cont=0
    while cont<len(city):
        print(cont+1,"-",city[cont])
        cont=cont+1
    op = int(input("Escolha o ponto de partida: "))
    print("DFS")
    g.DFS(op)

