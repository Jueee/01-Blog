if __name__ == '__main__':  
    string = input('please input string:')  
    with open('f:/test/test.txt', 'a') as file:  
        file.write(string)  
    file.close()  