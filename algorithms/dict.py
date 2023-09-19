class Dict():
    def __init__(self):
        pass

    def dictionary_example(self):
        mapping = {}
        # Create list of Students and their Scores on the recent exam
        students = ['Jeremy', 'Vanessa', 'Jeffrey', 'Jahseh', 'Satyam']
        scores = [95, 90, 45, 76, 85, 81]
        # Loop through the array and embed them within the dictionary
        for x in range(len(students)):
            mapping[students[x]] = scores[x]
        # Print out each key from the dictionary
        for x in mapping.keys():
            print(x)

    def sum_of_values(self, dict=None):
        sum = 0 
        for key, val in dict.items():
            if not isinstance(val, int):
                print(f"{key}'s value is not a valid integer. Skipping...")
            else:
                sum += val

        print(f"Final sum: {sum}")  

    def sort_keys(self, dict):
        keys = list(dict.keys())
        keys.sort()
        print("Original", dict.keys())
        print("Sorted", keys)

dict = Dict()

dictionary = {"hello": 4, "world": 'Jacobi', "I": 1, "am": 2, "Martha": 3}
dict.sum_of_values(dictionary)
dict.sort_keys(dictionary)

tupley = ("maple")

print(type(tupley))