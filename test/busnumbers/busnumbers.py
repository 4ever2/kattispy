n = int(input())
list_of_ints = sorted([int(k) for k in input().split(" ")])
final_string = ""

i = 0
while(i<n):
    index = str(list_of_ints[i])

    if(i+1 < n and i+2 < n and (list_of_ints[i]+1==list_of_ints[i+1]) and (list_of_ints[i]+2==list_of_ints[i+2])):
        end_of_index = list_of_ints[i+2]
        j = i+2
        while(j+1<n and list_of_ints[j]+1 == list_of_ints[j+1]):
            j=j+1

        index = index + "-" +str(list_of_ints[j])
        i=j+1
    else:
        i=i+1

    final_string = final_string + " " + index

print(final_string.lstrip())
