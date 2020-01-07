from move_interpreter import Interpreter


intp = Interpreter()

#moves = ["R", "U", "R_", "U_"]
moves = "RU"
intp.add_str_moves(moves)
runs = 1
max_runs = 1000
while (not intp.cbe.is_complete()):
    intp.add_str_moves(moves)
    runs += 1
    if(runs > max_runs - 1):
        print("Cutoff over", max_runs)
        break
    intp.cbe.show()
print("Complete after", runs, "runs.")


print()
intp.cbe.show()
intp.cbe.simple_show()
#intp.cbe.altshow()

print("---")
print(intp.cbe.get_block("A").get_stickers())
print("---")
