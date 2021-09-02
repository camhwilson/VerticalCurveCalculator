#importing all libraries
import tkinter as tk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import Tk, Canvas, Label, StringVar, OptionMenu, Entry, Button
from matplotlib import style

import lvc_functions as lvc_func

class MyFirstGUI:
    def __init__(self):
        main = Tk()
        self.main = main
        main.title("A simple GUI")


        style.use('seaborn-whitegrid')

        

        main.configure(bg = 'white')
        

        self.input_box = Canvas(main, width = 920, height = 170, bg = 'white')
        self.input_box.configure(borderwidth = 0, highlightthickness = 0)
        self.input_box.place(x = 10, y = 85)
        self.input_box.create_rectangle( 10, 3, 440, 165, fill='azure')

        self.input_box.create_rectangle( 525, 3, 900, 165, fill='lavender' )

        self.input_box.create_rectangle( 535, 17, 625, 42, fill='lavender blush')
        self.input_box.create_rectangle( 535, 52, 625, 77, fill='lavender blush')
        self.input_box.create_rectangle( 535, 87, 625, 112, fill='lavender blush')
        self.input_box.create_rectangle( 535, 122, 625, 147, fill='lavender blush')


        self.output_label_1 = Label(main, text = 'Minimum Length of Vertical Curve ', font = ('Times New Roman', 15), bg = 'lavender')
        self.output_label_1.place(x = 645, y = 100, height = 30 )

        self.output_label_2 = Label(main, text = 'SSD Value ', font = ('Times New Roman', 15), bg = 'lavender')
        self.output_label_2.place(x = 645, y = 136, height = 30 )

        self.output_label_3 = Label (main, text = 'Maxima Station', font = ('Times New Roman', 15), bg = 'lavender')
        self.output_label_3.place(x = 645, y = 172,  height = 30 )

        self.output_label_3 = Label (main, text = 'Maxima Elevation', font = ('Times New Roman', 15), bg = 'lavender')
        self.output_label_3.place(x = 645, y = 207,  height = 30 )



        #labeling input slots
        self.label_plus = Label(main,  text = '+', font = ('Times New Roman', 15), bg = 'azure')
        self.label_plus.place(x = 68, y = 95, width= 10, height = 30 )

        self.label_station = Label(main, text = 'BVC Station', font = ('Times New Roman', 15), bg = 'azure')
        self.label_station.place(x = 115, y = 95, width= 100, height = 30 )

        self.label_station = Label(main, text = 'BVC Elevation (ft)', font = ('Times New Roman', 15), bg = 'azure')
        self.label_station.place(x = 320, y = 95, width= 120, height = 30 )



        self.label_1 = Label(main, text = ' Design Speed ', font = ('Times New Roman', 15), bg = 'azure')
        self.label_1.place(x = 67, y = 185, width= 190, height = 30 )

        self.label_2 = Label(main, text = ' Grade 1, in %                ', font = ('Times New Roman', 15), bg = 'azure')
        self.label_2.place(x = 50, y = 125, width= 190, height = 30 )

        self.label_3 = Label(main, text = ' Grade 2, in %                ', font = ('Times New Roman', 15), bg = 'azure')
        self.label_3.place(x = 50, y = 155, width= 190, height = 30)

        self.label_4 = Label(main, text = '  AASHTO standard driver & object height?', font = ('Times New Roman', 15), bg = 'azure')
        self.label_4.place(x = 50, y = 215, width= 310, height = 30)



        self.title_label = Label (main, text = 'Vertical Curve Calculator', fg = 'steel blue',  font = ('Times New Roman', 30), bg = 'white')
        self.title_label.place(x = 10, y = 10)


        self.label_input_box = Label ( text = 'Inputs: ', font = ('Times New Roman', 20), bg = 'white')
        self.label_input_box.place(x = 50, y = 55)

        self.label_output_box = Label ( text = 'Outputs: ', font = ('Times New Roman', 20), bg = 'white')
        self.label_output_box.place(x = 570, y = 55)

        main.title('Vertical Curve Calculator')
        main.geometry('940x700')

        self.tkvar = StringVar(main)
        self.tkvar.set('yes')
        self.tkvar_1 = StringVar(main)
        self.tkvar_1.set('15 (mph)')


        ##############################        Printing ends       ####################################

        #input boxes
        self.inputBox_station_1 = Entry (main, bg = 'LightSteelBlue1')
        self.inputBox_station_1.place(x = 25,y = 95, width = 40, height = 30)

        self.inputBox_station_2 = Entry (main, bg = 'LightSteelBlue1')
        self.inputBox_station_2.place(x = 80,y = 95, width = 40, height = 30)

        self.inputBox_elevation = Entry (main, bg = 'LightSteelBlue1')
        self.inputBox_elevation.place(x = 245,y = 95, width = 70, height = 30)

        #  grade 1
        self.inputBox_2 = Entry (main, bg = 'LightSteelBlue1')
        self.inputBox_2.place(x = 25,y = 125, width = 40, height = 30)

        # grade 2
        self.inputBox_3 = Entry (main, bg = 'LightSteelBlue1')
        self.inputBox_3.place(x = 25, y = 155, width = 40, height = 30)

        # design speed
        popupmenu_speed = OptionMenu (main, self.tkvar_1, '15 (mph)', '20 (mph)', '25 (mph)', '30 (mph)', '35 (mph)', '40 (mph)', '45 (mph)', '50 (mph)', '55 (mph)', '60 (mph)', '65 (mph)', '70 (mph)', '75 (mph)', '80 (mph)')
        popupmenu_speed.place(x = 25, y = 185, width = 90, height = 30)

        # aashto assumption?
        popupmenu = OptionMenu (main, self.tkvar, 'yes', 'no', command = self.option_command)
        popupmenu.place(x = 25, y = 215, width = 45, height = 30)

        Button(main, width = 8, height = 5, text = 'Calculate', command = self.calculate).place(x =455 , y= 130)

        main.mainloop()


