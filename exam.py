medical_cause=input("did you have a medical cause Y or N:")
attend=int(input("enter the attendance of the student:"))
if medical_cause=="Y":
    print("you are allowed")
else:
    if attend>=75:
        print("allowed")
    else:
        print("not allowed")     