import pandas as pd 
import numpy as np

def patience_classification(reco, patience):
    if patience == 'lv2':
        book_page = reco[reco['book_page'] >= 900]
        if book_page:
            reco.loc[book_page.index, 'art_reputation'] -= 20

    elif patience == 'lv3':
        book_page = reco[reco['book_page'] >= 500]
        if book_page:
            reco.loc[book_page.index, 'art_reputation'] -= 20

def color_add_weight(reco, color_palettes):
    for co in list(color_palettes):
        color_contain = reco[reco['color'].str.contains(co.capitalize())]
        reco.loc[color_contain.index, 'art_reputation'] += 100

def atmo_add_weight(reco,novel_atmo):
    for atmo in list(novel_atmo):
        atmo_contain = reco[reco['atmosphere'].str.contains(atmo.capitalize())]
        reco.loc[atmo_contain.index, 'art_reputation'] += 50

def recommend_book(df,user_input):
    reco = df[df['book_genre'] == user_input['novel_genre']]

    color_add_weight(reco, user_input['color_palettes'])
    atmo_add_weight(reco, user_input['novel_atmo'])
    
    patience_classification(reco, user_input['patient'])

    result = reco[reco['art_reputation'] == reco['art_reputation'].max()]

    return result