






def grade_convertor(*grades):
    gp =[]
    for m in grades:
        if m == "s":
            gp.append(10)
        elif m == "a+":
            gp.append(9)
        elif m == "a":
            gp.append(8.5)
        elif m == "b+":
            gp.append(8)
        elif m == "b":
            gp.append(7.5)
        elif m == "c+":
            gp.append(7)
        elif m == "c":
            gp.append(6.5)
        elif m == "d":
            gp.append(6)
        elif m == "p":
            gp.append(5)
        elif m == "f":
            gp.append(0)

    gp = [float(x) for x in gp]
    sgpa = (gp[0]*3 + gp[1]*4 + gp[2]*3 + gp[3]
            * 4 + gp[4]*4 + gp[5]*1 + gp[6]*1)/(20)
    return sgpa
if __name__ == "__main__":
    
    m1 = (input("enter grade for mathemaics for information science -1: ")).lower()
    m2 = (input("enter grade for Chemistry/physics for information science: ")).lower()
    m3 = (input("enter grade for engineering graphic and Computer Aided Drawing: ")).lower()
    m4 = (input("enter grade for Introduction to Electrical and Electronics Engineering: ")).lower()
    m5 = (input("enter grade for Algorithmic Thinking with Python (ATP): ")).lower()
    m6 = (input("enter grade for Basic Electrical and Electronics Engineering Workshop: ")).lower()
    m7 = (input("enter grade for Life Skills and Professional Communication: ")).lower()
