import pprint

class BunnyHopper(object):
    """class to represent a mini springer kit for crafting purpose"""
    
    def __init__(self, color):
        self.color = color
        self.bunnies = list()
        self.printer = pprint.PrettyPrinter(indent=4)
        
        
    def craft(self):
        """return a list of lists with all mini springer kit colors to craft"""
        color_list = list()
        
        for bunny in self.bunnies:
            if bunny.color == "brown":
                color_list.append("brown")
            else:
                color_list.extend([bunny.color, bunny.craft()])
                
        return color_list
    
    
    def count(self, color="brown"):
        """counts number of mini springer kit of required color to craft"""
        color_list_flat = self.flatten(self.craft())
        
        return color_list_flat.count(color)
        
        
    def flatten(self, color_list, sequence=None):
        """flatten list of lists to one list for counting purpose"""
        if not sequence:
            sequence = list()
            
        for color in color_list:
            if isinstance(color, list):
                self.flatten(color, sequence)
            else:
                sequence.append(color)
                
        return sequence
    
    
    def print_color_list(self):
        """print list of list with pretty print"""
        color_list = self.craft()
        
        self.printer.pprint(color_list)

        
def main():
    """main function to choose craftable mini sprinter kit"""
    bunny_map = dict()
    bunny_colors = ["brown", "red", "yellow", "green", "white", "black", "pink", "cyan", "thunder", "primal"]

    for color in bunny_colors:
        bunny_map[color] = BunnyHopper(color)

    bunny_craft = {"brown": list(),
                   "red": [bunny_map["brown"], bunny_map["brown"], bunny_map["brown"]],
                   "yellow": [bunny_map["brown"], bunny_map["red"], bunny_map["red"]],
                   "green": [bunny_map["brown"], bunny_map["red"], bunny_map["yellow"]],
                   "white": [bunny_map["red"], bunny_map["yellow"], bunny_map["yellow"]],
                   "black": [bunny_map["red"], bunny_map["red"], bunny_map["green"]],
                   "pink": [bunny_map["red"], bunny_map["red"], bunny_map["white"]],
                   "cyan": [bunny_map["brown"], bunny_map["green"], bunny_map["black"]],
                   "thunder": [bunny_map["green"], bunny_map["black"], bunny_map["cyan"]],
                   "primal": [bunny_map["white"], bunny_map["pink"], bunny_map["pink"]],}

    for color in bunny_colors:
        bunny_map[color].bunnies = bunny_craft[color]

    end = True
    
    while(end):
        color = raw_input("Please specify the color of the mini springer kit you want to craft: ")
        msg = """\nYou need {} brown mini springer kits to craft the {} mini springer kit.
These are needed to craft the following mini springer kits:\n""".format(bunny_map[color].count("brown"), color)
        print(msg)
        color = color.lower()
        for bunny_color in bunny_colors[1:]:
            try:
                count = bunny_map[color].count(bunny_color)
            
                if count > 0:
                    print("\tYou need to craft {} {} mini springer kits.".format(count, bunny_color))
                    
            except KeyError:
                print("There is no mini springer kit with the color {}, sorry :(".format(color))
            
        next = raw_input("Do you want to find out the number of mini springer kits for another mini springer kit?\n")
        
        if next.lower().startswith("n"):
            end=False
