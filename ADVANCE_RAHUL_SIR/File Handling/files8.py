daily_tasks=[
    "WakesUp early \n",
    "Get fresh up\n",
    "Do Excercise and eat healthy\n",
    "Get Placed Soon"
]

try:
    with open("mydata.txt","w") as fh:
        if fh.writable():
            fh.writelines(daily_tasks)

except FileNotFoundError as fe:
    print(fe)