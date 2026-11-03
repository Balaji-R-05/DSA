def main():
  order = {"Ocelot":1, "Serval":2, "Lynx":3}
  X, Y = input().strip().split()
  if order[X] >= order[Y]:
    print("Yes")
  else:
    print("No")

if __name__ == "__main__":
  main()