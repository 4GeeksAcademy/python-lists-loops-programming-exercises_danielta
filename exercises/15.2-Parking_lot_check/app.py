parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here


def get_parking_lot(lot):
  state = {
  "total_slots": 0,
  "available_slots": 0,
  "occupied_slots": 0
  }
  for lane in range(0,len(lot)):
    for spot in range(0,len(lot[lane])):  
      if lot[lane][spot] == 1:
        state["occupied_slots"] += 1
        state["total_slots"] += 1
      elif lot[lane][spot] == 2:
        state["available_slots"] += 1
        state["total_slots"] += 1
      elif lot[lane][spot] == 0:
        None
  return(state)

print(get_parking_lot(parking_state))
