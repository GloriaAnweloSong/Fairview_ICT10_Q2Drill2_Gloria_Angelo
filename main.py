from pyscript import document, display

def add_member(e):
    document.getElementById('result').innerHTML = ""

    gr7 = {'Sher Mistle', 'Dia Mider'}
    gr8 = {'Ein Scribe', 'Johnny Dunnings'}
    gr9 = {'Paul Nomiyal', 'Stew Oaks'}
    gr10 = {'Nell Alonso', 'Bea Nomiyal'}

    club_list = gr7 | gr8 | gr9 | gr10

    added_name = ocument.getElementById('name').value
    added_name = document.getElementById('name').value
    name = fname + " " + lname

    added_name = document.getElementById('name').value

    new_club_list = {added_name}

    true_club_list = club_list | added_name # combines the two sets into one

    total_num = len(club_list | added_name)

    club_list = "<br>".join(sorted(true_club_lists))

    # display--
    document.getElementById('output1').innerHTML = f'All brands: <br> {brand_list}'
    display(f'Total Brands: {total_brands}', target="output1")