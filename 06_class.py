class Person(object):
	"""docstring for Person"""
	age = '23'
	sex = 'man'
	#它的参数中有一个self，它是为了方便我们引用对象自身。
	#方法的第一个参数必须是self,这个参数表示某个对象。对象拥有类的所有性质，那么我们可以通过self，调用类属性。
	def move(self,dx,dy):
		position = [0,0]
		position[0] = position[0] + dx
		position[1] = position[1] + dy
		print(self.sex,self.age)
		return position
#对属性的引用是通过 对象.属性（object.attribute） 的形式实现的。
a = Person()
print(a.age)
print('after move:',a.move(3,5))
print('after move:',a.move(5,6) + a.move(5,6))
		
#继承(inheritance)  用继承来说明父类-子类关系。子类自动具有父类的所有属性。
class Man(Person):
	way = '2323'
man = Man()
print(man.way,man.age,man.sex)


class Human(object):
    laugh = 'hahahaha'
    def show_laugh(self):
        print(self.laugh)
    def laugh_3th(self):
        for i in range(3):
            self.show_laugh()

li_lei = Human()          
li_lei.laugh_3th()

'''
__init__()是一个特殊方法(special method)。Python有一些特殊方法。
Python会特殊的对待它们。特殊方法的特点是名字前后有两个下划线。
如果你在类中定义了__init__()这个方法，创建对象时，Python会自动调用这个方法。这个过程也叫初始化。
'''
class happyBird(Man):
    more_words = "desf"
    def __init__(self,more_words):
        print ('We are happy birds.',more_words)

summer = happyBird('wq')

'''
leilei
'''
class Human(object):
    def __init__(self, input_gender):
        self.gender = input_gender
    def printGender(self):
        print(self.gender)

li_lei = Human('male') # 这里，'male'作为参数传递给__init__()方法的input_gender变量。
print(li_lei.gender)
li_lei.printGender()


#dir()用来查询一个类或者对象所有属性。
print(dir(happyBird))
#help()用来查询的说明文档。
print(help(Human))