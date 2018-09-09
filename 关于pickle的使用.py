import pickle


pickle_file=open(r'C:\Users\oy199\Desktop\my_list.pkl','rb')
my_list=pickle.load(pickle_file)
print(my_list)
#二进制读的形式


my_list=[123,3.14,'小甲鱼',['another list']]
pickle_file=open('E:\\my_list.pkl','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()
#二进制写的形式