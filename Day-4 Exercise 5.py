row1=['⬜️', '⬜️', '⬜️']
row2=['⬜️', '⬜️', '⬜️']
row3=['⬜️', '⬜️', '⬜️']
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?\n")
column=int(position[0])
row=int(position[1])
selected=map[column-1]
selected[row-1]="X"
print(f"Selected column is{column} and row is{row}")
print(f"{row1}\n{row2}\n{row3}")


