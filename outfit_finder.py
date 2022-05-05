# Import writer class from csv module
from csv import writer
import pandas as pd



class MyCloset:
    """ Represents an instance of a closet full of outfits. The user can interact with this closet.
    
    Attribute:
        closet_df(df): dataframe of the closet items 
    """
    

    closet_df = pd.read_csv ("fashion_project.csv")
    closet_df = pd.DataFrame((closet_df), 
                columns = ["category", "length","type",	"material",	"gender","occasion","weather","color"])
    print(closet_df)
        
    def __init__(self):
        """ Creates an instance of MyCloset object. 
            
        """
        #self.closet_df = pd.read_csv (self.path)
        #when we submit it we need to not hard code this line
        self.closet_df = pd.read_csv ("fashion_project.csv")
        self.criteria = []
        self.matched_items = []
        #self.ask_user()
        self.interpret_choice()
        #closet_df = pd.DataFrame((closet_df), 
               # columns = ["category", "length","type",	"material",	"gender","occasion","weather","color"])
       # print(self.closet_df)
    
    def ask_user(self):  
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
        print("1. pick an outfit for the day\n2. based on friends style\
            \n3. pack for a trip\n4. add new clothes to closet\
              \n5. rank my clothing items")
    
        user_choice = int(input("I would like to: "))
        if (user_choice == 1) or (user_choice == 2) or (user_choice == 3) or (user_choice == 4) or (user_choice == 5):
            return user_choice
        else: 
            user_choice = int(input("Please try again, enter 1 - 5."))
            return user_choice
        

    def day_outfit(self): 
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

        print("Would you like to find an outfit based on: \n1.Casual vs Formal?\n2.Color\n3.Weather ")
        day_answer = int(input("Insert number that corresponds to answer choice: "))
        if day_answer == 1:
            casform = input("casual or formal?")
            if casform == "casual":
                print("These are all the clothing you have that are casual.")
                casual = MyCloset.closet_df[MyCloset.closet_df["occasion"] == "casual"]
                print(casual)
                
                gender = input("\nAre you a male or female? ")
                if gender == "male":
                    male = casual[MyCloset.closet_df["gender"] == "male"]
                    print("Here are your closet items\n", male)
                    
                if gender == "female":
                    female = casual[MyCloset.closet_df["gender"] == "female"]
                    print("Here are your closet items\n", female)
            
            else:
                print("These are all the clothing you have that are casual.")
                formal = MyCloset.closet_df[MyCloset.closet_df["occasion"] == "formal"]
                print(formal)
                
                gender = input("\nAre you a male or female? ")
                if gender == "male":
                    male = formal[MyCloset.closet_df["gender"] == "male"]
                    print("Here are your closet items\n", male)
                    
                if gender == "female":
                    female = formal[MyCloset.closet_df["gender"] == "female"]
                    print("Here are your closet items\n", female)
        
        elif day_answer == 2:
            colors = MyCloset.closet_df.groupby("color")
            print(colors)
        
        else:
            print("Let's see what your closet has based on weather:")
            weather = input("What is the weather today? warm, cold, between? ")
            if weather == "warm":
                warm = MyCloset.closet_df[MyCloset.closet_df["weather"] == "warm"]
                print(warm)
            elif weather == "cold":
                cold = MyCloset.closet_df[MyCloset.closet_df["weather"] == "cold"]
                print(cold)
            else: 
                both = MyCloset.closet_df[MyCloset.closet_df["weather"] == "both"]
                print(both)
            
                    
                    
            """
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
                """
                
                        
    def get_criteria(self): 
        """Asks the user for criteria which they want to rank their outfits on. They can pick
            based on weather, color, and occasion.

        Returns:
            list (string tuples): A list of strings where each index is the answer for the choices. 
        """
        weather_choice = input("Please pick the weather: warm, cold, both: ")
        occasion_choice = input("Please pick the style: formal, causual, both ")
        color_choice = input("Please chose a color: black, blue, white, tan, gray, pink, purple, silver ")
        self.criteria.append(occasion_choice)
        self.criteria.append(color_choice)
        self.criteria.append(weather_choice)
        return self.criteria
    
    def rank_choices(self):
        """This is going to be the main ranking function for 
            each piece of clothing.
        
        Args:
            criteria (list): A list of tuples which represent each row of the dataframe 
                                where each row is a clothing item.
        
        Returns:
            A sorted and ranked list of closet items tuples based on the 
            current criteria.
        
        """
        wardrobe_lists = self.closet_df.to_records(index=False)
        #criteria = (occasion_choice, color_choice, weather_choice)
        self.matched_items = sorted(wardrobe_lists, key=lambda wardrobe_lists: ((wardrobe_lists[-1] == self.criteria[1]), 
                                                                  (wardrobe_lists[5] == self.criteria[0]), 
                                                                  (wardrobe_lists[6] == self.criteria[2])), 
                      reverse=True)
        return self.matched_items
    
    def highest_rated(self):
        """Picks out the highest ranked outfit from the list.
        
        Args:
            ranked (list): the returned ranked list from rank_choices
        
        Returns:
            A string representation of the top ranked outfit broken
            down into its compenents (top, bottoms, etc.).
        """
        #a list of tuples ordered by tops, bottoms, then shoes
        outfit_complete = []
        clothing_tops = [item for item in self.matched_items if 'tops' in item]
        clothing_bottoms = [item for item in self.matched_items if 'bottoms' in item]
        clothing_shoes = [item for item in self.matched_items if 'shoes' in item]
        outfit_complete.append(clothing_tops[0])
        outfit_complete.append(clothing_bottoms[0])
        outfit_complete.append(clothing_shoes[0])
        print('Top:', clothing_tops[0])
        print('Bottoms:', clothing_bottoms[0])
        print('Shoes:', clothing_shoes[0])
        #print('THIS IS THE COMPLETE OUTFIT!!!: ', outfit_complete)
        return outfit_complete
        
    
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
        
        #make dataframe with friend qualities
        #use dataframe comparisons/sets and such to compare
        #data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
        print("We see you want an outfit like your friends, let's see what we can do!")
        friend_length =input("Do your friends like long or short clothing? ") 
        friend_material = input("Do your friends like jeans, khakis or cotton? ")
        friends_color = input("What colors does your friend tend to where?")
        
        friend_df = {"length":[friend_length]}
        print(friend_df)
         
    
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
        concat() 
        *make new df with users new outfit
        *concat that new df with closet_df and return as closet_df? 
        magic methods
        Jiwon 
        This function will add clothing to the closet
        
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
        
    
    def my_outfits(self): 
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
        print(self.criteria )
    
        
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
    def interpret_choice(self):
        """Call the appropriate functions internally to interpret what the user wants to do
            upon instantiation of a MyCloset object.
        """
        choice = self.ask_user()
        if choice == 1:
            self.day_outfit()
        elif choice == 2:
            self.clothing_style()
        elif choice == 5:
            self.get_criteria()
            self.rank_choices()
            self.highest_rated()
      
if __name__ == "__main__":
    closet = MyCloset()
    #choice = closet.ask_user()
 

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




        