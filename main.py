import requests

def invasive_species(num):
  url = f"https://api-colombia.com/api/v1/Invasivespecie/{num}"

  response  = requests.get(url)
  data = response.json()

  information = {
    "id": data["id"],
    "name": data["name"],
    "scientificName": data["scientificName"],
    "impact": data["impact"]
  }
  

  return information





def main():
  print("Hello, students!")

  num = int(input("Numero de especie: "))
  resultado = invasive_species(num)
  print(resultado)

if __name__=="__main__":

  main()