#GUI specific functions
    def option_command(self):

        height = self.tkvar.get()

        if height == 'yes':
            try:
                self.inputBox_5.destroy()
                self.inputBox_6.destroy()
                self.label_5.destroy()
                self.label_6.destroy()
            except:
                pass
        if height == 'no':
            #5 - h1 (if aashto = no)
            self.inputBox_5 = Entry( bg = 'LightSteelBlue1')
            self.inputBox_5.place(x = 350, y = 185, width = 40, height = 30)

            self.label_5 = Label ( text = ' H1 (ft)', font = ('Times New Roman', 15), bg = 'azure')
            self.label_5.place(x = 390, y = 185, width = 50, height = 30)

            #6 - h2 (if aashto = no)
            self.inputBox_6 = Entry ( bg = 'LightSteelBlue1')
            self.inputBox_6.place(x = 350, y = 215, width = 40, height = 30)

            self.label_6 = Label ( text = ' H2 (ft)', font = ('Times New Roman', 15), bg = 'azure')
            self.label_6.place(x = 390 , y = 215, width = 50, height = 30)

    def gradient_error_message(self, G1, G2):
        #Grade 1
        if (G1 < -12 or G1 > 12):
            error_label_1 = Label(self.main, text = '*Between -12% and 12%', fg = 'red', font = ('Times New Roman', 15), bg = 'azure')
            error_label_1.place(x = 160, y = 125,  height = 30)
        #Grade 2
        if (G2 < -12 or G2 > 12):
            error_label_1 = Label(self.main, text = '*Between -12% and 12%', fg = 'red', font = ('Times New Roman', 15), bg = 'azure')
            error_label_1.place(x = 160, y = 155,  height = 30)


    def plot(self, G1, G2, x_adjustment, y_adjustment, lvc, SSD):
        a = (G2 - G1)/(2*lvc)
        b = G1

        a_1 = float(a)
        b_1 = float(b)

        x_extreme = -(b_1)/(2*a_1)

        x = np.arange (x_adjustment , lvc +x_adjustment, 0.01)
        y = (((x-x_adjustment)**2)*a_1 + b_1*(x-x_adjustment))/100 + y_adjustment
        q = ((x_extreme**2)*a_1 + b_1*x_extreme)/100

        
        x_before = np.arange (-lvc/2 + x_adjustment, x_adjustment , 0.01)
        z = ((G1)*(x_before- x_adjustment))/100 + y_adjustment

        x_before_dashed = np.arange (x_adjustment, lvc+100 +x_adjustment, 0.01)

        z_1 = ((G1)*(x_before_dashed-x_adjustment))/100+y_adjustment



        ##
        x_after = np.arange (lvc+x_adjustment, lvc*1.4+ x_adjustment,0.01)

        v = ((G2)*(x_after-x_adjustment-lvc))/100 + ((lvc**2)*a_1 + b_1*lvc)/100 + y_adjustment

        #

        tricky_point = (-G2*lvc + lvc**2*a_1 + b_1*lvc)/(G1-G2)

        tricky_point_y_value = ((G1)*tricky_point)/100

        x_after_dashed = np.arange (tricky_point+x_adjustment, lvc +x_adjustment,0.01)

        v_1 = ((G2)*(x_after_dashed-lvc-x_adjustment))/100 + ((lvc**2)*a_1 + b_1*lvc)/100 + y_adjustment

        tricky_point_y = ((lvc**2)*a_1 + b_1*lvc)/100



        #crest curve printing parameters

        x1 = ('Station')
        y1 = ('Elevation (ft)')

        if q > 0 :

            #establishing coordinates
            x_axis_bounds = [-lvc/2.5+ x_adjustment, lvc*1.33+ x_adjustment]

            if tricky_point_y_value > 0 and tricky_point_y > 0:
                #case 1
                if tricky_point_y > tricky_point_y_value:
                    y_axis_bounds = [ -tricky_point_y_value*0.6 + y_adjustment, tricky_point_y_value*2 + y_adjustment ]
                #case 2
                if tricky_point_y_value > tricky_point_y:
                    y_axis_bounds = [ -tricky_point_y_value*0.6+ y_adjustment, tricky_point_y_value*1.5+ y_adjustment]

            #case 3
            if tricky_point_y_value > 0 and tricky_point_y < 0 or tricky_point_y == 0:
                if SSD > 355 :
                    y_axis_bounds = [ 2*tricky_point_y-10+ y_adjustment, tricky_point_y_value*2+ y_adjustment]
                else:
                    y_axis_bounds = [ 2*tricky_point_y-3+ y_adjustment, tricky_point_y_value*2]

            #case 4 - works
            if tricky_point_y_value < 0 and tricky_point_y < 0:
                y_axis_bounds = [tricky_point_y*1.35+ y_adjustment, -tricky_point_y_value*2+ y_adjustment]



        #sag curve printing parameters
        if q < 0 :

            #establishing coordinates
            x_axis_bounds = [-lvc/2.5+ x_adjustment, lvc*1.33+ x_adjustment]
            if tricky_point_y_value < 0 and tricky_point_y < 0:
                #case 1
                if tricky_point_y < tricky_point_y_value:
                    y_axis_bounds = [  tricky_point_y_value*2+ y_adjustment, -tricky_point_y_value*0.6 + y_adjustment]
                #case 2
                if tricky_point_y_value < tricky_point_y:
                    y_axis_bounds = [  tricky_point_y_value*1.5+ y_adjustment, -tricky_point_y_value*0.6 + y_adjustment]
            #case 3
            if tricky_point_y_value < 0 and tricky_point_y > 0 or tricky_point_y == 0 :
                    if SSD > 355 :
                        y_axis_bounds = [ tricky_point_y_value*2+ y_adjustment, 2*tricky_point_y+10 + y_adjustment ]
                    else:
                        y_axis_bounds = [ tricky_point_y_value*2+ y_adjustment, 2*tricky_point_y+3  + y_adjustment]
            #case 4
            if tricky_point_y_value > 0 and tricky_point_y > 0:
                y_axis_bounds = [ -tricky_point_y_value*2+ y_adjustment, tricky_point_y*1.35+ y_adjustment]
                        
            
            
        f = Figure(figsize = (5,5), dpi = 100)
        a = f.add_subplot(111)

        a.plot(x,y,'k')

        a.plot(x_before,z,color = 'k')
        a.plot(x_before_dashed,z_1, color = 'k', linestyle ='dotted')
        a.plot(x_after,v,'k')
        a.plot(x_after_dashed,v_1,color = 'k', linestyle= 'dotted')



        a.set_xlabel(x1)
        a.set_ylabel(y1)
        a.set_xlim(x_axis_bounds)
        a.set_ylim(y_axis_bounds)


        a.plot(x_adjustment, y_adjustment, 'rx', label = 'BVC')
        a.plot( tricky_point+ x_adjustment, tricky_point_y_value + y_adjustment, 'gx' , label = 'PVI')
        a.plot(lvc + x_adjustment,tricky_point_y+ y_adjustment, 'bx', label = 'EVC')
        a.legend()

        canvas = FigureCanvasTkAgg(f, self.main)
        canvas.draw()
        canvas.get_tk_widget().place(x = 100, y = 265, width = 800, height = 400)


        b = []
        l = []
        for tick in a.xaxis.get_ticklabels():
            while tick.get_text() != '-10' and tick.get_text()!= '-20' :
                ticks = tick.get_text().replace(u'\N{MINUS SIGN}', '-')
                ticks_round = round(float(ticks)/100, 2)
                small_station_1 = (ticks_round - int(ticks_round))
                small_station = "{:.2f}".format(small_station_1)
                station = str(int(ticks_round)) +  ' + ' + small_station[2:]
                l.append(station)
                break
        a.set_xticklabels(l)
        return x_extreme, q

    #defining executable (takes form of button)
    def calculate(self):

        #retrieving inputs
        if len(self.inputBox_station_2.get()) == 1:
            box_2 = '0'+ self.inputBox_station_2.get()
        if len(self.inputBox_station_2.get()) == 2:
            box_2 = self.inputBox_station_2.get()
        else:
            box_2 = '00'

        x_adjustment = float(self.inputBox_station_1.get() + box_2)
        y_adjustment = float(self.inputBox_elevation.get())
        G1 = float(self.inputBox_2.get())
        G2 = float(self.inputBox_3.get())
        height = self.tkvar.get()
        design_speed = self.tkvar_1.get()

        if height == 'yes':
            H1 = 3.5
            H2 = 2
        if height == 'no':
            H1 = float(self.inputBox_5.get())
            H2 = float(self.inputBox_6.get())

        #Invalid variable input warnings, repeats instructions
        self.gradient_error_message(G1, G2)
    
        lvc, SSD, curve_type = lvc_func.get_ssd_and_lvc(design_speed, G1, G2, H1, H2)

        x_extreme, q = self.plot(G1, G2, x_adjustment, y_adjustment, lvc, SSD)

        #logic for maximum points
        extreme_station = lvc_func.station_from_feet(x_extreme+x_adjustment)
        
        elevation_statement = lvc_func.find_elev_max_statements(curve_type, G1, G2, extreme_station, q, y_adjustment)[0]
        max_elevation = lvc_func.find_elev_max_statements(curve_type, G1, G2, extreme_station, q, y_adjustment)[1]


        lvc_label_xy = (580, 29)
        
        SSD_label_xy = (580, 64)
        
        q_label_text_xy = (580, 99)
        
        elevation_label_text_xy = (580, 134)

        self.input_box.create_rectangle(535, 17, 625, 42, fill='lavender blush')
        self.input_box.create_text(*lvc_label_xy, text = '%s (ft)' %(round(lvc, 2)))

        self.input_box.create_rectangle(535, 52, 625, 77, fill='lavender blush')
        self.input_box.create_text(*SSD_label_xy, text = '%s (ft)' %(round(SSD, 2)))

        self.input_box.create_rectangle(535, 87, 625, 112, fill='lavender blush')
        self.input_box.create_text(*q_label_text_xy, text = elevation_statement)

        self.input_box.create_rectangle(535, 122, 625, 147, fill='lavender blush')
        self.input_box.create_text(*elevation_label_text_xy, text = max_elevation)

main = MyFirstGUI()

