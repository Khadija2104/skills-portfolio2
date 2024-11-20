import tkinter as tk
import random

# List of jokes embedded directly in the code as (setup, punchline) tuples
jokes = [
    ("Why did the chicken cross the road?", "To get to the other side."),
    ("What happens if you boil a clown?", "You get a laughing stock."),
    ("Why did the car get a flat tire?", "Because there was a fork in the road!"),
    ("How did the hipster burn his mouth?", "He ate his pizza before it was cool."),
    ("What did the janitor say when he jumped out of the closet?", "SUPPLIES!!!!"),
    ("Have you heard about the band 1023MB?", "It's probably because they haven't got a gig yet…"),
    ("Why does the golfer wear two pants?", "Because he's afraid he might get a 'Hole-in-one.'"),
    ("Why should you wear glasses to maths class?", "Because it helps with division."),
    ("Why does it take pirates so long to learn the alphabet?", "Because they could spend years at C."),
    ("Why did the woman go on the date with the mushroom?", "Because he was a fun-ghi."),
    ("Why do bananas never get lonely?", "Because they hang out in bunches."),
    ("What did the buffalo say when his kid went to college?", "Bison."),
    ("Why shouldn't you tell secrets in a cornfield?", "Too many ears."),
    ("What do you call someone who doesn't like carbs?", "Lack-Toast Intolerant."),
    ("Why did the can crusher quit his job?", "Because it was soda pressing."),
    ("Why did the birthday boy wrap himself in paper?", "He wanted to live in the present."),
    ("What does a house wear?", "A dress."),
    ("Why couldn't the toilet paper cross the road?", "Because it got stuck in a crack."),
    ("Why didn't the bike want to go anywhere?", "Because it was two-tired!"),
    ("Want to hear a pizza joke?", "Nahhh, it's too cheesy!"),
    ("Why are chemists great at solving problems?", "Because they have all of the solutions!"),
    ("Why is it impossible to starve in the desert?", "Because of all the sand which is there!"),
    ("What did the cheese say when it looked in the mirror?", "Halloumi!"),
    ("Why did the developer go broke?", "Because he used up all his cache."),
    ("Did you know that ants are the only animals that don't get sick?", "It's true! It's because they have little antibodies."),
    ("Why did the donut go to the dentist?", "To get a filling."),
    ("What do you call a bear with no teeth?", "A gummy bear!"),
    ("What does a vegan zombie like to eat?", "Graaains."),
    ("What do you call a dinosaur with only one eye?", "A Do-you-think-he-saw-us!"),
    ("Why should you never fall in love with a tennis player?", "Because to them... love means NOTHING!"),
    ("What did the full glass say to the empty glass?", "You look drunk."),
    ("What's a potato's favorite form of transportation?", "The gravy train."),
    ("What did one ocean say to the other?", "Nothing, they just waved."),
    ("What did the right eye say to the left eye?", "Honestly, between you and me something smells."),
    ("What do you call a dog that's been run over by a steamroller?", "Spot!"),
    ("What's the difference between a hippo and a zippo?", "One's pretty heavy and the other's a little lighter."),
    ("Why don't scientists trust Atoms?", "They make up everything.")
]

# Function to display the setup of a random joke
def tell_joke():
    global current_joke
    current_joke = random.choice(jokes)
    joke_text.set(current_joke[0])  # Show setup
    punchline_button.config(state=tk.NORMAL)
    next_joke_button.config(state=tk.DISABLED)

# Function to display the punchline
def show_punchline():
    if current_joke:
        joke_text.set(current_joke[1])  # Show punchline
        punchline_button.config(state=tk.DISABLED)
        next_joke_button.config(state=tk.NORMAL)

# Function to quit the program
def quit_program():
    root.quit()

# Initialize the tkinter root window
root = tk.Tk()
root.title("Alexa, Tell Me a Joke")

# Set window size and center it
root.geometry("800x600")
root.configure(bg="#FFEB99")  # Light yellow background

# Create the main frame for alignment
main_frame = tk.Frame(root, bg="#FFEB99")
main_frame.pack(expand=True)

# Joke text
joke_text = tk.StringVar()
joke_text.set("Press 'Tell me a Joke' to start!")

joke_label = tk.Label(
    main_frame, textvariable=joke_text, font=("Arial", 22), bg="#FFEB99", 
    wraplength=700, justify="center"
)
joke_label.pack(pady=20)

# Buttons centered below the text
next_joke_button = tk.Button(
    main_frame, text="Tell me a Joke", command=tell_joke, 
    font=("Arial", 16), bg="#FFC300", fg="black", width=15
)
next_joke_button.pack(pady=10)

punchline_button = tk.Button(
    main_frame, text="Show Punchline", command=show_punchline, 
    font=("Arial", 16), bg="#FFC300", fg="black", state=tk.DISABLED, width=15
)
punchline_button.pack(pady=10)

quit_button = tk.Button(
    main_frame, text="Quit", command=quit_program, 
    font=("Arial", 16), bg="#FF5733", fg="white", width=15
)
quit_button.pack(pady=10)

# Run the tkinter main loop
root.mainloop()
