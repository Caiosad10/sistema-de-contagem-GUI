import dados

def print_pets():
  if len(dados.pets) == 0:
    print("Não há pets cadastrados.")

  else:
    i = 1 
    for pet in dados.pets:
      print(f"{i}º - {pet.name} - {pet.raça}")
      i += 1