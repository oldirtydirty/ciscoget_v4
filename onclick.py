'''Message pop-up '''
import tkinter.messagebox

class OnClick:
    '''Popup Message'''
    def onclick(self) -> None:
        '''Warning'''
        tkinter.messagebox.showinfo("Motorola Solutions",
                                    "This program is strictly for MSI employee use. ")
