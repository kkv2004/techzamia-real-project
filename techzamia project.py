#project
import sys,pickle,os
def input_a_rec():
                d=dict()
                roll=int(input("Enter roll no.:"))
                name=input("Enter name of the student:")
                age=int(input("Enter the age:"))
                m1=int(input("Enter mark in subject1:"))
                m2=int(input("Enter mark in subject2:"))
                m3=int(input("Enter mark in subject3:"))
                s=m1+m2+m3
                avg=s/3
                d[roll]=[name,age,m1,m2,m3,s,avg]
                return d
def create():
                flag=True
                f=open("record.dat","wb")
                while flag==True:
                                d=input_a_rec()
                                pickle.dump(d,f)
                                opt=input("Enter yes or no:").lower()
                                if opt!='y':flag=False
                f.close()
                return d

def display():
                f=open("record.dat","rb")
                f.seek(0,2)
                size=f.tell()
                f.seek(0,0)
                while f.tell()!=size:
                                m=pickle.load(f)
                                for i in m.keys():
                                                print("Roll no.: ",i)
                                                print("Name : ",m[i][0])
                                                print("Age: ",m[i][1])
                                                print("Mark in subject1:",m[i][2])
                                                print("Mark in subject2:",m[i][3])
                                                print("Mark in subject3:",m[i][4])
                                                print("Sum of the marks of the 3 subjects:",m[i][5])
                                                print("Average of the marks of the 3 subjects: ",m[i][6])
                f.close()
def search():
                f=open("record.dat","rb")
                data=int(input("Enter the roll no. of the record to be searched:"))
                d=dict()
                f.seek(0,2)
                size=f.tell()
                f.seek(0,0)
                flag=True
                
                while f.tell()!=size and flag==True:
                                m=pickle.load(f)
                                for i in m.keys():
                                                if i==data:
                                                                d[i]=[m[i][0],m[i][1],m[i][2],m[i][3],m[i][4],m[i][5],m[i][6]]
                                                                flag=False
                if flag==True:
                                
                                print("Data not found in the file")
                                
                else:
                                print("Data found in the file")
                                for i in d.keys():
                                                print("Rollno.:",i)
                                                print("Name:",m[i][0])
                                                print("Age:",m[i][1])
                                                print("Mark in subject1:",m[i][2])
                                                print("Mark in subject2:",m[i][3])
                                                print("Mark in subject3:",m[i][4])
                                                print("Sum of the marks of the 3 subjects:",m[i][5])
                                                print("Average of the marks of the 3 subjects: ",m[i][6])

def delete():
                f=open("record.dat","rb")
                g=open("dummy.dat","wb")
                data=int(input("Enter the roll no. of the record to be deleted:"))
                f.seek(0,2)
                size=f.tell()
                f.seek(0,0)
                flag=True
                
                while size!=f.tell():
                                m=pickle.load(f)
                                for i in m.keys():
                                                if i!=data:
                                                             pickle.dump(m,g)
                                                             flag=False
                if flag==False:
                                print("Data deleted in the file")
                else:print("Data not found in the file")
                f.close()
                g.close()
                os.remove("record.dat")
                os.rename("dummy.dat","record.dat")
def insert_before():
                f=open("record.dat","rb")
                g=open("dummy.dat","wb")
                data=int(input("Enter the roll no. of the record to be inserted before:"))
                f.seek(0,2)
                size=f.tell()
                f.seek(0,0)
                flag=True
                
                while size!=f.tell():
                                m=pickle.load(f)
                                for i in m.keys():
                                                if i==data:
                                                             d=input_a_rec()
                                                             pickle.dump(d,g)
                                                             pickle.dump(m,g)
                                                             flag=False
                                                else:pickle.dump(m,g)
                if flag==False:
                                print("Data inserted before in the file")
                else:print("Data not found in the file")
                f.close()
                g.close()
                os.remove("record.dat")
                os.rename("dummy.dat","record.dat")
def insert_after():
                f=open("record.dat","rb")
                g=open("dummy.dat","wb")
                data=int(input("Enter the roll no. of the record to be inserted after:"))

                f.seek(0,2)
                size=f.tell()
                f.seek(0,0)
                flag=True
                
                while size!=f.tell():
                                m=pickle.load(f)
                                for i in m.keys():
                                                if i==data:
                                                             d=input_a_rec()
                                                             pickle.dump(m,g)
                                                             pickle.dump(d,g)
                                                             flag=False
                                                else:pickle.dump(m,g)
                if flag==False:
                                print("Data inserted after in the file")
                else:print("Data not found in the file")
                f.close()
                g.close()
                os.remove("record.dat")
                os.rename("dummy.dat","record.dat")
def modify():
                
                f=open("record.dat","rb")
                g=open("dummy.dat","wb")
                data=int(input("Enter the roll no. of the record to be modified:"))
                f.seek(0,2)
                size=f.tell()
                f.seek(0,0)
                flag=True
                
                while size!=f.tell():
                                m=pickle.load(f)
                                for i in m.keys():
                                                if i==data:
                                                             d=input_a_rec()
                                                             pickle.dump(d,g)
                                                             flag=False
                                                else:pickle.dump(m,g)
                if flag==False:
                                print("Data modified in the file")
                else:print("Data not found in the file")
                f.close()
                g.close()
                os.remove("record.dat")
                os.rename("dummy.dat","record.dat")
def sort():
                f=open("record.dat","rb")
                f.seek(0,2)
                size=f.tell()
                f.seek(0,0)
                l=[]
                while size!=f.tell():
                                m=pickle.load(f)
                                l.append(m)
                for i in range(len(l)-1):
                                for j in range(len(l)-1-i):
                                                if list(l[j].keys())[0]>list(l[j+1].keys())[0]:
                                                                l[j],l[j+1]=l[j+1],l[j]
                f=open("record.txt","wb")
                for i in l:
                                pickle.dump(i,f)
                f.close()
                print("Data sorted in the file")
while True:
                print("MENU")
                print("1.Create")
                print("2.Display")
                print("3.Search")
                print("4.Delete")
                print("5.Insert before")
                print("6.Insert after")
                print("7.Modify")
                print("8.Sort")
                print("9.Quit")
                opt=input("Select option 1-9:")
                if opt=='1':create()
                elif opt=='2':display()
                elif opt=='3':search()
                elif opt=='4':delete()
                elif opt=='5':insert_before()
                elif opt=='6':insert_after()
                elif opt=='7':modify()
                elif opt=='8':sort()
                elif opt=='9':sys.exit(0)
                else:print("Select a number 1-9:")
                                
                
                
 
