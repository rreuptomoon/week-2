


def avg(data):
    average_salary = 0
    flag = 0   
    for i in data['employees']:
        if i['manager'] == False:
             average_salary += i['salary']
             flag +=1
        elif i["name"] == "John":
            flag = False
            average_salary += i['salary']
            flag +=1
        elif i["salary"] > 60000:
            flag = False
            average_salary += i['salary']
            flag +=1

    return average_salary/flag
         

# 請用你的程式補完這個函式的區塊
res=avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
})

print("The average is salary ",int( res))



