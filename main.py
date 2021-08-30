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


style.use('seaborn-whitegrid')

main = Tk()

main.configure(bg = 'white')




input_box = Canvas(main, width = 920, height = 170, bg = 'white')
input_box.configure(borderwidth = 0, highlightthickness = 0)
input_box.place(x = 10, y = 85)
input_box.create_rectangle( 10, 3, 440, 165, fill='azure')

input_box.create_rectangle( 525, 3, 900, 165, fill='lavender' )

input_box.create_rectangle( 535, 17, 625, 42, fill='lavender blush')
input_box.create_rectangle( 535, 52, 625, 77, fill='lavender blush')
input_box.create_rectangle( 535, 87, 625, 112, fill='lavender blush')
input_box.create_rectangle( 535, 122, 625, 147, fill='lavender blush')


output_label_1 = Label(main, text = 'Minimum Length of Vertical Curve ', font = ('Times New Roman', 15), bg = 'lavender')
output_label_1.place(x = 645, y = 100, height = 30 )

output_label_2 = Label(main, text = 'SSD Value ', font = ('Times New Roman', 15), bg = 'lavender')
output_label_2.place(x = 645, y = 136, height = 30 )

output_label_3 = Label (main, text = 'Maxima Station', font = ('Times New Roman', 15), bg = 'lavender')
output_label_3.place(x = 645, y = 172,  height = 30 )

output_label_3 = Label (main, text = 'Maxima Elevation', font = ('Times New Roman', 15), bg = 'lavender')
output_label_3.place(x = 645, y = 207,  height = 30 )



#labeling input slots
label_plus = Label(main,  text = '+', font = ('Times New Roman', 15), bg = 'azure')
label_plus.place(x = 68, y = 95, width= 10, height = 30 )

label_station = Label(main, text = 'BVC Station', font = ('Times New Roman', 15), bg = 'azure')
label_station.place(x = 115, y = 95, width= 100, height = 30 )

label_station = Label(main, text = 'BVC Elevation (ft)', font = ('Times New Roman', 15), bg = 'azure')
label_station.place(x = 320, y = 95, width= 120, height = 30 )



label_1 = Label(main, text = ' Design Speed ', font = ('Times New Roman', 15), bg = 'azure')
label_1.place(x = 67, y = 185, width= 190, height = 30 )

label_2 = Label(main, text = ' Grade 1, in %                ', font = ('Times New Roman', 15), bg = 'azure')
label_2.place(x = 50, y = 125, width= 190, height = 30 )

label_3 = Label(main, text = ' Grade 2, in %                ', font = ('Times New Roman', 15), bg = 'azure')
label_3.place(x = 50, y = 155, width= 190, height = 30)

label_4 = Label(main, text = '  AASHTO standard driver & object height?', font = ('Times New Roman', 15), bg = 'azure')
label_4.place(x = 50, y = 215, width= 310, height = 30)



title_label = Label (main, text = 'Vertical Curve Calculator', fg = 'steel blue',  font = ('Times New Roman', 30), bg = 'white')
title_label.place(x = 10, y = 10)


label_input_box = Label ( text = 'Inputs: ', font = ('Times New Roman', 20), bg = 'white')
label_input_box.place(x = 50, y = 55)

label_output_box = Label ( text = 'Outputs: ', font = ('Times New Roman', 20), bg = 'white')
label_output_box.place(x = 570, y = 55)




main.title('Vertical Curve Calculator')
main.geometry('940x700')


tkvar = StringVar(main)
tkvar.set('yes')

tkvar_1 = StringVar(main)
tkvar_1.set('15 (mph)')


############




def option_command(main):

    height = tkvar.get()


    if height == 'yes':
        try:
            option_command.inputBox_5.destroy()
            option_command.inputBox_6.destroy()
            option_command.label_5.destroy()
            option_command.label_6.destroy()
        except:
            pass
    if height == 'no':
        #5 - h1 (if aashto = no)
        option_command.inputBox_5 = Entry( bg = 'LightSteelBlue1')
        option_command.inputBox_5.place(x = 350, y = 185, width = 40, height = 30)

        option_command.label_5 = Label ( text = ' H1 (ft)', font = ('Times New Roman', 15), bg = 'azure')
        option_command.label_5.place(x = 390, y = 185, width = 50, height = 30)

#6 - h2 (if aashto = no)
        option_command.inputBox_6 = Entry ( bg = 'LightSteelBlue1')
        option_command.inputBox_6.place(x = 350, y = 215, width = 40, height = 30)

        option_command.label_6 = Label ( text = ' H2 (ft)', font = ('Times New Roman', 15), bg = 'azure')
        option_command.label_6.place(x = 390 , y = 215, width = 50, height = 30)






