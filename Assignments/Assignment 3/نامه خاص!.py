numbers = [int(j) for j in input().split()]
sum = int(input())

visited={}
answers=[]

for i in range (len(numbers)):

    otherNumber = sum - numbers[i]

    if otherNumber in visited :
        answers.append(visited[otherNumber]+i)

    else:
       visited[numbers[i]] = i

answers.sort()

if len(answers)==0:
    print("Not Found!")
else:
    for ans in answers:
        print(ans)