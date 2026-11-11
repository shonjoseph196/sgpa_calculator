#Same Program in Terminal

def grade_convertor(*grades):
    gp =[]
    for m in grades:
        if m.lower() == "s":
            gp.append(10)
        elif m.lower() == "a+":
            gp.append(9)
        elif m.lower() == "a":
            gp.append(8.5)
        elif m.lower() == "b+":
            gp.append(8)
        elif m.lower() == "b":
            gp.append(7.5)
        elif m.lower() == "c+":
            gp.append(7)
        elif m.lower() == "c":
            gp.append(6.5)
        elif m.lower() == "d":
            gp.append(6)
        elif m.lower() == "p":
            gp.append(5)
        elif m.lower()   == "f":
            gp.append(0)
        else:
            print("Invalid grade entered. Please enter a valid grade.")
            return None

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
    print(grade_convertor(m1, m2, m3, m4, m5, m6, m7)) 