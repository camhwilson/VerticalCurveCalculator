
#Non-GUI specific functions
def get_ssd_and_lvc(design_speed, G1, G2, H1, H2):
        
        SSD = determine_SSD(design_speed)
        A = abs(G2 - G1)
        curve_type = crest_or_sag(G1, G2)
        
        if curve_type == 'crest' :
            lvc = get_crest_lvc(SSD, H1, H2, A)
        
        if curve_type == 'sag':
            lvc = get_sag_lvc(SSD, A)
        return lvc, SSD, curve_type

def determine_SSD(design_speed):
    ssd_dict = {'15 (mph)': 80, '20 (mph)': 115,  '25 (mph)': 155, '30 (mph)': 200, 
                    '35 (mph)': 250, '40 (mph)': 305, '45 (mph)': 360, '50 (mph)': 425, 
                    '55 (mph)': 495, '60 (mph)': 570, '65 (mph)': 645, '70 (mph)': 730, 
                    '75 (mph)': 820, '80 (mph)':910}
    return ssd_dict[design_speed]

def station_from_feet(ticks):
        ticks_round = round(float(ticks)/100, 2)
        small_station_1 = (ticks_round - int(ticks_round))
        small_station = "{:.2f}".format(small_station_1)
        station = str(int(ticks_round)) +  ' + ' + small_station[2:]
        return station

def find_elev_max_statements(curve_type, G1, G2, extreme_station, q, y_adjustment):
        if curve_type == 'crest':
            if G1 > 0 and G2 < 0:
                elevation_statement = '%s' %(extreme_station)
                max_elevation = '%s (ft)' %(round(q+y_adjustment, 2))
            if G1 < 0 and G2 < 0:
                elevation_statement = 'N/A'
                max_elevation = 'N/A'
            if G1 > 0 and G2 > 0:
                elevation_statement = 'N/A'
                max_elevation = 'N/A'
        if curve_type == 'sag':
            if G1 < 0 and G2 > 0:
                elevation_statement = '%s' %(extreme_station)
                max_elevation = '%s (ft)' %(round(q+y_adjustment, 2))
            if G1 > 0 and G2 > 0:
                elevation_statement = 'N/A'
                max_elevation = 'N/A'
            if G1 < 0 and G2 < 0:
                elevation_statement = 'N/A'
                max_elevation = 'N/A'
        return elevation_statement, max_elevation

def crest_or_sag(G1, G2):
    G1 = float(G1)
    G2 = float(G2)
    if G1 > 0 and G2 > 0 and abs(G1) > abs(G2) :
        curve_type = 'crest'
    if G1 < 0 and G2 < 0 and abs(G1) < abs(G2) :
        curve_type = 'crest'

    if G1 > 0 and G2 < 0:
        curve_type = 'crest'

    #Sag Cases
    if G1 < 0 and G2 < 0 and abs(G1) > abs(G2) :
        curve_type = 'sag'

    if G1 > 0 and G2 > 0 and abs(G1) < abs(G2) :
        curve_type = 'sag'

    if G1 < 0 and G2 > 0 :
        curve_type = 'sag'
    return curve_type

def get_crest_lvc(SSD, H1, H2, A):
    # Equation Determination
    # #first lvc answer is based on assumption that L<SSD
    lvc = 2*SSD - (200*(H1**(1/2) + H2**(1/2))**2)/A
    #If assumption that L < SSD is incorrect
    if lvc > float(SSD) or lvc < 0:
        lvc = (A*SSD**2)/(200*(H1**(1/2) + H2**(1/2))**2)
    return lvc

def get_sag_lvc(SSD, A):
    #first lvc is based on assumption that L<SSD
    lvc = 2*SSD - (400 + 2.5*SSD)/A
    #If assumption that L<SSD is incorrect
    if lvc > SSD or lvc < 0:
        lvc = (A*(SSD**2))/(400+3.5*SSD)
    return lvc
