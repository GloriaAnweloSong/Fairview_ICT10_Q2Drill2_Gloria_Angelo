from pyscript import document, display

def add_member(e):
    document.getElementById('result').innerHTML = ""

    gr7 = {'Sher Mistle', 'Dia Mider'}
    gr8 = {'Ein Scribe', 'Johnny Dunnings'}
    gr9 = {'Paul Nomiyal', 'Stew Oaks'}
    gr10 = {'Nell Alonso', 'Bea Nomiyal'}

    club_list = gr7 | gr8 | gr9 | gr10

    document.getElementById('fname').value
    document.getElementById('lname').value

    name = fname + " " + lname

    added_name = document.getElementById('name').value

    new_club_list = {added_name}

    true_club_list = club_list | added_name # combines the two sets into one

    total_num = len(club_list | added_name)

    display_list = "<br>".join(sorted(true_club_list))

    # display--
    document.getElementById('result').innerHTML = f'All members: <br> {display_list}'
    display(f'Total Members: {total_num}', target="result")