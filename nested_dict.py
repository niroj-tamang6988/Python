#nested dictionary

student= {
    "name" : "Niroj",
    "subject" : {
        "maths" : 90,
        "english" : 80,
        "computer" : 95
    }
}

print(student) #print all student dictionary
print(student["subject"]) #print subject of student only
print(student["subject"]["maths"])  #print the value of the maths computer only