#defining executable (takes form of button)
def calculate():

    #retrieving inputs

    if len(inputBox_station_2.get()) == 1:
        box_2 = '0'+ inputBox_station_2.get()
    if len(inputBox_station_2.get()) == 2:
        box_2 = inputBox_station_2.get()
    else:
        pass

    x_adjustment = float(inputBox_station_1.get() + box_2)
    y_adjustment = float(inputBox_elevation.get())
    G1 = inputBox_2.get()
    G2 = inputBox_3.get()
    height = tkvar.get()
    design_speed = tkvar_1.get()


    if height == 'yes':
        H1 = 3.5
        H2 = 2
    if height == 'no':
        H1 = option_command.inputBox_5.get()
        H2 = option_command.inputBox_6.get()


    #Invalid variable input warnings

    x = list(range(15,85,5))

    #Grade 1

    if (float(G1) < -12 or float(G1) > 12):
    #instruction repeat
        error_label_1 = Label(main, text = '*Between -12% and 12%', fg = 'red', font = ('Times New Roman', 15), bg = 'azure')
        error_label_1.place(x = 160, y = 125,  height = 30)


    #Grade 2
    if (float(G2) < -12 or float(G2) > 12):

        error_label_1 = Label(main, text = '*Between -12% and 12%', fg = 'red', font = ('Times New Roman', 15), bg = 'azure')
        error_label_1.place(x = 160, y = 155,  height = 30 )


    #determination of SSD variable
    if design_speed == '15 (mph)' :
        SSD = 80
    if design_speed == '20 (mph)' :
        SSD = 115
    if design_speed == '25 (mph)' :
        SSD = 155
    if design_speed == '30 (mph)' :
        SSD = 200
    if design_speed == '35 (mph)' :
        SSD = 250
    if design_speed == '40 (mph)' :
        SSD = 305
    if design_speed == '45 (mph)' :
        SSD = 360
    if design_speed == '50 (mph)' :
        SSD = 425
    if design_speed == '55 (mph)' :
        SSD = 495
    if design_speed == '60 (mph)' :
        SSD = 570
    if design_speed == '65 (mph)' :
        SSD = 645
    if design_speed == '70 (mph)' :
        SSD = 730
    if design_speed == '75 (mph)' :
        SSD = 820
    if design_speed == '80 (mph)' :
        SSD = 910





    G_1 = float(G1)
    G_2 = float(G2)

    A = G_2 - G_1
    A_1 = abs(A)


    #Crest/Sag logic
    #Crest Cases
    if G_1 > 0 and G_2 > 0 and abs(G_1) > abs(G_2) :
        curve_type = 'crest'

    if G_1 < 0 and G_2 < 0 and abs(G_1) < abs(G_2) :
        curve_type = 'crest'

    if G_1 > 0 and G_2 < 0:
        curve_type = 'crest'

    #Sag Cases
    if G_1 < 0 and G_2 < 0 and abs(G_1) > abs(G_2) :
        curve_type = 'sag'

    if G_1 > 0 and G_2 > 0 and abs(G_1) < abs(G_2) :
        curve_type = 'sag'

    if G_1 < 0 and G_2 > 0 :
        curve_type = 'sag'


#If this curve is a crest curve

    if curve_type == str('crest') :

        H_1 = float(H1)
        H_2 = float(H2)



        # Equation Determination
        #ans_1 is based on assumption that L<SSD
        ans_1 = 2*SSD - (200*(H_1**(1/2) + H_2**(1/2))**2)/A_1


    #If assumption that L < SSD is incorrect
        if float(ans_1) > float(SSD) or float(ans_1) < 0 :

            ans_2 = (A_1*SSD**2)/(200*(H_1**(1/2) + H_2**(1/2))**2)
            ans_1 = 0

#If this curve is a sag curve

    #ans_1 is based on assumption that L<SSD
    if curve_type == str('sag'):

        ans_1 = 2*SSD - (400 + 2.5*SSD)/A


    #If assumption that L<SSD is incorrect
        if float(ans_1) > float(SSD) or float(ans_1) < 0 :

            ans_2 = (A*(SSD**2))/(400+3.5*SSD)
            ans_1 = 0

##############################        Printing to GUI Begins       ####################################


    if float (ans_1) != 0 :
        lvc = ans_1

    else:
        lvc = ans_2


    half_lvc = lvc/2


    a = (G_2 - G_1)/(2*lvc)
    b = G_1

    a_1 = float(a)
    b_1 = float(b)

    x_extreme = -(b_1)/(2*a_1)

    ##
    x = np.arange (x_adjustment , lvc +x_adjustment, 0.01)

    y = (((x-x_adjustment)**2)*a_1 + b_1*(x-x_adjustment))/100 + y_adjustment

    q = ((x_extreme**2)*a_1 + b_1*x_extreme)/100




    ##
    x_before = np.arange (-lvc/2 + x_adjustment, x_adjustment , 0.01)

    z = ((G_1)*(x_before- x_adjustment))/100 + y_adjustment

    #
    x_before_dashed = np.arange (x_adjustment, lvc+100 +x_adjustment, 0.01)

    z_1 = ((G_1)*(x_before_dashed-x_adjustment))/100+y_adjustment



    ##
    x_after = np.arange (lvc+x_adjustment, lvc*1.4+ x_adjustment,0.01)

    v = ((G_2)*(x_after-x_adjustment-lvc))/100 + ((lvc**2)*a_1 + b_1*lvc)/100 + y_adjustment

    #

    tricky_point = (-G_2*lvc + lvc**2*a_1 + b_1*lvc)/(G_1-G_2)

    tricky_point_y_value = ((G_1)*tricky_point)/100

    x_after_dashed = np.arange (tricky_point+x_adjustment, lvc +x_adjustment,0.01)

    v_1 = ((G_2)*(x_after_dashed-lvc-x_adjustment))/100 + ((lvc**2)*a_1 + b_1*lvc)/100 + y_adjustment

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
                y_axis_bounds = [ 2*tricky_point_y-10+ y_adjustment , tricky_point_y_value*2+ y_adjustment]
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

    canvas = FigureCanvasTkAgg(f, main)
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

