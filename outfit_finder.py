class MyCloset:
    """ Help users pick an outfit based on 
    criteria given by the user
    """
    
    def open_closet(filepath): 
        """
        Function that reads in users closet file
        Display current closet to the users 
        (maybe in table format) 
        
        Args:
            filepath (path): access to closet file 

        Returns:
            The file path to access data from the CSV
        """

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
    
    def rank_choices(criteria):
            """This is going to be the main ranking function for 
            each piece of clothing.
        
        Args:
            criteria (list): list of strings with the answers to questions
                to serve as the sorting criteria
        
        Returns:
            A sorted and ranked list of closet items based on the 
            current criteria.
        
        """
    def highest_rated(ranked):
        """Picks out the highest ranked outfit from the list.
        
        Args:
            ranked (list): the returned ranked list from rank_choices
        
        Returns:
            A string representation of the top ranked outfit broken
            down into its compenents (top, bottoms, etc.).
        """
    
    def clothing_style():
        """
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
    def add_clothing():
        """
        This function will add clothing to the closet
        
        Args: 
        filepath (file): path to the csv file 
        add_clothing_name (str): bottoms/tops or shoes
        add_clothing_color(str): clothing color
        add_clothing_length (str): long, short
        add_clothing material (str): jean, cotton, khaki, spandex
        add_clothing_gender (str): male or female
        add_clothing_weather (str): warm or cold
        
        Raises
            ValueError if user doesn't input the correct data type
            for the clothing item 
        
        
        """
    
    def my_outfits(): 
        """
        Function that outputs outfits to a textfile
        
        Args:
            new_outfit (list): top, bottom and shoes that will 
            be created as a list under "outfit" in new textfile 
        
        Returns:
             my_outfits(textfile): new textfile where the columns chosen will be
            saved to 

        """
    
    
    def ask_user():  
        """
        Function that asks user what they want to do
            1. pick an outfit for the day
            2. based on friends style 
            3. Pack for a trip
            4. add new clothes to closet
            
    
        """
    def display():
        """
        This will be at the end to show the user results when they finalized their decsion of which clothes they chose. 
        
        """
    
    
    
    #if __name__ == “__main__”: 
        """
        This is actually our main function that should call everything 
        
        #ask_user() should get called first 
        
            If user picks 1 run: 
                - day_oufit()
                - ranking function
                - funtion that displays the number 1 outfit of each item 
            
            if user picks 2:
                
        """