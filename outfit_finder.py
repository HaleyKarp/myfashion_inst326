# Import writer class from csv module
from csv import writer
import pandas as pd



class MyCloset:
    """ Help users pick an outfit based on 
    criteria given by the user
    
    Attribute:
        closet_df(df): dataframe of the closet items 
    """
    
    closet_df = pd.read_csv ("fashion_project.csv")
    closet_df = pd.DataFrame((closet_df), 
                columns = ["category", "length","type",	"material",	"gender","occasion","weather","color"])
    print(closet_df)
    
    def __init__(self, closet_df):
        """ 
            Docstring
        """
        self.closet = closet_df
        criteria = []
    
    
    def ask_user(user_choice):  
        """
        Function that asks user what they want to do
            1. pick an outfit for the day
            2. based on friends style 
            3. Pack for a trip
            4. add new clothes to closet
        
        Args:
            user_choice (int): indicates what the user wants to do first 
        
        Returns:
            user_choice (int): indicates what the user wants to do first 
        
        """
        print("What would you like to do?")
        print("1. pick an outfit for the day\n2. based on friends style\n3. pack for a trip\n4. add new clothes to closet")
        user_choice = int(input("I would like to: "))
          
        if (user_choice != 1 and user_choice !=2 and 
            user_choice != 3 and user_choice !=4):
            raise ValueError ("This is not a valid answer choice")
        else:
            return user_choice
        

    def day_outfit(): 
        """
        Allow user to indicate what they want to find an outfit for, 
        based on type of attire, color, or the weather 
        
        Args: 
            choice (int): 1,2, or 3 for users choice
            
        Raises:  
            ValueError is user doesn't input on of the answer choices 
        
        Return: 
            user_choice (int): indicates if user wants outfit based on options 
        
        1. An outfit for a casual or formal event?
        2. What colors are they looking for? 
        3. What is the weather supposed to be like?
    
        """
        #print(MyCloset.closet_df)
        print("Would you like to find an outfit based on: \n1.Casual vs Formal?\n2.Color\n3.Weather ")
        day_answer = int(input("Insert number that corresponds to answer choice: "))
        if day_answer == 1:
            casform = input("casual or formal?")
            if casform == "casual":
                print("These are all the clothing you have that are casual.")
                casual = MyCloset.closet_df[MyCloset.closet_df["occasion"] == "casual"]
                print(casual)
                
                gender = input("\nAre you a male or female? ")
                if gender == "female":
                    female_casual = casual[MyCloset.closet_df["gender"] == "female"]
                    female_bottoms = female_casual[MyCloset.closet_df["category"] == "bottoms"]
                    bottom_color = input("Would you like the bottoms to be blue, white, or black?")
                    if bottom_color == "blue":
                        bottoms_color = female_bottoms[MyCloset.closet_df["color"] == "blue"]
                        print(f"We reccomend one of these bottoms: \n{bottoms_color}")
                        
                    
                    #female_tops = casual[MyCloset.closet_df["category"] == "tops"]
                        #print(female_tops)
                        #tops_color = female_tops[MyCloset.closet_df["color"] != "blue"]
                        #print(f"The tops we reccomend to pair with it are: \n {tops_color}")
                        #print(female_casual.loc[1])
                    #female_tops = female_casual[MyCloset.closet_df["category"] == "tops"]
                    #female_shoes = female_casual[MyCloset.closet_df["category"] == "shoes"]
                    
                    
                elif gender == "male":
                    male_casual = casual[MyCloset.closet_df["gender"] == "male"]
                    print(male_casual)
                
            elif casform == "formal":
                print("These are all the clothing you have that are formal.")
                print(MyCloset.closet_df[MyCloset.closet_df["occasion"] == "formal"])
                
                        
    def rank_choices():
            """This is going to be the main ranking function for 
            each piece of clothing.
        
        Args:
            criteria (list): list of strings with the answers to questions
                to serve as the sorting criteria
        
        Returns:
            A sorted and ranked list of closet items based on the 
            current criteria.
        
        """
    def highest_rated():
        """Picks out the highest ranked outfit from the list.
        
        Args:
            ranked (list): the returned ranked list from rank_choices
        
        Returns:
            A string representation of the top ranked outfit broken
            down into its compenents (top, bottoms, etc.).
        """
        
    
    def clothing_style():
        """
        Sequence unpacking?!?!?!
        Read it in as a tuple and unpack it!!!
        Jiwon :) 
        If user picks based on friends style
            Ask user to indicate what the friend 
            is most likely to wear for 
        
        Args:
            friend_tops (list): different types of tops the friends where
            friend_bottoms (list): list of attributes of bottoms the friends
            might where
            friend_shoes (list): list of shoes the friends where 
            match_friend (list): list of clothing items from your closet
            that match friend based on similarities 
        
        Return:
            match_friend (list): list of clothing items from your closet

        """
        
        
        
        
    
    def packing():
        """
        Andy
        If user packs for a trip
        Function
            Ask user how many days they are
            staying? 
            depending on number of days, 
            give outfits accordingly to wear 
            each day 
        
        Args:
            days (int): number of days they are going on the trip
            outfit (list): outfit list
        
        Returns:
            list: outfit list

        """
    def add_clothing(self, closet_df):
        """

        This function will ask users to add a clothing as a new row to CSV file.
        
        Args: 
        filepath (file): path to the csv file 
        add_clothing_name (str): bottoms/tops or shoes
        add_clothing_color(str): clothing color
        add_clothing_length (str): long, short
        add_clothing material (str): jean, cotton, khaki, spandex
        add_clothing_gender (str): male or female
        add_clothing_weather (str): warm or cold
    
        """
        add_clothing_name = str(input("write the type of clothing: \n"))
        add_clothing_color = str(input("color?: \n"))
        add_clothing_length = str(input("length?: \n"))
        add_clothing_material = str(input("material?: \n"))
        add_clothing_gender = str(input("gender?: \n"))
        add_clothing_weather = str(input("weather?: \n"))
        
        new_row = [add_clothing_name, add_clothing_color, add_clothing_length, 
                    add_clothing_material, add_clothing_gender, add_clothing_weather]
        
        with open(closet_df, 'a') as f:
            # Pass this file object to csv.writer() and get a writer object
            writer_object = writer(f)
            # Pass the list as an argument into the writerow()
            writer_object.writerow(new_row)
            
            #Close the file object
            f.close()
                    
                    
        
        
    
    def my_outfits(): 
        """
        Haley 
        Take users criteria and rank priority to determine outfits
        
        Args:
            new_outfit (list): top, bottom and shoes that will 
            be created as a list under "outfit" in new textfile 
        
        Returns:
             my_outfits(textfile): new textfile where the columns chosen will be
            saved to 
            
        What do you want to rank outfits by? 
        length: 
        append to criteria
        type:
        append
        citeria = [long, short, pants, leggings]
            
        
        Saved to a list, that grace can read in to rank choices

        """
    
        
    def display():
        """
        Andy and Jay 
        Take what grace has ranked, and send it to a textfile 
            This function will display all "outfits" made from the 
            textfile that the user can output to
        
        Args:
            my_outfits(textfile): new textfile where the columns chosen will be
            saved to 
        
        Return: 
            display the outfits made by the user 

        """
      
if __name__ == "__main__":
    MyCloset()
    if MyCloset.ask_user(user_choice= 1):
        MyCloset.day_outfit()
    elif MyCloset.ask_user(user_choice = 2):
        MyCloset.clothing_style()
    elif MyCloset.ask_user(user_choice = 3):
        MyCloset.packing()
    elif MyCloset.ask_user(user_choice = 4):
        MyCloset.add_clothing()
        
        

"""
    MyCloset.display()
    MyCloset.ask_user()
    MyCloset.my_outfits()
    MyCloset.add_clothing()
    MyCloset.packing()
    MyCloset.clothing_style()
    MyCloset.highest_rated()
    MyCloset.rank_choices()
    MyCloset.day_outfit()
"""


"""
This is actually our main function that should call everything 
        (mini notes below abt ideas for this)
        ask_user() should get called first 
        If user picks 1 run: 
                - day_oufit()
                - ranking function
                - funtion that displays the number 1 outfit of each item 
    if user picks 2...
"""




        