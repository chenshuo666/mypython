import random
game_count=0
all_counts=[]
while True:
    game_count+=1 #游戏次数
    guess_count=0 #每次游戏猜的次数
    answer=random.randint(0,99) #随机产生的数字和猜的数字进行比较
    while True:
        guess=int(input("请猜一个数字（0-99）："))
        guess_count+=1
        if guess==answer:
            print('恭喜你猜中了')
            print("你总共猜了"+str(guess_count)+"次")
            all_counts.append(guess_count)
            break;
        elif guess>answer:
            print("你猜的数字过大了")
        elif guess<answer:
            print("你猜的数字过小了")
    onmore=input("你要在玩一次吗（Y/N）？")
    if onmore!='Y'and onmore!='y':
        print("欢迎下次再来，你的成绩是："+str(all_counts))
        print("平均猜中的次数"+str(sum(all_counts)/float(len(all_counts))))
        break;