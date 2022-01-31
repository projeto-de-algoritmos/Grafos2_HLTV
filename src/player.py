class Player:
    # identificador  == -1, invalido, nao atribuido.
    def __init__(self,identificador=-1,nome="",foto="",nacionalidade="",conexoes=[]):
        self.identificador = identificador
        self.nome = nome
        self.foto = foto
        self.nacionalidade = nacionalidade
        self.conexoes = conexoes

    def __str__(self):
        ans = "Nome:{}\nNacionalidade:{}\n".format(self.nome,self.nacionalidade)
        ans += "IMG:{}\n".format(self.foto)
        ans += "Id:{}\n".format(self.identificador)
        ans += "conexoes:{}\n".format(self.conexoes)
        return ans


    def to_dict(self):
        dicionario = {}
        dicionario['nome'] = self.nome
        dicionario['foto'] = self.foto
        dicionario['nacionalidade'] = self.nacionalidade
        dicionario['identificador'] = self.identificador
        dicionario['conexoes'] = self.conexoes.__str__()[1:-1]

        return dicionario

    def connect(self,id_team_mate=-1):
        if (id_team_mate not in self.conexoes) and id_team_mate != -1 and id_team_mate != self.identificador:
            self.conexoes.append(id_team_mate)
            return True
