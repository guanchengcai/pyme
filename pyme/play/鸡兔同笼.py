print('请输入笼子里面有多少头。')
head = int(input())
print('请输入笼子里面有多少脚。')
feet = int(input())
answer = int((feet/2)-head)
if not answer>0 or not head - answer > 0:
    print('不可能的')
else:
    print('有'+str(answer)+'鸡,'+str(head-answer)+'兔。')