from moviepy.editor import VideoFileClip
from threading import Thread
from tkinter.filedialog import askopenfile

from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button



from kivy.core.window import Window
Window.size = (500,650)
##################################################################################################

class MyApp(MDApp):

    def FileChooser(self, event):
        self.file = askopenfile(mode='r', filetypes=[("mp4 files", "*.mp4")])

        self.mp4_file = self.file.name
        self.mp3_file = self.mp4_file.replace("mp4", "mp3")


        self.locationLabel.text = self.mp4_file

        self.locationLabel.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.convert_button.pos_hint = {"center_x": 0.5, "center_y": 0.35}

    ##################################################################################################

    def writeAudio (self):
        self.video=VideoFileClip(self.mp4_file)
        self.audio = self.video.audio

        try:

            self.audio.write_audiofile(self.mp3_file)
            print("DONE")

            self.successLabel.text= "successfuly converted"
            self.successLabel.pos_hint = {"center_x": 0.5, "center_y": 0.20}

            self.audio.close()
            self.video.close()
        except:
            self.successLabel.text = "Error writing Audio .. plz try again"
            self.successLabel.pos_hint = {"center_x": 0.5, "center_y": 0.20}


    def writeAudieoThread (self, event):
        thread1=Thread(target=self.writeAudio)
        thread1.start()


    ##################################################################################################

    def build(self):

        # Create a layout to hold your widgets
        layout = MDRelativeLayout(md_bg_color= [155/255,80/255,88/255])


    ##################################################################################################### img
        self.img = Image(source="mp4mp3.png",
                         size_hint=(0.5, 0.7),
                         pos_hint={"center_x": 0.5, "center_y": 0.8})
        layout.add_widget(self.img)
    ##################################################################################################### text
        self.filechooserlabel = Label(text="plz select ur video to convert it to mp3",
                                      pos_hint={"center_x": 0.4, "center_y": 0.58},
                                      size_hint=(1, 1),
                                      font_size=20,
                                      color=(1, 1, 1))
        layout.add_widget(self.filechooserlabel)
    ##################################################################################################### button
        self.select_button = Button(text=" select ",
                                    size_hint=(None, None),
                                    pos=(380, 360),
                                    height=40,
                                    color=(1, 1, 1),
                                    on_press=self.FileChooser)

        layout.add_widget(self.select_button)
    ##################################################################################################### location
        self.locationLabel = Label(text=" ",
                                    pos_hint={"center_x": 0.5, "center_y": 20},
                                    size_hint=(1, 1),
                                    pos=(380, 360),
                                    color=(1, 1, 1) )

        layout.add_widget(self.locationLabel)
    ##################################################################################################### button
        self.convert_button = Button(text=" Convert ",
                                    pos_hint={"center_x": 0.5, "center_y": 20},
                                    size_hint=(0.2, 0.1),
                                    size=(75,75),
                                    font_name="Comic",
                                    bold=True,
                                    font_size=24,
                                    on_press=self.writeAudieoThread)
        layout.add_widget(self.convert_button)
        ##################################################################################################### SUCSESS LABEL
        self.successLabel = Label(text=" ",
                                   pos_hint={"center_x": 0.5, "center_y": 20},
                                   size_hint=(1, 1),
                                   color=(1, 1, 1))

        layout.add_widget(self.successLabel)


        return layout

##################################################################################################

# layouts
if __name__ == "__main__":
    MyApp().run()

















