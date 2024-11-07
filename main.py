'''sort(width, height, length, mass)
Input:  width: int 
        height: int
        length: int
        mass: int
Output:
        Either "REGULAR", "SPECIAL" or "REJECTED"
'''
def sort(width: int, height: int, length: int, mass: int):
  c = 0
  if mass >= 20:
    c += 1
  if width * height * length >= 1000000 or width >= 150 or height >= 150 or length >= 150:
    c += 1

  if c == 0:
    return "REGULAR"
  if c == 1:
    return "SPECIAL"

  return "REJECTED"


def test_sort():
  assert sort(100, 100, 50, 10) == "REGULAR", "Failed on regular package"

  assert sort(100, 100, 50,
              25) == "SPECIAL", "Failed on special package (mass)"

  assert sort(200, 100, 50,
              10) == "SPECIAL", "Failed on special package (volume)"

  assert sort(160, 100, 50,
              10) == "SPECIAL", "Failed on special package (dimension)"

  assert sort(200, 100, 50,
              30) == "REJECTED", "Failed on rejected package (mass and volume)"

  assert sort(
      160, 100, 50,
      25) == "REJECTED", "Failed on rejected package (mass and dimension)"

  assert sort(
      200, 200, 50,
      10) == "SPECIAL", "Failed on rejected package (volume and dimension)"

  assert sort(
      200, 200, 50, 30
  ) == "REJECTED", "Failed on rejected package (mass, volume, and dimension)"

  print("All tests passed.")


test_sort()
infos = input("Enter width, height, length, and mass (seperated by spaces): ")
sep_infos = list(filter(lambda x: x != "", infos.split(" ")))
num_infos = list(filter(lambda x: x.isnumeric(), sep_infos))
infos = list(map(lambda x: int(x), num_infos))
if len(infos) == 4:
  print(sort(*infos))
else:
  print("Invalid input")
