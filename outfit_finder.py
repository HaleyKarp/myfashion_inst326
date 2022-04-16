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
        
        #with open to open closet file 
        #display file contents to user with columns 
        
        
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
    
    def clothing_style(short,sleeve_long,knee_high,long_pants):
        """
        If user picks based on friends style
            Ask user to indicate what the friend 
            is most likely to wear for 
            tops:
                short sleeve/long, etc
            bottoms: knee high, short, long pants, etc
            shoes: heels, sandals, flip flops 
        
        Use the criteria to return an outfit that
        has all three of those implemented 
        (need to match certain colors) 
        
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

    """
    def add_clothing():
     """
    This function will add clothing to the closet
        
     """
     
    def sub_clothing():
        """
        This function will get rid of old/irrelevant clothes
        
        """
    
    """
    Function
    If user needs to add clothing items to closet
    
    """
    
    """
    Function that saves the created outfits to a new textfile? 
    Just an idea
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