################


    #logic for maximum points


    def station_from_feet(ticks):
        ticks_round = round(float(ticks)/100, 2)
        small_station_1 = (ticks_round - int(ticks_round))
        small_station = "{:.2f}".format(small_station_1)
        station = str(int(ticks_round)) +  ' + ' + small_station[2:]
        return station

    extreme_station = station_from_feet(x_extreme+x_adjustment)

    if curve_type == 'crest':
        if G_1 > 0 and G_2 < 0:
            elevation_statement = '%s' %(extreme_station)
            max_elevation = '%s (ft)' %(round(q+y_adjustment, 2))
        if G_1 < 0 and G_2 < 0:
            elevation_statement = 'N/A'
            max_elevation = 'N/A'
        if G_1 > 0 and G_2 > 0:
            elevation_statement = 'N/A'
            max_elevation = 'N/A'

    if curve_type == 'sag':
        if G_1 < 0 and G_2 > 0:
            elevation_statement = '%s' %(extreme_station)
            max_elevation = '%s (ft)' %(round(q+y_adjustment, 2))
        if G_1 > 0 and G_2 > 0:
            elevation_statement = 'N/A'
            max_elevation = 'N/A'
        if G_1 < 0 and G_2 < 0:
            elevation_statement = 'N/A'
            max_elevation = 'N/A'


    lvc_label_text_x = 580
    lvc_label_text_y = 29

    SSD_label_text_x = 580
    SSD_label_text_y = 64

    q_label_text_x = 580
    q_label_text_y = 99

    elevation_label_text_x = 580
    elevation_label_text_y = 134

    input_box.create_rectangle( 535, 17, 625, 42, fill='lavender blush')
    input_box.create_text(lvc_label_text_x, lvc_label_text_y, text = '%s (ft)' %(round(lvc, 2)))

    input_box.create_rectangle( 535, 52, 625, 77, fill='lavender blush')
    input_box.create_text(SSD_label_text_x, SSD_label_text_y, text = '%s (ft)' %(round(SSD, 2)))

    input_box.create_rectangle( 535, 87, 625, 112, fill='lavender blush')
    input_box.create_text(q_label_text_x, q_label_text_y, text = elevation_statement)

    input_box.create_rectangle( 535, 122, 625, 147, fill='lavender blush')
    input_box.create_text(elevation_label_text_x, elevation_label_text_y, text = max_elevation)


###### canvas box 2


    _text_x = 60

    key_text_x = 40
    key_text_y = 12

    bvc_text_x = _text_x
    bvc_text_y = 40

    evc_text_x = _text_x
    evc_text_y = 65


    pvi_text_x = _text_x
    pvi_text_y = 90










##############################        Printing ends       ####################################





#input boxes

inputBox_station_1 = Entry (main, bg = 'LightSteelBlue1')
inputBox_station_1.place(x = 25,y = 95, width = 40, height = 30)

inputBox_station_2 = Entry (main, bg = 'LightSteelBlue1')
inputBox_station_2.place(x = 80,y = 95, width = 40, height = 30)

inputBox_elevation = Entry (main, bg = 'LightSteelBlue1')
inputBox_elevation.place(x = 245,y = 95, width = 70, height = 30)




#  grade 1
inputBox_2 = Entry (main, bg = 'LightSteelBlue1')
inputBox_2.place(x = 25,y = 125, width = 40, height = 30)




# grade 2
inputBox_3 = Entry (main, bg = 'LightSteelBlue1')
inputBox_3.place(x = 25, y = 155, width = 40, height = 30)


# design speed
popupmenu_speed = OptionMenu (main, tkvar_1, '15 (mph)', '20 (mph)', '25 (mph)', '30 (mph)', '35 (mph)', '40 (mph)', '45 (mph)', '50 (mph)', '55 (mph)', '60 (mph)', '65 (mph)', '70 (mph)', '75 (mph)', '80 (mph)')
popupmenu_speed.place(x = 25, y = 185, width = 90, height = 30)





# aashto assumption?
popupmenu = OptionMenu (main, tkvar, 'yes', 'no', command = option_command)
popupmenu.place(x = 25, y = 215, width = 45, height = 30)



Button(main, width = 8, height = 5, text = 'Calculate', command = calculate).place(x =455 , y= 130)


main.mainloop()



