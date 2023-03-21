from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:

    def __init__(self):
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Five item list
        self.all_calculations = ['0 F° is -18 C°', '0 C° is 32 F°',
                                 '30 F° is -1 C°', '30 C° is 86 F°',
                                 '40 F° is 4 C°']

        # # Six item list
        # self.all_calculations = ['0 F° is -18 C°', '0 C° is 32 F°',
        #                          '30 F° is -1 C°', '30 C° is 86 F°',
        #                          '40 F° is 4 C°', '100 C° is 212 F°']

        # Set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(self.temp_frame, padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        state=DISABLED,
                                        command=lambda: self.to_history(self.all_calculations))
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

        # **** Remove when integrating!! ***
        self.to_history_button.config(state=NORMAL)

    def to_history(self, all_calculations):
        HistoryExport(self, all_calculations)


class HistoryExport:

    def __init__(self, partner, calc_list):

        # set maximum number of calculations to 5
        # this can be change if we want to show fewer /
        # more calculations
        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

        # Function converts contents of calculations list
        # into a string.
        self.get_calc_string(calc_list)

        # setup dialogue box and background colour
        self.history_box = Toplevel()
        background = "#ff0000"

        # disable help button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, classes help and
        # 'releases' help button
        self.history_box.protocol('WN_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.help_frame = Frame(self.history_box, width=300,
                                height=200,
                                bg=background)
        self.help_frame.grid()

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_history,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    def get_calc_string(self, var_calculations):
        max_calcs = self.var_max_calcs.get()

    # closes help dialogue (used by button and x at top of dialogue)
    def close_history(self, partner):
        # Put help button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()

