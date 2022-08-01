nominee1 = input("Enter the name of the 1st nominee : ")
nominee2 = input("Enter the name of the 2st nominee : ")

nm1_votes = 0
nm2_votes = 0
voter_id = [1,2,3,4,5,6,7,8,9,10]
no_of_voter = len(voter_id)
while True:
    if voter_id ==[]:
        print ("voting session is over")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes / no_of_voter)*100
            print(nominee1, "has won the election" , percent, "% of votes")
            break
        elif  nm2_votes > nm1_votes:
            percent = (nm2_votes/no_of_voter)*100
            print(nominee2 ," has  won the election", percent, "% of votes")
            break
        else:
            print("both have egual votes~!!! Governmet will decide the winner")

    voter = int( input( "Enter your voter id: "))
    if voter in voter_id:
        print("you are a voter")
        voter_id.remove(voter)
        print("--------------")
        print("to give vote to" , nominee1, "press 1 " )
        print("to give vote to " , nominee2, "press 2")
        print("----------")
        vote = int(input("Enter you precious vote : "))
        if vote == 1:
            nm1_votes +=1
            print(nominee1, "Thanks you to give important vote to them")
        elif vote == 2:
            nm2_votes +=1
            print(nominee2, "Thankyou to give your important vote  to them ")
        elif vote > 2:
            print("check your press key")
        else:
            print("your are note a voter or you have already voted")