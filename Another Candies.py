def second_main():   
        studen = input()
        try:          
            sum = 0
            i=0
            while(i<int(studen)):
                candy = int(input())
                sum += candy
                i+=1
            if sum % int(studen) == 0 or sum == int(studen):
                return "YES"
            else:
                return "NO"
        except:
            return second_main()
def main():
    N = int(input())
    for j in range(0,N):
        print(second_main())
main()
